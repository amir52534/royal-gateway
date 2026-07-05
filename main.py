# main.py - Royal Gateway v9.2
# پنل مدیریت کامل با آمار واقعی

import os
import json
import hashlib
import secrets
import logging
import asyncio
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# واردات pages
from pages import LOGIN_HTML, DASHBOARD_HTML, get_public_page_html

# واردات relay_vless
import relay_vless

# ========== تنظیمات ==========
DATA_DIR = "/data" if os.path.exists("/data") else "data"
os.makedirs(DATA_DIR, exist_ok=True)

DATA_FILE = os.path.join(DATA_DIR, "data.json")
PASSWORD_FILE = os.path.join(DATA_DIR, "password_hash.txt")
ACTIVITY_LOG_FILE = os.path.join(DATA_DIR, "activity.jsonl")
ERROR_LOG_FILE = os.path.join(DATA_DIR, "errors.jsonl")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ========== متغیرهای سراسری ==========
links: List[Dict] = []
subs: List[Dict] = []
password_hash: Optional[str] = None
activity_logs: List[Dict] = []
error_logs: List[Dict] = []
start_time = time.time()

# ========== توابع کمکی ==========
def fmt_bytes(b: int) -> str:
    if b < 1024:
        return f"{b} B"
    elif b < 1024 ** 2:
        return f"{b/1024:.1f} KB"
    elif b < 1024 ** 3:
        return f"{b/1024**2:.2f} MB"
    else:
        return f"{b/1024**3:.2f} GB"

def generate_uuid() -> str:
    import uuid
    return str(uuid.uuid4())

def hash_password(password: str, salt: Optional[str] = None) -> tuple:
    if salt is None:
        salt = secrets.token_hex(16)
    combined = salt + password
    hash_val = hashlib.sha256(combined.encode()).hexdigest()
    return hash_val, salt

def verify_password(password: str, stored_hash: str, salt: str) -> bool:
    combined = salt + password
    return hashlib.sha256(combined.encode()).hexdigest() == stored_hash

# ========== توابع لاگ ==========
def load_activity_logs():
    global activity_logs
    activity_logs = []
    if os.path.exists(ACTIVITY_LOG_FILE):
        try:
            with open(ACTIVITY_LOG_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        entry = json.loads(line.strip())
                        activity_logs.append(entry)
                    except:
                        continue
        except:
            pass
    if len(activity_logs) > 1000:
        activity_logs = activity_logs[-1000:]

def add_activity_log(message: str, level: str = "info", kind: str = "system"):
    entry = {
        'time': datetime.now().isoformat(),
        'message': message,
        'level': level,
        'kind': kind
    }
    activity_logs.append(entry)
    if len(activity_logs) > 1000:
        activity_logs = activity_logs[-1000:]
    try:
        with open(ACTIVITY_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    except:
        pass
    logger.info(f"[{kind}] {message}")

def add_error_log(error: str, url: Optional[str] = None):
    entry = {
        'time': datetime.now().isoformat(),
        'error': error,
        'url': url
    }
    error_logs.append(entry)
    if len(error_logs) > 500:
        error_logs = error_logs[-500:]
    try:
        with open(ERROR_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    except:
        pass
    logger.error(f"{error} (URL: {url})")

# ========== توابع داده ==========
def load_data():
    global links, subs, password_hash
    
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                links = data.get('links', [])
                subs = data.get('subs', [])
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            links = []
            subs = []
    else:
        default_link = {
            'uuid': generate_uuid(),
            'label': 'لینک پیش‌فرض',
            'note': 'بدون محدودیت',
            'limit_bytes': 0,
            'used_bytes': 0,
            'active': True,
            'expires_at': None,
            'created_at': datetime.now().isoformat(),
            'protocol': 'vless-ws',
            'sub_id': None,
            'vless_link': '',
            'sub_url': ''
        }
        links = [default_link]
        subs = []
        save_data()
    
    if os.path.exists(PASSWORD_FILE):
        try:
            with open(PASSWORD_FILE, 'r', encoding='utf-8') as f:
                password_hash = f.read().strip()
        except:
            password_hash = None
    
    _setup_links()
    _setup_subs()
    load_activity_logs()

def save_data():
    try:
        data = {'links': links, 'subs': subs}
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Error saving data: {e}")

def save_password_hash(hash_val: str):
    global password_hash
    password_hash = hash_val
    try:
        with open(PASSWORD_FILE, 'w', encoding='utf-8') as f:
            f.write(hash_val)
    except Exception as e:
        logger.error(f"Error saving password: {e}")

def _setup_links():
    import urllib.parse
    base_url = os.getenv('BASE_URL', 'https://royal-gateway.railway.app')
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    for link in links:
        vless_parts = [
            f"vless://{link['uuid']}",
            f"@{base_url.replace('https://', '').replace('http://', '')}",
            "?security=tls",
            "&encryption=none",
            "&headerType=ws",
            "&path=/ws",
            "&type=ws",
            f"&sni={base_url.replace('https://', '').replace('http://', '').split('/')[0]}",
            "&fp=chrome",
            "#" + urllib.parse.quote(link['label'])
        ]
        link['vless_link'] = ''.join(vless_parts)
        link['sub_url'] = f"{base_url}/sub/{link['uuid']}"

def _setup_subs():
    import urllib.parse
    base_url = os.getenv('BASE_URL', 'https://royal-gateway.railway.app')
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    for sub in subs:
        sub['public_url'] = f"{base_url}/public/{sub['sub_id']}"
        sub['sub_url'] = f"{base_url}/sub-group/{sub['sub_id']}"

# ========== توابع مورد نیاز relay_vless ==========
def _get_links_data() -> List[Dict]:
    return links

def _get_link_by_uuid(uuid_str: str) -> Optional[Dict]:
    for link in links:
        if link.get('uuid') == uuid_str:
            return link
    return None

def _update_link_usage(uuid_str: str, bytes_used: int, direction: str = "rx"):
    for link in links:
        if link.get('uuid') == uuid_str:
            link['used_bytes'] = link.get('used_bytes', 0) + bytes_used
            save_data()
            break

def _add_log(message: str, level: str = "info", kind: str = "system"):
    add_activity_log(message, level, kind)

# ========== مقداردهی relay_vless ==========
relay_vless.initialize_relay(
    _get_links_data,
    _get_link_by_uuid,
    _update_link_usage,
    _add_log
)

# ========== Session Management ==========
sessions = {}

def create_session() -> str:
    session_id = secrets.token_hex(32)
    sessions[session_id] = time.time() + 7 * 24 * 3600
    return session_id

def check_session(session_id: Optional[str]) -> bool:
    if not session_id or session_id not in sessions:
        return False
    if sessions[session_id] < time.time():
        del sessions[session_id]
        return False
    return True

def get_session(request: Request) -> Optional[str]:
    return request.cookies.get("session")

# ========== FastAPI با lifespan ==========
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Royal Gateway v9.2 starting...")
    load_data()
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # راه‌اندازی WebSocket
    asyncio.create_task(relay_vless.start_websocket_server(
        host="0.0.0.0",
        port=443
    ))
    
    logger.info("Royal Gateway v9.2 started successfully")
    yield
    
    logger.info("Royal Gateway shutting down...")
    for conn in list(relay_vless.active_connections.values()):
        try:
            await conn.close(1001, "Server shutting down")
        except:
            pass

app = FastAPI(
    title="Royal Gateway",
    description="پنل مدیریت Royal Gateway v9.2",
    version="9.2",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== Routes ==========
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    session_id = get_session(request)
    if check_session(session_id):
        return RedirectResponse(url="/dashboard")
    return RedirectResponse(url="/login")

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    return LOGIN_HTML

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    if not check_session(get_session(request)):
        return RedirectResponse(url="/login", status_code=302)
    return DASHBOARD_HTML

# ========== API ==========
@app.post("/api/login")
async def api_login(request: Request, data: Dict[str, str]):
    global password_hash
    password = data.get('password', '')
    
    if password_hash is None:
        hash_val, salt = hash_password("123456")
        save_password_hash(f"{hash_val}:{salt}")
        password_hash = f"{hash_val}:{salt}"
    
    try:
        stored_hash, salt = password_hash.split(':')
        if verify_password(password, stored_hash, salt):
            session_id = create_session()
            response = JSONResponse({"success": True})
            response.set_cookie(
                key="session",
                value=session_id,
                httponly=True,
                max_age=7*24*3600,
                secure=True,
                samesite="lax"
            )
            add_activity_log("ورود موفق", "ok", "auth")
            return response
    except:
        pass
    
    add_activity_log("ورود ناموفق", "err", "auth")
    raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")

@app.post("/api/logout")
async def api_logout(request: Request):
    session_id = get_session(request)
    if session_id and session_id in sessions:
        del sessions[session_id]
    response = JSONResponse({"success": True})
    response.delete_cookie("session")
    return response

@app.get("/api/me")
async def api_me(request: Request):
    return {"authenticated": check_session(get_session(request))}

@app.post("/api/change-password")
async def change_password(request: Request, data: Dict[str, str]):
    global password_hash
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    current = data.get('current_password', '')
    new_pass = data.get('new_password', '')
    
    if len(new_pass) < 4:
        raise HTTPException(status_code=400, detail="رمز جدید باید حداقل ۴ کاراکتر باشد")
    
    try:
        stored_hash, salt = password_hash.split(':')
        if not verify_password(current, stored_hash, salt):
            raise HTTPException(status_code=401, detail="رمز فعلی اشتباه است")
    except:
        raise HTTPException(status_code=401, detail="رمز فعلی اشتباه است")
    
    hash_val, salt = hash_password(new_pass)
    save_password_hash(f"{hash_val}:{salt}")
    password_hash = f"{hash_val}:{salt}"
    add_activity_log("رمز عبور تغییر کرد", "ok", "auth")
    return {"success": True}

# ========== API: Stats (واقعی) ==========
@app.get("/stats")
async def get_stats(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    stats_data = relay_vless.get_stats()
    
    total_links = len(links)
    active_links = sum(1 for l in links if l.get('active', False) and not l.get('expired', False))
    
    hourly = {}
    for ts, mb in stats_data.get('hourly_traffic', {}).items():
        hourly[ts] = mb * 1024 * 1024
    
    hourly_values = list(stats_data.get('hourly_traffic', {}).values())
    
    uptime_seconds = time.time() - start_time
    uptime_hours = int(uptime_seconds // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    uptime_str = f"{uptime_hours}h {uptime_minutes}m"
    
    return {
        'active_connections': stats_data.get('active_connections', 0),
        'peak_connections': stats_data.get('peak_connections', 0),
        'total_connections': stats_data.get('total_connections', 0),
        'total_traffic_mb': stats_data.get('total_traffic_mb', 0),
        'total_used_mb': stats_data.get('total_used_all_links_mb', 0),
        'links_count': total_links,
        'active_links': active_links,
        'subs_count': len(subs),
        'total_errors': len(error_logs),
        'hourly': hourly,
        'avg_hourly_mb': stats_data.get('avg_hourly_mb', 0),
        'peak_hourly_mb': stats_data.get('peak_hourly_mb', 0),
        'min_hourly_mb': stats_data.get('min_hourly_mb', 0),
        'uptime': uptime_str,
        'last_update': stats_data.get('last_update', datetime.now().isoformat()),
        'recent_errors': error_logs[-10:] if error_logs else [],
        'connections': stats_data.get('connections', [])
    }

# ========== API: Links ==========
@app.get("/api/links")
async def get_links(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for link in links:
        if link.get('expires_at'):
            try:
                exp = datetime.fromisoformat(link['expires_at'])
                link['expired'] = exp < datetime.now()
            except:
                link['expired'] = False
        else:
            link['expired'] = False
        link['used_fmt'] = fmt_bytes(link.get('used_bytes', 0))
    
    return {"links": links}

@app.post("/api/links")
async def create_link(request: Request, data: Dict[str, Any]):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    label = data.get('label', 'کانفیگ جدید')
    limit_value = float(data.get('limit_value', 0))
    limit_unit = data.get('limit_unit', 'MB')
    expires_days = int(data.get('expires_days', 0))
    note = data.get('note', '')
    sub_id = data.get('sub_id')
    protocol = data.get('protocol', 'vless-ws')
    
    if limit_value <= 0:
        limit_bytes = 0
    else:
        units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
        limit_bytes = int(limit_value * units.get(limit_unit, 1024**2))
    
    expires_at = None
    if expires_days > 0:
        expires_at = (datetime.now() + timedelta(days=expires_days)).isoformat()
    
    uuid_str = generate_uuid()
    
    link = {
        'uuid': uuid_str,
        'label': label,
        'note': note,
        'limit_bytes': limit_bytes,
        'used_bytes': 0,
        'active': True,
        'expires_at': expires_at,
        'created_at': datetime.now().isoformat(),
        'protocol': protocol,
        'sub_id': sub_id,
        'vless_link': '',
        'sub_url': ''
    }
    
    links.append(link)
    _setup_links()
    save_data()
    add_activity_log(f"کانفیگ جدید: {label}", "ok", "link")
    return {"success": True, "uuid": uuid_str}

@app.patch("/api/links/{uuid}")
async def update_link(request: Request, uuid: str, data: Dict[str, Any]):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for link in links:
        if link['uuid'] == uuid:
            if 'label' in data:
                link['label'] = data['label']
            if 'note' in data:
                link['note'] = data['note']
            if 'active' in data:
                link['active'] = bool(data['active'])
            if 'reset_usage' in data and data['reset_usage']:
                link['used_bytes'] = 0
            if 'sub_id' in data:
                link['sub_id'] = data['sub_id']
            if 'limit_value' in data:
                limit_value = float(data['limit_value'])
                limit_unit = data.get('limit_unit', 'MB')
                if limit_value <= 0:
                    link['limit_bytes'] = 0
                else:
                    units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
                    link['limit_bytes'] = int(limit_value * units.get(limit_unit, 1024**2))
            if 'expires_days' in data:
                days = int(data['expires_days'])
                if days > 0:
                    link['expires_at'] = (datetime.now() + timedelta(days=days)).isoformat()
                else:
                    link['expires_at'] = None
            
            save_data()
            add_activity_log(f"کانفیگ ویرایش شد: {link['label']}", "ok", "link")
            return {"success": True}
    
    raise HTTPException(status_code=404, detail="Link not found")

@app.delete("/api/links/{uuid}")
async def delete_link(request: Request, uuid: str):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for i, link in enumerate(links):
        if link['uuid'] == uuid:
            label = link['label']
            del links[i]
            save_data()
            add_activity_log(f"کانفیگ حذف شد: {label}", "ok", "link")
            return {"success": True}
    
    raise HTTPException(status_code=404, detail="Link not found")

# ========== API: Subs ==========
@app.get("/api/subs")
async def get_subs(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for sub in subs:
        sub_links = [l for l in links if l.get('sub_id') == sub['sub_id']]
        sub['links_count'] = len(sub_links)
        sub['active_count'] = sum(1 for l in sub_links if l.get('active', False) and not l.get('expired', False))
        sub['total_used'] = sum(l.get('used_bytes', 0) for l in sub_links)
        sub['total_used_fmt'] = fmt_bytes(sub['total_used'])
    
    return {"subs": subs}

@app.post("/api/subs")
async def create_sub(request: Request, data: Dict[str, Any]):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    name = data.get('name', 'گروه جدید')
    desc = data.get('desc', '')
    password = data.get('password', '')
    
    sub_id = secrets.token_hex(8)
    
    sub = {
        'sub_id': sub_id,
        'name': name,
        'desc': desc,
        'has_password': bool(password),
        'password_hash': None,
        'link_ids': [],
        'created_at': datetime.now().isoformat(),
        'public_url': '',
        'sub_url': ''
    }
    
    if password:
        hash_val, salt = hash_password(password)
        sub['password_hash'] = f"{hash_val}:{salt}"
    
    subs.append(sub)
    _setup_subs()
    save_data()
    add_activity_log(f"گروه جدید: {name}", "ok", "sub")
    return {"success": True, "sub_id": sub_id}

@app.patch("/api/subs/{sub_id}")
async def update_sub(request: Request, sub_id: str, data: Dict[str, Any]):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for sub in subs:
        if sub['sub_id'] == sub_id:
            if 'name' in data:
                sub['name'] = data['name']
            if 'desc' in data:
                sub['desc'] = data['desc']
            if 'link_ids' in data:
                sub['link_ids'] = data['link_ids']
            if 'password' in data and data['password']:
                hash_val, salt = hash_password(data['password'])
                sub['password_hash'] = f"{hash_val}:{salt}"
                sub['has_password'] = True
            
            save_data()
            add_activity_log(f"گروه ویرایش شد: {sub['name']}", "ok", "sub")
            return {"success": True}
    
    raise HTTPException(status_code=404, detail="Sub not found")

@app.delete("/api/subs/{sub_id}")
async def delete_sub(request: Request, sub_id: str):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for i, sub in enumerate(subs):
        if sub['sub_id'] == sub_id:
            name = sub['name']
            for link in links:
                if link.get('sub_id') == sub_id:
                    link['sub_id'] = None
            del subs[i]
            save_data()
            add_activity_log(f"گروه حذف شد: {name}", "ok", "sub")
            return {"success": True}
    
    raise HTTPException(status_code=404, detail="Sub not found")

# ========== API: Activity ==========
@app.get("/api/activity")
async def get_activity(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    return {"logs": activity_logs[-100:]}

# ========== Public Endpoints ==========
@app.get("/public/{sub_id}")
async def public_sub_page(sub_id: str):
    sub = next((s for s in subs if s['sub_id'] == sub_id), None)
    if not sub:
        raise HTTPException(status_code=404, detail="گروه یافت نشد")
    return HTMLResponse(get_public_page_html(sub_id))

@app.get("/api/public/sub/{sub_id}")
async def api_public_sub(sub_id: str, pw: Optional[str] = None):
    sub = next((s for s in subs if s['sub_id'] == sub_id), None)
    if not sub:
        raise HTTPException(status_code=404)
    
    if sub.get('has_password'):
        if not pw:
            return {"locked": True, "name": sub.get('name', 'گروه')}
        try:
            stored_hash, salt = sub['password_hash'].split(':')
            if not verify_password(pw, stored_hash, salt):
                return {"locked": True, "name": sub.get('name', 'گروه')}
        except:
            return {"locked": True, "name": sub.get('name', 'گروه')}
    
    sub_links = [l for l in links if l.get('sub_id') == sub_id and l.get('active', False)]
    total_used = sum(l.get('used_bytes', 0) for l in sub_links)
    
    result_links = []
    for l in sub_links:
        result_links.append({
            'uuid': l['uuid'],
            'label': l['label'],
            'protocol': l.get('protocol', 'vless-ws'),
            'active': l.get('active', False),
            'expired': l.get('expired', False),
            'limit_bytes': l.get('limit_bytes', 0),
            'used_bytes': l.get('used_bytes', 0),
            'used_fmt': fmt_bytes(l.get('used_bytes', 0)),
            'vless_link': l.get('vless_link', ''),
            'sub_url': l.get('sub_url', ''),
            'connections': len([c for c in relay_vless.connection_metadata.values() if c.get('uuid') == l['uuid']])
        })
    
    return {
        'name': sub.get('name', 'گروه'),
        'desc': sub.get('desc', ''),
        'locked': False,
        'links': result_links,
        'active_connections': len(relay_vless.active_connections),
        'total_used_fmt': fmt_bytes(total_used)
    }

@app.get("/sub-group/{sub_id}")
async def sub_group(sub_id: str, pw: Optional[str] = None):
    sub = next((s for s in subs if s['sub_id'] == sub_id), None)
    if not sub:
        raise HTTPException(status_code=404)
    
    if sub.get('has_password'):
        if not pw:
            raise HTTPException(status_code=401, detail="Password required")
        try:
            stored_hash, salt = sub['password_hash'].split(':')
            if not verify_password(pw, stored_hash, salt):
                raise HTTPException(status_code=401, detail="Invalid password")
        except:
            raise HTTPException(status_code=401, detail="Invalid password")
    
    sub_links = [l for l in links if l.get('sub_id') == sub_id and l.get('active', False)]
    content = "\n".join(l.get('vless_link', '') for l in sub_links if l.get('vless_link'))
    return Response(content=content.strip(), media_type="text/plain")

@app.get("/sub/{uuid}")
async def sub_single(uuid: str):
    link = next((l for l in links if l['uuid'] == uuid), None)
    if not link or not link.get('active', False):
        return Response(content="", media_type="text/plain")
    return Response(content=link.get('vless_link', ''), media_type="text/plain")

@app.get("/sub-all")
async def sub_all(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    content = "\n".join(l.get('vless_link', '') for l in links if l.get('active', False) and not l.get('expired', False))
    return Response(content=content.strip(), media_type="text/plain")

# ========== WebSocket Test ==========
@app.get("/ws-test")
async def ws_test_page():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html dir="rtl">
    <head><title>تست WebSocket</title>
    <style>body{font-family:Vazirmatn,sans-serif;background:#0f0a04;color:#fff;padding:20px}
    input,button{padding:10px;border-radius:8px;border:1px solid #F59E0B;background:#1a1208;color:#fff;font-family:inherit}
    button{background:#F59E0B;color:#0f0a04;cursor:pointer;font-weight:700}
    #log{background:#1a1208;padding:15px;border-radius:8px;margin-top:15px;max-height:400px;overflow:auto;font-size:12px;font-family:monospace;white-space:pre-wrap}</style>
    </head>
    <body>
    <h1 style="color:#FBBF24">🧪 تست WebSocket</h1>
    <input type="text" id="uuid" placeholder="UUID را وارد کنید" style="width:300px">
    <button onclick="connect()">اتصال</button>
    <button onclick="sendPing()">Ping</button>
    <button onclick="disconnect()">قطع</button>
    <div id="log">منتظر اتصال...</div>
    <script>
    let ws;
    function log(m){document.getElementById('log').textContent+=m+'\\n';}
    function connect(){
        const u=document.getElementById('uuid').value;
        if(!u){log('❌ UUID را وارد کنید');return}
        const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;
        ws=new WebSocket(url);
        ws.onopen=()=>log('✅ متصل شد');
        ws.onmessage=e=>{log('📩 دریافت: '+e.data);try{const d=JSON.parse(e.data);if(d.stats)log('📊 آمار: '+JSON.stringify(d.stats,null,2));}catch{}}
        ws.onerror=()=>log('❌ خطا');
        ws.onclose=()=>log('🔌 قطع شد');
    }
    function sendPing(){if(ws&&ws.readyState===1){ws.send(JSON.stringify({type:'ping'}));log('📤 Ping ارسال شد');}}
    function disconnect(){if(ws)ws.close();}
    </script>
    </body></html>
    """)

# ========== اجرا ==========
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run("main:app", host=host, port=port, reload=False, log_level="info")

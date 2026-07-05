# main.py - نسخه اصلاح‌شده با رفع تمام خطاها

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

from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

# ========== واردات pages ==========
from pages import LOGIN_HTML, DASHBOARD_HTML, get_public_page_html

# ========== واردات relay_vless ==========
import relay_vless

# ========== تنظیمات ==========
DATA_DIR = "/data" if os.path.exists("/data") else "data"
os.makedirs(DATA_DIR, exist_ok=True)

DATA_FILE = os.path.join(DATA_DIR, "data.json")
PASSWORD_FILE = os.path.join(DATA_DIR, "password_hash.txt")

# لاگر
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ========== مدل‌های داده ==========
class LinkData(BaseModel):
    uuid: str
    label: str
    note: str = ""
    limit_bytes: int
    used_bytes: int = 0
    active: bool = True
    expires_at: Optional[str] = None
    created_at: str
    protocol: str = "vless-ws"
    sub_id: Optional[str] = None
    vless_link: str = ""
    sub_url: str = ""

class SubData(BaseModel):
    sub_id: str
    name: str
    desc: str = ""
    has_password: bool = False
    password_hash: Optional[str] = None
    link_ids: List[str] = []
    created_at: str
    public_url: str = ""
    sub_url: str = ""

# ========== متغیرهای سراسری ==========
links: List[Dict] = []
subs: List[Dict] = []
password_hash: Optional[str] = None
activity_logs: List[Dict] = []
error_logs: List[Dict] = []

# ========== توابع کمکی ==========
def fmt_bytes(b: int) -> str:
    """فرمت‌بندی بایت‌ها"""
    if b < 1024:
        return f"{b} B"
    elif b < 1024 ** 2:
        return f"{b/1024:.1f} KB"
    elif b < 1024 ** 3:
        return f"{b/1024**2:.2f} MB"
    else:
        return f"{b/1024**3:.2f} GB"

def generate_uuid() -> str:
    """تولید UUID تصادفی"""
    import uuid
    return str(uuid.uuid4())

def hash_password(password: str, salt: Optional[str] = None) -> tuple:
    """هش کردن رمز عبور با SHA-256 + Salt"""
    if salt is None:
        salt = secrets.token_hex(16)
    combined = salt + password
    hash_val = hashlib.sha256(combined.encode()).hexdigest()
    return hash_val, salt

def verify_password(password: str, stored_hash: str, salt: str) -> bool:
    """تأیید رمز عبور"""
    combined = salt + password
    return hashlib.sha256(combined.encode()).hexdigest() == stored_hash

def load_data():
    """بارگذاری داده‌ها از فایل"""
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
        # داده‌های پیش‌فرض
        default_link = {
            'uuid': generate_uuid(),
            'label': 'Default Link',
            'note': 'لینک پیش‌فرض بدون محدودیت',
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
    
    # بارگذاری هش رمز
    if os.path.exists(PASSWORD_FILE):
        try:
            with open(PASSWORD_FILE, 'r', encoding='utf-8') as f:
                password_hash = f.read().strip()
        except:
            password_hash = None
    
    # تنظیم لینک‌ها
    _setup_links()

def save_data():
    """ذخیره داده‌ها در فایل"""
    try:
        data = {
            'links': links,
            'subs': subs
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Error saving data: {e}")

def save_password_hash(hash_val: str):
    """ذخیره هش رمز"""
    global password_hash
    password_hash = hash_val
    try:
        with open(PASSWORD_FILE, 'w', encoding='utf-8') as f:
            f.write(hash_val)
    except Exception as e:
        logger.error(f"Error saving password: {e}")

def _setup_links():
    """تنظیم لینک‌های VLESS"""
    import urllib.parse
    
    base_url = os.getenv('BASE_URL', 'https://royal-gateway.railway.app')
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    for link in links:
        # لینک اصلی
        vless_parts = [
            f"vless://{link['uuid']}",
            f"@{base_url.replace('https://', '').replace('http://', '')}",
            "?security=tls",
            "&encryption=none",
            "&headerType=ws",
            "&path=/ws",
            "&type=ws",
            f"&sni={base_url.replace('https://', '').replace('http://', '').split('/')[0]}",
            f"&fp=chrome",
            "#" + urllib.parse.quote(link['label'])
        ]
        link['vless_link'] = ''.join(vless_parts)
        
        # لینک ساب
        link['sub_url'] = f"{base_url}/sub/{link['uuid']}"

def _setup_subs():
    """تنظیم لینک‌های گروه‌ها"""
    import urllib.parse
    
    base_url = os.getenv('BASE_URL', 'https://royal-gateway.railway.app')
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    for sub in subs:
        sub['public_url'] = f"{base_url}/public/{sub['sub_id']}"
        sub['sub_url'] = f"{base_url}/sub-group/{sub['sub_id']}"

def add_activity_log(message: str, level: str = "info", kind: str = "system"):
    """افزودن لاگ فعالیت"""
    global activity_logs
    entry = {
        'time': datetime.now().isoformat(),
        'message': message,
        'level': level,
        'kind': kind
    }
    activity_logs.append(entry)
    if len(activity_logs) > 1000:
        activity_logs = activity_logs[-1000:]
    logger.info(f"[{kind}] {message}")

def add_error_log(error: str, url: Optional[str] = None):
    """افزودن لاگ خطا"""
    global error_logs
    entry = {
        'time': datetime.now().isoformat(),
        'error': error,
        'url': url
    }
    error_logs.append(entry)
    if len(error_logs) > 500:
        error_logs = error_logs[-500:]
    logger.error(f"{error} (URL: {url})")

# ========== توابع مورد نیاز relay_vless ==========

def _get_links_data() -> List[Dict]:
    """دسترسی به داده‌های لینک‌ها"""
    return links

def _get_link_by_uuid(uuid_str: str) -> Optional[Dict]:
    """دریافت لینک بر اساس UUID"""
    for link in links:
        if link.get('uuid') == uuid_str:
            return link
    return None

def _update_link_usage(uuid_str: str, bytes_used: int, direction: str = "rx"):
    """به‌روزرسانی مصرف لینک"""
    for link in links:
        if link.get('uuid') == uuid_str:
            if direction == "rx":
                link['used_bytes'] = link.get('used_bytes', 0) + bytes_used
            else:
                link['used_bytes'] = link.get('used_bytes', 0) + bytes_used
            save_data()
            break

def _add_log(message: str, level: str = "info", kind: str = "system"):
    """افزودن لاگ"""
    add_activity_log(message, level, kind)

# ========== مقداردهی relay_vless ==========

# مقداردهی relay با توابع مورد نیاز
relay_vless.initialize_relay(
    _get_links_data,
    _get_link_by_uuid,
    _update_link_usage,
    _add_log
)

# ========== اپلیکیشن FastAPI با lifespan ==========

@asynccontextmanager
async def lifespan(app: FastAPI):
    """مدیریت چرخه حیات اپلیکیشن"""
    # Startup
    logger.info("Royal Gateway v9.2 starting...")
    load_data()
    _setup_subs()
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # راه‌اندازی سرور WebSocket در پس‌زمینه
    asyncio.create_task(relay_vless.start_websocket_server(
        host="0.0.0.0",
        port=443
    ))
    
    logger.info("Royal Gateway v9.2 started successfully")
    yield
    
    # Shutdown
    logger.info("Royal Gateway shutting down...")
    # بستن اتصالات WebSocket
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

# ========== Middleware ==========

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== Session Management ==========

sessions = {}  # session_id -> expiry

def create_session() -> str:
    """ایجاد سشن جدید"""
    session_id = secrets.token_hex(32)
    sessions[session_id] = time.time() + 7 * 24 * 3600  # 7 روز
    return session_id

def check_session(session_id: Optional[str]) -> bool:
    """بررسی اعتبار سشن"""
    if not session_id:
        return False
    if session_id not in sessions:
        return False
    if sessions[session_id] < time.time():
        del sessions[session_id]
        return False
    return True

def get_session(request: Request) -> Optional[str]:
    """دریافت سشن از کوکی"""
    return request.cookies.get("session")

# ========== API Endpoints ==========

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    """صفحه ورود"""
    return LOGIN_HTML

@app.post("/api/login")
async def api_login(request: Request, data: Dict[str, str]):
    """API ورود"""
    global password_hash
    
    password = data.get('password', '')
    
    # اگر رمز تنظیم نشده، از رمز پیش‌فرض استفاده کن
    if password_hash is None:
        hash_val, salt = hash_password("123456")
        save_password_hash(f"{hash_val}:{salt}")
        password_hash = f"{hash_val}:{salt}"
    
    # بررسی رمز
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
    """خروج از سیستم"""
    session_id = get_session(request)
    if session_id and session_id in sessions:
        del sessions[session_id]
    response = JSONResponse({"success": True})
    response.delete_cookie("session")
    return response

@app.get("/api/me")
async def api_me(request: Request):
    """بررسی وضعیت احراز هویت"""
    session_id = get_session(request)
    authenticated = check_session(session_id)
    return {"authenticated": authenticated}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    """صفحه داشبورد"""
    session_id = get_session(request)
    if not check_session(session_id):
        return RedirectResponse(url="/login", status_code=302)
    return DASHBOARD_HTML

# ========== API: Stats ==========

@app.get("/stats")
async def get_stats(request: Request):
    """دریافت آمار کلی"""
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    active_links = sum(1 for l in links if l.get('active', False) and not l.get('expired', False))
    total_links = len(links)
    active_conns = relay_vless.get_connection_count()
    
    # ترافیک ساعتی
    hourly = {}
    # ... اینجا می‌توانید آمار ساعتی را محاسبه کنید
    
    # خطاهای اخیر
    recent_errors = error_logs[-10:] if error_logs else []
    
    return {
        'active_connections': active_conns,
        'links_count': total_links,
        'active_links': active_links,
        'subs_count': len(subs),
        'total_errors': len(error_logs),
        'uptime': "0h 0m",  # می‌توانید آپتایم را محاسبه کنید
        'hourly': hourly,
        'recent_errors': recent_errors
    }

# ========== API: Links ==========

@app.get("/api/links")
async def get_links(request: Request):
    """دریافت لیست کانفیگ‌ها"""
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    # محاسبه انقضا
    for link in links:
        if link.get('expires_at'):
            try:
                exp = datetime.fromisoformat(link['expires_at'])
                link['expired'] = exp < datetime.now()
            except:
                link['expired'] = False
        else:
            link['expired'] = False
        
        # فرمت مصرف
        link['used_fmt'] = fmt_bytes(link.get('used_bytes', 0))
    
    return {"links": links}

@app.post("/api/links")
async def create_link(request: Request, data: Dict[str, Any]):
    """ساخت کانفیگ جدید"""
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    label = data.get('label', 'کانفیگ جدید')
    limit_value = float(data.get('limit_value', 0))
    limit_unit = data.get('limit_unit', 'MB')
    expires_days = int(data.get('expires_days', 0))
    note = data.get('note', '')
    sub_id = data.get('sub_id')
    protocol = data.get('protocol', 'vless-ws')
    
    # محاسبه سهمیه
    if limit_value <= 0:
        limit_bytes = 0
    else:
        units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
        limit_bytes = int(limit_value * units.get(limit_unit, 1024**2))
    
    # محاسبه انقضا
    expires_at = None
    if expires_days > 0:
        expires_at = (datetime.now() + timedelta(days=expires_days)).isoformat()
    
    # ساخت UUID
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
    """ویرایش کانفیگ"""
    session_id = get_session(request)
    if not check_session(session_id):
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
    """حذف کانفیگ"""
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    global links
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
    """دریافت لیست گروه‌ها"""
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    for sub in subs:
        # تعداد لینک‌ها
        sub_links = [l for l in links if l.get('sub_id') == sub['sub_id']]
        sub['links_count'] = len(sub_links)
        sub['active_count'] = sum(1 for l in sub_links if l.get('active', False) and not l.get('expired', False))
        sub['total_used'] = sum(l.get('used_bytes', 0) for l in sub_links)
        sub['total_used_fmt'] = fmt_bytes(sub['total_used'])
    
    return {"subs": subs}

@app.post("/api/subs")
async def create_sub(request: Request, data: Dict[str, Any]):
    """ساخت گروه جدید"""
    session_id = get_session(request)
    if not check_session(session_id):
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
    """ویرایش گروه"""
    session_id = get_session(request)
    if not check_session(session_id):
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
    """حذف گروه"""
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    global subs
    for i, sub in enumerate(subs):
        if sub['sub_id'] == sub_id:
            name = sub['name']
            # حذف ارتباط با لینک‌ها
            for link in links:
                if link.get('sub_id') == sub_id:
                    link['sub_id'] = None
            del subs[i]
            save_data()
            add_activity_log(f"گروه حذف شد: {name}", "ok", "sub")
            return {"success": True}
    
    raise HTTPException(status_code=404, detail="Sub not found")

# ========== API: Activity & Errors ==========

@app.get("/api/activity")
async def get_activity(request: Request):
    """دریافت لاگ فعالیت‌ها"""
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    return {"logs": activity_logs[-100:]}

# ========== API: Change Password ==========

@app.post("/api/change-password")
async def change_password(request: Request, data: Dict[str, str]):
    """تغییر رمز عبور"""
    global password_hash
    
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    current = data.get('current_password', '')
    new_pass = data.get('new_password', '')
    
    if len(new_pass) < 4:
        raise HTTPException(status_code=400, detail="رمز جدید باید حداقل ۴ کاراکتر باشد")
    
    # بررسی رمز فعلی
    try:
        stored_hash, salt = password_hash.split(':')
        if not verify_password(current, stored_hash, salt):
            raise HTTPException(status_code=401, detail="رمز فعلی اشتباه است")
    except:
        raise HTTPException(status_code=401, detail="رمز فعلی اشتباه است")
    
    # ذخیره رمز جدید
    hash_val, salt = hash_password(new_pass)
    save_password_hash(f"{hash_val}:{salt}")
    password_hash = f"{hash_val}:{salt}"
    
    add_activity_log("رمز عبور تغییر کرد", "ok", "auth")
    return {"success": True}

# ========== Public Endpoints ==========

@app.get("/public/{sub_id}")
async def public_sub_page(sub_id: str):
    """صفحه پابلیک گروه"""
    sub = next((s for s in subs if s['sub_id'] == sub_id), None)
    if not sub:
        raise HTTPException(status_code=404, detail="گروه یافت نشد")
    
    return HTMLResponse(get_public_page_html(sub_id))

@app.get("/api/public/sub/{sub_id}")
async def api_public_sub(sub_id: str, pw: Optional[str] = None):
    """API پابلیک گروه"""
    sub = next((s for s in subs if s['sub_id'] == sub_id), None)
    if not sub:
        raise HTTPException(status_code=404, detail="گروه یافت نشد")
    
    # بررسی رمز
    if sub.get('has_password'):
        if not pw:
            return {"locked": True, "name": sub.get('name', 'گروه')}
        
        try:
            stored_hash, salt = sub['password_hash'].split(':')
            if not verify_password(pw, stored_hash, salt):
                return {"locked": True, "name": sub.get('name', 'گروه')}
        except:
            return {"locked": True, "name": sub.get('name', 'گروه')}
    
    # دریافت لینک‌های گروه
    sub_links = [l for l in links if l.get('sub_id') == sub_id and l.get('active', False)]
    
    # محاسبه آمار
    total_used = sum(l.get('used_bytes', 0) for l in sub_links)
    active_conns = 0
    for l in sub_links:
        conns = [c for c in relay_vless.connection_metadata.values() if c.get('uuid') == l['uuid']]
        active_conns += len(conns)
    
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
        'active_connections': active_conns,
        'total_used_fmt': fmt_bytes(total_used)
    }

@app.get("/sub-group/{sub_id}")
async def sub_group(sub_id: str, pw: Optional[str] = None):
    """لینک سابسکریپشن گروه"""
    sub = next((s for s in subs if s['sub_id'] == sub_id), None)
    if not sub:
        raise HTTPException(status_code=404)
    
    # بررسی رمز
    if sub.get('has_password'):
        if not pw:
            raise HTTPException(status_code=401, detail="Password required")
        
        try:
            stored_hash, salt = sub['password_hash'].split(':')
            if not verify_password(pw, stored_hash, salt):
                raise HTTPException(status_code=401, detail="Invalid password")
        except:
            raise HTTPException(status_code=401, detail="Invalid password")
    
    # تولید سابسکریپشن
    sub_links = [l for l in links if l.get('sub_id') == sub_id and l.get('active', False)]
    
    if not sub_links:
        return Response(content="", media_type="text/plain")
    
    # ساخت محتوای ساب (فرمت VLESS)
    content = ""
    for l in sub_links:
        if l.get('vless_link'):
            content += l['vless_link'] + "\n"
    
    return Response(content=content.strip(), media_type="text/plain")

@app.get("/sub/{uuid}")
async def sub_single(uuid: str):
    """سابسکریپشن تکی"""
    link = next((l for l in links if l['uuid'] == uuid), None)
    if not link:
        raise HTTPException(status_code=404)
    
    if not link.get('active', False):
        return Response(content="", media_type="text/plain")
    
    content = link.get('vless_link', '')
    return Response(content=content, media_type="text/plain")

@app.get("/sub-all")
async def sub_all(request: Request):
    """سابسکریپشن کامل (فقط ادمین)"""
    session_id = get_session(request)
    if not check_session(session_id):
        raise HTTPException(status_code=401)
    
    content = ""
    for l in links:
        if l.get('active', False) and not l.get('expired', False):
            if l.get('vless_link'):
                content += l['vless_link'] + "\n"
    
    return Response(content=content.strip(), media_type="text/plain")

# ========== WebSocket Test Endpoint ==========

@app.get("/ws-test")
async def ws_test_page():
    """صفحه تست WebSocket"""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head><title>WebSocket Test</title></head>
    <body>
        <h1>WebSocket Test</h1>
        <input type="text" id="uuid" placeholder="Enter UUID">
        <button onclick="connect()">Connect</button>
        <button onclick="send()">Send</button>
        <button onclick="disconnect()">Disconnect</button>
        <pre id="log"></pre>
        <script>
            let ws;
            function log(msg) {
                document.getElementById('log').textContent += msg + '\\n';
            }
            function connect() {
                const uuid = document.getElementById('uuid').value;
                const url = (location.protocol === 'https:' ? 'wss:' : 'ws:') + '//' + location.host + '/ws/' + uuid;
                ws = new WebSocket(url);
                ws.onopen = () => log('[OPEN] Connected');
                ws.onmessage = (e) => log('[MSG] ' + e.data);
                ws.onerror = () => log('[ERROR] Connection failed');
                ws.onclose = () => log('[CLOSE] Disconnected');
            }
            function send() {
                if (ws && ws.readyState === 1) {
                    ws.send('Hello from test!');
                    log('[SEND] Hello from test!');
                }
            }
            function disconnect() {
                if (ws) ws.close();
            }
        </script>
    </body>
    </html>
    """)

# ========== روت اصلی ==========

@app.get("/")
async def root(request: Request):
    """ریشه سایت"""
    session_id = get_session(request)
    if check_session(session_id):
        return RedirectResponse(url="/dashboard")
    return RedirectResponse(url="/login")

# ========== اجرا ==========

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=False,
        log_level="info"
    )

# main.py - نسخه ساده شده با رفع خطای activity_logs

import os
import json
import hashlib
import secrets
import logging
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from pages import LOGIN_HTML, DASHBOARD_HTML, get_public_page_html

# ========== تنظیمات ==========
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

DATA_FILE = os.path.join(DATA_DIR, "data.json")
PASSWORD_FILE = os.path.join(DATA_DIR, "password.txt")

# ========== متغیرهای سراسری ==========
links: List[Dict] = []
subs: List[Dict] = []
password_hash: str = ""
password_salt: str = ""
active_websockets: Dict[str, Dict] = {}
traffic_stats = {'total_bytes': 0, 'hourly': {}, 'last_update': None}
activity_logs: List[Dict] = []
error_logs: List[Dict] = []
start_time = time.time()
sessions: Dict[str, float] = {}

# ========== توابع لاگ - ساده شده ==========
def add_activity_log(message: str, level: str = "info", kind: str = "system"):
    """افزودن لاگ فعالیت - بدون استفاده از global"""
    try:
        entry = {
            'time': datetime.now().isoformat(),
            'message': message,
            'level': level,
            'kind': kind
        }
        # مستقیم به لیست اضافه می‌کنیم
        activity_logs.append(entry)
        if len(activity_logs) > 500:
            activity_logs[:] = activity_logs[-500:]
        logger.info(f"[{kind}] {message}")
    except Exception as e:
        logger.error(f"Error in add_activity_log: {e}")

def add_error_log(error: str, url: Optional[str] = None):
    """افزودن لاگ خطا"""
    try:
        entry = {
            'time': datetime.now().isoformat(),
            'error': error,
            'url': url
        }
        error_logs.append(entry)
        if len(error_logs) > 200:
            error_logs[:] = error_logs[-200:]
        logger.error(f"{error}")
    except Exception as e:
        logger.error(f"Error in add_error_log: {e}")

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

# ========== توابع داده ==========
def load_data():
    global links, subs, password_hash, password_salt
    
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
                content = f.read().strip()
                if ':' in content:
                    password_hash, password_salt = content.split(':', 1)
                else:
                    password_hash = content
                    password_salt = secrets.token_hex(16)
        except Exception as e:
            logger.error(f"Error loading password: {e}")
            password_hash, password_salt = hash_password("123456")
            save_password()
    else:
        password_hash, password_salt = hash_password("123456")
        save_password()
    
    setup_links()
    setup_subs()
    
    logger.info(f"Data loaded: {len(links)} links, {len(subs)} subs")

def save_data():
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({'links': links, 'subs': subs}, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Error saving data: {e}")

def save_password():
    global password_hash, password_salt
    try:
        with open(PASSWORD_FILE, 'w', encoding='utf-8') as f:
            f.write(f"{password_hash}:{password_salt}")
    except Exception as e:
        logger.error(f"Error saving password: {e}")

def setup_links():
    base_url = os.getenv('BASE_URL', 'http://localhost:8000')
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    host = base_url.replace('https://', '').replace('http://', '').split('/')[0]
    
    for link in links:
        import urllib.parse
        link['vless_link'] = f"vless://{link['uuid']}@{host}?security=tls&encryption=none&headerType=ws&path=/ws&type=ws&sni={host}&fp=chrome#{urllib.parse.quote(link['label'])}"
        link['sub_url'] = f"{base_url}/sub/{link['uuid']}"

def setup_subs():
    base_url = os.getenv('BASE_URL', 'http://localhost:8000')
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    for sub in subs:
        sub['public_url'] = f"{base_url}/public/{sub['sub_id']}"
        sub['sub_url'] = f"{base_url}/sub-group/{sub['sub_id']}"

# ========== Session ==========
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

# ========== FastAPI ==========
app = FastAPI(title="Royal Gateway", version="9.2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== WebSocket ==========
@app.websocket("/ws/{uuid}")
async def websocket_endpoint(websocket: WebSocket, uuid: str):
    await websocket.accept()
    
    link = next((l for l in links if l.get('uuid') == uuid), None)
    
    if not link:
        await websocket.send_text("ERROR: Invalid UUID")
        await websocket.close()
        return
    
    if not link.get('active', False):
        await websocket.send_text("ERROR: Link inactive")
        await websocket.close()
        return
    
    ws_id = str(int(time.time() * 1000)) + secrets.token_hex(4)
    active_websockets[ws_id] = {
        'uuid': uuid,
        'label': link.get('label', 'Unknown'),
        'connected_at': time.time()
    }
    
    try:
        while True:
            data = await websocket.receive()
            if data.get('type') == 'websocket.receive':
                if 'bytes' in data:
                    size = len(data['bytes'])
                    link['used_bytes'] = link.get('used_bytes', 0) + size
                    traffic_stats['total_bytes'] += size
                    save_data()
                    await websocket.send_bytes(data['bytes'])
                elif 'text' in data:
                    await websocket.send_text(f"Echo: {data['text']}")
    except WebSocketDisconnect:
        pass
    finally:
        if ws_id in active_websockets:
            del active_websockets[ws_id]

# ========== Routes ==========
@app.get("/")
async def root(request: Request):
    if check_session(get_session(request)):
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
async def api_login(data: Dict[str, str]):
    global password_hash, password_salt
    
    password = data.get('password', '')
    logger.info(f"Login attempt with password: {password}")
    
    # اطمینان از وجود رمز
    if not password_hash:
        password_hash, password_salt = hash_password("123456")
        save_password()
        logger.info("Default password created")
    
    try:
        if verify_password(password, password_hash, password_salt):
            session_id = create_session()
            response = JSONResponse({"success": True})
            response.set_cookie(
                key="session",
                value=session_id,
                httponly=True,
                max_age=7*24*3600,
                secure=False,
                samesite="lax",
                path="/"
            )
            logger.info("Login successful")
            return response
        else:
            logger.warning("Login failed: wrong password")
            raise HTTPException(status_code=401, detail="رمز عبور اشتباه است")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Login error: {e}")
        raise HTTPException(status_code=500, detail=f"خطا: {str(e)}")

@app.post("/api/logout")
async def api_logout(request: Request):
    session_id = get_session(request)
    if session_id and session_id in sessions:
        del sessions[session_id]
    response = JSONResponse({"success": True})
    response.delete_cookie("session", path="/")
    return response

@app.get("/api/me")
async def api_me(request: Request):
    return {"authenticated": check_session(get_session(request))}

# ========== API: Stats ==========
@app.get("/stats")
async def get_stats(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    total_links = len(links)
    active_links = sum(1 for l in links if l.get('active', False) and not l.get('expired', False))
    total_used_bytes = sum(l.get('used_bytes', 0) for l in links)
    
    uptime_seconds = time.time() - start_time
    uptime_str = f"{int(uptime_seconds // 3600)}h {int((uptime_seconds % 3600) // 60)}m"
    
    return {
        'active_connections': len(active_websockets),
        'links_count': total_links,
        'active_links': active_links,
        'subs_count': len(subs),
        'total_errors': 0,
        'total_traffic_mb': traffic_stats['total_bytes'] / (1024 * 1024),
        'total_used_mb': total_used_bytes / (1024 * 1024),
        'hourly': traffic_stats['hourly'],
        'avg_hourly_mb': 0,
        'peak_hourly_mb': 0,
        'min_hourly_mb': 0,
        'uptime': uptime_str,
        'last_update': datetime.now().isoformat(),
        'recent_errors': []
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
    setup_links()
    save_data()
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
    setup_subs()
    save_data()
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
            return {"success": True}
    
    raise HTTPException(status_code=404, detail="Sub not found")

# ========== API: Activity ==========
@app.get("/api/activity")
async def get_activity(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    return {"logs": []}

# ========== Public ==========
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
        conns = [w for w in active_websockets.values() if w.get('uuid') == l['uuid']]
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
            'connections': len(conns)
        })
    
    return {
        'name': sub.get('name', 'گروه'),
        'desc': sub.get('desc', ''),
        'locked': False,
        'links': result_links,
        'active_connections': len(active_websockets),
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
    <head><meta charset="UTF-8"><title>تست WebSocket</title>
    <style>
        body{font-family:Vazirmatn;background:#0f0a04;color:#FFF8ED;padding:30px}
        input,button{padding:12px 16px;border-radius:10px;border:1px solid #F59E0B;background:#1a1208;color:#FFF8ED;font-family:inherit;font-size:14px}
        button{background:linear-gradient(135deg,#F59E0B,#D97706);color:#0f0a04;cursor:pointer;font-weight:700;border:none}
        button:hover{transform:translateY(-2px)}
        .box{background:#1a1208;border:1px solid rgba(245,158,11,0.1);border-radius:12px;padding:20px;margin-top:15px;max-height:400px;overflow:auto;font-family:monospace;font-size:12px;white-space:pre-wrap}
        .status{display:inline-block;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:700}
        .status.on{background:#10B981;color:#fff}
        .status.off{background:#EF4444;color:#fff}
    </style>
    </head>
    <body>
        <h1 style="color:#FBBF24">🧪 تست WebSocket</h1>
        <p style="color:#8B7A5A">UUID یک کانفیگ فعال را وارد کنید</p>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin:15px 0">
            <input type="text" id="uuid" placeholder="UUID" style="flex:1;min-width:200px">
            <button onclick="connect()">🟢 اتصال</button>
            <button onclick="sendMsg()">📤 ارسال</button>
            <button onclick="disconnect()">🔴 قطع</button>
        </div>
        <div>وضعیت: <span class="status off" id="status">قطع</span></div>
        <div class="box" id="log">منتظر اتصال...</div>
        <script>
            let ws;
            function log(m){const el=document.getElementById('log');el.textContent+=m+'\\n';el.scrollTop=el.scrollHeight;}
            function setStatus(on){const el=document.getElementById('status');el.className='status '+(on?'on':'off');el.textContent=on?'🟢 متصل':'🔴 قطع';}
            function connect(){
                const u=document.getElementById('uuid').value.trim();
                if(!u){log('❌ UUID را وارد کنید');return}
                const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;
                log('🔄 اتصال به: '+url);
                ws=new WebSocket(url);
                ws.onopen=()=>{log('✅ متصل شد');setStatus(true);};
                ws.onmessage=(e)=>{log('📩 دریافت: '+e.data);};
                ws.onerror=()=>{log('❌ خطا');setStatus(false);};
                ws.onclose=()=>{log('🔌 قطع شد');setStatus(false);};
            }
            function sendMsg(){
                if(!ws||ws.readyState!==1){log('❌ اتصال برقرار نیست');return;}
                ws.send('سلام از تست!');
                log('📤 ارسال شد');
            }
            function disconnect(){if(ws){ws.close();log('🔌 قطع');setStatus(false);}}
        </script>
    </body>
    </html>
    """)

# ========== اجرا ==========
if __name__ == "__main__":
    load_data()
    
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port, reload=False, log_level="info")

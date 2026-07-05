# main.py - Royal Gateway v9.2 (یکپارچه کامل)

import os
import json
import hashlib
import secrets
import logging
import time
import asyncio
import socket
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, StreamingResponse
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
LINKS: Dict[str, Dict] = {}
SUBS: List[Dict] = []
password_hash: str = ""
password_salt: str = ""
active_connections: Dict[str, Dict] = {}
traffic_stats = {'total_bytes': 0, 'hourly': {}, 'last_update': None}
activity_logs: List[Dict] = []
error_logs: List[Dict] = []
start_time = time.time()
sessions: Dict[str, float] = {}

# قفل‌ها
LINKS_LOCK = asyncio.Lock()
XHTTP_LOCK = asyncio.Lock()

# ========== تنظیمات XHTTP ==========
XHTTP_BUF = 512 * 1024
DOWNLINK_QUEUE_MAX = 512
SESSION_IDLE_TIMEOUT = 30
REAPER_INTERVAL = 10
TCP_CONNECT_TIMEOUT = 10.0

SOCK_BUF_SIZE = 2 * 1024 * 1024
FLOW_MIN_HW = 256 * 1024
FLOW_MAX_HW = 16 * 1024 * 1024
FLOW_START_HW = 2 * 1024 * 1024
FLOW_FAST_DRAIN_MS = 2.0
FLOW_SLOW_DRAIN_MS = 25.0

QUOTA_MIN_BATCH = 32 * 1024
QUOTA_MAX_BATCH = 1 * 1024 * 1024
QUOTA_START_BATCH = 64 * 1024
QUOTA_CHECK_INTERVAL = 0.2

PACKET_UP_HIGH_WATER = 2 * 1024 * 1024

xhttp_sessions: dict = {}

FINGERPRINTS = {
    "chrome": {
        "content-type": "application/grpc",
        "cache-control": "no-cache, no-store",
        "x-accel-buffering": "no",
        "server": "cloudflare",
    },
    "plain": {
        "content-type": "application/octet-stream",
        "cache-control": "no-store",
        "x-accel-buffering": "no",
    },
}
DEFAULT_FINGERPRINT = "chrome"

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

def now_ir():
    return datetime.now()

def hash_password(password: str, salt: Optional[str] = None) -> tuple:
    if salt is None:
        salt = secrets.token_hex(16)
    combined = salt + password
    hash_val = hashlib.sha256(combined.encode()).hexdigest()
    return hash_val, salt

def verify_password(password: str, stored_hash: str, salt: str) -> bool:
    combined = salt + password
    return hashlib.sha256(combined.encode()).hexdigest() == stored_hash

def is_link_allowed(link: Optional[Dict]) -> bool:
    if not link:
        return False
    if not link.get('active', False):
        return False
    if link.get('expired', False):
        return False
    limit = link.get('limit_bytes', 0)
    used = link.get('used_bytes', 0)
    if limit > 0 and used >= limit:
        return False
    return True

def log_activity(kind: str, message: str, level: str = "info"):
    entry = {
        'time': datetime.now().isoformat(),
        'kind': kind,
        'message': message,
        'level': level
    }
    activity_logs.append(entry)
    if len(activity_logs) > 500:
        activity_logs[:] = activity_logs[-500:]
    logger.info(f"[{kind}] {message}")

def add_error_log(error: str, url: Optional[str] = None):
    entry = {
        'time': datetime.now().isoformat(),
        'error': error,
        'url': url
    }
    error_logs.append(entry)
    if len(error_logs) > 200:
        error_logs[:] = error_logs[-200:]
    logger.error(f"{error}")

# ========== توابع داده ==========
def load_data():
    global LINKS, SUBS, password_hash, password_salt
    
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                links_list = data.get('links', [])
                SUBS = data.get('subs', [])
                LINKS = {l['uuid']: l for l in links_list}
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            LINKS = {}
            SUBS = []
    else:
        default_uuid = generate_uuid()
        default_link = {
            'uuid': default_uuid,
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
        LINKS = {default_uuid: default_link}
        SUBS = []
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
    
    logger.info(f"Data loaded: {len(LINKS)} links, {len(SUBS)} subs")

def save_data():
    try:
        links_list = list(LINKS.values())
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({'links': links_list, 'subs': SUBS}, f, ensure_ascii=False, indent=2)
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
    
    for uuid, link in LINKS.items():
        import urllib.parse
        link['vless_link'] = f"vless://{uuid}@{host}?security=tls&encryption=none&headerType=ws&path=/ws&type=ws&sni={host}&fp=chrome#{urllib.parse.quote(link['label'])}"
        link['sub_url'] = f"{base_url}/sub/{uuid}"

def setup_subs():
    base_url = os.getenv('BASE_URL', 'http://localhost:8000')
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    for sub in SUBS:
        sub['public_url'] = f"{base_url}/public/{sub['sub_id']}"
        sub['sub_url'] = f"{base_url}/sub-group/{sub['sub_id']}"

# ========== توابع VLESS ==========
RELAY_BUF = 256 * 1024

def _ws_client_ip(ws: WebSocket) -> str:
    fwd = ws.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = ws.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return ws.client.host if ws.client else "نامشخص"

async def parse_vless_header(chunk: bytes):
    if len(chunk) < 24:
        raise ValueError("chunk too small")
    pos = 1
    pos += 16
    addon_len = chunk[pos]
    pos += 1 + addon_len
    command = chunk[pos]
    pos += 1
    port = int.from_bytes(chunk[pos:pos+2], "big")
    pos += 2
    addr_type = chunk[pos]
    pos += 1
    if addr_type == 1:
        address = ".".join(str(b) for b in chunk[pos:pos+4])
        pos += 4
    elif addr_type == 2:
        dlen = chunk[pos]
        pos += 1
        address = chunk[pos:pos+dlen].decode("utf-8", errors="ignore")
        pos += dlen
    elif addr_type == 3:
        ab = chunk[pos:pos+16]
        pos += 16
        address = ":".join(f"{ab[i]:02x}{ab[i+1]:02x}" for i in range(0, 16, 2))
    else:
        raise ValueError(f"unknown addr type: {addr_type}")
    return command, address, port, chunk[pos:]

async def check_and_use(uid: str, n: int) -> bool:
    async with LINKS_LOCK:
        link = LINKS.get(uid)
        if link is None:
            return False
        if not is_link_allowed(link):
            return False
        link["used_bytes"] = link.get("used_bytes", 0) + n
        traffic_stats["total_bytes"] += n
        hour_key = datetime.now().strftime("%H:00")
        if hour_key not in traffic_stats["hourly"]:
            traffic_stats["hourly"][hour_key] = 0
        traffic_stats["hourly"][hour_key] += n
    return True

async def relay_ws_to_tcp(ws: WebSocket, writer: asyncio.StreamWriter, conn_id: str, uid: str):
    try:
        while True:
            msg = await ws.receive()
            if msg["type"] == "websocket.disconnect":
                break
            data = msg.get("bytes") or (msg.get("text") or "").encode()
            if not data:
                continue
            if not await check_and_use(uid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            if conn_id in active_connections:
                active_connections[conn_id]["bytes"] = active_connections[conn_id].get("bytes", 0) + len(data)
            writer.write(data)
            if writer.transport.get_write_buffer_size() > RELAY_BUF:
                await writer.drain()
    except (WebSocketDisconnect, Exception):
        pass
    finally:
        try:
            writer.write_eof()
        except Exception:
            pass

async def relay_tcp_to_ws(ws: WebSocket, reader: asyncio.StreamReader, conn_id: str, uid: str):
    first = True
    try:
        while True:
            data = await reader.read(RELAY_BUF)
            if not data:
                break
            if not await check_and_use(uid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            if conn_id in active_connections:
                active_connections[conn_id]["bytes"] = active_connections[conn_id].get("bytes", 0) + len(data)
            payload = (b"\x00\x00" + data) if first else data
            first = False
            await ws.send_bytes(payload)
    except Exception:
        pass

async def websocket_tunnel(ws: WebSocket, uuid: str):
    await ws.accept()

    link = LINKS.get(uuid)

    if not is_link_allowed(link):
        logger.warning(f"WS rejected uuid={uuid[:8]}…")
        await ws.close(code=1008, reason="not authorized")
        return

    ip = _ws_client_ip(ws)
    conn_id = secrets.token_urlsafe(6)
    active_connections[conn_id] = {
        "uuid": uuid,
        "ip": ip,
        "transport": "vless-ws",
        "connected_at": datetime.now().isoformat(),
        "bytes": 0,
    }
    logger.info(f"WS [{conn_id}] uuid={uuid[:8]}… ip={ip}")
    log_activity("connection", f"اتصال جدید از {ip} (کانفیگ {link.get('label','?')})", "info")
    writer = None

    try:
        first_msg = await asyncio.wait_for(ws.receive(), timeout=15.0)
        if first_msg["type"] == "websocket.disconnect":
            return
        first_chunk = first_msg.get("bytes") or (first_msg.get("text") or "").encode()
        if not first_chunk:
            return

        command, address, port, payload = await parse_vless_header(first_chunk)

        if not await check_and_use(uuid, len(first_chunk)):
            await ws.close(code=1008, reason="quota/disabled")
            return

        if conn_id in active_connections:
            active_connections[conn_id]["bytes"] = active_connections[conn_id].get("bytes", 0) + len(first_chunk)
        logger.info(f"[{conn_id}] → {address}:{port}")

        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(address, port),
            timeout=10.0
        )
        sock = writer.transport.get_extra_info('socket')
        if sock:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        if payload:
            writer.write(payload)
            await writer.drain()

        done, pending = await asyncio.wait(
            {
                asyncio.create_task(relay_ws_to_tcp(ws, writer, conn_id, uuid)),
                asyncio.create_task(relay_tcp_to_ws(ws, reader, conn_id, uuid)),
            },
            return_when=asyncio.FIRST_COMPLETED,
        )
        for t in pending:
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass

        asyncio.create_task(save_data())

    except WebSocketDisconnect:
        pass
    except asyncio.TimeoutError:
        error_logs.append({"error": "connection timeout", "time": datetime.now().isoformat()})
    except Exception as exc:
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        logger.error(f"WS error [{conn_id}]: {exc}")
    finally:
        if writer:
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        active_connections.pop(conn_id, None)
        logger.info(f"WS closed [{conn_id}] total={len(active_connections)}")

# ========== توابع XHTTP ==========
def _resp_headers(fp: str) -> dict:
    return dict(FINGERPRINTS.get(fp, FINGERPRINTS[DEFAULT_FINGERPRINT]))

def _tune_socket(writer: asyncio.StreamWriter):
    sock = writer.transport.get_extra_info("socket")
    if not sock:
        return
    try:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUF_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUF_SIZE)
    except OSError:
        pass

class _QuotaGate:
    __slots__ = ("uuid", "pending", "last_check", "ok", "batch_bytes", "rate_ewma")

    def __init__(self, uuid: str):
        self.uuid = uuid
        self.pending = 0
        self.last_check = time.monotonic()
        self.ok = True
        self.batch_bytes = QUOTA_START_BATCH
        self.rate_ewma = 0.0

    async def add(self, nbytes: int) -> bool:
        if not self.ok:
            return False
        self.pending += nbytes
        now = time.monotonic()
        elapsed = now - self.last_check
        if self.pending >= self.batch_bytes or elapsed >= QUOTA_CHECK_INTERVAL:
            flush, self.pending = self.pending, 0
            if elapsed > 0:
                inst_rate = flush / elapsed
                self.rate_ewma = inst_rate if self.rate_ewma == 0 else (0.7 * self.rate_ewma + 0.3 * inst_rate)
                target = int(self.rate_ewma * QUOTA_CHECK_INTERVAL)
                self.batch_bytes = max(QUOTA_MIN_BATCH, min(QUOTA_MAX_BATCH, target or QUOTA_MIN_BATCH))
            self.last_check = now
            self.ok = await check_and_use(self.uuid, flush)
            return self.ok
        return True

    async def flush(self) -> bool:
        if self.pending:
            flush, self.pending = self.pending, 0
            self.ok = self.ok and await check_and_use(self.uuid, flush)
        return self.ok

class _AdaptiveFlow:
    __slots__ = ("high_water", "last_drain_ms")

    def __init__(self):
        self.high_water = FLOW_START_HW
        self.last_drain_ms = 0.0

    def should_drain(self, buf_size: int) -> bool:
        return buf_size > self.high_water

    async def drain(self, writer: asyncio.StreamWriter):
        t0 = time.monotonic()
        await writer.drain()
        elapsed_ms = (time.monotonic() - t0) * 1000
        self.last_drain_ms = elapsed_ms
        if elapsed_ms < FLOW_FAST_DRAIN_MS:
            self.high_water = min(FLOW_MAX_HW, int(self.high_water * 1.5) + 65536)
        elif elapsed_ms > FLOW_SLOW_DRAIN_MS:
            self.high_water = max(FLOW_MIN_HW, self.high_water // 2)

def _req_client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"

async def _open_tcp_from_header(first_chunk: bytes):
    command, address, port, payload = await parse_vless_header(first_chunk)
    reader, writer = await asyncio.wait_for(
        asyncio.open_connection(address, port), timeout=TCP_CONNECT_TIMEOUT
    )
    _tune_socket(writer)
    if payload:
        writer.write(payload)
        await writer.drain()
    return reader, writer, address, port

async def _check_link(uuid: str):
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not is_link_allowed(link):
        raise HTTPException(status_code=403, detail="not authorized")

async def _get_or_create_session(uuid: str, mode: str, session_id: str, ip: str = "نامشخص") -> dict:
    async with XHTTP_LOCK:
        sess = xhttp_sessions.get(session_id)
        if sess is not None:
            sess["last_seen"] = time.time()
            return sess
        conn_id = secrets.token_urlsafe(6)
        active_connections[conn_id] = {
            "uuid": uuid,
            "ip": ip,
            "connected_at": datetime.now().isoformat(),
            "bytes": 0,
            "transport": f"xhttp-{mode}",
        }
        sess = {
            "uuid": uuid, "mode": mode, "writer": None,
            "downlink_task": None, "uplink_task": None,
            "down_q": asyncio.Queue(maxsize=DOWNLINK_QUEUE_MAX),
            "last_seen": time.time(),
            "conn_id": conn_id, "tcp_open": False, "closed": False,
            "seq_buf": {}, "next_seq": 0,
            "gate": None,
            "flow": None,
        }
        xhttp_sessions[session_id] = sess
        logger.info(f"new XHTTP[{mode}] session [{session_id[:8]}] uuid={uuid[:8]}")
        return sess

async def _teardown(session_id: str):
    async with XHTTP_LOCK:
        sess = xhttp_sessions.pop(session_id, None)
    if not sess:
        return
    sess["closed"] = True
    for t in ("uplink_task", "downlink_task"):
        task = sess.get(t)
        if task:
            task.cancel()
            try:
                await task
            except (asyncio.CancelledError, Exception):
                pass
    writer = sess.get("writer")
    if writer:
        try:
            writer.close()
            await writer.wait_closed()
        except Exception:
            pass
    active_connections.pop(sess.get("conn_id"), None)
    dq = sess.get("down_q")
    if dq:
        try:
            dq.put_nowait(None)
        except Exception:
            pass
    logger.info(f"closed XHTTP[{sess.get('mode')}] [{session_id[:8]}] total={len(xhttp_sessions)}")

async def _reaper():
    while True:
        await asyncio.sleep(REAPER_INTERVAL)
        now = time.time()
        async with XHTTP_LOCK:
            stale = [sid for sid, s in xhttp_sessions.items()
                     if now - s["last_seen"] > SESSION_IDLE_TIMEOUT and not s.get("tcp_open")]
        for sid in stale:
            await _teardown(sid)

_reaper_started = False

def ensure_reaper():
    global _reaper_started
    if not _reaper_started:
        asyncio.create_task(_reaper())
        _reaper_started = True

async def _pump_tcp_to_queue(session_id: str, uuid: str, reader: asyncio.StreamReader, down_q: asyncio.Queue):
    first = True
    gate = _QuotaGate(uuid)
    try:
        while True:
            data = await reader.read(XHTTP_BUF)
            if not data:
                break
            if not await gate.add(len(data)):
                break
            async with XHTTP_LOCK:
                sess = xhttp_sessions.get(session_id)
            if sess:
                c = active_connections.get(sess["conn_id"])
                if c:
                    c["bytes"] += len(data)
            payload = (b"\x00\x00" + data) if first else data
            first = False
            await down_q.put(payload)
    except (asyncio.CancelledError, Exception):
        pass
    finally:
        await gate.flush()
        await _teardown(session_id)

async def _open_tcp_for_session(session_id: str, uuid: str, sess: dict, first_chunk: bytes):
    reader, writer, address, port = await _open_tcp_from_header(first_chunk)
    logger.info(f"connect XHTTP[{sess['mode']}] [{session_id[:8]}] -> {address}:{port}")
    sess["writer"] = writer
    sess["tcp_open"] = True
    sess["downlink_task"] = asyncio.create_task(
        _pump_tcp_to_queue(session_id, uuid, reader, sess["down_q"])
    )
    asyncio.create_task(save_data())

def _downstream_gen(sess: dict):
    async def gen():
        try:
            while True:
                chunk = await sess["down_q"].get()
                if chunk is None:
                    break
                sess["last_seen"] = time.time()
                yield chunk
        finally:
            pass
    return gen()

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
    await websocket_tunnel(websocket, uuid)

# ========== XHTTP Routes ==========
@app.get("/xhttp-siz10/{mode}/{uuid}/{session_id}")
async def xhttp_downlink(mode: str, uuid: str, session_id: str, request: Request):
    ensure_reaper()
    if mode not in ("packet-up", "stream-up"):
        raise HTTPException(status_code=404, detail="unknown mode")
    await _check_link(uuid)
    fp = request.query_params.get("fp", DEFAULT_FINGERPRINT)
    sess = await _get_or_create_session(uuid, mode, session_id, _req_client_ip(request))
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")

    headers = _resp_headers(fp)
    return StreamingResponse(_downstream_gen(sess), headers=headers, media_type=headers["content-type"])

@app.post("/xhttp-siz10/packet-up/{uuid}/{session_id}/{seq}")
async def packet_up_upload(uuid: str, session_id: str, seq: int, request: Request):
    ensure_reaper()
    sess = await _get_or_create_session(uuid, "packet-up", session_id, _req_client_ip(request))
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")

    sess["last_seen"] = time.time()
    body = await request.body()
    if not body:
        return {"ok": True}

    if not await check_and_use(uuid, len(body)):
        await _teardown(session_id)
        raise HTTPException(status_code=403, detail="quota/disabled/unknown")

    if sess["conn_id"] in active_connections:
        active_connections[sess["conn_id"]]["bytes"] += len(body)

    try:
        if sess["writer"] is None:
            if seq != 0:
                sess["seq_buf"][seq] = body
                return {"ok": True, "buffered": True}
            await _open_tcp_for_session(session_id, uuid, sess, body)
            nxt = 1
            while nxt in sess["seq_buf"]:
                pending = sess["seq_buf"].pop(nxt)
                sess["writer"].write(pending)
                nxt += 1
            sess["next_seq"] = nxt
            return {"ok": True, "connected": True}

        if seq == sess["next_seq"]:
            sess["writer"].write(body)
            sess["next_seq"] += 1
            while sess["next_seq"] in sess["seq_buf"]:
                pending = sess["seq_buf"].pop(sess["next_seq"])
                sess["writer"].write(pending)
                sess["next_seq"] += 1
        else:
            sess["seq_buf"][seq] = body

        if sess["writer"].transport.get_write_buffer_size() > PACKET_UP_HIGH_WATER:
            await sess["writer"].drain()
    except Exception as exc:
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        await _teardown(session_id)
        raise HTTPException(status_code=502, detail="write failed")

    return {"ok": True}

@app.post("/xhttp-siz10/stream-up/{uuid}/{session_id}")
async def stream_up_upload(uuid: str, session_id: str, request: Request):
    ensure_reaper()
    sess = await _get_or_create_session(uuid, "stream-up", session_id, _req_client_ip(request))
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")

    gate = sess.get("gate")
    if gate is None:
        gate = _QuotaGate(uuid)
        sess["gate"] = gate

    flow = sess.get("flow")
    if flow is None:
        flow = _AdaptiveFlow()
        sess["flow"] = flow

    conn = active_connections.get(sess["conn_id"])
    writer = sess["writer"]

    try:
        async for chunk in request.stream():
            if not chunk:
                continue
            sess["last_seen"] = time.time()

            if not await gate.add(len(chunk)):
                raise HTTPException(status_code=403, detail="quota/disabled/unknown")

            if conn:
                conn["bytes"] += len(chunk)

            if writer is None:
                await _open_tcp_for_session(session_id, uuid, sess, chunk)
                writer = sess["writer"]
                continue

            writer.write(chunk)
            if flow.should_drain(writer.transport.get_write_buffer_size()):
                await flow.drain(writer)
    except HTTPException:
        await gate.flush()
        await _teardown(session_id)
        raise
    except Exception as exc:
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        await gate.flush()
        await _teardown(session_id)
        raise HTTPException(status_code=502, detail="stream error")

    await gate.flush()
    return {"ok": True}

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
    
    if not password_hash:
        password_hash, password_salt = hash_password("123456")
        save_password()
    
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
            log_activity("auth", "ورود موفق", "info")
            return response
        else:
            log_activity("auth", "ورود ناموفق - رمز اشتباه", "error")
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

@app.post("/api/change-password")
async def change_password(request: Request, data: Dict[str, str]):
    global password_hash, password_salt
    
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    current = data.get('current_password', '')
    new_pass = data.get('new_password', '')
    
    if len(new_pass) < 4:
        raise HTTPException(status_code=400, detail="رمز جدید باید حداقل ۴ کاراکتر باشد")
    
    if not verify_password(current, password_hash, password_salt):
        raise HTTPException(status_code=401, detail="رمز فعلی اشتباه است")
    
    password_hash, password_salt = hash_password(new_pass)
    save_password()
    
    log_activity("auth", "رمز عبور تغییر کرد", "info")
    return {"success": True}

# ========== API: Stats ==========
@app.get("/stats")
async def get_stats(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    total_links = len(LINKS)
    active_links = sum(1 for l in LINKS.values() if l.get('active', False) and not l.get('expired', False))
    total_used_bytes = sum(l.get('used_bytes', 0) for l in LINKS.values())
    
    uptime_seconds = time.time() - start_time
    uptime_str = f"{int(uptime_seconds // 3600)}h {int((uptime_seconds % 3600) // 60)}m"
    
    return {
        'active_connections': len(active_connections),
        'links_count': total_links,
        'active_links': active_links,
        'subs_count': len(SUBS),
        'total_errors': len(error_logs),
        'total_traffic_mb': traffic_stats['total_bytes'] / (1024 * 1024),
        'total_used_mb': total_used_bytes / (1024 * 1024),
        'hourly': traffic_stats['hourly'],
        'uptime': uptime_str,
        'last_update': datetime.now().isoformat(),
        'recent_errors': error_logs[-10:] if error_logs else []
    }

# ========== API: Links ==========
@app.get("/api/links")
async def get_links(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    links_list = []
    for uuid, link in LINKS.items():
        if link.get('expires_at'):
            try:
                exp = datetime.fromisoformat(link['expires_at'])
                link['expired'] = exp < datetime.now()
            except:
                link['expired'] = False
        else:
            link['expired'] = False
        link['used_fmt'] = fmt_bytes(link.get('used_bytes', 0))
        links_list.append(link)
    
    return {"links": links_list}

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
    
    LINKS[uuid_str] = link
    setup_links()
    save_data()
    log_activity("link", f"کانفیگ جدید: {label}", "info")
    return {"success": True, "uuid": uuid_str, "vless_link": link['vless_link']}

@app.patch("/api/links/{uuid}")
async def update_link(request: Request, uuid: str, data: Dict[str, Any]):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    if uuid not in LINKS:
        raise HTTPException(status_code=404, detail="Link not found")
    
    link = LINKS[uuid]
    
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
    log_activity("link", f"کانفیگ ویرایش شد: {link['label']}", "info")
    return {"success": True}

@app.delete("/api/links/{uuid}")
async def delete_link(request: Request, uuid: str):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    if uuid not in LINKS:
        raise HTTPException(status_code=404, detail="Link not found")
    
    label = LINKS[uuid]['label']
    del LINKS[uuid]
    save_data()
    log_activity("link", f"کانفیگ حذف شد: {label}", "info")
    return {"success": True}

# ========== API: Subs ==========
@app.get("/api/subs")
async def get_subs(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for sub in SUBS:
        sub_links = [l for l in LINKS.values() if l.get('sub_id') == sub['sub_id']]
        sub['links_count'] = len(sub_links)
        sub['active_count'] = sum(1 for l in sub_links if l.get('active', False) and not l.get('expired', False))
        sub['total_used'] = sum(l.get('used_bytes', 0) for l in sub_links)
        sub['total_used_fmt'] = fmt_bytes(sub['total_used'])
    
    return {"subs": SUBS}

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
    
    SUBS.append(sub)
    setup_subs()
    save_data()
    log_activity("sub", f"گروه جدید: {name}", "info")
    return {"success": True, "sub_id": sub_id}

@app.patch("/api/subs/{sub_id}")
async def update_sub(request: Request, sub_id: str, data: Dict[str, Any]):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for sub in SUBS:
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
            log_activity("sub", f"گروه ویرایش شد: {sub['name']}", "info")
            return {"success": True}
    
    raise HTTPException(status_code=404, detail="Sub not found")

@app.delete("/api/subs/{sub_id}")
async def delete_sub(request: Request, sub_id: str):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    
    for i, sub in enumerate(SUBS):
        if sub['sub_id'] == sub_id:
            name = sub['name']
            for link in LINKS.values():
                if link.get('sub_id') == sub_id:
                    link['sub_id'] = None
            del SUBS[i]
            save_data()
            log_activity("sub", f"گروه حذف شد: {name}", "info")
            return {"success": True}
    
    raise HTTPException(status_code=404, detail="Sub not found")

# ========== API: Activity ==========
@app.get("/api/activity")
async def get_activity(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    return {"logs": activity_logs[-100:]}

# ========== Public ==========
@app.get("/public/{sub_id}")
async def public_sub_page(sub_id: str):
    sub = next((s for s in SUBS if s['sub_id'] == sub_id), None)
    if not sub:
        raise HTTPException(status_code=404, detail="گروه یافت نشد")
    return HTMLResponse(get_public_page_html(sub_id))

@app.get("/api/public/sub/{sub_id}")
async def api_public_sub(sub_id: str, pw: Optional[str] = None):
    sub = next((s for s in SUBS if s['sub_id'] == sub_id), None)
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
    
    sub_links = [l for l in LINKS.values() if l.get('sub_id') == sub_id and l.get('active', False)]
    total_used = sum(l.get('used_bytes', 0) for l in sub_links)
    
    result_links = []
    for l in sub_links:
        conns = [c for c in active_connections.values() if c.get('uuid') == l['uuid']]
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
        'active_connections': len(active_connections),
        'total_used_fmt': fmt_bytes(total_used)
    }

@app.get("/sub-group/{sub_id}")
async def sub_group(sub_id: str, pw: Optional[str] = None):
    sub = next((s for s in SUBS if s['sub_id'] == sub_id), None)
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
    
    sub_links = [l for l in LINKS.values() if l.get('sub_id') == sub_id and l.get('active', False)]
    content = "\n".join(l.get('vless_link', '') for l in sub_links if l.get('vless_link'))
    return Response(content=content.strip(), media_type="text/plain")

@app.get("/sub/{uuid}")
async def sub_single(uuid: str):
    link = LINKS.get(uuid)
    if not link or not link.get('active', False):
        return Response(content="", media_type="text/plain")
    return Response(content=link.get('vless_link', ''), media_type="text/plain")

@app.get("/sub-all")
async def sub_all(request: Request):
    if not check_session(get_session(request)):
        raise HTTPException(status_code=401)
    content = "\n".join(l.get('vless_link', '') for l in LINKS.values() if l.get('active', False) and not l.get('expired', False))
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

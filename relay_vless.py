# relay_vless.py
import asyncio
import json
import logging
import time
import uuid
from typing import Dict, Any, Optional, Set
import websockets
from websockets.exceptions import ConnectionClosed, WebSocketException
import ssl
import os

# تنظیم لاگر
logger = logging.getLogger(__name__)

# ثابت‌های داخلی
RELAY_BUF = 65536  # بافر پیش‌فرض
CONNECT_TIMEOUT = 10
MAX_CONNECTIONS = 1000

# دیکشنری برای ذخیره اتصالات فعال
active_connections: Dict[str, websockets.WebSocketServerProtocol] = {}
connection_metadata: Dict[str, Dict[str, Any]] = {}
connection_stats: Dict[str, Dict[str, Any]] = {}

# متغیرهای جهانی که بعداً از main مقداردهی می‌شوند
_links_data = None
_get_link_by_uuid = None
_update_link_usage = None
_add_log = None
_connection_counter = 0

def initialize_relay(links_data_func, get_link_func, update_usage_func, add_log_func):
    """مقداردهی اولیه با توابع از main"""
    global _links_data, _get_link_by_uuid, _update_link_usage, _add_log
    _links_data = links_data_func
    _get_link_by_uuid = get_link_func
    _update_link_usage = update_usage_func
    _add_log = add_log_func


async def handle_websocket(websocket, path: str):
    """مدیریت اتصال WebSocket"""
    global _connection_counter
    
    # استخراج UUID از مسیر
    uuid_str = path.strip('/').split('/')[-1] if path else None
    
    if not uuid_str:
        await websocket.close(1008, "UUID required")
        return
    
    # اعتبارسنجی UUID از طریق تابع دریافت شده از main
    if _get_link_by_uuid is None:
        logger.error("Relay not initialized properly")
        await websocket.close(1011, "Server not ready")
        return
    
    link = _get_link_by_uuid(uuid_str)
    
    if not link:
        logger.warning(f"Invalid UUID: {uuid_str}")
        await websocket.close(1008, "Invalid UUID")
        return
    
    # بررسی فعال بودن
    if not link.get('active', False):
        logger.warning(f"Inactive link: {uuid_str}")
        await websocket.close(1008, "Link inactive")
        return
    
    # بررسی انقضا
    if link.get('expired', False):
        logger.warning(f"Expired link: {uuid_str}")
        await websocket.close(1008, "Link expired")
        return
    
    # بررسی سهمیه
    limit_bytes = link.get('limit_bytes', 0)
    used_bytes = link.get('used_bytes', 0)
    
    if limit_bytes > 0 and used_bytes >= limit_bytes:
        logger.warning(f"Quota exceeded for: {uuid_str}")
        await websocket.close(1008, "Quota exceeded")
        return
    
    # ذخیره اتصال
    client_ip = websocket.remote_address[0] if websocket.remote_address else "unknown"
    conn_id = str(uuid.uuid4())[:8]
    
    active_connections[conn_id] = websocket
    connection_metadata[conn_id] = {
        'uuid': uuid_str,
        'ip': client_ip,
        'label': link.get('label', 'Unknown'),
        'connected_at': time.time(),
        'bytes_received': 0,
        'bytes_sent': 0
    }
    _connection_counter += 1
    
    logger.info(f"WebSocket connected: {uuid_str} from {client_ip}")
    if _add_log:
        _add_log(f"WebSocket connected: {link.get('label')} from {client_ip}", "ok", "connection")
    
    try:
        # حلقه اصلی دریافت داده
        async for message in websocket:
            # به‌روزرسانی آمار
            if isinstance(message, bytes):
                size = len(message)
                connection_metadata[conn_id]['bytes_received'] += size
                # به‌روزرسانی مصرف در main
                if _update_link_usage:
                    _update_link_usage(uuid_str, size, "rx")
                # اکو کردن پیام (برای تست)
                await websocket.send(message)
                connection_metadata[conn_id]['bytes_sent'] += size
                if _update_link_usage:
                    _update_link_usage(uuid_str, size, "tx")
            else:
                # پیام متنی - معمولاً برای کنترل
                try:
                    data = json.loads(message)
                    if data.get('type') == 'ping':
                        await websocket.send(json.dumps({'type': 'pong', 'timestamp': time.time()}))
                except json.JSONDecodeError:
                    await websocket.send(f"Echo: {message}")
                    if _update_link_usage:
                        _update_link_usage(uuid_str, len(message.encode()), "tx")
    
    except ConnectionClosed:
        logger.info(f"Connection closed: {conn_id}")
    except WebSocketException as e:
        logger.error(f"WebSocket error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        # پاک‌سازی
        if conn_id in active_connections:
            del active_connections[conn_id]
        if conn_id in connection_metadata:
            del connection_metadata[conn_id]
        if _add_log:
            _add_log(f"WebSocket disconnected: {link.get('label')}", "info", "connection")


async def start_websocket_server(host: str = "0.0.0.0", port: int = 443):
    """راه‌اندازی سرور WebSocket"""
    try:
        # برای Railway با TLS
        ssl_context = None
        # اگر فایل‌های SSL وجود دارند
        cert_file = os.getenv('SSL_CERT_FILE')
        key_file = os.getenv('SSL_KEY_FILE')
        
        if cert_file and key_file and os.path.exists(cert_file) and os.path.exists(key_file):
            ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_context.load_cert_chain(cert_file, key_file)
            logger.info(f"SSL enabled with cert: {cert_file}")
        
        server = await websockets.serve(
            handle_websocket,
            host,
            port,
            ssl=ssl_context,
            max_size=RELAY_BUF,
            max_queue=1024
        )
        
        logger.info(f"WebSocket server started on {host}:{port}")
        await server.wait_closed()
        
    except Exception as e:
        logger.error(f"Failed to start WebSocket server: {e}")
        raise


def get_active_connections() -> Dict:
    """دریافت لیست اتصالات فعال"""
    result = {}
    for conn_id, meta in connection_metadata.items():
        if conn_id in active_connections:
            result[conn_id] = {
                'uuid': meta.get('uuid'),
                'ip': meta.get('ip'),
                'label': meta.get('label'),
                'connected_at': meta.get('connected_at'),
                'bytes_received': meta.get('bytes_received', 0),
                'bytes_sent': meta.get('bytes_sent', 0)
            }
    return result


def get_connection_count() -> int:
    """دریافت تعداد اتصالات فعال"""
    return len(active_connections)


def get_connection_stats() -> Dict[str, Any]:
    """دریافت آمار کلی اتصالات"""
    total_rx = sum(m.get('bytes_received', 0) for m in connection_metadata.values())
    total_tx = sum(m.get('bytes_sent', 0) for m in connection_metadata.values())
    unique_ips = set(m.get('ip') for m in connection_metadata.values() if m.get('ip'))
    
    return {
        'active': len(active_connections),
        'total_rx': total_rx,
        'total_tx': total_tx,
        'total_bytes': total_rx + total_tx,
        'unique_ips': len(unique_ips),
        'connections': get_active_connections()
    }

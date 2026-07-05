# relay_vless.py - Royal Gateway v9.2
# مدیریت WebSocket و آمار واقعی

import asyncio
import json
import logging
import time
import uuid
from typing import Dict, Any, Optional, List
from datetime import datetime
import websockets
from websockets.exceptions import ConnectionClosed, WebSocketException
import ssl
import os

logger = logging.getLogger(__name__)

# ========== تنظیمات ==========
RELAY_BUF = 65536
CONNECT_TIMEOUT = 10
MAX_CONNECTIONS = 1000

# ========== دیکشنری‌های ذخیره‌سازی ==========
active_connections: Dict[str, websockets.WebSocketServerProtocol] = {}
connection_metadata: Dict[str, Dict[str, Any]] = {}

# ========== آمار واقعی ==========
stats = {
    'total_bytes_rx': 0,
    'total_bytes_tx': 0,
    'total_connections': 0,
    'peak_connections': 0,
    'hourly_traffic': {},
    'daily_traffic': {},
    'last_update': None,
    'start_time': time.time(),
}

# ========== توابع از main ==========
_links_data = None
_get_link_by_uuid = None
_update_link_usage = None
_add_log = None


def initialize_relay(links_data_func, get_link_func, update_usage_func, add_log_func):
    """مقداردهی اولیه با توابع از main"""
    global _links_data, _get_link_by_uuid, _update_link_usage, _add_log
    _links_data = links_data_func
    _get_link_by_uuid = get_link_func
    _update_link_usage = update_usage_func
    _add_log = add_log_func


def update_stats(bytes_rx: int = 0, bytes_tx: int = 0):
    """به‌روزرسانی آمار کلی"""
    global stats
    
    now = datetime.now()
    
    stats['total_bytes_rx'] += bytes_rx
    stats['total_bytes_tx'] += bytes_tx
    stats['last_update'] = now.isoformat()
    
    # آمار ساعتی
    hour_key = now.strftime("%Y-%m-%d %H:00")
    if hour_key not in stats['hourly_traffic']:
        stats['hourly_traffic'][hour_key] = 0
    stats['hourly_traffic'][hour_key] += (bytes_rx + bytes_tx)
    
    # فقط 72 ساعت اخیر را نگه دار
    keys = sorted(stats['hourly_traffic'].keys())
    if len(keys) > 72:
        for k in keys[:-72]:
            del stats['hourly_traffic'][k]
    
    # آمار روزانه
    day_key = now.strftime("%Y-%m-%d")
    if day_key not in stats['daily_traffic']:
        stats['daily_traffic'][day_key] = 0
    stats['daily_traffic'][day_key] += (bytes_rx + bytes_tx)
    
    keys = sorted(stats['daily_traffic'].keys())
    if len(keys) > 30:
        for k in keys[:-30]:
            del stats['daily_traffic'][k]
    
    # پیک اتصالات
    current = len(active_connections)
    if current > stats['peak_connections']:
        stats['peak_connections'] = current


def get_stats() -> Dict[str, Any]:
    """دریافت آمار کامل"""
    global stats
    
    total_used = 0
    total_links = 0
    active_links = 0
    expired_links = 0
    
    if _links_data:
        for link in _links_data():
            total_links += 1
            total_used += link.get('used_bytes', 0)
            if link.get('active', False):
                active_links += 1
            if link.get('expired', False):
                expired_links += 1
    
    hourly_data = {}
    for ts, bytes_val in stats['hourly_traffic'].items():
        hourly_data[ts] = bytes_val / (1024 * 1024)
    
    hourly_values = list(hourly_data.values())
    
    return {
        'active_connections': len(active_connections),
        'peak_connections': stats['peak_connections'],
        'total_connections': stats['total_connections'],
        'total_bytes_rx': stats['total_bytes_rx'],
        'total_bytes_tx': stats['total_bytes_tx'],
        'total_bytes': stats['total_bytes_rx'] + stats['total_bytes_tx'],
        'total_traffic_mb': (stats['total_bytes_rx'] + stats['total_bytes_tx']) / (1024 * 1024),
        'total_used_all_links': total_used,
        'total_used_all_links_mb': total_used / (1024 * 1024),
        'total_links': total_links,
        'active_links': active_links,
        'expired_links': expired_links,
        'hourly_traffic': hourly_data,
        'daily_traffic': stats['daily_traffic'],
        'avg_hourly_mb': sum(hourly_values) / len(hourly_values) if hourly_values else 0,
        'peak_hourly_mb': max(hourly_values) if hourly_values else 0,
        'min_hourly_mb': min(hourly_values) if hourly_values else 0,
        'last_update': stats['last_update'],
        'start_time': stats['start_time'],
        'uptime_seconds': time.time() - stats['start_time'],
        'connections': get_active_connections()
    }


def get_active_connections() -> List[Dict[str, Any]]:
    """دریافت لیست اتصالات فعال"""
    result = []
    for conn_id, meta in connection_metadata.items():
        if conn_id in active_connections:
            total_bytes = meta.get('bytes_rx', 0) + meta.get('bytes_tx', 0)
            result.append({
                'id': conn_id,
                'uuid': meta.get('uuid'),
                'ip': meta.get('ip'),
                'label': meta.get('label'),
                'connected_at': meta.get('connected_at'),
                'duration_sec': time.time() - meta.get('connected_at', time.time()),
                'bytes_rx': meta.get('bytes_rx', 0),
                'bytes_tx': meta.get('bytes_tx', 0),
                'bytes_total': total_bytes,
                'bytes_fmt': _fmt_bytes(total_bytes),
                'transport': meta.get('transport', 'vless-ws')
            })
    return result


def get_connection_count() -> int:
    return len(active_connections)


def _fmt_bytes(b: int) -> str:
    if b < 1024:
        return f"{b} B"
    elif b < 1024 ** 2:
        return f"{b/1024:.1f} KB"
    elif b < 1024 ** 3:
        return f"{b/1024**2:.2f} MB"
    else:
        return f"{b/1024**3:.2f} GB"


async def handle_websocket(websocket, path: str):
    """مدیریت اتصال WebSocket"""
    global stats
    
    uuid_str = path.strip('/').split('/')[-1] if path else None
    
    if not uuid_str:
        await websocket.close(1008, "UUID required")
        return
    
    if _get_link_by_uuid is None:
        await websocket.close(1011, "Server not ready")
        return
    
    link = _get_link_by_uuid(uuid_str)
    
    if not link:
        await websocket.close(1008, "Invalid UUID")
        return
    
    if not link.get('active', False):
        await websocket.close(1008, "Link inactive")
        return
    
    if link.get('expired', False):
        await websocket.close(1008, "Link expired")
        return
    
    limit_bytes = link.get('limit_bytes', 0)
    used_bytes = link.get('used_bytes', 0)
    
    if limit_bytes > 0 and used_bytes >= limit_bytes:
        await websocket.close(1008, "Quota exceeded")
        return
    
    client_ip = websocket.remote_address[0] if websocket.remote_address else "unknown"
    conn_id = str(uuid.uuid4())[:8]
    
    active_connections[conn_id] = websocket
    connection_metadata[conn_id] = {
        'uuid': uuid_str,
        'ip': client_ip,
        'label': link.get('label', 'Unknown'),
        'connected_at': time.time(),
        'bytes_rx': 0,
        'bytes_tx': 0,
        'transport': link.get('protocol', 'vless-ws')
    }
    
    stats['total_connections'] += 1
    
    if len(active_connections) > stats['peak_connections']:
        stats['peak_connections'] = len(active_connections)
    
    logger.info(f"WebSocket connected: {uuid_str} from {client_ip}")
    if _add_log:
        _add_log(f"اتصال WebSocket: {link.get('label')} از {client_ip}", "ok", "connection")
    
    try:
        async for message in websocket:
            if isinstance(message, bytes):
                size = len(message)
                connection_metadata[conn_id]['bytes_rx'] += size
                update_stats(bytes_rx=size)
                if _update_link_usage:
                    _update_link_usage(uuid_str, size, "rx")
                await websocket.send(message)
                connection_metadata[conn_id]['bytes_tx'] += size
                update_stats(bytes_tx=size)
                if _update_link_usage:
                    _update_link_usage(uuid_str, size, "tx")
            else:
                try:
                    data = json.loads(message)
                    if data.get('type') == 'ping':
                        await websocket.send(json.dumps({
                            'type': 'pong',
                            'timestamp': time.time(),
                            'stats': {
                                'connections': len(active_connections),
                                'total_traffic_mb': (stats['total_bytes_rx'] + stats['total_bytes_tx']) / (1024 * 1024)
                            }
                        }))
                except json.JSONDecodeError:
                    await websocket.send(f"Echo: {message}")
                    if _update_link_usage:
                        _update_link_usage(uuid_str, len(message.encode()), "tx")
                        update_stats(bytes_tx=len(message.encode()))
    
    except ConnectionClosed:
        pass
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        if conn_id in active_connections:
            del active_connections[conn_id]
        if conn_id in connection_metadata:
            del connection_metadata[conn_id]
        if _add_log:
            _add_log(f"قطع اتصال WebSocket: {link.get('label')}", "info", "connection")


async def start_websocket_server(host: str = "0.0.0.0", port: int = 443):
    """راه‌اندازی سرور WebSocket"""
    try:
        ssl_context = None
        cert_file = os.getenv('SSL_CERT_FILE')
        key_file = os.getenv('SSL_KEY_FILE')
        
        if cert_file and key_file and os.path.exists(cert_file) and os.path.exists(key_file):
            ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_context.load_cert_chain(cert_file, key_file)
            logger.info(f"SSL enabled")
        
        server = await websockets.serve(
            handle_websocket,
            host,
            port,
            ssl=ssl_context,
            max_size=RELAY_BUF,
            max_queue=1024,
            ping_interval=20,
            ping_timeout=60
        )
        
        logger.info(f"WebSocket server started on {host}:{port}")
        await server.wait_closed()
        
    except Exception as e:
        logger.error(f"Failed to start WebSocket server: {e}")
        raise

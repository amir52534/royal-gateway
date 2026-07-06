# shared.py — Shared mutable state for Royal Gateway
import asyncio
import threading
import collections

# ── VLESS Relay State ──
RELAY_BUF = 32768
connections: dict = {}
sub_clients: dict = {}
TIMEOUT = 30

# ── Core State ──
stats = {
    "total_bytes": 0,
    "total_requests": 0,
    "total_errors": 0,
    "start_time": 0,
}

hourly_traffic = collections.defaultdict(int)
error_logs = collections.deque(maxlen=100)
LINKS: dict = {}
LINKS_LOCK = asyncio.Lock()

# ── User State ──
USERS: dict = {}
USERS_LOCK = asyncio.Lock()

# ── Subscription Groups State ──
SUBS: dict = {}
SUBS_LOCK = asyncio.Lock()

# ── Settings State ──
SETTINGS: dict = {}
SETTINGS_LOCK = asyncio.Lock()

# ── Sessions State ──
SESSIONS: dict = {}
SESSIONS_LOCK = asyncio.Lock()

# ── Groups State ──
GROUPS: dict = {}
GROUPS_LOCK = asyncio.Lock()

# ── IP Pool & Blacklist State ──
IP_POOL: list = []
IP_POOL_LOCK = asyncio.Lock()
IP_BLACKLIST: set = set()
IP_BLACKLIST_LOCK = asyncio.Lock()
IP_LOCK = threading.Lock()

# ── User IP Mapping ──
USER_IP_MAP: dict = {}
USER_IP_MAP_LOCK = asyncio.Lock()

# ── WebSocket Live Clients ──
WS_LIVE_CLIENTS: set = set()
ws_client_count = 0

# ── Activity & Error Logs ──
activity_logs = collections.deque(maxlen=200)

# ── HTTP Client ──
http_client = None
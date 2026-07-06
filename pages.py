# pages.py — Royal Panel Enterprise Theme
# تمام مسیرهای /spider به /royal تغییر داده شده

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Royal Panel · ورود</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root {
  --royal-gold: #D4A02B;
  --royal-dark: #0A0806;
  --royal-light: #14100E;
  --royal-gold-dark: #A67C1E;
  --royal-gold-glow: rgba(212, 160, 43, 0.15);
}
*{margin:0;padding:0;box-sizing:border-box}
body {
  background: var(--royal-dark);
  font-family: 'Vazirmatn', sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: 
    radial-gradient(ellipse at 20% 50%, rgba(212,160,43,0.06) 0%, transparent 60%),
    radial-gradient(ellipse at 80% 50%, rgba(212,160,43,0.04) 0%, transparent 60%);
}
.login-box {
  background: var(--royal-light);
  border: 1px solid rgba(212,160,43,0.12);
  border-radius: 24px;
  padding: 48px 40px 40px;
  max-width: 420px;
  width: 100%;
  box-shadow: 0 25px 60px rgba(0,0,0,0.8), 0 0 80px rgba(212,160,43,0.04);
  position: relative;
  overflow: hidden;
}
.login-box::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(212,160,43,0.03), transparent 70%);
  pointer-events: none;
}
.royal-logo {
  text-align: center;
  margin-bottom: 32px;
}
.royal-logo svg {
  width: 72px;
  height: 72px;
  filter: drop-shadow(0 0 30px rgba(212,160,43,0.15));
}
.royal-title {
  font-size: 32px;
  font-weight: 900;
  background: linear-gradient(135deg, #D4A02B, #F0D060, #D4A02B);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: 2px;
  margin-top: 8px;
  text-shadow: 0 0 40px rgba(212,160,43,0.1);
}
.royal-sub {
  color: rgba(212,160,43,0.4);
  font-size: 13px;
  text-align: center;
  margin-top: 4px;
  letter-spacing: 4px;
  font-weight: 300;
}
.input-group {
  margin-bottom: 20px;
}
.input-group label {
  display: block;
  color: rgba(212,160,43,0.6);
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 8px;
}
.input-group input {
  width: 100%;
  padding: 14px 18px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(212,160,43,0.1);
  border-radius: 12px;
  color: #EDE8E0;
  font-family: 'Vazirmatn', sans-serif;
  font-size: 14px;
  transition: all 0.3s;
  outline: none;
}
.input-group input:focus {
  border-color: var(--royal-gold);
  box-shadow: 0 0 0 3px rgba(212,160,43,0.08);
  background: rgba(255,255,255,0.06);
}
.input-group input::placeholder {
  color: rgba(255,255,255,0.15);
}
.login-btn {
  width: 100%;
  padding: 16px;
  background: linear-gradient(135deg, #D4A02B, #F0D060);
  border: none;
  border-radius: 12px;
  color: #0A0806;
  font-family: 'Vazirmatn', sans-serif;
  font-size: 16px;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.3s;
  letter-spacing: 1px;
  position: relative;
  overflow: hidden;
}
.login-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(212,160,43,0.2);
}
.login-btn:active {
  transform: translateY(0);
}
.login-btn::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #F0D060, #D4A02B);
  opacity: 0;
  transition: opacity 0.3s;
}
.login-btn:hover::after {
  opacity: 1;
}
.login-btn span {
  position: relative;
  z-index: 1;
}
.hint-box {
  background: rgba(212,160,43,0.04);
  border: 1px solid rgba(212,160,43,0.08);
  border-radius: 12px;
  padding: 12px 16px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.hint-label {
  color: rgba(212,160,43,0.4);
  font-size: 11px;
  font-weight: 600;
}
.hint-value {
  color: var(--royal-gold);
  font-family: 'Inter', monospace;
  font-size: 13px;
  font-weight: 700;
  background: rgba(212,160,43,0.08);
  padding: 4px 14px;
  border-radius: 8px;
  cursor: pointer;
  border: 1px solid rgba(212,160,43,0.1);
  transition: all 0.2s;
}
.hint-value:hover {
  background: rgba(212,160,43,0.15);
  transform: scale(1.05);
}
.footer {
  text-align: center;
  margin-top: 24px;
  color: rgba(212,160,43,0.15);
  font-size: 10px;
  letter-spacing: 2px;
}
.error-msg {
  display: none;
  background: rgba(232,74,74,0.08);
  border: 1px solid rgba(232,74,74,0.15);
  border-radius: 12px;
  padding: 10px 14px;
  color: #E84A4A;
  font-size: 12px;
  margin-bottom: 16px;
  align-items: center;
  gap: 8px;
}
.error-msg.show {
  display: flex;
}
</style>
</head>
<body>
<div class="login-box">
  <div class="royal-logo">
    <svg viewBox="0 0 100 100">
      <defs>
        <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#D4A02B"/>
          <stop offset="100%" style="stop-color:#F0D060"/>
        </linearGradient>
      </defs>
      <rect x="10" y="10" width="80" height="80" rx="16" fill="none" stroke="url(#g)" stroke-width="2"/>
      <path d="M50,25 L50,75 M25,50 L75,50" stroke="url(#g)" stroke-width="3" stroke-linecap="round"/>
      <circle cx="50" cy="50" r="12" fill="none" stroke="url(#g)" stroke-width="2"/>
      <circle cx="50" cy="50" r="4" fill="url(#g)"/>
      <path d="M50,30 L58,42 L66,50 L58,58 L50,70 L42,58 L34,50 L42,42 Z" fill="url(#g)" opacity="0.2"/>
    </svg>
    <div class="royal-title">ROYAL</div>
    <div class="royal-sub">NEXUS</div>
  </div>
  
  <div class="error-msg" id="err"><span id="err-text"></span></div>
  
  <div class="hint-box">
    <span class="hint-label">🔑 رمز پیش‌فرض</span>
    <span class="hint-value" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span>
  </div>
  
  <form id="login-form">
    <div class="input-group">
      <label>رمز عبور</label>
      <input type="password" id="pw" placeholder="••••••••" autofocus required>
    </div>
    <button type="submit" class="login-btn" id="btn"><span>✦ ورود به پنل ✦</span></button>
  </form>
  <div class="footer">ROYAL NEXUS v1.0</div>
</div>
<script>
document.getElementById('login-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  const btn = document.getElementById('btn'), err = document.getElementById('err'), et = document.getElementById('err-text');
  err.classList.remove('show');
  btn.disabled = true;
  btn.innerHTML = '<span>⏳</span>';
  try {
    const r = await fetch('/api/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({password: document.getElementById('pw').value})
    });
    if (!r.ok) {
      const d = await r.json().catch(() => ({}));
      throw new Error(d.detail || 'خطا');
    }
    location.href = '/royal';
  } catch(ex) {
    et.textContent = ex.message;
    err.classList.add('show');
    btn.disabled = false;
    btn.innerHTML = '<span>✦ ورود به پنل ✦</span>';
  }
});
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Royal Nexus · داشبورد</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root {
  --royal-gold: #D4A02B;
  --royal-dark: #0A0806;
  --royal-light: #14100E;
  --royal-gold-dark: #A67C1E;
  --royal-gold-glow: rgba(212,160,43,0.12);
  --royal-gold-glow-strong: rgba(212,160,43,0.2);
  
  --bg: var(--royal-dark);
  --surface: rgba(20,16,14,0.92);
  --surface-glass: rgba(20,16,14,0.7);
  --text-primary: #EDE8E0;
  --text-secondary: rgba(212,160,43,0.5);
  --border: rgba(212,160,43,0.06);
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 20px rgba(0,0,0,0.4);
  --shadow-lg: 0 12px 48px rgba(0,0,0,0.6);
  --shadow-hover: 0 8px 30px rgba(0,0,0,0.5);
  --gradient: linear-gradient(135deg, #D4A02B, #F0D060);
  --gradient-purple: linear-gradient(135deg, #D4A02B, #F0D060);
  --radius-sm: 12px;
  --radius: 18px;
  --radius-lg: 24px;
  --radius-xl: 28px;
  --sidebar-w: 260px;
  --topbar-h: 68px;
  --transition: .3s ease;
}

*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--text-primary);min-height:100vh;display:flex;font-size:14px;transition:background var(--transition),color var(--transition);overflow-x:hidden}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(212,160,43,0.15);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(212,160,43,0.3)}
a{color:inherit;text-decoration:none}

.bg-particles{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.bg-p{position:absolute;border-radius:50%;animation:bgDrift linear infinite}
@keyframes bgDrift{0%{transform:translate(0,0) scale(1);opacity:0}10%{opacity:.4}90%{opacity:.4}100%{transform:translate(80px,-60px) scale(.2);opacity:0}}

.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--surface);backdrop-filter:blur(20px) saturate(160%);-webkit-backdrop-filter:blur(20px) saturate(160%);border-left:1px solid var(--border);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform var(--transition),background var(--transition),border-color var(--transition);box-shadow:var(--shadow-sm)}
.sidebar-logo{display:flex;align-items:center;gap:12px;padding:22px 18px 18px;border-bottom:1px solid var(--border);flex-shrink:0}
.sidebar-logo svg{width:36px;height:36px;filter:drop-shadow(0 0 20px rgba(212,160,43,0.12));flex-shrink:0}
.sidebar-logo-text{font-size:15px;font-weight:900;background:linear-gradient(135deg, #D4A02B, #F0D060);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sidebar-logo-sub{font-size:9.5px;color:var(--text-secondary)}
.sidebar-nav{flex:1;overflow-y:auto;padding:8px 0}
.nav-section{padding:16px 18px 6px;font-size:9px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--text-secondary);opacity:.6}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 14px;color:var(--text-secondary);font-size:12.5px;font-weight:500;cursor:pointer;border-right:3px solid transparent;transition:all .2s;margin:1px 8px;border-radius:0 var(--radius-sm) var(--radius-sm) 0;position:relative}
.nav-item i{font-size:17px;width:22px;text-align:center;flex-shrink:0}
.nav-item:hover{background:rgba(212,160,43,0.04);color:var(--royal-gold)}
.nav-item.active{background:linear-gradient(135deg, rgba(212,160,43,0.08), rgba(212,160,43,0.04));color:var(--royal-gold);border-right-color:var(--royal-gold);font-weight:700}
.nav-item.active i{color:var(--royal-gold)}
.nav-badge{margin-right:auto;background:rgba(212,160,43,0.1);color:var(--royal-gold);font-size:9px;padding:2px 7px;border-radius:20px;font-weight:700}
.sidebar-footer{padding:12px 16px;border-top:1px solid var(--border);flex-shrink:0}
.sidebar-user{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.sidebar-avatar{width:38px;height:38px;border-radius:var(--radius-sm);background:var(--gradient);display:flex;align-items:center;justify-content:center;color:var(--royal-dark);font-size:16px;flex-shrink:0;box-shadow:0 4px 12px rgba(212,160,43,0.12)}
.sidebar-user-name{font-size:12.5px;font-weight:700;color:var(--text-primary)}
.sidebar-user-role{font-size:9.5px;color:var(--text-secondary)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;width:100%;padding:9px;border:none;border-radius:var(--radius-sm);background:rgba(212,160,43,0.04);color:var(--text-secondary);font-family:inherit;font-size:11.5px;font-weight:600;cursor:pointer;transition:all .2s;border:1px solid var(--border)}
.theme-btn:hover{background:rgba(212,160,43,0.08);color:var(--royal-gold)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;width:100%;padding:9px;border:none;border-radius:var(--radius-sm);background:rgba(232,74,74,0.04);color:#E84A4A;font-family:inherit;font-size:11.5px;font-weight:600;cursor:pointer;transition:all .2s;margin-top:6px;border:1px solid rgba(232,74,74,0.06)}
.logout-btn:hover{background:rgba(232,74,74,0.08)}

.mobile-top{display:none;position:fixed;top:0;right:0;left:0;height:56px;background:var(--surface);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);z-index:150;align-items:center;justify-content:space-between;padding:0 14px}
.mobile-brand{display:flex;align-items:center;gap:9px}
.mobile-brand svg{width:28px;height:28px;filter:drop-shadow(0 0 10px rgba(212,160,43,0.1))}
.mobile-brand span{font-size:13px;font-weight:700;background:linear-gradient(135deg,#D4A02B,#F0D060);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.mobile-actions{display:flex;gap:6px}
.mob-btn{background:rgba(212,160,43,0.04);border:1px solid var(--border);color:var(--text-secondary);width:34px;height:34px;border-radius:10px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.6);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}

.main{margin-right:var(--sidebar-w);flex:1;padding:24px 28px 40px;min-width:0;transition:margin var(--transition);position:relative;z-index:1}
.page{display:none;animation:fadeIn .25s ease}
.page.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.topbar-title{font-size:20px;font-weight:800;color:var(--text-primary);display:flex;align-items:center;gap:9px;letter-spacing:-.02em}
.topbar-title i{color:var(--royal-gold);font-size:21px}
.topbar-sub{font-size:11px;color:var(--text-secondary);margin-top:3px}
.topbar-right{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.welcome-text{font-size:12.5px;color:var(--text-secondary);display:flex;align-items:center;gap:5px;font-weight:500}
.bell-btn{width:38px;height:38px;border-radius:var(--radius-sm);background:rgba(212,160,43,0.04);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:17px;transition:all .2s;position:relative}
.bell-btn:hover{background:rgba(212,160,43,0.08);color:var(--royal-gold)}
.bell-btn::after{content:'';position:absolute;top:8px;left:8px;width:7px;height:7px;border-radius:50%;background:#D4A02B;border:2px solid var(--surface)}

.btn{font-family:'Vazirmatn',sans-serif;font-size:12px;font-weight:600;border-radius:var(--radius);padding:9px 16px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .2s;white-space:nowrap}
.btn i{font-size:13px}
.btn-primary{background:var(--gradient);color:var(--royal-dark);box-shadow:0 4px 20px rgba(212,160,43,0.12)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(212,160,43,0.2)}
.btn-primary:active{transform:translateY(0)}
.btn-ghost{background:rgba(212,160,43,0.04);color:var(--royal-gold);border:1px solid rgba(212,160,43,0.08)}
.btn-ghost:hover{background:rgba(212,160,43,0.08)}
.btn-danger{background:rgba(232,74,74,0.04);color:#E84A4A;border:1px solid rgba(232,74,74,0.08)}
.btn-danger:hover{background:rgba(232,74,74,0.08)}
.btn-sm{padding:5px 10px;font-size:10.5px;border-radius:10px}
.btn-icon{width:32px;height:32px;padding:0;justify-content:center;border-radius:10px}
.btn-purple{background:rgba(212,160,43,0.06);color:var(--royal-gold);border:1px solid rgba(212,160,43,0.1)}
.btn-purple:hover{background:rgba(212,160,43,0.1)}
.btn-success{background:rgba(123,207,168,0.06);color:#7BCFA8;border:1px solid rgba(123,207,168,0.08)}
.btn-success:hover{background:rgba(123,207,168,0.1)}

.badge{font-size:9.5px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.badge-blue{background:rgba(212,160,43,0.08);color:var(--royal-gold)}
.badge-green{background:rgba(123,207,168,0.08);color:#7BCFA8}
.badge-red{background:rgba(232,74,74,0.08);color:#E84A4A}
.badge-purple{background:rgba(212,160,43,0.06);color:#F0D060}
.badge-amber{background:rgba(245,158,11,0.08);color:#F59E0B}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dot-green{background:#7BCFA8}
.dot-red{background:#E84A4A}
.dot-blue{background:var(--royal-gold)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}

.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.stat-card{background:var(--surface-glass);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px 18px 16px;transition:all var(--transition);position:relative;overflow:hidden;cursor:default}
.stat-card:hover{transform:translateY(-3px);border-color:rgba(212,160,43,0.12);box-shadow:var(--shadow-hover)}
.stat-card::after{content:'';position:absolute;top:0;right:0;width:4px;height:40px;background:var(--gradient);border-radius:0 0 0 6px;transition:height .3s}
.stat-card:hover::after{height:60px}
.stat-icon{width:40px;height:40px;border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px}
.stat-icon.blue{background:rgba(212,160,43,0.08);color:var(--royal-gold)}
.stat-icon.purple{background:rgba(212,160,43,0.06);color:#F0D060}
.stat-icon.green{background:rgba(123,207,168,0.08);color:#7BCFA8}
.stat-icon.red{background:rgba(232,74,74,0.08);color:#E84A4A}
.stat-label{font-size:10px;font-weight:700;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.06em;margin-bottom:5px}
.stat-value{font-size:26px;font-weight:800;color:var(--text-primary);line-height:1;letter-spacing:-.02em}
.stat-sub{font-size:10px;color:var(--text-secondary);margin-top:7px;display:flex;align-items:center;gap:4px}
.stat-sub.up{color:#7BCFA8}

.quick-actions{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
.qa-btn{display:flex;align-items:center;gap:10px;padding:14px 16px;border-radius:var(--radius);border:1px solid var(--border);background:var(--surface-glass);backdrop-filter:blur(12px);color:var(--text-primary);font-family:inherit;font-size:12.5px;font-weight:600;cursor:pointer;transition:all var(--transition)}
.qa-btn:hover{background:var(--gradient);color:var(--royal-dark);border-color:transparent;box-shadow:0 6px 20px rgba(212,160,43,0.15);transform:translateY(-2px)}
.qa-btn i{font-size:18px}

.server-panel{background:var(--surface-glass);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:22px 24px 20px;margin-bottom:20px;box-shadow:var(--shadow-sm)}
.server-title{font-size:14px;font-weight:800;color:var(--text-primary);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.server-title i{color:var(--royal-gold);font-size:17px}
.server-bars{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.srv-bar-item{display:flex;flex-direction:column;gap:7px}
.srv-bar-label{display:flex;justify-content:space-between;font-size:10.5px;font-weight:600}
.srv-bar-name{color:var(--text-secondary)}
.srv-bar-pct{color:var(--text-primary)}
.srv-bar-track{height:8px;border-radius:4px;background:rgba(212,160,43,0.06);overflow:hidden}
.srv-bar-fill{height:100%;border-radius:4px;transition:width .6s ease;position:relative}
.srv-bar-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.1),transparent);width:50%;animation:shimmer 2s linear infinite}
.srv-bar-fill.blue{background:linear-gradient(90deg,#D4A02B,#F0D060)}
.srv-bar-fill.purple{background:linear-gradient(90deg,#F0D060,#D4A02B)}
.srv-bar-fill.amber{background:linear-gradient(90deg,#D4A02B,#D4A02B)}
.srv-bar-fill.green{background:linear-gradient(90deg,#D4A02B,#F0D060)}
@keyframes shimmer{0%{transform:translateX(-100%)}100%{transform:translateX(200%)}}

.table-wrap{background:var(--surface-glass);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm)}
.table-wrap table{width:100%;border-collapse:collapse}
.table-wrap th{background:rgba(212,160,43,0.04);font-size:10px;font-weight:800;color:var(--royal-gold);text-transform:uppercase;letter-spacing:.06em;padding:12px 14px;text-align:right;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:1}
.table-wrap td{padding:12px 14px;font-size:12px;color:rgba(237,232,224,0.8);border-bottom:1px solid var(--border);transition:background .15s}
.table-wrap tr:hover td{background:rgba(212,160,43,0.02)}
.table-wrap tr:last-child td{border-bottom:none}
.proto-badge{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700}
.pb-vless{background:rgba(212,160,43,0.12);color:var(--royal-gold)}
.pb-vmess{background:rgba(212,160,43,0.08);color:#F0D060}
.pb-trojan{background:rgba(212,160,43,0.1);color:#D4A02B}
.pb-ss{background:rgba(123,207,168,0.08);color:#7BCFA8}
.usage-bar-wrap{width:100%;min-width:100px}
.usage-bar{height:6px;border-radius:3px;background:rgba(212,160,43,0.06);overflow:hidden;margin-bottom:3px}
.usage-fill{height:100%;border-radius:3px;background:linear-gradient(90deg,#D4A02B,#F0D060);transition:width .5s ease}
.usage-text{font-size:9.5px;color:var(--text-secondary);display:flex;justify-content:space-between}
.status-dot{display:flex;align-items:center;gap:5px;font-weight:600;font-size:11px}
.status-dot.active{color:#7BCFA8}
.status-dot.expired{color:#E84A4A}
.exp-chip{font-size:9px;padding:2px 8px;border-radius:6px;font-weight:700}
.exp-ok{background:rgba(123,207,168,0.08);color:#7BCFA8}
.exp-warn{background:rgba(245,158,11,0.08);color:#F59E0B}
.exp-bad{background:rgba(232,74,74,0.08);color:#E84A4A}
.action-btns{display:flex;gap:4px}

.modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}
.modal-overlay.open{display:flex}
.modal-card{background:var(--royal-light);backdrop-filter:blur(24px) saturate(180%);border:1px solid var(--border);border-radius:var(--radius-xl);padding:0;max-width:540px;width:100%;max-height:90vh;overflow-y:auto;box-shadow:var(--shadow-lg);animation:modalIn .25s ease}
@keyframes modalIn{from{opacity:0;transform:scale(.95) translateY(10px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-head{padding:22px 26px 18px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;position:relative}
.modal-head::before{content:'';position:absolute;top:0;right:0;width:150px;height:150px;background:radial-gradient(circle,rgba(212,160,43,0.04),transparent 70%);pointer-events:none}
.modal-title{font-size:16px;font-weight:800;color:var(--text-primary);display:flex;align-items:center;gap:8px;position:relative;z-index:1}
.modal-title i{color:var(--royal-gold);font-size:18px}
.modal-close{width:32px;height:32px;border-radius:10px;background:rgba(212,160,43,0.04);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;transition:all .2s}
.modal-close:hover{background:rgba(232,74,74,0.08);color:#E84A4A;border-color:rgba(232,74,74,0.12)}
.modal-body{padding:20px 26px}
.modal-footer{padding:16px 26px 20px;border-top:1px solid var(--border);display:flex;gap:10px;justify-content:flex-end}
.form-field{margin-bottom:14px}
.form-field label{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:800;color:var(--text-secondary);text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.form-field label i{color:var(--royal-gold);font-size:13px}
.form-input{width:100%;padding:10px 14px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,0.04);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12.5px;outline:none;transition:all .2s}
.form-input:focus{border-color:var(--royal-gold);box-shadow:0 0 0 3px rgba(212,160,43,0.06)}
.form-input::placeholder{color:var(--text-secondary);opacity:.5}
.form-row{display:flex;gap:10px;flex-wrap:wrap}
.form-row .form-field{flex:1;min-width:120px}
.form-select{width:100%;padding:10px 14px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,0.04);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12.5px;outline:none;cursor:pointer}
.form-select:focus{border-color:var(--royal-gold)}
.form-textarea{width:100%;padding:10px 14px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,0.04);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:12.5px;outline:none;resize:vertical;min-height:70px}
.toggle-wrap{display:flex;align-items:center;gap:10px}
.toggle-switch{width:44px;height:24px;border-radius:12px;background:rgba(100,116,139,0.2);position:relative;cursor:pointer;transition:all .3s;border:none;flex-shrink:0}
.toggle-switch::after{content:'';position:absolute;width:18px;height:18px;border-radius:50%;background:#EDE8E0;right:3px;top:3px;transition:all .3s;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.toggle-switch.on{background:linear-gradient(135deg,#D4A02B,#F0D060)}
.toggle-switch.on::after{right:23px}
.toggle-label{font-size:11.5px;color:var(--text-secondary);font-weight:600}

.cfg-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.cfg-card-item{background:var(--surface-glass);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:0;overflow:hidden;transition:all var(--transition)}
.cfg-card-item:hover{border-color:rgba(212,160,43,0.12);transform:translateY(-2px);box-shadow:var(--shadow-hover)}
.cfg-card-top{padding:16px 18px 12px;display:flex;align-items:flex-start;justify-content:space-between;gap:10px}
.cfg-card-label{font-size:14px;font-weight:700;color:var(--text-primary)}
.cfg-card-body{padding:0 18px 14px}
.cfg-code{background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:var(--radius-sm);padding:11px 13px;font-family:'Inter',monospace;font-size:10px;color:var(--royal-gold);word-break:break-all;line-height:1.7;max-height:80px;overflow-y:auto;margin-bottom:10px}
.cfg-card-actions{display:flex;gap:6px;flex-wrap:wrap;padding:0 18px 14px}

.log-list{display:flex;flex-direction:column}
.log-row{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid var(--border)}
.log-row:last-child{border-bottom:none}
.log-icon-s{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.log-icon-s.info{background:rgba(212,160,43,0.08);color:var(--royal-gold)}
.log-icon-s.ok{background:rgba(123,207,168,0.08);color:#7BCFA8}
.log-icon-s.warn{background:rgba(245,158,11,0.08);color:#F59E0B}
.log-icon-s.err{background:rgba(232,74,74,0.08);color:#E84A4A}
.log-content{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--text-primary);line-height:1.6}
.log-time{font-size:9.5px;color:var(--text-secondary);margin-top:3px;display:flex;align-items:center;gap:5px}

.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--surface);backdrop-filter:blur(20px);border:1px solid var(--border);color:var(--text-primary);border-radius:var(--radius);padding:11px 20px;font-size:12.5px;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow-lg);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(212,160,43,0.2);background:rgba(212,160,43,0.06);color:var(--royal-gold)}
.toast.err{border-color:rgba(232,74,74,0.2);background:rgba(232,74,74,0.04);color:#E84A4A}

.empty-state{text-align:center;padding:60px 20px;color:var(--text-secondary)}
.empty-state i{font-size:44px;opacity:.3;display:block;margin-bottom:14px}
.empty-state p{font-size:13px}

.chart-card{background:var(--surface-glass);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px 22px;margin-bottom:20px;box-shadow:var(--shadow-sm)}
.chart-title{font-size:13px;font-weight:800;color:var(--text-primary);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.chart-title i{color:var(--royal-gold)}
.chart-canvas-wrap{position:relative;height:300px}

@media(max-width:1100px){
  .stats-grid{grid-template-columns:repeat(2,1fr)}
  .server-bars{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:860px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,0.5)}
  .main{margin-right:0;padding-top:72px}
  .mobile-top{display:flex}
  .quick-actions{grid-template-columns:repeat(2,1fr)}
  .stats-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:520px){
  .stats-grid{grid-template-columns:1fr}
  .quick-actions{grid-template-columns:1fr}
  .main{padding:62px 12px 40px}
  .server-bars{grid-template-columns:1fr}
  .cfg-grid{grid-template-columns:1fr}
  .form-row{flex-direction:column}
}
</style>
</head>
<body>
<div class="bg-particles">
  <div class="bg-p" style="width:4px;height:4px;background:var(--royal-gold);top:10%;left:20%;animation-duration:18s"></div>
  <div class="bg-p" style="width:3px;height:3px;background:#F0D060;top:70%;left:40%;animation-duration:22s;animation-delay:-6s"></div>
  <div class="bg-p" style="width:5px;height:5px;background:var(--royal-gold);top:40%;left:70%;animation-duration:16s;animation-delay:-10s"></div>
  <div class="bg-p" style="width:3px;height:3px;background:#D4A02B;top:80%;left:15%;animation-duration:20s;animation-delay:-3s"></div>
  <div class="bg-p" style="width:4px;height:4px;background:#F0D060;top:25%;left:55%;animation-duration:19s;animation-delay:-8s"></div>
</div>
<div class="toast" id="toast"></div>
<div class="overlay" id="overlay"></div>

<!-- MODALS -->
<div class="modal-overlay" id="modal-create-user">
  <div class="modal-card">
    <div class="modal-head">
      <div class="modal-title"><i class="ti ti-user-plus"></i> ایجاد کاربر جدید</div>
      <button class="modal-close" onclick="closeModal('modal-create-user')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <form id="create-user-form">
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-user"></i> نام کاربری</label><input class="form-input" id="cu-username" placeholder="username" required></div>
          <div class="form-field"><label><i class="ti ti-lock"></i> رمز عبور</label><input class="form-input" id="cu-password" type="password" placeholder="••••" required></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-plug-connected"></i> پروتکل</label><select class="form-select" id="cu-protocol"><option value="vless">VLESS</option><option value="vmess">VMess</option><option value="trojan">Trojan</option><option value="shadowsocks">Shadowsocks</option><option value="reality">Reality</option></select></div>
          <div class="form-field"><label><i class="ti ti-server"></i> سرور</label><select class="form-select" id="cu-server"><option value="">انتخاب سرور...</option></select></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-gauge"></i> محدودیت ترافیک</label><input class="form-input" id="cu-traffic" type="number" min="0" step="0.1" placeholder="مقدار"></div>
          <div class="form-field"><label>واحد</label><select class="form-select" id="cu-traffic-unit"><option value="GB">GB</option><option value="MB">MB</option><option value="TB">TB</option><option value="unlimited">نامحدود</option></select></div>
        </div>
        <div class="form-row">
          <div class="form-field"><label><i class="ti ti-calendar"></i> روزهای انقضا</label><input class="form-input" id="cu-expire" type="number" min="0" placeholder="0 = نامحدود"></div>
          <div class="form-field"><label><i class="ti ti-users"></i> اتصال همزمان</label><input class="form-input" id="cu-concurrent" type="number" min="1" value="1"></div>
        </div>
        <div class="form-field"><label><i class="ti ti-notes"></i> یادداشت</label><textarea class="form-textarea" id="cu-notes" placeholder="یادداشت اختیاری..."></textarea></div>
        <div class="toggle-wrap">
          <button type="button" class="toggle-switch on" id="cu-active-toggle" onclick="this.classList.toggle('on')"></button>
          <span class="toggle-label">فعال</span>
        </div>
      </form>
    </div>
    <div class="modal-footer">
      <button class="btn btn-ghost" onclick="closeModal('modal-create-user')">انصراف</button>
      <button class="btn btn-primary" onclick="createUser()"><i class="ti ti-user-plus"></i> ایجاد کاربر</button>
    </div>
  </div>
</div>

<div class="modal-overlay" id="modal-config">
  <div class="modal-card" style="max-width:460px">
    <div class="modal-head">
      <div class="modal-title"><i class="ti ti-link"></i> کانفیگ</div>
      <button class="modal-close" onclick="closeModal('modal-config')"><i class="ti ti-x"></i></button>
    </div>
    <div class="modal-body">
      <div class="cfg-code" style="max-height:none;font-size:11px" id="config-text"></div>
      <div style="margin-top:14px;display:flex;gap:8px">
        <button class="btn btn-primary" onclick="copyConfigText()"><i class="ti ti-copy"></i> کپی</button>
        <button class="btn btn-ghost" onclick="showQRCode()"><i class="ti ti-qrcode"></i> QR Code</button>
      </div>
      <div id="config-qr" style="margin-top:14px;text-align:center;display:none">
        <img id="config-qr-img" src="" alt="QR" style="max-width:200px;border-radius:12px;background:#fff;padding:8px">
      </div>
    </div>
  </div>
</div>

<!-- MOBILE TOP -->
<div class="mobile-top">
  <div class="mobile-brand">
    <svg width="28" height="28" viewBox="0 0 100 100"><defs><linearGradient id="mg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#D4A02B"/><stop offset="100%" style="stop-color:#F0D060"/></linearGradient></defs><rect x="10" y="10" width="80" height="80" rx="12" fill="none" stroke="url(#mg1)" stroke-width="2"/><path d="M50,25 L50,75 M25,50 L75,50" stroke="url(#mg1)" stroke-width="2.5" stroke-linecap="round"/><circle cx="50" cy="50" r="10" fill="none" stroke="url(#mg1)" stroke-width="1.5"/><circle cx="50" cy="50" r="3.5" fill="url(#mg1)"/></svg>
    <span>Royal Nexus</span>
  </div>
  <div class="mobile-actions">
    <button class="mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-icon-mob"></i></button>
    <button class="mob-btn" id="menu-toggle" onclick="toggleSidebar()"><i class="ti ti-menu-2"></i></button>
  </div>
</div>

<!-- SIDEBAR -->
<aside class="sidebar" id="sidebar">
  <div class="sidebar-logo">
    <svg width="36" height="36" viewBox="0 0 100 100"><defs><linearGradient id="sg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#D4A02B"/><stop offset="100%" style="stop-color:#F0D060"/></linearGradient></defs><rect x="10" y="10" width="80" height="80" rx="14" fill="none" stroke="url(#sg1)" stroke-width="2"/><path d="M50,25 L50,75 M25,50 L75,50" stroke="url(#sg1)" stroke-width="2.5" stroke-linecap="round"/><circle cx="50" cy="50" r="12" fill="none" stroke="url(#sg1)" stroke-width="1.5"/><circle cx="50" cy="50" r="4" fill="url(#sg1)"/><path d="M50,30 L58,42 L66,50 L58,58 L50,70 L42,58 L34,50 L42,42 Z" fill="url(#sg1)" opacity="0.15"/></svg>
    <div><div class="sidebar-logo-text">Royal Nexus</div><div class="sidebar-logo-sub">Management Panel</div></div>
  </div>
  <div class="sidebar-nav">
    <div class="nav-section">منوی اصلی</div>
    <div class="nav-item active" data-page="dash"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-item" data-page="users"><i class="ti ti-users"></i> کاربران <span class="nav-badge" id="users-count">0</span></div>
    <div class="nav-item" data-page="configs"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="configs-count">0</span></div>
    <div class="nav-item" data-page="servers"><i class="ti ti-server-2"></i> سرورها</div>
    <div class="nav-item" data-page="plans"><i class="ti ti-receipt-2"></i> پلن‌ها</div>
    <div class="nav-item" data-page="groups"><i class="ti ti-folders"></i> گروه‌ها</div>
    <div class="nav-item" data-page="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-item" data-page="logs"><i class="ti ti-history"></i> لاگ‌ها</div>
    <div class="nav-section">سیستم</div>
    <div class="nav-item" data-page="api"><i class="ti ti-api"></i> API</div>
    <div class="nav-item" data-page="tools"><i class="ti ti-tools"></i> ابزارها</div>
    <div class="nav-item" data-page="settings"><i class="ti ti-settings"></i> تنظیمات</div>
    <div class="nav-item" data-page="logout" style="color:#E84A4A"><i class="ti ti-logout"></i> خروج</div>
  </div>
  <div class="sidebar-footer">
    <div class="sidebar-user">
      <div class="sidebar-avatar"><i class="ti ti-crown"></i></div>
      <div><div class="sidebar-user-name">ادمین</div><div class="sidebar-user-role">مدیر سیستم</div></div>
    </div>
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم تاریک</span></button>
    <button class="logout-btn" onclick="doLogout()"><i class="ti ti-logout"></i> خروج از حساب</button>
  </div>
</aside>

<!-- MAIN CONTENT -->
<main class="main">
  <!-- DASHBOARD PAGE -->
  <section class="page active" id="page-dash">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="topbar-sub" id="last-updated">در حال بارگذاری...</div></div>
      <div class="topbar-right">
        <span class="welcome-text">سلام ادمین 👑</span>
        <button class="bell-btn" title="اعلان‌ها"><i class="ti ti-bell"></i></button>
        <button class="btn btn-primary" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> ایجاد کاربر جدید</button>
      </div>
    </div>
    <div class="stats-grid">
      <div class="stat-card"><div class="stat-icon blue"><i class="ti ti-users"></i></div><div class="stat-label">کاربران فعال</div><div class="stat-value" id="s-active-users">—</div><div class="stat-sub up" id="s-users-trend"><i class="ti ti-trending-up"></i> —</div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-link"></i></div><div class="stat-label">کانفیگ‌های فعال</div><div class="stat-value" id="s-active-configs">—</div></div>
      <div class="stat-card"><div class="stat-icon purple"><i class="ti ti-transfer"></i></div><div class="stat-label">مصرف ترافیک</div><div class="stat-value" id="s-traffic">—<span style="font-size:14px;font-weight:500;color:var(--text-secondary)">GB</span></div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-server-2"></i></div><div class="stat-label">سرورهای آنلاین</div><div class="stat-value" id="s-online-servers">—</div><div class="stat-sub"><span class="dot dot-green pulse"></span> آنلاین</div></div>
    </div>
    <div class="quick-actions">
      <button class="qa-btn" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> افزودن کاربر</button>
      <button class="qa-btn" onclick="switchPage('configs')"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      <button class="qa-btn" onclick="switchPage('traffic')"><i class="ti ti-chart-bar"></i> گزارش ترافیک</button>
      <button class="qa-btn"><i class="ti ti-database"></i> بکاپ</button>
    </div>
    <div class="server-panel">
      <div class="server-title"><i class="ti ti-activity"></i> وضعیت سرور</div>
      <div class="server-bars">
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">CPU</span><span class="srv-bar-pct" id="srv-cpu">—%</span></div><div class="srv-bar-track"><div class="srv-bar-fill blue" id="srv-cpu-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">RAM</span><span class="srv-bar-pct" id="srv-ram">—%</span></div><div class="srv-bar-track"><div class="srv-bar-fill purple" id="srv-ram-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">Disk</span><span class="srv-bar-pct" id="srv-disk">—%</span></div><div class="srv-bar-track"><div class="srv-bar-fill amber" id="srv-disk-bar" style="width:0%"></div></div></div>
        <div class="srv-bar-item"><div class="srv-bar-label"><span class="srv-bar-name">Network</span><span class="srv-bar-pct" id="srv-net">— MB/s</span></div><div class="srv-bar-track"><div class="srv-bar-fill green" id="srv-net-bar" style="width:0%"></div></div></div>
      </div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>نام کاربری</th><th>پروتکل</th><th>مصرف</th><th>انقضا</th><th>وضعیت</th><th>عملیات</th></tr></thead>
        <tbody id="dash-users-table"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--text-secondary)">در حال بارگذاری...</td></tr></tbody>
      </table>
    </div>
  </section>

  <!-- USERS PAGE -->
  <section class="page" id="page-users">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-users"></i> کاربران</div><div class="topbar-sub">مدیریت کاربران و کانفیگ‌ها</div></div>
      <div class="topbar-right">
        <button class="btn btn-primary" onclick="openModal('modal-create-user')"><i class="ti ti-user-plus"></i> ایجاد کاربر جدید</button>
      </div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>نام کاربری</th><th>پروتکل</th><th>مصرف</th><th>انقضا</th><th>وضعیت</th><th>عملیات</th></tr></thead>
        <tbody id="users-table"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--text-secondary)">در حال بارگذاری...</td></tr></tbody>
      </table>
    </div>
  </section>

  <!-- CONFIGS PAGE -->
  <section class="page" id="page-configs">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="topbar-sub">مدیریت کانفیگ‌های کاربران</div></div>
      <div class="topbar-right"><span class="badge badge-blue" id="cfg-total">۰ کانفیگ</span></div>
    </div>
    <div class="cfg-grid" id="configs-grid"></div>
    <div class="empty-state" id="configs-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
  </section>

  <!-- TRAFFIC PAGE -->
  <section class="page" id="page-traffic">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="topbar-sub">آمار مصرف پهنای باند</div></div>
      <div class="topbar-right"><button class="btn btn-ghost" onclick="refreshAll()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>
    </div>
    <div class="chart-card">
      <div class="chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک (MB)</div>
      <div class="chart-canvas-wrap"><canvas id="traffic-chart"></canvas></div>
    </div>
    <div class="stats-grid" style="grid-template-columns:repeat(3,1fr)">
      <div class="stat-card"><div class="stat-icon blue"><i class="ti ti-arrow-up-right"></i></div><div class="stat-label">میانگین ساعتی</div><div class="stat-value" id="t-avg" style="font-size:20px">—</div></div>
      <div class="stat-card"><div class="stat-icon purple"><i class="ti ti-chart-bar"></i></div><div class="stat-label">پیک مصرف</div><div class="stat-value" id="t-peak" style="font-size:20px">—</div></div>
      <div class="stat-card"><div class="stat-icon green"><i class="ti ti-database"></i></div><div class="stat-label">کل مصرف</div><div class="stat-value" id="t-total" style="font-size:20px">—</div></div>
    </div>
  </section>

  <!-- LOGS PAGE -->
  <section class="page" id="page-logs">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-history"></i> لاگ‌ها</div><div class="topbar-sub">تاریخچه فعالیت‌های سیستم</div></div>
      <div class="topbar-right"><button class="btn btn-ghost" onclick="loadLogs()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>
    </div>
    <div class="table-wrap">
      <div class="log-list" id="logs-list"><div class="empty-state"><i class="ti ti-history-toggle"></i><p>در حال بارگذاری...</p></div></div>
    </div>
  </section>

  <!-- SERVERS PAGE -->
  <section class="page" id="page-servers">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-server-2"></i> سرورها</div></div></div>
    <div class="empty-state"><i class="ti ti-server-off"></i><p>بخش مدیریت سرورها</p></div>
  </section>

  <!-- PLANS PAGE -->
  <section class="page" id="page-plans">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-receipt-2"></i> پلن‌ها</div></div></div>
    <div class="empty-state"><i class="ti ti-package-off"></i><p>بخش مدیریت پلن‌ها</p></div>
  </section>

  <!-- GROUPS PAGE -->
  <section class="page" id="page-groups">
    <div class="topbar"><div><div class="topbar-title"><i class="ti ti-folders"></i> گروه‌ها</div></div></div>
    <div class="empty-state"><i class="ti ti-folders-off"></i><p>بخش مدیریت گروه‌ها</p></div>
  </section>

  <!-- SETTINGS PAGE -->
  <section class="page" id="page-settings">
    <div class="topbar">
      <div><div class="topbar-title"><i class="ti ti-settings"></i> تنظیمات</div><div class="topbar-sub">تنظیمات عمومی پنل</div></div>
      <div class="topbar-right"><button class="btn btn-primary" onclick="saveSettings()"><i class="ti ti-device-floppy"></i> ذخیره تغییرات</button></div>
    </div>

    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-world"></i> دامنه و شبکه</div>
      </div>
      <div style="padding:18px 22px">
        <div class="form-field">
          <label><i class="ti ti-world-www"></i> دامنه اصلی</label>
          <input class="form-input" id="set-domain" placeholder="example.com" dir="ltr">
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-route"></i> نوع انتقال پیش‌فرض</label>
            <select class="form-select" id="set-transport">
              <option value="ws">WebSocket (WS)</option>
              <option value="xhttp">XHTTP</option>
              <option value="tcp">TCP</option>
            </select>
          </div>
          <div class="form-field">
            <label><i class="ti ti-plug-connected"></i> مد اتصال پیش‌فرض</label>
            <select class="form-select" id="set-conn-mode">
              <option value="ws">WebSocket</option>
              <option value="xhttp">XHTTP</option>
              <option value="tcp">TCP</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-toggle-right"></i> پروتکل‌ها و مدها</div>
      </div>
      <div style="padding:18px 22px">
        <div class="form-row" style="margin-bottom:12px">
          <div class="form-field">
            <label><i class="ti ti-protocol"></i> پروتکل‌های فعال</label>
            <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:6px">
              <label style="display:flex;align-items:center;gap:5px;font-size:12px;cursor:pointer;padding:6px 12px;background:rgba(212,160,43,0.04);border-radius:8px;border:1px solid var(--border)"><input type="checkbox" id="set-proto-vless" checked onchange="updateProtoCheckboxes()"> VLESS</label>
              <label style="display:flex;align-items:center;gap:5px;font-size:12px;cursor:pointer;padding:6px 12px;background:rgba(212,160,43,0.04);border-radius:8px;border:1px solid var(--border)"><input type="checkbox" id="set-proto-vmess" onchange="updateProtoCheckboxes()"> VMess</label>
              <label style="display:flex;align-items:center;gap:5px;font-size:12px;cursor:pointer;padding:6px 12px;background:rgba(212,160,43,0.04);border-radius:8px;border:1px solid var(--border)"><input type="checkbox" id="set-proto-trojan" onchange="updateProtoCheckboxes()"> Trojan</label>
              <label style="display:flex;align-items:center;gap:5px;font-size:12px;cursor:pointer;padding:6px 12px;background:rgba(212,160,43,0.04);border-radius:8px;border:1px solid var(--border)"><input type="checkbox" id="set-proto-reality" onchange="updateProtoCheckboxes()"> Reality</label>
            </div>
          </div>
        </div>
        <div class="toggle-wrap" style="margin-bottom:10px">
          <button type="button" class="toggle-switch on" id="set-ws-mode" onclick="this.classList.toggle('on')"></button>
          <span class="toggle-label">WebSocket Mode</span>
        </div>
        <div class="toggle-wrap">
          <button type="button" class="toggle-switch on" id="set-xhttp-mode" onclick="this.classList.toggle('on')"></button>
          <span class="toggle-label">XHTTP Mode</span>
        </div>
      </div>
    </div>

    <div class="table-wrap" style="margin-bottom:18px">
      <div style="padding:18px 22px;border-bottom:1px solid var(--border)">
        <div class="server-title" style="margin-bottom:0"><i class="ti ti-shield-lock"></i> تنظیمات Reality</div>
      </div>
      <div style="padding:18px 22px">
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-plug"></i> پورت Reality</label>
            <input class="form-input" id="set-real-port" type="number" placeholder="1234">
          </div>
          <div class="form-field">
            <label><i class="ti ti-globe"></i> Destination (dest)</label>
            <input class="form-input" id="set-real-dest" placeholder="google.com:443" dir="ltr">
          </div>
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-key"></i> Public Key</label>
            <input class="form-input" id="set-real-pbk" placeholder="x25519 public key" dir="ltr">
          </div>
          <div class="form-field">
            <label><i class="ti ti-hash"></i> Short ID</label>
            <input class="form-input" id="set-real-sid" placeholder="6ba85179e30d4fc2" dir="ltr">
          </div>
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-link"></i> SpiderX Path</label>
            <input class="form-input" id="set-real-spx" placeholder="/" dir="ltr">
          </div>
          <div class="form-field">
            <label><i class="ti ti-globe"></i> SNI (Reality)</label>
            <input class="form-input" id="set-real-sni" placeholder="www.google.com" dir="ltr">
          </div>
        </div>
        <div class="form-row">
          <div class="form-field">
            <label><i class="ti ti-world"></i> دامنه خارجی</label>
            <input class="form-input" id="set-real-ext-domain" placeholder="ext.example.com" dir="ltr">
          </div>
          <div class="form-field">
            <label><i class="ti ti-plug"></i> پورت خارجی</label>
            <input class="form-input" id="set-real-ext-port" type="number" placeholder="443">
          </div>
        </div>
        <div style="margin-top:12px;display:flex;gap:8px">
          <button class="btn btn-ghost" onclick="generateRealityKeys()"><i class="ti ti-key"></i> تولید کلید Reality</button>
          <button class="btn btn-ghost" onclick="saveRealitySettings()"><i class="ti ti-device-floppy"></i> ذخیره Reality</button>
        </div>
      </div>
    </div>
  </section>
</main>

<script>
/* ============ GLOBALS ============ */
var isDark=true;
var currentPage='dash';
var currentConfigText='';
var allUsers=[],allLinks=[];

function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  var ti=document.getElementById('theme-icon'),tm=document.getElementById('theme-icon-mob'),tl=document.getElementById('theme-label');
  if(ti)ti.className='ti '+(dark?'ti-sun':'ti-moon');
  if(tm)tm.className='ti '+(dark?'ti-sun':'ti-moon');
  if(tl)tl.textContent=dark?'تم روشن':'تم تاریک';
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('royal-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);

function toast(msg,type){
  var t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(function(){t.classList.remove('show')},2500);
}
function esc(s){return String(s||'').replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,function(d){return'۰۱۲۳۴۵۶۷۸۹'[d]})}

async function authFetch(url,opts){
  var r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
async function checkAuth(){
  try{var r=await fetch('/api/me');var d=await r.json();if(!d.authenticated)location.href='/login'}catch(e){}
}
async function doLogout(){
  try{await fetch('/api/logout',{method:'POST'})}catch(e){}
  location.href='/login';
}

function toggleSidebar(){
  var sb=document.getElementById('sidebar'),ov=document.getElementById('overlay');
  sb.classList.toggle('open');ov.classList.toggle('show');
}
document.getElementById('menu-toggle').onclick=toggleSidebar;
document.getElementById('overlay').onclick=toggleSidebar;

function switchPage(name){
  if(name==='logout'){doLogout();return}
  currentPage=name;
  document.querySelectorAll('.nav-item').forEach(function(el){el.classList.toggle('active',el.dataset.page===name)});
  document.querySelectorAll('.page').forEach(function(el){el.classList.toggle('active',el.id==='page-'+name)});
  toggleSidebar();window.scrollTo({top:0,behavior:'smooth'});
  var loaders={users:loadUsers,configs:loadConfigs,traffic:loadTraffic,logs:loadLogs,dash:loadDashboard,settings:loadSettings};
  if(loaders[name])loaders[name]();
}
document.querySelectorAll('.nav-item').forEach(function(el){el.onclick=function(){switchPage(el.dataset.page)}});

function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
document.querySelectorAll('.modal-overlay').forEach(function(m){m.addEventListener('click',function(e){if(e.target===m)m.classList.remove('open')})});

async function createUser(){
  var form=document.getElementById('create-user-form');
  var traffic=document.getElementById('cu-traffic').value;
  var unit=document.getElementById('cu-traffic-unit').value;
  var active=document.getElementById('cu-active-toggle').classList.contains('on');
  var body={
    label:document.getElementById('cu-username').value.trim(),
    password:document.getElementById('cu-password').value,
    protocol:document.getElementById('cu-protocol').value,
    limit_value:traffic||'0',
    limit_unit:unit==='unlimited'?'GB':unit,
    expires_days:document.getElementById('cu-expire').value||'0',
    concurrent:document.getElementById('cu-concurrent').value||'1',
    server_id:document.getElementById('cu-server').value||null,
    note:document.getElementById('cu-notes').value.trim(),
    active:active
  };
  if(!body.label){toast('نام کاربری الزامی است','err');return}
  try{
    var r=await authFetch('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok){var d=await r.json().catch(function(){return{}});throw new Error(d.detail||'خطا')}
    toast('کاربر با موفقیت ایجاد شد ✓','ok');
    closeModal('modal-create-user');
    ['cu-username','cu-password','cu-traffic','cu-expire','cu-concurrent','cu-notes'].forEach(function(id){document.getElementById(id).value=''});
    loadUsers();loadConfigs();loadDashboard();
  }catch(e){toast(e.message,'err')}
}

async function loadUsers(){
  try{
    var r=await authFetch('/api/links'),d=await r.json();
    allLinks=d.links||[];
    document.getElementById('users-count').textContent=allLinks.length;
    renderUsersTable(allLinks,'users-table');
  }catch(e){console.error(e)}
}

function renderUsersTable(links,tableId){
  var tbody=document.getElementById(tableId);
  if(!links.length){tbody.innerHTML='<tr><td colspan="6"><div class="empty-state"><i class="ti ti-users-off"></i><p>کاربری وجود ندارد</p></div></td></tr>';return}
  tbody.innerHTML=links.map(function(l){
    var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
    var bc=pct>90?'#E84A4A':pct>70?'#F59E0B':'#D4A02B';
    var lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
    var protoClass=l.protocol==='vless'||l.protocol==='vless-ws'?'pb-vless':l.protocol==='vmess'?'pb-vmess':l.protocol==='trojan'?'pb-trojan':l.protocol==='shadowsocks'?'pb-ss':'pb-vless';
    var protoFa=l.protocol==='vless-ws'?'VLESS':l.protocol==='vmess'?'VMess':l.protocol==='trojan'?'Trojan':l.protocol==='shadowsocks'?'Shadowsocks':l.protocol==='reality'?'Reality':l.protocol||'VLESS';
    var isActive=l.active&&!l.expired;
    var expText=l.expired?'منقضی':l.expires_at?new Date(l.expires_at).toLocaleDateString('fa-IR'):'نامحدود';
    var expCls=l.expired?'exp-bad':l.expires_at?'exp-ok':'exp-ok';
    return '<tr><td style="font-weight:600">'+esc(l.label)+'</td>'+
      '<td><span class="proto-badge '+protoClass+'">'+protoFa+'</span></td>'+
      '<td><div class="usage-bar-wrap"><div class="usage-bar"><div class="usage-fill" style="width:'+pct+'%;background:'+bc+'"></div></div><div class="usage-text"><span>'+fmtB(l.used_bytes)+'</span><span>'+lim+'</span></div></div></td>'+
      '<td><span class="exp-chip '+expCls+'">'+expText+'</span></td>'+
      '<td><div class="status-dot '+(isActive?'active':'expired')+'"><span class="dot '+(isActive?'dot-green':'dot-red')+' '+(isActive?'pulse':'')+'"></span>'+(isActive?'فعال':'غیرفعال')+'</div></td>'+
      '<td><div class="action-btns">'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="viewConfig(\''+l.uuid+'\')" title="مشاهده"><i class="ti ti-eye"></i></button>'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="copyLink(\''+l.uuid+'\')" title="کپی"><i class="ti ti-copy"></i></button>'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="toggleUser(\''+l.uuid+'\')" title="فعال/غیرفعال"><i class="ti ti-toggle-'+(isActive?'right':'left')+'"></i></button>'+
        '<button class="btn btn-sm btn-danger btn-icon" onclick="deleteUser(\''+l.uuid+'\')" title="حذف"><i class="ti ti-trash"></i></button>'+
      '</div></td></tr>';
  }).join('');
}

async function viewConfig(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link){toast('کانفیگ یافت نشد','err');return}
  currentConfigText=link.vless_link||'';
  document.getElementById('config-text').textContent=currentConfigText;
  document.getElementById('config-qr').style.display='none';
  openModal('modal-config');
}
function copyConfigText(){
  if(!currentConfigText)return;
  navigator.clipboard.writeText(currentConfigText).then(function(){toast('کانفیگ کپی شد ✓','ok')});
}
function showQRCode(){
  if(!currentConfigText)return;
  var img='https://api.qrserver.com/v1/create-qr-code/?size=220x220&data='+encodeURIComponent(currentConfigText);
  document.getElementById('config-qr-img').src=img;
  document.getElementById('config-qr').style.display='block';
}
function copyLink(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link||!link.vless_link)return;
  navigator.clipboard.writeText(link.vless_link).then(function(){toast('لینک کپی شد ✓','ok')});
}
async function toggleUser(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link)return;
  try{
    var r=await authFetch('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:!link.active})});
    if(!r.ok)throw new Error();
    toast('وضعیت تغییر کرد ✓','ok');loadUsers();loadDashboard();
  }catch(e){toast('خطا در تغییر وضعیت','err')}
}
async function deleteUser(uuid){
  if(!confirm('آیا از حذف این کاربر اطمینان دارید؟'))return;
  try{
    var r=await authFetch('/api/links/'+uuid,{method:'DELETE'});
    if(!r.ok)throw new Error();
    toast('کاربر حذف شد ✓','ok');loadUsers();loadDashboard();loadConfigs();
  }catch(e){toast('خطا در حذف','err')}
}

async function loadConfigs(){
  try{
    var r=await authFetch('/api/links'),d=await r.json();
    allLinks=d.links||[];
    document.getElementById('configs-count').textContent=allLinks.length;
    document.getElementById('cfg-total').textContent=toFa(allLinks.length)+' کانفیگ';
    var grid=document.getElementById('configs-grid'),empty=document.getElementById('configs-empty');
    if(!allLinks.length){grid.innerHTML='';empty.style.display='block';return}
    empty.style.display='none';
    grid.innerHTML=allLinks.map(function(l){
      var protoFa=l.protocol==='vless-ws'?'VLESS':l.protocol==='vmess'?'VMess':l.protocol==='trojan'?'Trojan':l.protocol==='reality'?'Reality':l.protocol||'VLESS';
      var protoClass=l.protocol==='vless-ws'?'pb-vless':l.protocol==='vmess'?'pb-vmess':l.protocol==='trojan'?'pb-trojan':'pb-vless';
      var isActive=l.active&&!l.expired;
      var pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
      return '<div class="cfg-card-item">'+
        '<div class="cfg-card-top"><span class="cfg-card-label">'+esc(l.label)+'</span><span class="badge '+(isActive?'badge-green':'badge-red')+'"><span class="dot '+(isActive?'dot-green':'dot-red')+' '+(isActive?'pulse':'')+'"></span> '+(isActive?'فعال':'غیرفعال')+'</span></div>'+
        '<div class="cfg-card-body"><span class="proto-badge '+protoClass+'" style="margin-bottom:8px;display:inline-block">'+protoFa+'</span>'+
        '<div class="usage-bar-wrap" style="margin-bottom:8px"><div class="usage-bar"><div class="usage-fill" style="width:'+pct+'%"></div></div><div class="usage-text"><span>'+fmtB(l.used_bytes)+'</span><span>'+(l.limit_bytes===0?'∞':fmtB(l.limit_bytes))+'</span></div></div></div>'+
        '<div class="cfg-card-actions">'+
        '<button class="btn btn-sm btn-ghost" onclick="viewConfig(\''+l.uuid+'\')"><i class="ti ti-eye"></i> مشاهده</button>'+
        '<button class="btn btn-sm btn-ghost" onclick="copyLink(\''+l.uuid+'\')"><i class="ti ti-copy"></i> کپی</button>'+
        '<button class="btn btn-sm btn-ghost btn-icon" onclick="showQRForLink(\''+l.uuid+'\')"><i class="ti ti-qrcode"></i></button>'+
        '</div></div>';
    }).join('');
  }catch(e){console.error(e)}
}
function showQRForLink(uuid){
  var link=allLinks.find(function(l){return l.uuid===uuid});
  if(!link||!link.vless_link)return;
  currentConfigText=link.vless_link;
  document.getElementById('config-text').textContent=currentConfigText;
  showQRCode();
  openModal('modal-config');
}

var trafficChart=null;
async function loadTraffic(){
  try{
    var r=await authFetch('/stats'),d=await r.json();
    document.getElementById('t-total').textContent=d.total_traffic_mb.toFixed(1)+' MB';
    if(d.hourly){
      var labels=Object.keys(d.hourly).sort(),vals=labels.map(function(k){return +(d.hourly[k]/1024**2).toFixed(2)});
      if(vals.length){
        var total=vals.reduce(function(a,b){return a+b},0);
        var avg=total/vals.length;
        var peak=Math.max.apply(null,vals);
        document.getElementById('t-avg').textContent=avg.toFixed(2)+' MB';
        document.getElementById('t-peak').textContent=peak.toFixed(2)+' MB';
      }
      var canvas=document.getElementById('traffic-chart');
      if(!canvas)return;
      var ctx=canvas.getContext('2d');
      if(trafficChart){trafficChart.data.labels=labels;trafficChart.data.datasets[0].data=vals;trafficChart.update()}
      else{
        var grad=ctx.createLinearGradient(0,0,0,300);
        grad.addColorStop(0,'rgba(212,160,43,0.35)');grad.addColorStop(1,'rgba(212,160,43,0)');
        trafficChart=new Chart(ctx,{
          type:'line',data:{labels:labels,datasets:[{data:vals,borderColor:'#D4A02B',backgroundColor:grad,fill:true,tension:.4,pointRadius:0,borderWidth:2.5}]},
          options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
            scales:{x:{grid:{display:false},ticks:{font:{size:9,color:'rgba(212,160,43,0.4)'}}},y:{grid:{color:'rgba(212,160,43,0.04)'},ticks:{font:{size:9,color:'rgba(212,160,43,0.4)'},callback:function(v){return v+' MB'}}}},
            interaction:{mode:'index',intersect:false}}
        });
      }
    }
  }catch(e){console.error(e)}
}

async function loadLogs(){
  try{
    var r=await authFetch('/api/activity'),d=await r.json();
    var logs=(d.logs||[]).slice().reverse();
    var el=document.getElementById('logs-list');
    if(!logs.length){el.innerHTML='<div class="empty-state"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div>';return}
    var icMap={ok:'ti-circle-check ok',err:'ti-circle-x err',warn:'ti-alert-triangle warn',info:'ti-info-circle info'};
    el.innerHTML=logs.map(function(l){
      return '<div class="log-row"><div class="log-icon-s '+(l.level||'info')+'"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div><div class="log-content"><div class="log-msg">'+esc(l.message)+'</div><div class="log-time"><i class="ti ti-clock"></i> '+new Date(l.time).toLocaleString('fa-IR')+'</div></div></div>';
    }).join('');
  }catch(e){console.error(e)}
}

async function loadDashboard(){
  try{
    var r=await authFetch('/stats'),d=await r.json();
    document.getElementById('s-active-users').textContent=d.active_links||'0';
    document.getElementById('s-active-configs').textContent=d.active_links||'0';
    document.getElementById('s-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span style="font-size:14px;font-weight:500;color:var(--text-secondary)">GB</span>';
    document.getElementById('s-online-servers').textContent='1';
    document.getElementById('s-users-trend').innerHTML='<i class="ti ti-trending-up"></i> '+toFa(d.active_connections||0)+' اتصال';
    document.getElementById('last-updated').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('srv-cpu').textContent='32%';document.getElementById('srv-cpu-bar').style.width='32%';
    document.getElementById('srv-ram').textContent='58%';document.getElementById('srv-ram-bar').style.width='58%';
    document.getElementById('srv-disk').textContent='41%';document.getElementById('srv-disk-bar').style.width='41%';
    document.getElementById('srv-net').textContent='12 MB/s';document.getElementById('srv-net-bar').style.width='24%';
    var lr=await authFetch('/api/links'),ld=await lr.json();
    allLinks=ld.links||[];
    document.getElementById('users-count').textContent=allLinks.length;
    renderUsersTable(allLinks,'dash-users-table');
  }catch(e){console.error(e)}
}

async function loadSettings(){
  try{
    var r=await authFetch('/api/tools/settings'),d=await r.json();
    document.getElementById('set-domain').value=d.domain||'';
    document.getElementById('set-transport').value=d.default_transport||'ws';
    document.getElementById('set-conn-mode').value=d.default_connection_mode||'ws';
    var protos=d.enabled_protocols||['vless'];
    document.getElementById('set-proto-vless').checked=protos.includes('vless');
    document.getElementById('set-proto-vmess').checked=protos.includes('vmess');
    document.getElementById('set-proto-trojan').checked=protos.includes('trojan');
    document.getElementById('set-proto-reality').checked=protos.includes('reality');
    var wsEl=document.getElementById('set-ws-mode');
    d.websocket_mode!==false?wsEl.classList.add('on'):wsEl.classList.remove('on');
    var xhEl=document.getElementById('set-xhttp-mode');
    d.xhttp_mode!==false?xhEl.classList.add('on'):xhEl.classList.remove('on');
    var real=d.reality||{};
    document.getElementById('set-real-port').value=real.port||1234;
    document.getElementById('set-real-dest').value=real.dest||'google.com:443';
    document.getElementById('set-real-pbk').value=real.public_key||'';
    document.getElementById('set-real-sid').value=real.short_id||'6ba85179e30d4fc2';
    document.getElementById('set-real-spx').value=real.spiderx||'/';
    document.getElementById('set-real-sni').value=real.sni||d.domain||'';
    document.getElementById('set-real-ext-domain').value=real.external_domain||d.domain||'';
    document.getElementById('set-real-ext-port').value=real.external_port||443;
  }catch(e){console.error(e)}
}

async function saveSettings(){
  try{
    var protos=[];
    if(document.getElementById('set-proto-vless').checked)protos.push('vless');
    if(document.getElementById('set-proto-vmess').checked)protos.push('vmess');
    if(document.getElementById('set-proto-trojan').checked)protos.push('trojan');
    if(document.getElementById('set-proto-reality').checked)protos.push('reality');
    var body={
      domain:document.getElementById('set-domain').value.trim(),
      default_transport:document.getElementById('set-transport').value,
      default_connection_mode:document.getElementById('set-conn-mode').value,
      enabled_protocols:protos,
      websocket_mode:document.getElementById('set-ws-mode').classList.contains('on'),
      xhttp_mode:document.getElementById('set-xhttp-mode').classList.contains('on')
    };
    var r=await authFetch('/api/tools/settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    toast('تنظیمات ذخیره شد ✓','ok');
  }catch(e){toast('خطا در ذخیره تنظیمات','err')}
}

async function saveRealitySettings(){
  try{
    var body={
      port:parseInt(document.getElementById('set-real-port').value)||1234,
      dest:document.getElementById('set-real-dest').value.trim(),
      public_key:document.getElementById('set-real-pbk').value.trim(),
      short_id:document.getElementById('set-real-sid').value.trim(),
      spiderx:document.getElementById('set-real-spx').value.trim(),
      sni:document.getElementById('set-real-sni').value.trim(),
      external_domain:document.getElementById('set-real-ext-domain').value.trim(),
      external_port:parseInt(document.getElementById('set-real-ext-port').value)||443
    };
    var r=await authFetch('/api/tools/reality-settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    toast('تنظیمات Reality ذخیره شد ✓','ok');
  }catch(e){toast('خطا در ذخیره Reality','err')}
}

async function generateRealityKeys(){
  try{
    var r=await authFetch('/api/tools/generate-reality-keys',{method:'POST'});
    var d=await r.json();
    document.getElementById('set-real-pbk').value=d.public_key||'';
    toast('کلیدهای Reality تولید شد ✓','ok');
  }catch(e){toast('خطا در تولید کلید','err')}
}

function updateProtoCheckboxes(){}

function refreshAll(){
  loadDashboard();loadUsers();loadConfigs();loadTraffic();loadLogs();
  toast('بروزرسانی شد ✓','ok');
}

document.addEventListener('DOMContentLoaded',async function(){
  await checkAuth();
  loadDashboard();
  setInterval(function(){
    if(currentPage==='dash')loadDashboard();
    if(currentPage==='users')loadUsers();
    if(currentPage==='configs')loadConfigs();
    if(currentPage==='traffic')loadTraffic();
    if(currentPage==='logs')loadLogs();
    if(currentPage==='settings')loadSettings();
  },5000);
});
</script>
</body></html>"""

def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Royal Nexus · اشتراک</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
:root{{
  --royal-gold:#D4A02B;--royal-dark:#0A0806;--royal-light:#14100E;
  --text-primary:#EDE8E0;--text-secondary:rgba(212,160,43,0.4);
  --bg:var(--royal-dark);--surface:rgba(20,16,14,0.85);--surface-glass:rgba(20,16,14,0.7);
  --border:rgba(212,160,43,0.06);--radius:18px;--radius-lg:24px;--radius-xl:28px;
  --shadow-sm:0 2px 8px rgba(0,0,0,0.3);--shadow-md:0 8px 24px rgba(0,0,0,0.4);
  --shadow-lg:0 16px 48px rgba(0,0,0,0.5);
}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{min-height:100%;background:var(--bg);font-family:'Vazirmatn',sans-serif;color:var(--text-primary);font-size:14px}}
.bg-glow{{position:fixed;inset:0;z-index:0;pointer-events:none}}
.bg-orb{{position:absolute;border-radius:50%;filter:blur(120px);opacity:.08;animation:float 14s ease-in-out infinite}}
.bg-orb:nth-child(1){{width:450px;height:450px;background:#D4A02B;top:-150px;left:-100px}}
.bg-orb:nth-child(2){{width:350px;height:350px;background:#F0D060;bottom:-100px;right:-80px;animation-delay:-7s}}
@keyframes float{{0%,100%{{transform:translateY(0) scale(1)}}50%{{transform:translateY(-25px) scale(1.04)}}}}
.wrap{{position:relative;z-index:10;max-width:680px;margin:0 auto;padding:28px 16px 60px}}
.top-bar{{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;gap:10px}}
.brand{{display:flex;align-items:center;gap:10px}}
.brand svg{{width:38px;height:38px;filter:drop-shadow(0 0 20px rgba(212,160,43,0.12))}}
.brand-name{{font-size:14px;font-weight:900;background:linear-gradient(135deg,#D4A02B,#F0D060);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.brand-sub{{font-size:9.5px;color:var(--text-secondary)}}
.theme-toggle{{width:38px;height:38px;border-radius:var(--radius);background:var(--surface);backdrop-filter:blur(12px);border:1px solid var(--border);color:var(--text-secondary);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;transition:all .2s}}
.theme-toggle:hover{{background:rgba(212,160,43,0.06);color:var(--royal-gold)}}
.info-card{{background:var(--surface);backdrop-filter:blur(20px) saturate(160%);border:1px solid var(--border);border-radius:var(--radius-xl);padding:28px 26px 24px;margin-bottom:18px;box-shadow:var(--shadow-lg);position:relative;overflow:hidden}}
.info-card::before{{content:'';position:absolute;top:0;right:0;width:180px;height:180px;background:radial-gradient(circle,rgba(212,160,43,0.04),transparent 70%);pointer-events:none}}
.info-name{{font-size:22px;font-weight:800;color:var(--text-primary);position:relative;z-index:1;letter-spacing:-.02em}}
.info-desc{{font-size:12.5px;color:var(--text-secondary);margin-top:6px;position:relative;z-index:1;line-height:1.7}}
.info-stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px;position:relative;z-index:1}}
.info-stat{{text-align:center;padding:12px 8px;background:rgba(212,160,43,0.04);border-radius:var(--radius);border:1px solid var(--border)}}
.info-s-val{{font-size:18px;font-weight:800;color:var(--text-primary)}}
.info-s-label{{font-size:9px;color:var(--text-secondary);margin-top:3px;font-weight:600;text-transform:uppercase;letter-spacing:.04em}}
.section-title{{font-size:12.5px;font-weight:800;color:var(--text-secondary);margin-bottom:12px;display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}}
.section-title i{{color:var(--royal-gold);font-size:15px}}
.cfg-card{{background:var(--surface);backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px 20px 18px;margin-bottom:12px;box-shadow:var(--shadow-sm);transition:all .3s}}
.cfg-card:hover{{border-color:rgba(212,160,43,0.12);transform:translateY(-2px);box-shadow:var(--shadow-md)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px}}
.cfg-name{{font-size:14px;font-weight:700;color:var(--text-primary)}}
.cfg-status{{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;white-space:nowrap}}
.cfg-status.ok{{background:rgba(212,160,43,0.08);color:var(--royal-gold)}}
.cfg-status.no{{background:rgba(232,74,74,0.08);color:#E84A4A}}
.cfg-code{{background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:var(--radius);padding:12px 14px;font-family:'Inter',monospace;font-size:10px;color:var(--royal-gold);word-break:break-all;line-height:1.7;margin-bottom:10px;max-height:80px;overflow-y:auto}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap}}
.btn{{font-family:'Vazirmatn',sans-serif;font-size:11.5px;font-weight:700;border-radius:var(--radius);padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;border:none;transition:all .2s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(135deg,#D4A02B,#F0D060);color:var(--royal-dark);box-shadow:0 4px 14px rgba(212,160,43,0.12)}}
.btn-p:hover{{transform:translateY(-1px);box-shadow:0 6px 20px rgba(212,160,43,0.18)}}
.btn-ghost{{background:rgba(212,160,43,0.04);color:var(--royal-gold);border:1px solid rgba(212,160,43,0.08)}}
.btn-ghost:hover{{background:rgba(212,160,43,0.08)}}
.lock-page{{display:flex;align-items:center;justify-content:center;min-height:70vh}}
.lock-card{{background:var(--surface);backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:var(--radius-xl);padding:40px 32px 34px;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow-lg)}}
.lock-icon{{width:64px;height:64px;border-radius:18px;background:rgba(212,160,43,0.08);border:1px solid rgba(212,160,43,0.12);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;font-size:28px;color:var(--royal-gold)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--text-primary)}}
.lock-sub{{font-size:12px;color:var(--text-secondary);margin-bottom:20px;line-height:1.7}}
.lock-field{{position:relative;margin-bottom:14px}}
.lock-input{{width:100%;padding:13px 44px;border-radius:var(--radius);border:1.5px solid var(--border);background:rgba(255,255,255,0.04);backdrop-filter:blur(8px);color:var(--text-primary);font-family:inherit;font-size:14px;text-align:center;outline:none;transition:all .2s;letter-spacing:.1em}}
.lock-input:focus{{border-color:var(--royal-gold);box-shadow:0 0 0 4px rgba(212,160,43,0.04)}}
.lock-icon-left{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--text-secondary);font-size:16px;pointer-events:none}}
.lock-err{{color:#E84A4A;font-size:11px;margin-bottom:10px;min-height:18px}}
.toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--surface);backdrop-filter:blur(16px);border:1px solid var(--border);color:var(--text-primary);border-radius:var(--radius);padding:10px 20px;font-size:12px;opacity:0;transition:all .3s;z-index:999;pointer-events:none;white-space:nowrap;box-shadow:var(--shadow-md)}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(212,160,43,0.2);color:var(--royal-gold)}}
.empty{{text-align:center;padding:60px 20px;color:var(--text-secondary)}}
.empty i{{font-size:40px;opacity:.3;display:block;margin-bottom:12px}}
.footer{{text-align:center;padding-top:30px;font-size:10.5px;color:var(--text-secondary)}}
@media(max-width:500px){{.info-stats{{grid-template-columns:1fr 1fr}}.wrap{{padding:20px 12px 50px}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>
</head>
<body>
<div class="bg-glow"><div class="bg-orb"></div><div class="bg-orb"></div></div>
<div class="toast" id="toast"></div>
<div class="wrap">
  <div class="top-bar">
    <div class="brand">
      <svg width="38" height="38" viewBox="0 0 100 100"><defs><linearGradient id="bgg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#D4A02B"/><stop offset="100%" style="stop-color:#F0D060"/></linearGradient></defs><rect x="10" y="10" width="80" height="80" rx="12" fill="none" stroke="url(#bgg)" stroke-width="2"/><path d="M50,25 L50,75 M25,50 L75,50" stroke="url(#bgg)" stroke-width="2.5" stroke-linecap="round"/><circle cx="50" cy="50" r="10" fill="none" stroke="url(#bgg)" stroke-width="1.5"/><circle cx="50" cy="50" r="3.5" fill="url(#bgg)"/></svg>
      <div><div class="brand-name">Royal Nexus</div><div class="brand-sub">Gateway</div></div>
    </div>
    <button class="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
  </div>
  <div id="root"><div class="empty"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i><p>در حال بارگذاری...</p></div></div>
  <div class="footer">Royal Nexus · Gateway</div>
</div>
<script>
var UUID_KEY='{uuid_key}',savedPw='',currentData=null;
var isDark=localStorage.getItem('royal-pub-theme')==='dark';
function applyTheme(d){{document.documentElement.setAttribute('data-theme',d?'dark':'light');document.getElementById('theme-icon').className='ti '+(d?'ti-sun':'ti-moon')}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('royal-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);
function toast(m,t){{var el=document.getElementById('toast');el.textContent=m;el.className='toast show'+(t?' '+t:'');setTimeout(function(){{el.classList.remove('show')}},2400)}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]}})}}
function fmtB(b){{if(!b)return'0 B';if(b<1024)return b+' B';if(b<1024**2)return(b/1024).toFixed(1)+' KB';if(b<1024**3)return(b/1024**2).toFixed(2)+' MB';return(b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,function(d){{return'۰۱۲۳۴۵۶۷۸۹'[d]}})}}
async function loadData(pw){{var u='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');var r=await fetch(u);return r.json()}}
function renderLock(name,err){{document.getElementById('root').innerHTML='<div class="lock-page"><div class="lock-card"><div class="lock-icon"><i class="ti ti-shield-lock"></i></div><div class="lock-title">'+esc(name)+'</div><div class="lock-sub">این گروه با رمز محافظت می‌شود</div><div class="lock-err" id="lock-err">'+(err?'<i class="ti ti-alert-circle"></i> '+esc(err):'')+'</div><div class="lock-field"><i class="ti ti-lock lock-icon-left"></i><input class="lock-input" type="password" id="lock-pw" placeholder="••••••••" autofocus></div><button class="btn btn-p" style="width:100%;justify-content:center;padding:12px" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود</button></div></div>';document.getElementById('lock-pw').addEventListener('keydown',function(e){{if(e.key==='Enter')submitLock()}})}}
async function submitLock(){{var pw=document.getElementById('lock-pw').value;var d=await loadData(pw);if(d.locked){{renderLock(d.name,'رمز اشتباه است');return}}savedPw=pw;renderContent(d)}}
function renderContent(d){{currentData=d;var active=d.links.filter(function(l){{return l.active}}).length;var subUrl=d.sub_url||(location.protocol+'//'+location.host+'/sub-group/'+UUID_KEY);subUrl+=savedPw?'?pw='+encodeURIComponent(savedPw):'';
document.getElementById('root').innerHTML='<div class="info-card"><div class="info-name">'+esc(d.name)+'</div>'+(d.desc?'<div class="info-desc">'+esc(d.desc)+'</div>':'')+
'<div class="info-stats"><div class="info-stat"><div class="info-s-val">'+toFa(active)+'</div><div class="info-s-label">کانفیگ فعال</div></div><div class="info-stat"><div class="info-s-val">'+toFa(d.links.length)+'</div><div class="info-s-label">کل کانفیگ‌ها</div></div><div class="info-stat"><div class="info-s-val">'+esc(d.total_used_fmt||'0')+'</div><div class="info-s-label">مصرف</div></div></div></div>'+
'<div class="section-title"><i class="ti ti-link"></i> کانفیگ‌ها ('+toFa(d.links.length)+' عدد)</div>'+
(d.links.length?d.links.map(function(l){{return'<div class="cfg-card"><div class="cfg-head"><div class="cfg-name">'+esc(l.label)+'</div><span class="cfg-status '+(l.active?'ok':'no')+'">'+(l.active?'<i class="ti ti-circle-check"></i> فعال':'<i class="ti ti-circle-x"></i> غیرفعال')+'</span></div><div class="cfg-code">'+esc(l.vless_link)+'</div><div class="cfg-actions"><button class="btn btn-p" onclick="navigator.clipboard.writeText(\''+esc(l.vless_link).replace(/'/g,"\\'")+'\').then(function(){{toast(\'کپی شد ✓\',\'ok\')}})"><i class="ti ti-copy"></i> کپی لینک</button><button class="btn btn-ghost" onclick="window.open(\'https://api.qrserver.com/v1/create-qr-code/?size=220x220&data='+encodeURIComponent(l.vless_link)+'\',\'_blank\')"><i class="ti ti-qrcode"></i> QR Code</button></div></div>'}}).join(''):'<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی در این گروه وجود ندارد</p></div>')+
'<div style="margin-top:16px;text-align:center"><button class="btn btn-ghost" style="justify-content:center" onclick="location.reload()"><i class="ti ti-refresh"></i> بروزرسانی</button></div>';
}}
async function init(){{try{{var d=await loadData();if(d.locked){{renderLock(d.name);return}}renderContent(d)}}catch(e){{document.getElementById('root').innerHTML='<div class="empty"><i class="ti ti-alert-circle" style="color:#E84A4A"></i><p>خطا در بارگذاری</p></div>'}}}}
init();
</script>
</body></html>""" 
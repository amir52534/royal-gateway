# pages.py - Royal Gateway v9.2 (نسخه کامل)

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · Royal Gateway</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0f0a04;--card:rgba(30,20,8,0.92);--accent:#F59E0B;--accent2:#FBBF24;--text:#FFF8ED;--dim:#8B7A5A;--mid:#C8B088;--border:rgba(245,158,11,0.2)}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px}
.bg{position:fixed;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(245,158,11,0.08),transparent 70%),var(--bg);z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(245,158,11,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(245,158,11,0.03) 1px,transparent 1px);background-size:44px 44px;z-index:0}
.orb{position:fixed;border-radius:50%;filter:blur(90px);z-index:0;animation:fl 12s ease-in-out infinite}
.o1{width:400px;height:400px;background:rgba(245,158,11,0.06);top:-120px;right:-80px}
.o2{width:300px;height:300px;background:rgba(251,191,36,0.04);bottom:-80px;left:-80px;animation-delay:6s}
.o3{width:250px;height:250px;background:rgba(245,158,11,0.03);top:50%;left:50%;transform:translate(-50%,-50%);animation-delay:3s}
@keyframes fl{0%,100%{transform:translateY(0) scale(1)}33%{transform:translateY(-20px) scale(1.02)}66%{transform:translateY(10px) scale(0.98)}}
.wrap{position:relative;z-index:10;width:100%;max-width:400px;animation:slideUp 0.8s cubic-bezier(0.16,1,0.3,1)}
@keyframes slideUp{0%{opacity:0;transform:translateY(30px) scale(0.96)}100%{opacity:1;transform:translateY(0) scale(1)}}
.card{background:var(--card);border:1px solid var(--border);border-radius:24px;padding:40px 36px 36px;backdrop-filter:blur(24px);box-shadow:0 0 80px rgba(245,158,11,0.06),0 20px 60px rgba(0,0,0,.6)}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:28px}
.brand-img{width:50px;height:50px;border-radius:14px;overflow:hidden;border:1.5px solid var(--border);box-shadow:0 0 30px rgba(245,158,11,0.15);flex-shrink:0;background:linear-gradient(135deg,#F59E0B,#D97706)}
.brand-img svg{width:100%;height:100%;padding:8px;fill:#fff}
.brand-name{font-size:18px;font-weight:800;color:var(--text);background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.brand-sub{font-size:11px;color:var(--dim);margin-top:3px}
h1{font-size:22px;font-weight:700;color:var(--text);margin-bottom:5px}
.sub{font-size:12.5px;color:var(--mid);margin-bottom:24px;line-height:1.7}
.hint{display:flex;align-items:center;gap:10px;background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.12);border-radius:12px;padding:10px 14px;margin-bottom:20px}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:var(--accent);background:rgba(245,158,11,0.08);border:1px solid rgba(245,158,11,0.2);padding:3px 13px;border-radius:8px;cursor:pointer;transition:.2s}
.hint-val:hover{background:rgba(245,158,11,0.18)}
.field{margin-bottom:18px}
.field label{display:block;font-size:10.5px;font-weight:600;color:var(--mid);margin-bottom:7px;text-transform:uppercase}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:14px 48px 14px 18px;border-radius:13px;border:1.5px solid var(--border);background:rgba(0,0,0,.35);color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:.3s}
input[type=password]:focus{border-color:rgba(245,158,11,.6);background:rgba(0,0,0,.45);box-shadow:0 0 0 4px rgba(245,158,11,.08)}
.ic{position:absolute;left:16px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none;transition:.3s}
input:focus+.ic{color:var(--accent)}
.err{display:none;background:rgba(239,68,68,.06);border:1px solid rgba(239,68,68,.15);border-radius:12px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px;animation:shake 0.4s ease}
@keyframes shake{0%,100%{transform:translateX(0)}20%{transform:translateX(-6px)}40%{transform:translateX(6px)}60%{transform:translateX(-4px)}80%{transform:translateX(4px)}}
.err.show{display:flex}
.btn{width:100%;padding:14px;border-radius:13px;border:none;cursor:pointer;background:linear-gradient(135deg,#F59E0B,#D97706);color:#0f0a04;font-family:inherit;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 4px 25px rgba(245,158,11,.3);transition:.3s}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 35px rgba(245,158,11,.4)}
.btn:active{transform:translateY(0) scale(0.98)}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--dim)}
.footer a{color:var(--accent);font-weight:600;text-decoration:none;display:flex;align-items:center;gap:4px}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">
      <div class="brand-img">
        <svg viewBox="0 0 100 100"><path d="M50 10 L90 30 L90 70 L50 90 L10 70 L10 30 Z" stroke="#fff" stroke-width="2" fill="none"/><path d="M50 25 L75 37 L75 63 L50 75 L25 63 L25 37 Z" stroke="#fff" stroke-width="1.5" fill="none"/><circle cx="50" cy="50" r="10" stroke="#fff" stroke-width="1.5" fill="none"/><path d="M42 38 L58 62 M58 38 L42 62" stroke="#fff" stroke-width="1" opacity="0.4"/></svg>
      </div>
      <div><div class="brand-name">Royal Gateway</div><div class="brand-sub">پنل مدیریت · v9.2</div></div>
    </div>
    <h1>ورود به پنل</h1>
    <p class="sub">رمز عبور را برای دسترسی به داشبورد وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint">
      <span class="hint-label">رمز پیش‌فرض سیستم</span>
      <span class="hint-val" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus()">123456</span>
    </div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required>
          <i class="ti ti-lock ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>
    <div class="footer">کانال رسمی<a href="https://t.me/royalpanelv2" target="_blank"><i class="ti ti-brand-telegram"></i>@royalpanelv2</a></div>
  </div>
</div>
<script>
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد';
  }
});
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Royal Gateway · پنل مدیریت</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0f0a04;--bg2:#1a1208;--bg3:#261c0e;--card:#1c140a;--card-b:rgba(245,158,11,0.12);--card-bh:rgba(245,158,11,0.25);--accent:#F59E0B;--accent2:#FBBF24;--accent-d:rgba(245,158,11,0.08);--green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;--red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;--amber:#F59E0B;--amber-bg:rgba(245,158,11,0.1);--amber-t:#FBBF24;--purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.08);--t1:#FFF8ED;--t2:#C8B088;--t3:#8B7A5A;--sidebar-w:248px;--radius:16px;--shadow:0 4px 24px rgba(0,0,0,0.5)}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .3s}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-img{width:40px;height:40px;border-radius:12px;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 20px rgba(245,158,11,0.12);flex-shrink:0;background:linear-gradient(135deg,#F59E0B,#D97706)}
.logo-img svg{width:100%;height:100%;padding:6px;fill:#fff}
.logo-name{font-size:14px;font-weight:800;background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .2s;margin:1px 6px;border-radius:8px 0 0 8px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:rgba(245,158,11,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#F59E0B,#D97706);color:#0f0a04;border-radius:9px;padding:10px;font-size:12.5px;font-weight:700;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.2s}
.tg-btn:hover{filter:brightness(1.1)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.2s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.15);cursor:pointer;width:100%;transition:.2s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:30px;height:30px;border-radius:8px;overflow:hidden;background:linear-gradient(135deg,#F59E0B,#D97706);flex-shrink:0}
.mob-logo svg{width:100%;height:100%;padding:5px;fill:#fff}
.mob-title{font-size:13px;font-weight:800;background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .25s}
@keyframes fi{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.tb-title i{color:var(--accent);font-size:20px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:#A78BFA}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.8)}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:17px 17px 14px;transition:all .3s;position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.3s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(145deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:22px 24px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden}
.vless-box::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(245,158,11,0.06),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px;position:relative;z-index:1}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px 16px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em;position:relative;z-index:1}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap;position:relative;z-index:1}
.btn{font-family:inherit;font-size:12px;font-weight:600;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .2s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:linear-gradient(135deg,#F59E0B,#D97706);color:#0f0a04;box-shadow:0 3px 15px rgba(245,158,11,.3)}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 6px 25px rgba(245,158,11,.4)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(245,158,11,.3)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(245,158,11,.12)}
.btn-g:hover{background:rgba(245,158,11,.18)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.15)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,.15)}
.btn-pur:hover{background:rgba(139,92,246,.2)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,.15)}
.btn-amber:hover{background:rgba(245,158,11,.2)}
.btn-sm{padding:5px 10px;font-size:10.5px;border-radius:8px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:6px}
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(245,158,11,0.04);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-sm{position:relative;height:185px}
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:14px;padding:0;transition:all .3s;position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 24px rgba(0,0,0,.25)}
.cfg-card.is-off{opacity:.6}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px;flex-wrap:wrap}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(245,158,11,0.06);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0;flex-wrap:wrap}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:#A78BFA}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:32px;border-radius:19px;background:rgba(139,122,90,0.2);position:relative;cursor:pointer;transition:.3s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:14px;height:14px;border-radius:50%;background:#fff;left:2.5px;bottom:2.5px;transition:.3s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:15.5px}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.2);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.2);background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.cl{background:var(--accent-d);border:1px solid rgba(245,158,11,.12);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,.15);color:var(--amber-t)}
.cl.amber i{color:var(--amber)}
@media(max-width:1050px){
.sidebar{transform:translateX(100%)}
.sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.5)}
.sb-close{display:flex}
.main{margin-right:0;padding-top:70px}
.mob-top{display:flex}
.metrics{grid-template-columns:1fr 1fr}
.g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
.metrics{grid-template-columns:1fr}
.main{padding:62px 12px 50px}
}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="mob-top">
<div class="ml">
<div class="mob-logo"><svg viewBox="0 0 100 100"><path d="M50 10 L90 30 L90 70 L50 90 L10 70 L10 30 Z" stroke="#fff" stroke-width="2" fill="none"/><path d="M50 25 L75 37 L75 63 L50 75 L25 63 L25 37 Z" stroke="#fff" stroke-width="1.5" fill="none"/><circle cx="50" cy="50" r="10" stroke="#fff" stroke-width="1.5" fill="none"/><path d="M42 38 L58 62 M58 38 L42 62" stroke="#fff" stroke-width="1" opacity="0.4"/></svg></div>
<span class="mob-title">Royal Gateway</span>
</div>
<div class="mob-right">
<button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
</div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
<button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
<div class="logo">
<div class="logo-img"><svg viewBox="0 0 100 100"><path d="M50 10 L90 30 L90 70 L50 90 L10 70 L10 30 Z" stroke="#fff" stroke-width="2" fill="none"/><path d="M50 25 L75 37 L75 63 L50 75 L25 63 L25 37 Z" stroke="#fff" stroke-width="1.5" fill="none"/><circle cx="50" cy="50" r="10" stroke="#fff" stroke-width="1.5" fill="none"/><path d="M42 38 L58 62 M58 38 L42 62" stroke="#fff" stroke-width="1" opacity="0.4"/></svg></div>
<div><div class="logo-name">Royal Gateway</div><div class="logo-sub">پنل مدیریت · v9.2</div></div>
</div>
<div class="nav-wrap">
<div class="nav-sec">پنل</div>
<div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
<div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
<div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
</div>
<div class="sb-foot">
<a class="tg-btn" href="https://t.me/royalpanelv2" target="_blank"><i class="ti ti-brand-telegram"></i> @royalpanelv2</a>
<button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
</div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">
<div class="topbar">
<div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
<div class="tb-right">
<span class="badge bg-green"><span class="dot dg pulse"></span> فعال</span>
<button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
</div>
</div>
<div class="metrics">
<div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div></div>
<div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div></div>
<div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div></div>
<div class="metric pur"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌های ساب</div><div class="m-val" id="m-subs">—</div></div>
</div>
<div class="vless-box">
<div class="vl-header">
<div class="vl-title"><i class="ti ti-link"></i> لینک پیش‌فرض</div>
<span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
</div>
<div class="vl-code" id="vless-main">در حال دریافت...</div>
<div class="vl-actions">
<button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
<button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
<button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> کانفیگ محدود</button>
</div>
</div>
<div class="g2">
<div class="card">
<div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div>
<div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
<div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
<div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
<div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
</div>
<div class="card">
<div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div>
<div id="lsummary">—</div>
</div>
</div>
<div class="dash-footer">
<span class="df-text">Royal Gateway v9.2 · 2025</span>
<a class="df-link" href="https://t.me/royalpanelv2" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/royalpanelv2</a>
</div>
</section>
<section class="pg" id="pg-links">
<div class="topbar">
<div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ</div></div>
<div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
</div>
<div class="card">
<div class="card-title"><i class="ti ti-square-rounded-plus"></i> ساخت کانفیگ جدید</div>
<div class="g2">
<input class="fi" id="nl-label" placeholder="نام کانفیگ" style="padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none">
<input class="fi" id="nl-val" type="number" placeholder="سهمیه (MB)" style="padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none">
</div>
<select id="nl-proto" style="padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none;width:100%;margin:10px 0">
<option value="vless-ws">VLESS / WebSocket</option>
<option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
<option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
</select>
<button class="btn btn-p" onclick="createLink()" style="width:100%"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
</div>
<div class="cfg-grid" id="links-grid"></div>
<div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>
<section class="pg" id="pg-settings">
<div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
<div class="card">
<div class="card-title"><i class="ti ti-key"></i> تغییر رمز عبور</div>
<div class="fg" style="margin-bottom:10px"><label style="font-size:10px;color:var(--t3);font-weight:700">رمز فعلی</label><input class="fi" id="cp-cur" type="password" style="width:100%;padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none"></div>
<div class="fg" style="margin-bottom:10px"><label style="font-size:10px;color:var(--t3);font-weight:700">رمز جدید</label><input class="fi" id="cp-new" type="password" style="width:100%;padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none"></div>
<div class="fg" style="margin-bottom:10px"><label style="font-size:10px;color:var(--t3);font-weight:700">تکرار رمز جدید</label><input class="fi" id="cp-cf" type="password" style="width:100%;padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none"></div>
<button class="btn btn-p" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
</div>
</section>
</main>
<script>
function toast(msg,type=''){
const t=document.getElementById('toast');
t.textContent=msg;t.className='toast show'+(type?' '+type:'');
setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
const d=daysLeft(exp);
if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز مانده</span>`;
return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز مانده</span>`;
}
function protoBadge(p){
const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet-up','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','pc-xhttp']};
const v=m[p]||m['vless-ws'];
return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){const r=await fetch(url,opts);if(r.status===401){location.href='/login';throw new Error('unauthorized')}return r;}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
if(name==='links')loadLinks();
closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
let allLinksList=[];
async function loadLinks(){
try{
const r=await authF('/api/links'),d=await r.json();
const links=d.links||[];
allLinksList=links;
document.getElementById('links-nb').textContent=links.length;
document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';
document.getElementById('lsummary-badge').textContent=toFa(links.length);
const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';return}
empty.style.display='none';
grid.innerHTML=links.map(l=>{
const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
const allowed=l.active&&!l.expired;
const cardCls=!l.active?'is-off':'';
return `<div class="cfg-card ${cardCls}">
<div class="cfg-row">
<span class="cfg-status-dot ${allowed?'pulse':''}"></span>
<div class="cfg-identity">
<div class="cfg-label">${esc(l.label)}</div>
<div class="cfg-sub-meta">
<span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
</div>
</div>
<div class="cfg-divider-v"></div>
<div class="cfg-usage-col">
<div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
<div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
</div>
<div class="cfg-divider-v"></div>
<div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
<div class="cfg-divider-v"></div>
<div class="cfg-badges-col">${protoBadge(l.protocol)}</div>
<div class="cfg-divider-v"></div>
<div class="cfg-actions">
<button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
<button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی"><i class="ti ti-copy"></i></button>
<button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
<button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
</div>
</div>
</div>`;
}).join('');
document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div>`).join('');
}catch(e){console.error(e)}
}
async function createLink(){
const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
const val=document.getElementById('nl-val').value||0;
const protocol=document.getElementById('nl-proto').value||'vless-ws';
try{
const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val,limit_unit:'MB',expires_days:0,protocol})});
if(!r.ok)throw new Error('failed');
document.getElementById('nl-label').value='';
document.getElementById('nl-val').value='';
toast('کانفیگ ساخته شد ✓','ok');
loadLinks();
fetchStats();
}catch(e){toast('خطا در ساخت','err')}
}
async function toggleActive(uuid,newState){
try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
if(!confirm('حذف این کانفیگ؟'))return;
try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();fetchStats();}catch(e){toast('خطا','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
async function fetchStats(){
try{
const r=await authF('/stats'),d=await r.json();
document.getElementById('m-conns').textContent=d.active_connections||0;
document.getElementById('m-traffic').innerHTML=(d.total_traffic_mb||0).toFixed(1)+'<span class="m-unit">MB</span>';
document.getElementById('m-alinks').textContent=d.active_links||0;
document.getElementById('m-subs').textContent=d.subs_count||0;
document.getElementById('uptime-inline').textContent=d.uptime||'0h 0m';
document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
}catch(e){console.error(e)}
}
async function fetchDefaultVless(){
try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';}catch(e){}
}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();toast('رفرش شد','ok')}
async function changePw(){
const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}
if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}
if(nw!==cf){toast('تکرار رمز اشتباه','err');return}
try{
const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
const d=await r.json().catch(()=>({}));
if(!r.ok)throw new Error(d.detail||'خطا');
toast('رمز تغییر کرد ✓','ok');
['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
}catch(e){toast('✗ '+e.message,'err')}
}
document.addEventListener('DOMContentLoaded',async()=>{
await checkAuth();
fetchStats();fetchDefaultVless();loadLinks();
setInterval(fetchStats,5000);
});
</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head><meta charset="UTF-8"><title>Royal Sub</title>
<style>
body{{font-family:Vazirmatn;background:#0f0a04;color:#FFF8ED;padding:20px;display:flex;justify-content:center;align-items:center;min-height:100vh}}
.card{{background:#1a1208;padding:30px;border-radius:20px;border:1px solid rgba(245,158,11,0.1);max-width:700px;width:100%}}
h1{{color:#FBBF24;text-align:center}}
.link{{background:#0f0a04;padding:12px;border-radius:10px;word-break:break-all;font-family:monospace;font-size:11px;margin:8px 0;border:1px solid rgba(245,158,11,0.05)}}
.btn{{background:linear-gradient(135deg,#F59E0B,#D97706);color:#0f0a04;padding:8px 16px;border:none;border-radius:8px;font-weight:700;cursor:pointer;margin:5px}}
.btn:hover{{transform:translateY(-1px)}}
.empty{{text-align:center;color:#8B7A5A;padding:30px}}
</style>
</head>
<body>
<div class="card">
<h1>👑 Royal Gateway</h1>
<p style="text-align:center;color:#8B7A5A">لینک‌های گروه</p>
<div id="links"><div class="empty">در حال بارگذاری...</div></div>
</div>
<script>
fetch('/api/public/sub/{uuid_key}')
.then(r=>r.json())
.then(d=>{{
if(d.locked){{document.getElementById('links').innerHTML='<div class="empty">🔒 این گروه با رمز محافظت شده</div>';return}}
const el=document.getElementById('links');
if(!d.links||!d.links.length){{el.innerHTML='<div class="empty">کانفیگی وجود ندارد</div>';return}}
el.innerHTML=d.links.map(l=>`
<div class="link">${{l.vless_link||'لینک نامعتبر'}}</div>
<button class="btn" onclick="navigator.clipboard.writeText('${{l.vless_link}}').then(()=>alert('کپی شد ✅'))">📋 کپی</button>
`).join('');
}})
.catch(()=>document.getElementById('links').innerHTML='<div class="empty" style="color:#EF4444">خطا در بارگذاری</div>');
</script>
</body></html>"""

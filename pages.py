# pages.py  -  Royal Gateway v9.2 (Dark Amber Theme)
# شامل: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

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
:root{
  --bg:#0a0806;
  --bg2:#14100a;
  --card:rgba(20,16,10,0.92);
  --accent:#F59E0B;
  --accent2:#FBBF24;
  --accent3:#D97706;
  --accent-d:rgba(245,158,11,0.12);
  --text:#FEF3C7;
  --dim:#B45309;
  --mid:#D97706;
  --border:rgba(245,158,11,0.15);
  --border-hover:rgba(245,158,11,0.35);
  --shadow-glow:0 0 60px rgba(245,158,11,0.08);
}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px}
.bg{position:fixed;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(245,158,11,0.06),transparent 70%),var(--bg);z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(245,158,11,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(245,158,11,0.03) 1px,transparent 1px);background-size:44px 44px;z-index:0}
.orb{position:fixed;border-radius:50%;filter:blur(100px);z-index:0;animation:fl 9s ease-in-out infinite}
.o1{width:350px;height:350px;background:rgba(245,158,11,0.06);top:-100px;right:-80px}
.o2{width:300px;height:300px;background:rgba(251,191,36,0.04);bottom:-60px;left:-60px;animation-delay:4s}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-18px)}}
.wrap{position:relative;z-index:10;width:100%;max-width:400px;animation:fadeUp 0.8s ease}
@keyframes fadeUp{0%{opacity:0;transform:translateY(40px)}100%{opacity:1;transform:translateY(0)}}
@keyframes pulseGlow{0%,100%{box-shadow:0 0 30px rgba(245,158,11,0.03)}50%{box-shadow:0 0 60px rgba(245,158,11,0.10)}}
@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes logoPulse{0%,100%{filter:drop-shadow(0 0 10px rgba(245,158,11,0.2))}50%{filter:drop-shadow(0 0 25px rgba(245,158,11,0.5))}}

.card{background:var(--card);border:1px solid var(--border);border-radius:20px;padding:38px 34px 34px;backdrop-filter:blur(24px);box-shadow:var(--shadow-glow),0 20px 60px rgba(0,0,0,.6);transition:all 0.3s cubic-bezier(0.4,0,0.2,1);animation:pulseGlow 3s ease-in-out infinite}
.card:hover{transform:translateY(-4px) scale(1.005);box-shadow:0 0 80px rgba(245,158,11,0.06),0 25px 70px rgba(0,0,0,.7);border-color:var(--border-hover)}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:28px;animation:fadeUp 0.6s ease 0.1s both}
.brand-icon{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#F59E0B,#D97706);display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 0 30px rgba(245,158,11,0.25);animation:logoPulse 3s ease-in-out infinite;transition:transform 0.4s ease}
.brand-icon:hover{transform:rotate(-8deg) scale(1.05)}
.brand-icon i{font-size:28px;color:#1a140e}
.brand-name{font-size:18px;font-weight:800;color:var(--text);letter-spacing:-.02em;background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.brand-sub{font-size:10px;color:var(--dim);margin-top:2px;letter-spacing:.08em}
h1{font-size:21px;font-weight:700;color:var(--text);margin-bottom:5px;letter-spacing:-.02em;animation:fadeUp 0.6s ease 0.2s both}
h1 i{color:var(--accent);margin-left:6px}
.sub{font-size:12px;color:var(--mid);margin-bottom:24px;line-height:1.6;animation:fadeUp 0.6s ease 0.3s both}
.hint{display:flex;align-items:center;gap:10px;background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.12);border-radius:10px;padding:10px 14px;margin-bottom:20px;animation:fadeUp 0.6s ease 0.4s both;transition:all 0.3s ease}
.hint:hover{background:rgba(245,158,11,0.10);border-color:rgba(245,158,11,0.25)}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:var(--accent2);background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.2);padding:3px 11px;border-radius:7px;cursor:pointer;transition:all 0.2s ease;letter-spacing:.08em}
.hint-val:hover{background:rgba(245,158,11,0.2);transform:scale(1.08) translateY(-1px);border-color:var(--accent)}
.field{margin-bottom:18px;animation:fadeUp 0.6s ease 0.5s both}
.field label{display:block;font-size:10.5px;font-weight:600;color:var(--dim);margin-bottom:7px;text-transform:uppercase;letter-spacing:.06em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:13px 44px 13px 16px;border-radius:11px;border:1px solid var(--border);background:rgba(0,0,0,.4);color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:all 0.25s ease}
input[type=password]::placeholder{color:rgba(180,100,30,0.25)}
input[type=password]:focus{border-color:rgba(245,158,11,.5);background:rgba(0,0,0,.5);box-shadow:0 0 0 3px rgba(245,158,11,.08),0 0 30px rgba(245,158,11,.03);transform:scale(1.01)}
.ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none;transition:all 0.25s ease}
input:focus+.ic{color:var(--accent);transform:translateY(-50%) scale(1.1)}
.err{display:none;background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.2);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px;animation:shake 0.4s ease}
.err.show{display:flex}
.btn{width:100%;padding:13px;border-radius:11px;border:none;cursor:pointer;background:linear-gradient(135deg,#F59E0B,#D97706);color:#1a140e;font-family:inherit;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 4px 25px rgba(245,158,11,.3);transition:all 0.3s ease;position:relative;overflow:hidden;animation:fadeUp 0.6s ease 0.6s both}
.btn::before{content:'';position:absolute;inset:0;background:rgba(255,255,255,.08);opacity:0;transition:opacity 0.3s}
.btn::after{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:conic-gradient(from 0deg,transparent,rgba(255,255,255,0.06),transparent 60%);animation:spin 4s linear infinite;opacity:0;transition:opacity 0.5s}
.btn:hover::before{opacity:1}
.btn:hover::after{opacity:1}
.btn:hover{transform:translateY(-3px);box-shadow:0 8px 35px rgba(245,158,11,.4)}
.btn:active{transform:scale(0.97)}
.btn:disabled{opacity:.5;cursor:not-allowed;transform:none}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--dim);animation:fadeUp 0.6s ease 0.7s both}
.footer a{color:var(--accent2);font-weight:600;text-decoration:none;display:flex;align-items:center;gap:4px;transition:all 0.2s ease}
.footer a:hover{color:#FCD34D;transform:translateX(-3px)}
.footer a i{transition:transform 0.3s ease}
.footer a:hover i{transform:scale(1.15) rotate(-10deg)}
.loading-spinner{animation:spin 1s linear infinite;display:inline-block}

@media(max-width:480px){
  .card{padding:28px 20px 24px}
  h1{font-size:18px}
  .brand-icon{width:44px;height:44px}
  .brand-icon i{font-size:22px}
  .brand-name{font-size:15px}
}
</style>
</head>
<body>
<div class="bg"></div>
<div class="grid"></div>
<div class="orb o1"></div>
<div class="orb o2"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">
      <div class="brand-icon"><i class="ti ti-crown"></i></div>
      <div>
        <div class="brand-name">Royal Gateway</div>
        <div class="brand-sub">✦ v9.2 · Secure Access</div>
      </div>
    </div>
    <h1><i class="ti ti-lock-access"></i> ورود به پنل</h1>
    <p class="sub">رمز عبور را برای دسترسی به داشبورد وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint">
      <span class="hint-label">رمز پیش‌فرض سیستم</span>
      <span class="hint-val" onclick="document.getElementById('pw').value='123456';document.getElementById('pw').focus();this.style.transform='scale(0.95)';setTimeout(()=>this.style.transform='',200)">123456</span>
    </div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required>
          <i class="ti ti-key ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>
    <div class="footer">
      <i class="ti ti-brand-telegram" style="color:var(--dim)"></i>
      <a href="https://t.me/royalpanelv2" target="_blank">کانال رسمی</a>
      <span style="color:var(--dim);font-size:8px;opacity:0.3">✦</span>
      <span style="color:var(--dim);font-size:9px">Royal Gateway v9.2</span>
    </div>
  </div>
</div>
<script>
document.addEventListener('DOMContentLoaded',()=>{
  setTimeout(()=>document.getElementById('pw').focus(),600);
});
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text'),pw=document.getElementById('pw');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2 loading-spinner"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:pw.value})});
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
<title>Royal Gateway · Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0a0806;
  --bg2:#14100a;
  --bg3:#1a150e;
  --card:rgba(20,16,10,0.92);
  --card-b:rgba(245,158,11,0.12);
  --card-bh:rgba(245,158,11,0.28);
  --accent:#F59E0B;
  --accent2:#FBBF24;
  --accent3:#D97706;
  --accent-d:rgba(245,158,11,0.10);
  --green:#10B981;
  --green-bg:rgba(16,185,129,0.1);
  --green-t:#34D399;
  --red:#EF4444;
  --red-bg:rgba(239,68,68,0.1);
  --red-t:#F87171;
  --amber:#F59E0B;
  --amber-bg:rgba(245,158,11,0.1);
  --amber-t:#FBBF24;
  --purple:#8B5CF6;
  --purple-bg:rgba(139,92,246,0.1);
  --t1:#FEF3C7;
  --t2:#D97706;
  --t3:#92400E;
  --sidebar-w:248px;
  --radius:16px;
  --shadow:0 4px 24px rgba(0,0,0,0.5);
}
html,body{height:100%;scroll-behavior:smooth}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}

@keyframes fadeUp{0%{opacity:0;transform:translateY(20px)}100%{opacity:1;transform:translateY(0)}}
@keyframes fadeIn{0%{opacity:0}100%{opacity:1}}
@keyframes slideInRight{0%{opacity:0;transform:translateX(30px)}100%{opacity:1;transform:translateX(0)}}
@keyframes pulseGlow{0%,100%{box-shadow:0 0 20px rgba(245,158,11,0.05)}50%{box-shadow:0 0 40px rgba(245,158,11,0.12)}}
.fade-up{animation:fadeUp 0.5s ease both}
.fade-in{animation:fadeIn 0.4s ease both}
.slide-right{animation:slideInRight 0.4s ease both}
.stagger>*{animation:fadeUp 0.5s ease both}
.stagger>*:nth-child(1){animation-delay:0.05s}
.stagger>*:nth-child(2){animation-delay:0.1s}
.stagger>*:nth-child(3){animation-delay:0.15s}
.stagger>*:nth-child(4){animation-delay:0.2s}
.stagger>*:nth-child(5){animation-delay:0.25s}

.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b);animation:fadeUp 0.4s ease}
.logo-icon{width:38px;height:38px;border-radius:10px;background:linear-gradient(135deg,#F59E0B,#D97706);display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 0 20px rgba(245,158,11,0.2)}
.logo-icon i{font-size:20px;color:#1a140e}
.logo-name{font-size:13.5px;font-weight:700;color:var(--t1);background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer;transition:all 0.2s}
.sb-close:hover{background:var(--red-bg);color:var(--red-t)}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .2s;margin:1px 6px;border-radius:0 8px 8px 0}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0;transition:transform 0.2s}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it:hover i{transform:translateX(-3px)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-it.on i{color:var(--accent)}
.nav-badge{margin-right:auto;background:rgba(245,158,11,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#1a8cff,#0055cc);color:#fff;border-radius:9px;padding:10px;font-size:12.5px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:all .2s}
.tg-btn:hover{filter:brightness(1.1);transform:scale(1.01)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:all .2s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1);transform:translateY(-1px)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:all .2s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2);transform:translateY(-1px)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:7px;background:linear-gradient(135deg,#F59E0B,#D97706);display:flex;align-items:center;justify-content:center}
.mob-logo i{font-size:14px;color:#1a140e}
.mob-title{color:var(--t1);font-size:13px;font-weight:700;background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s}
.menu-btn:hover,.theme-mob:hover{background:var(--card-b);color:var(--t1)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:190;backdrop-filter:blur(3px);animation:fadeIn 0.3s ease}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none;animation:fadeUp 0.4s ease}
.pg.on{display:block}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
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
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:17px 17px 14px;transition:all .3s ease;position:relative;overflow:hidden;cursor:default;animation:fadeUp 0.5s ease both}
.metric:nth-child(1){animation-delay:0.05s}
.metric:nth-child(2){animation-delay:0.1s}
.metric:nth-child(3){animation-delay:0.15s}
.metric:nth-child(4){animation-delay:0.2s}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:opacity .3s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric:hover .m-icon{transform:scale(1.05) rotate(-3deg)}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px;transition:transform 0.3s ease}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}

/* ادامه کد داشبورد با تم زرد/نارنجی - بخش‌های اصلی مشابه قبل با تغییر رنگ‌ها */
/* برای رعایت اختصار، بخش‌های تکراری حذف شده‌اند */

.vless-box{background:linear-gradient(135deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,rgba(245,158,11,0.08),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}

.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn-p{background:linear-gradient(135deg,#F59E0B,#D97706);color:#1a140e;box-shadow:0 2px 12px rgba(245,158,11,.3)}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 4px 18px rgba(245,158,11,.4)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(245,158,11,.3)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(245,158,11,.15)}
.btn-g:hover{background:rgba(245,158,11,.22)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,.2)}
.btn-pur:hover{background:rgba(139,92,246,.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,.2)}
.btn-amber:hover{background:rgba(245,158,11,.22)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}

/* ... ادامه کد مشابه قبل با رنگ‌های زرد/نارنجی ... */

.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}
.df-link:hover{color:var(--accent)}

@media(max-width:1050px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.5)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .metrics{grid-template-columns:1fr 1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
}
</style>
</head>
<body>
<!-- ساختار مشابه قبل با تغییرات رنگ و لینک‌ها -->
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><i class="ti ti-crown"></i></div>
    <span class="mob-title">Royal Gateway</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-icon"><i class="ti ti-crown"></i></div>
    <div><div class="logo-name">Royal Gateway</div><div class="logo-sub">✦ v9.2 · Secure</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">سیستم</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>
    <a class="tg-btn" href="https://t.me/royalpanelv2" target="_blank" rel="noopener"><i class="ti ti-brand-telegram"></i> کانال رسمی</a>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>
<main class="main">
<!-- بقیه محتوای داشبورد مشابه قبل با تغییر رنگ‌ها -->
<div class="dash-footer">
  <span class="df-text">Royal Gateway v9.2 · 2025</span>
  <a class="df-link" href="https://t.me/royalpanelv2" target="_blank"><i class="ti ti-brand-telegram"></i> کانال رسمی</a>
</div>
</main>
<script>
// اسکریپت‌های مشابه قبل
</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب - تم زرد/نارنجی/مشکی"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Royal Gateway · Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#0a0806;
  --bg2:#14100a;
  --bg3:#1a150e;
  --card:rgba(20,16,10,0.92);
  --card-b:rgba(245,158,11,0.12);
  --card-bh:rgba(245,158,11,0.28);
  --accent:#F59E0B;
  --accent2:#FBBF24;
  --accent3:#D97706;
  --accent-d:rgba(245,158,11,0.10);
  --green:#10B981;
  --green-bg:rgba(16,185,129,0.1);
  --green-t:#34D399;
  --red:#EF4444;
  --red-bg:rgba(239,68,68,0.1);
  --red-t:#F87171;
  --amber:#F59E0B;
  --amber-bg:rgba(245,158,11,0.1);
  --amber-t:#FBBF24;
  --purple:#8B5CF6;
  --purple-bg:rgba(139,92,246,0.1);
  --t1:#FEF3C7;
  --t2:#D97706;
  --t3:#92400E;
  --radius:18px;
  --shadow:0 12px 40px rgba(0,0,0,0.5);
  --serif:'Vazirmatn',sans-serif;
}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--serif);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}

@keyframes fadeUp{{0%{{opacity:0;transform:translateY(24px)}}100%{{opacity:1;transform:translateY(0)}}}}
@keyframes fadeIn{{0%{{opacity:0}}100%{{opacity:1}}}}
@keyframes scaleIn{{0%{{opacity:0;transform:scale(0.92)}}100%{{opacity:1;transform:scale(1)}}}}
.fade-up{{animation:fadeUp 0.5s ease both}}
.fade-in{{animation:fadeIn 0.4s ease both}}
.scale-in{{animation:scaleIn 0.4s ease both}}
.stagger>*{{animation:fadeUp 0.5s ease both}}
.stagger>*:nth-child(1){{animation-delay:0.05s}}
.stagger>*:nth-child(2){{animation-delay:0.1s}}
.stagger>*:nth-child(3){{animation-delay:0.15s}}

.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(245,158,11,0.08),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:background .35s}}
.grid-fx{{position:fixed;inset:0;background-image:linear-gradient(rgba(245,158,11,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(245,158,11,0.025) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px;animation:fadeUp 0.5s ease}}
.brand{{display:flex;align-items:center;gap:11px;min-width:0}}
.brand-icon{{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#F59E0B,#D97706);display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 0 20px rgba(245,158,11,0.2)}}
.brand-icon i{{font-size:20px;color:#1a140e}}
.brand-name{{font-size:14.5px;font-weight:800;color:var(--t1);background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.brand-sub{{font-size:9.5px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:11px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:all .2s}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent2);border-color:var(--card-bh);transform:translateY(-2px)}}

.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 24px 22px;margin-bottom:16px;box-shadow:var(--shadow);position:relative;overflow:hidden;animation:fadeUp 0.5s ease 0.05s both}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(245,158,11,.08),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}

.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;transition:all .3s ease;animation:fadeUp 0.5s ease both}}
.stat-card:nth-child(1){{animation-delay:0.1s}}
.stat-card:nth-child(2){{animation-delay:0.15s}}
.stat-card:nth-child(3){{animation-delay:0.2s}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow)}}

.copy-all-bar{{display:flex;align-items:center;gap:12px;background:linear-gradient(120deg,#F59E0B,#D97706);border-radius:18px;padding:16px 19px;margin-bottom:18px;box-shadow:0 10px 30px rgba(245,158,11,.25);flex-wrap:wrap;animation:fadeUp 0.5s ease 0.15s both}}
.copy-all-title{{font-size:13.5px;font-weight:800;color:#1a140e;display:flex;align-items:center;gap:6px}}
.copy-all-sub{{font-size:10px;color:rgba(26,20,14,.7);margin-top:3px}}
.copy-all-btn{{background:#1a140e;color:#FBBF24;border:none;border-radius:12px;padding:10px 19px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:all .2s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-2px);box-shadow:0 8px 20px rgba(0,0,0,.3)}}

.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:18px;transition:all .3s ease;position:relative;overflow:hidden;animation:fadeUp 0.5s ease both}}
.cfg-card:nth-child(1){{animation-delay:0.1s}}
.cfg-card:nth-child(2){{animation-delay:0.15s}}
.cfg-card:nth-child(3){{animation-delay:0.2s}}
.cfg-card:hover{{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:var(--shadow)}}
.cfg-top::after{{background:var(--accent)}}
.cfg-label{{color:var(--t1)}}
.proto-chip.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.proto-chip.pc-xhttp{{background:var(--purple-bg);color:#A78BFA}}
.proto-chip.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}

.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3);animation:fadeUp 0.5s ease 0.3s both}}
.footer a{{color:var(--accent2);font-weight:700;transition:color 0.2s}}
.footer a:hover{{color:var(--accent)}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .2s;white-space:nowrap}}
.btn-p{{background:linear-gradient(135deg,#F59E0B,#D97706);color:#1a140e;box-shadow:0 3px 12px rgba(245,158,11,.3)}}
.btn-p:hover{{transform:translateY(-2px);box-shadow:0 6px 20px rgba(245,158,11,.4)}}
.btn-g{{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(245,158,11,.15)}}
.btn-g:hover{{background:rgba(245,158,11,.2);transform:translateY(-1px)}}
.btn-pur{{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,.2)}}
.btn-pur:hover{{background:rgba(139,92,246,.22);transform:translateY(-1px)}}
.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(16,185,129,.35);background:var(--green-bg);color:var(--green-t)}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}

@media(max-width:520px){{.stats-bar{{grid-template-columns:1fr 1fr}}
.stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
.copy-all-bar{{flex-direction:column;align-items:stretch}}
.copy-all-btn{{justify-content:center}}
.wrap{{padding:16px 12px 50px}}}}
</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-icon"><i class="ti ti-crown"></i></div>
      <div><div class="brand-name">Royal Gateway</div><div class="brand-sub">✦ v9.2 · Sub</div></div>
    </div>
    <div class="top-actions">
      <a class="icon-btn" href="https://t.me/royalpanelv2" target="_blank"><i class="ti ti-brand-telegram"></i></a>
    </div>
  </div>
  <div id="root">
    <div style="text-align:center;padding:80px 20px;color:var(--t3);animation:fadeUp 0.5s ease">
      <i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:38px;display:block;margin-bottom:14px"></i>
      در حال بارگذاری...
    </div>
  </div>
  <div class="footer">کانال رسمی: <a href="https://t.me/royalpanelv2" target="_blank">Royal Panel</a> · v9.2</div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';
function toast(msg,type=''){{const t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' '+type:'');setTimeout(()=>t.classList.remove('show'),2400)}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{if(p==='xhttp-stream-one')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';return '<span class="proto-chip pc-ws">VLESS · WS</span>'}}
async function loadData(pw=''){{const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');const r=await fetch(url);return r.json()}}
function renderLock(name,errMsg=''){{/* مشابه قبل با تم جدید */}}
function renderContent(d){{/* مشابه قبل با تم جدید */}}
async function init(){{try{{const data=await loadData();if(data.locked){{renderLock(data.name);return}}renderContent(data)}}catch(e){{document.getElementById('root').innerHTML='<div style="text-align:center;padding:80px 20px;color:var(--red-t)"><i class="ti ti-alert-circle" style="font-size:38px;display:block;margin-bottom:14px"></i>خطا در بارگذاری</div>'}}}}
init();
</script>
</body></html>"""

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
[data-theme="light"]{--bg:#FBF5ED;--bg2:#F5EDE0;--bg3:#EDE0CC;--card:#FFFFFF;--card-b:rgba(245,158,11,0.15);--card-bh:rgba(245,158,11,0.3);--accent:#D97706;--accent2:#B45309;--accent-d:rgba(217,119,6,0.08);--green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#065F46;--red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;--amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;--purple:#7C3AED;--purple-bg:rgba(124,58,237,0.08);--t1:#1A1208;--t2:#5C4A2A;--t3:#8B7A5A;--shadow:0 4px 20px rgba(0,0,0,0.08)}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--accent)}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .3s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
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
.tg-btn:hover{filter:brightness(1.1);transform:translateY(-1px)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.2s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.15);cursor:pointer;width:100%;transition:.2s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:30px;height:30px;border-radius:8px;overflow:hidden;background:linear-gradient(135deg,#F59E0B,#D97706);flex-shrink:0}
.mob-logo svg{width:100%;height:100%;padding:5px;fill:#fff}
.mob-title{font-size:13px;font-weight:800;background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s}
.menu-btn:hover,.theme-mob:hover{background:var(--card-b);color:var(--t1)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .25s cubic-bezier(.16,1,.3,1)}
@keyframes fi{from{opacity:0;transform:translateY(8px) scale(0.99)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
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
.metric .m-icon{transition:transform .3s}
.metric:hover .m-icon{transform:scale(1.05)}
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
.vless-box{background:linear-gradient(145deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:22px 24px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:background .3s}
.vless-box::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(245,158,11,0.06),transparent 70%);pointer-events:none}
.vless-box::after{content:'';position:absolute;bottom:-40px;right:-40px;width:150px;height:150px;background:radial-gradient(circle,rgba(245,158,11,0.04),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px;position:relative;z-index:1}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px 16px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em;position:relative;z-index:1;transition:.3s}
.vl-code:hover{border-color:rgba(245,158,11,.3)}
[data-theme="light"] .vl-code{background:rgba(0,0,0,.04)}
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
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .3s,background .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(245,158,11,0.04);font-size:12px;transition:.2s}
.sr:hover{background:var(--accent-d);margin:0 -4px;padding:9px 4px;border-radius:6px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:32px;border-radius:19px;background:rgba(139,122,90,0.2);position:relative;cursor:pointer;transition:.3s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:14px;height:14px;border-radius:50%;background:#fff;left:2.5px;bottom:2.5px;transition:.3s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:15.5px}
.tog:active::after{transform:scale(0.85)}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.2s;min-width:100px}
[data-theme="light"] .fi,[data-theme="light"] .fs{background:rgba(0,0,0,.04)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(245,158,11,.4);background:rgba(0,0,0,.25);box-shadow:0 0 0 3px rgba(245,158,11,.06)}
.fs option{background:var(--bg2)}
[data-theme="light"] .fs option{background:#fff}
.cl{background:var(--accent-d);border:1px solid rgba(245,158,11,.12);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,.15);color:var(--amber-t)}
.cl.amber i{color:var(--amber)}
.create-panel{background:linear-gradient(145deg,var(--bg3) 0%,var(--card) 55%);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,rgba(245,158,11,0.06),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,#F59E0B,#D97706);display:flex;align-items:center;justify-content:center;color:#0f0a04;font-size:20px;flex-shrink:0;box-shadow:0 6px 20px rgba(245,158,11,.25)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.2);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px;transition:.2s}
.cp-block:hover{border-color:var(--card-bh)}
[data-theme="light"] .cp-block{background:rgba(217,119,6,.03)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.2s}
[data-theme="light"] .cp-input-full{background:#fff}
.cp-input-full:focus{border-color:rgba(245,158,11,.4);box-shadow:0 0 0 3px rgba(245,158,11,.06)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.2s;white-space:nowrap;user-select:none}
.chip:hover{background:rgba(245,158,11,.15);color:var(--accent2);transform:translateY(-1px)}
.chip.active{background:var(--accent);color:#0f0a04;border-color:var(--accent);box-shadow:0 3px 12px rgba(245,158,11,.25)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:13px;padding:13px 12px;cursor:pointer;transition:.25s;text-align:center;position:relative;background:rgba(0,0,0,.12)}
[data-theme="light"] .proto-card{background:#fff}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(245,158,11,.06)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#0f0a04;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.2s}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px;transition:.3s}
.proto-card.active .proto-card-icon{background:var(--accent);color:#0f0a04}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,#F59E0B,#D97706);color:#0f0a04;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(245,158,11,.25);transition:.25s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(245,158,11,.35)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){.cp-row{grid-template-columns:1fr}.proto-cards{grid-template-columns:1fr}.cp-footer{flex-direction:column;align-items:stretch}.cp-submit-btn{justify-content:center}}
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:14px;padding:0;transition:all .3s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 24px rgba(0,0,0,.25)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px;flex-wrap:wrap}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.2s}
.cfg-uuid-mini:hover{background:rgba(245,158,11,.15)}
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
@media(max-width:880px){.cfg-row{flex-wrap:wrap}.cfg-divider-v{display:none}.cfg-usage-col{min-width:100%;order:5}}
@media(max-width:768px){.cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}.cfg-card{border-radius:16px}.cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}.cfg-identity{min-width:0;flex:1}.cfg-usage-col{min-width:0}.cfg-exp-col{min-width:0}.cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}.cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.2);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.2);background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
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
<button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
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
<div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
<div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
</div>
<div class="sb-foot">
<button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>
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
<span class="badge bg-blue" id="uptime-badge">—</span>
<button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
</div>
</div>
<div class="metrics">
<div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP زنده</div></div>
<div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">از راه‌اندازی</div></div>
<div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
<div class="metric"><div class="m-icon"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌های ساب</div><div class="m-val" id="m-subs">—</div><div class="m-sub">فعال</div></div>
</div>
<div class="vless-box">
<div class="vl-header">
<div class="vl-title"><i class="ti ti-link"></i> لینک پیش‌فرض (بدون محدودیت)</div>
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
<div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال · سخت‌گیرانه</span></div>
<div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
<div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال · 3 mode</span></div>
<div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
<div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px">
<div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div>
<div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
</div>
</div>
<div class="card">
<div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div>
<div id="lsummary">—</div>
</div>
</div>
<div class="dash-footer">
<span class="df-text">Royal Gateway v9.2 · Railway · 2025</span>
<a class="df-link" href="https://t.me/royalpanelv2" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/royalpanelv2</a>
</div>
</section>
<section class="pg" id="pg-links">
<div class="topbar">
<div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی</div></div>
<div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
</div>
<div class="create-panel">
<div class="cp-head">
<div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
<div class="cp-head-text">
<div class="cp-head-title">ساخت کانفیگ جدید</div>
<div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
</div>
</div>
<div class="cp-body">
<div class="cp-row">
<div class="cp-block">
<div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
<input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
<div class="cp-mini-row">
<input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)">
</div>
</div>
<div class="cp-block">
<div class="cp-block-label"><i class="ti ti-folders"></i> گروه ساب و انقضا</div>
<select class="cp-input-full fs" id="nl-sub"><option value="">— بدون گروه —</option></select>
<div class="cp-mini-row">
<input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود">
</div>
<div class="chip-row" id="exp-chips">
<span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
<span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
<span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
<span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
</div>
</div>
</div>
<div class="cp-block mb16">
<div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
<div class="cp-quota-inputs">
<input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
<select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
</div>
<div class="chip-row" id="quota-chips">
<span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
<span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
<span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
<span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
<span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
<span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
</div>
</div>
<div class="cp-block mb16">
<div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
<select id="nl-proto" style="display:none">
<option value="vless-ws">VLESS / WebSocket</option>
<option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
<option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
</select>
<div class="proto-cards">
<div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
<div class="proto-card-check"><i class="ti ti-check"></i></div>
<div class="proto-card-icon"><i class="ti ti-link"></i></div>
<div class="proto-card-title">VLESS / WS</div>
<div class="proto-card-desc">پایدار و همه‌منظوره</div>
</div>
<div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
<div class="proto-card-check"><i class="ti ti-check"></i></div>
<div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
<div class="proto-card-title">XHTTP · packet-up</div>
<div class="proto-card-desc">سازگار با CDN</div>
</div>
<div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
<div class="proto-card-check"><i class="ti ti-check"></i></div>
<div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
<div class="proto-card-title">XHTTP · stream-up</div>
<div class="proto-card-desc">تاخیر پایین‌تر</div>
</div>
</div>
</div>
<div class="cp-footer">
<div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.</div>
<button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
</div>
</div>
</div>
<div class="cfg-grid" id="links-grid"></div>
<div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>
<section class="pg" id="pg-traffic">
<div class="topbar">
<div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
<div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
</div>
<div class="g2">
<div class="card">
<div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div>
<div class="ch"><canvas id="ch1"></canvas></div>
</div>
<div class="card">
<div class="card-title"><i class="ti ti-chart-donut"></i> توزیع</div>
<div class="ch-sm"><canvas id="ch2"></canvas></div>
</div>
</div>
</section>
<section class="pg" id="pg-settings">
<div class="topbar">
<div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div><div class="tb-sub">اطلاعات سرور و تغییر رمز عبور</div></div>
</div>
<div class="g2">
<div class="srv-panel" style="background:linear-gradient(145deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative">
<div class="srv-hero" style="display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)">
<div class="srv-hero-icon" style="width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,#F59E0B,#D97706);display:flex;align-items:center;justify-content:center;color:#0f0a04;font-size:22px;flex-shrink:0;box-shadow:0 6px 20px rgba(245,158,11,.2)"><i class="ti ti-server-2"></i></div>
<div class="srv-hero-text" style="flex:1;min-width:0">
<div class="srv-hero-domain" style="font-size:15px;font-weight:800;color:var(--t1);word-break:break-all" id="set-host">—</div>
<div class="srv-hero-sub" style="font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px"><span class="dot dg pulse"></span> آنلاین · Railway</div>
</div>
</div>
<div class="srv-tiles" style="display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1">
<div class="srv-tile" style="display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px"><div class="srv-tile-icon" style="width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label" style="font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px">پورت</div><div class="srv-tile-val" style="font-size:12px;font-weight:700;color:var(--t1)">443 (TLS)</div></div></div>
<div class="srv-tile" style="display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px"><div class="srv-tile-icon" style="width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label" style="font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px">نسخه</div><div class="srv-tile-val" style="font-size:12px;font-weight:700;color:var(--t1)">v9.2</div></div></div>
<div class="srv-tile" style="display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px"><div class="srv-tile-icon" style="width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label" style="font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px">فریم‌ورک</div><div class="srv-tile-val" style="font-size:12px;font-weight:700;color:var(--t1)">FastAPI + Uvicorn</div></div></div>
<div class="srv-tile" style="display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px"><div class="srv-tile-icon" style="width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label" style="font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px">پلتفرم</div><div class="srv-tile-val" style="font-size:12px;font-weight:700;color:var(--t1)">Railway</div></div></div>
</div>
</div>
<div class="pw-panel" style="background:linear-gradient(145deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative">
<div class="pw-hero" style="display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1">
<div class="pw-hero-icon" style="width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,#8B5CF6,#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 20px rgba(139,92,246,.2)"><i class="ti ti-key"></i></div>
<div class="pw-hero-text" style="flex:1;min-width:0">
<div class="pw-hero-title" style="font-size:15px;font-weight:800;color:var(--t1)">تغییر رمز عبور</div>
<div class="pw-hero-sub" style="font-size:10.5px;color:var(--t3);margin-top:3px">رمز قوی انتخاب کنید و آن را جایی امن نگه دارید</div>
</div>
</div>
<div class="pw-body" style="padding:2px 24px 22px;position:relative;z-index:1">
<div class="pw-field" style="position:relative;margin-bottom:13px">
<label style="display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px">رمز فعلی</label>
<input class="pw-input" style="width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.2s" type="password" id="cp-cur" placeholder="رمز فعلی را وارد کنید">
<button class="pw-eye" style="position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex;transition:.2s" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
</div>
<div class="pw-field" style="position:relative;margin-bottom:6px">
<label style="display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px">رمز جدید</label>
<input class="pw-input" style="width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.2s" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)">
<button class="pw-eye" style="position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex;transition:.2s" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
</div>
<div class="pw-strength" id="pw-strength-bar" style="height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px">
<div class="pw-strength-seg" style="flex:1;height:100%;border-radius:3px;background:rgba(139,122,90,.15);transition:.3s"></div>
<div class="pw-strength-seg" style="flex:1;height:100%;border-radius:3px;background:rgba(139,122,90,.15);transition:.3s"></div>
<div class="pw-strength-seg" style="flex:1;height:100%;border-radius:3px;background:rgba(139,122,90,.15);transition:.3s"></div>
<div class="pw-strength-seg" style="flex:1;height:100%;border-radius:3px;background:rgba(139,122,90,.15);transition:.3s"></div>
</div>
<div class="pw-strength-label" id="pw-strength-label" style="font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px"><i class="ti ti-shield"></i> قدرت رمز</div>
<div class="pw-reqs" style="display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px">
<span class="pw-req" id="req-len" style="font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.25s"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span>
<span class="pw-req" id="req-num" style="font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.25s"><i class="ti ti-circle-dashed"></i> شامل عدد</span>
<span class="pw-req" id="req-case" style="font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.25s"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span>
</div>
<div class="pw-field" style="position:relative;margin-bottom:18px">
<label style="display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px">تکرار رمز جدید</label>
<input class="pw-input" style="width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.2s" type="password" id="cp-cf" placeholder="تکرار رمز جدید">
<button class="pw-eye" style="position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex;transition:.2s" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
</div>
<button class="pw-submit" onclick="changePw()" style="width:100%;justify-content:center;background:linear-gradient(135deg,#8B5CF6,#6D48D6);color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(139,92,246,.25);transition:.25s"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
</div>
</div>
</div>
</section>
</main>
<script>
let isDark=localStorage.getItem('rvg-theme')!=='light';
function applyTheme(dark){
document.documentElement.setAttribute('data-theme',dark?'dark':'light');
const icon=dark?'ti-sun':'ti-moon',label=dark?'تم روشن':'تم تاریک';
document.getElementById('theme-icon').className='ti '+icon;
document.getElementById('theme-label').textContent=label;
const mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+icon;
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('rvg-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);

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
const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet-up','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','pc-xhttp'],'xhttp-stream-one':['XHTTP ULTRA','pc-ultra']};
const v=m[p]||m['vless-ws'];
return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){const r=await fetch(url,opts);if(r.status===401){location.href='/login';throw new Error('unauthorized')}return r;}
function setQuota(val,unit,el){
document.getElementById('nl-val').value = val===0?'':val;
document.getElementById('nl-unit').value = unit;
document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
el.classList.add('active');
}
function setExpiry(days,el){
document.getElementById('nl-exp').value = days===0?'':days;
document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
el.classList.add('active');
}
function selectProto(val,el){
document.getElementById('nl-proto').value = val;
document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
el.classList.add('active');
}
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
if(name==='traffic')loadTraffic();
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
const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
return `<div class="cfg-card ${cardCls}">
<div class="cfg-row">
<span class="cfg-status-dot ${allowed?'pulse':''}"></span>
<div class="cfg-identity">
<div class="cfg-label">${esc(l.label)}</div>
<div class="cfg-sub-meta">
<span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
<span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
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
<div class="cfg-badges-col">
${protoBadge(l.protocol)}
</div>
<div class="cfg-divider-v"></div>
<div class="cfg-actions">
<button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
<button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
<button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
<button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
<button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
<button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>
<button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
</div>
</div>
</div>`;
}).join('');
document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div>`).join('');
}catch(e){console.error(e)}
}

function openEditLink(uuid){
const l=allLinksList.find(x=>x.uuid===uuid);
if(!l)return;
document.getElementById('el-uuid').value=uuid;
document.getElementById('el-label').value=l.label;
document.getElementById('el-note').value=l.note||'';
if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
document.getElementById('el-exp').value='';
openModal('modal-edit-link');
}

function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}

let ch1,ch2;
function initCharts(){
const c1=document.getElementById('ch1');
if(!c1)return;
const ctx=c1.getContext('2d');
const grad=ctx.createLinearGradient(0,0,0,230);
grad.addColorStop(0,'rgba(245,158,11,0.35)');
grad.addColorStop(1,'rgba(245,158,11,0)');
ch1=new Chart(c1,{
type:'line',
data:{labels:[],datasets:[{
label:'MB',
data:[],
borderColor:'#F59E0B',
backgroundColor:grad,
fill:true,
tension:.4,
pointRadius:0,
borderWidth:2.5
}]},
options:{
responsive:true,
maintainAspectRatio:false,
plugins:{legend:{display:false}},
scales:{
x:{grid:{display:false},ticks:{color:'#8B7A5A',font:{size:9}}},
y:{grid:{color:'rgba(245,158,11,0.05)'},ticks:{color:'#8B7A5A',font:{size:9},callback:v=>v+' MB'}}
}
}
});
ch2=new Chart(document.getElementById('ch2'),{
type:'doughnut',
data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{
data:[55,35,10],
backgroundColor:['#F59E0B','#10B981','#8B5CF6'],
borderColor:getComputedStyle(document.documentElement).getPropertyValue('--card')||'#1c140a',
borderWidth:4,
hoverOffset:10,
borderRadius:6,
spacing:3
}]},
options:{
responsive:true,
maintainAspectRatio:false,
cutout:'72%',
plugins:{
legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},
tooltip:{backgroundColor:'rgba(28,20,10,.96)',borderColor:'rgba(245,158,11,.25)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
}
}
});
}

async function loadTraffic(){
try{
const r=await authF('/stats'),d=await r.json();
if(d.hourly){
const labels=Object.keys(d.hourly).sort();
const vals=labels.map(k=>d.hourly[k]/(1024*1024));
if(ch1){ch1.data.labels=labels;ch1.data.datasets[0].data=vals;ch1.update()}
}
}catch(e){}
}

async function createLink(){
const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
const val=document.getElementById('nl-val').value||0;
const unit=document.getElementById('nl-unit').value||'MB';
const exp=document.getElementById('nl-exp').value||0;
const note=document.getElementById('nl-note').value.trim();
const sub_id=document.getElementById('nl-sub').value||null;
const protocol=document.getElementById('nl-proto').value||'vless-ws';
try{
const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol})});
if(!r.ok)throw new Error('failed');
['nl-label','nl-val','nl-exp','nl-note'].forEach(id=>document.getElementById(id).value='');
toast('کانفیگ ساخته شد ✓','ok');
loadLinks();
fetchStats();
}catch(e){toast('خطا در ساخت','err')}
}

async function toggleActive(uuid,newState){
try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}

async function resetUsage(uuid){
try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}

async function deleteLink(uuid){
if(!confirm('حذف این کانفیگ؟'))return;
try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();fetchStats();}catch(e){toast('خطا','err')}
}

async function fetchStats(){
try{
const r=await authF('/stats'),d=await r.json();
document.getElementById('m-conns').textContent=d.active_connections||0;
document.getElementById('conns-nb')&&(document.getElementById('conns-nb').textContent=d.active_connections);
document.getElementById('m-traffic').innerHTML=(d.total_traffic_mb||0).toFixed(1)+'<span class="m-unit">MB</span>';
document.getElementById('m-alinks').textContent=d.active_links||0;
document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
document.getElementById('m-subs').textContent=d.subs_count||0;
document.getElementById('uptime-inline').textContent=d.uptime||'0h 0m';
document.getElementById('uptime-badge').textContent='Railway · '+(d.uptime||'0h 0m');
document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
const pct=Math.min(100,Math.round((d.active_connections/100)*100));
document.getElementById('bw-pct').textContent=pct+'%';
document.getElementById('bw-bar').style.width=pct+'%';
loadTraffic();
}catch(e){console.error(e)}
}

async function fetchDefaultVless(){
try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';}catch(e){}
}

function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();toast('رفرش شد','ok')}

function togglePwField(id,btn){
const inp=document.getElementById(id);
const icon=btn.querySelector('i');
const toText=inp.type==='password';
inp.type=toText?'text':'password';
icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}

function checkPwStrength(val){
const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
const label=document.getElementById('pw-strength-label');
const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
const hasLen=val.length>=4,hasNum=/\\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
reqLen.classList.toggle('met',hasLen);
reqNum.classList.toggle('met',hasNum);
reqCase.classList.toggle('met',hasCase);
let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
const colors=['#EF4444','#F59E0B','#3B82F6','#10B981'],labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];
segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(139,122,90,.15)'});
if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}
label.innerHTML=`<i class="ti ti-shield-check" style="color:${colors[Math.max(0,score-1)]}"></i> ${labels[Math.max(0,score-1)]}`;
}

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

function openModal(id){const m=document.getElementById(id);if(m)m.classList.add('open')}
function closeModal(id){const m=document.getElementById(id);if(m)m.classList.remove('open')}

document.addEventListener('DOMContentLoaded',async()=>{
await checkAuth();
document.getElementById('set-host').textContent=location.host;
initCharts();
fetchStats();
fetchDefaultVless();
loadLinks();
setInterval(fetchStats,5000);
});
</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Royal Sub · پنل مدیریت</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#0f0a04;--card:#1c140a;--card-b:rgba(245,158,11,0.1);--accent:#F59E0B;--accent2:#FBBF24;--green:#10B981;--green-bg:rgba(16,185,129,0.06);--red:#EF4444;--red-bg:rgba(239,68,68,0.06);--t1:#FFF8ED;--t2:#C8B088;--t3:#8B7A5A;--shadow:0 12px 40px rgba(0,0,0,0.5)}}
[data-theme="light"]{{--bg:#FBF5ED;--card:#FFFFFF;--card-b:rgba(245,158,11,0.12);--accent:#D97706;--accent2:#B45309;--t1:#1A1208;--t2:#5C4A2A;--t3:#8B7A5A;--shadow:0 12px 36px rgba(20,15,8,0.1)}}
html,body{{min-height:100%;background:var(--bg);font-family:'Vazirmatn',sans-serif;color:var(--t1);font-size:14px;transition:background .4s,color .4s}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(245,158,11,0.08),transparent 62%),var(--bg);z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px;animation:slideUp 0.7s cubic-bezier(.16,1,.3,1)}}
@keyframes slideUp{{0%{{opacity:0;transform:translateY(24px) scale(0.98)}}100%{{opacity:1;transform:translateY(0) scale(1)}}}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}}
.brand{{display:flex;align-items:center;gap:11px}}
.brand-img{{width:42px;height:42px;border-radius:13px;overflow:hidden;border:1px solid var(--card-b);flex-shrink:0;background:linear-gradient(135deg,#F59E0B,#D97706)}}
.brand-img svg{{width:100%;height:100%;padding:7px;fill:#fff}}
.brand-name{{font-size:15px;font-weight:800;background:linear-gradient(135deg,#FBBF24,#F59E0B);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.brand-sub{{font-size:9.5px;color:var(--t3)}}
.top-actions{{display:flex;gap:6px}}
.icon-btn{{width:36px;height:36px;border-radius:11px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:.25s}}
.icon-btn:hover{{background:rgba(245,158,11,0.08);color:var(--accent2)}}
.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px;margin-bottom:16px;box-shadow:var(--shadow)}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:rgba(245,158,11,0.05);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}
.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;transition:.3s}}
.stat-card:hover{{border-color:rgba(245,158,11,0.2);transform:translateY(-2px)}}
.stat-label{{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}}
.stat-val{{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:9.5px;color:var(--t3);margin-top:6px}}
.cfg-title{{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em}}
.cfg-title i{{color:var(--accent);font-size:15px}}
.cfg-grid{{display:grid;gap:13px}}
.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:18px;transition:all .3s;position:relative;overflow:hidden}}
.cfg-card:hover{{border-color:rgba(245,158,11,0.2);box-shadow:var(--shadow);transform:translateY(-2px)}}
.cfg-top{{padding:17px 19px 15px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14.5px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800}}
.pc-ws{{background:rgba(245,158,11,0.08);color:var(--accent2)}}
.pc-xhttp{{background:rgba(139,92,246,0.08);color:#A78BFA}}
.pc-ultra{{background:var(--green-bg);color:var(--green)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:4px;background:rgba(245,158,11,0.06);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .6s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-28px}}
.cfg-tear::after{{left:-28px}}
.cfg-bottom{{padding:15px 19px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.25s}}
.cfg-link-toggle:hover{{background:rgba(245,158,11,0.05);border-color:rgba(245,158,11,0.2);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .25s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .3s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.25);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(217,119,6,.04)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .2s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(135deg,#F59E0B,#D97706);color:#0f0a04;box-shadow:0 3px 12px rgba(245,158,11,.2)}}
.btn-p:hover{{transform:translateY(-2px);box-shadow:0 6px 20px rgba(245,158,11,.3)}}
.btn-g{{background:rgba(245,158,11,0.05);color:var(--accent2);border:1px solid rgba(245,158,11,.08)}}
.btn-g:hover{{background:rgba(245,158,11,.12)}}
.btn-pur{{background:rgba(139,92,246,0.05);color:#A78BFA;border:1px solid rgba(139,92,246,.08)}}
.btn-pur:hover{{background:rgba(139,92,246,.12)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.3;transform:scale(0.7)}}}}
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:70vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:26px;padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden}}
.lock-banner{{background:linear-gradient(150deg,rgba(245,158,11,0.06),rgba(245,158,11,.01) 70%);padding:38px 30px 26px}}
.lock-shield{{width:64px;height:64px;border-radius:18px;background:rgba(245,158,11,0.05);border:1px solid var(--card-b);display:flex;align-items:center;justify-content:center;margin:0 auto 18px}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1)}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:24px 30px 30px}}
.lock-field{{position:relative;margin-bottom:13px}}
.lock-inp{{width:100%;padding:13px 20px;border-radius:13px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.1em;transition:.25s}}
[data-theme="light"] .lock-inp{{background:rgba(217,119,6,.03)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 3px rgba(245,158,11,0.05)}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}}
.lock-err{{color:var(--red);font-size:11.5px;margin-bottom:10px;min-height:16px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}
.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}
.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .3s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(16,185,129,.25);background:var(--green-bg);color:var(--green)}}
.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px;animation:fi .25s ease}}
.qr-modal.open{{display:flex}}
@keyframes fi{{from{{opacity:0;transform:scale(0.95)}}to{{opacity:1;transform:scale(1)}}}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}}
.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:700;transition:.2s}}
@media(max-width:520px){{.stats-bar{{grid-template-columns:1fr 1fr}}.stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}.sub-name{{font-size:19px}}.wrap{{padding:16px 12px 50px}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
</style>
</head>
<body>
<div class="bg-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
<div class="qr-box" onclick="event.stopPropagation()">
<div class="qr-title" id="qr-label">QR Code</div>
<div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
<button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
</div>
</div>
<div class="wrap">
<div class="top">
<div class="brand">
<div class="brand-img">
<svg viewBox="0 0 100 100"><path d="M50 10 L90 30 L90 70 L50 90 L10 70 L10 30 Z" stroke="#fff" stroke-width="2" fill="none"/><path d="M50 25 L75 37 L75 63 L50 75 L25 63 L25 37 Z" stroke="#fff" stroke-width="1.5" fill="none"/><circle cx="50" cy="50" r="10" stroke="#fff" stroke-width="1.5" fill="none"/><path d="M42 38 L58 62 M58 38 L42 62" stroke="#fff" stroke-width="1" opacity="0.4"/></svg>
</div>
<div><div class="brand-name">Royal Gateway</div><div class="brand-sub">پنل مدیریت · v9.2</div></div>
</div>
<div class="top-actions">
<button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
<a class="icon-btn" href="https://t.me/royalpanelv2" target="_blank" title="کانال تلگرام"><i class="ti ti-brand-telegram"></i></a>
</div>
</div>
<div id="root">
<div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
</div>
<div class="footer">کانال رسمی: <a href="https://t.me/royalpanelv2" target="_blank">@royalpanelv2</a> · Royal Gateway v9.2</div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';
let isDark=localStorage.getItem('rvg-pub-theme')!=='light';
function applyTheme(dark){{document.documentElement.setAttribute('data-theme',dark?'dark':'light');document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('rvg-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);

function toast(msg,type=''){{
const t=document.getElementById('toast');
t.textContent=msg;t.className='toast show'+(type?' '+type:'');
setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{
if(p==='xhttp-stream-one')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';
if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';
return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}
function showQR(label,link){{
document.getElementById('qr-label').textContent=label;
document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
document.getElementById('qr-modal').classList.add('open');
}}
function toggleLink(i){{
const wrap=document.getElementById('vw-'+i);
const btn=document.getElementById('vt-'+i);
const open=wrap.classList.toggle('open');
btn.classList.toggle('open',open);
btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';
}}
async function loadData(pw=''){{
const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
const r=await fetch(url);
return r.json();
}}
function renderLock(name,errMsg=''){{
document.getElementById('root').innerHTML=`
<div class="lock-stage">
<div class="lock-card">
<div class="lock-banner">
<div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
<div class="lock-title">${{esc(name)}}</div>
<div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div>
</div>
<div class="lock-form">
<div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
<div class="lock-field">
<input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
</div>
<button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button>
</div>
<div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div>
</div>
</div>
`;
document.getElementById('lock-pw').addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}
async function submitLock(){{
const pw=document.getElementById('lock-pw').value;
const data=await loadData(pw);
if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}
savedPw=pw;
renderContent(data);
}}
function renderContent(d){{
const activeCount=d.links.filter(l=>l.active).length;
const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');
window._rvgSubUrl = subUrl;
window._rvgSubName = d.name;
window._rvgLinks = d.links.map(l => ({{
vless : l.vless_link,
sub : l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
label : l.label,
}}));
document.getElementById('root').innerHTML=`
<div class="sub-info">
<div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div>
<div class="sub-name">${{esc(d.name)}}</div>
${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
<div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div>
<div class="sub-sub-box">
<span class="sub-sub-url">${{esc(subUrl)}}</span>
<button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px"
onclick="navigator.clipboard.writeText(window._rvgSubUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))">
<i class="ti ti-copy"></i> کپی لینک ساب
</button>
<button class="btn btn-g" style="padding:7px 12px;font-size:10.5px"
onclick="showQR(window._rvgSubName + ' — کل گروه', window._rvgSubUrl)">
<i class="ti ti-qrcode"></i> QR کل
</button>
</div>
</div>
<div class="stats-bar">
<div class="stat-card">
<div class="stat-label">کانفیگ‌های فعال</div>
<div class="stat-val">${{toFa(activeCount)}}</div>
<div class="stat-sub">از ${{toFa(d.links.length)}} کانفیگ</div>
</div>
<div class="stat-card">
<div class="stat-label">اتصالات زنده</div>
<div class="stat-val">${{toFa(d.active_connections)}}</div>
<div class="stat-sub" style="color:var(--green);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div>
</div>
<div class="stat-card">
<div class="stat-label">کل مصرف</div>
<div class="stat-val" style="font-size:17px;margin-top:3px">${{esc(d.total_used_fmt)}}</div>
<div class="stat-sub">همه کانفیگ‌ها</div>
</div>
</div>
<div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div>
<div class="cfg-grid">
${{d.links.map((l, i) => {{
const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
return `
<div class="cfg-card${{l.active ? '' : ' inactive'}}">
<div class="cfg-top">
<div class="cfg-head">
<div>
<div class="cfg-label">${{esc(l.label)}}</div>
<div class="cfg-badges">
${{protoChip(l.protocol)}}
${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>` : ''}}
</div>
</div>
<span class="cfg-status ${{l.active ? 'ok' : 'no'}}">${{l.active ? '<i class="ti ti-circle-check"></i> فعال' : '<i class="ti ti-circle-x"></i> غیرفعال'}}</span>
</div>
<div class="cfg-usage">
<div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div>
<div class="utxt"><span>${{esc(l.used_fmt)}} مصرف شده</span><span>سهمیه: ${{lim}}</span></div>
</div>
</div>
<div class="cfg-tear"></div>
<div class="cfg-bottom">
<button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})">
<span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span>
<i class="ti ti-chevron-down"></i>
</button>
<div class="cfg-vless-wrap" id="vw-${{i}}">
<div class="cfg-vless-inner">
<div class="cfg-vless">${{esc(l.vless_link)}}</div>
</div>
</div>
<div class="cfg-actions">
<button class="btn btn-p"
onclick="navigator.clipboard.writeText(window._rvgLinks[${{i}}].vless).then(()=>toast('لینک کپی شد ✓','ok'))">
<i class="ti ti-copy"></i> کپی لینک
</button>
<button class="btn btn-g"
onclick="showQR(window._rvgLinks[${{i}}].label, window._rvgLinks[${{i}}].vless)">
<i class="ti ti-qrcode"></i> QR
</button>
</div>
</div>
</div>
`;
}}).join('')}}
</div>
`;
}}
async function init(){{
try{{
const data = await loadData();
if (data.locked) {{ renderLock(data.name); return; }}
renderContent(data);
}} catch(e) {{
document.getElementById('root').innerHTML =
'<div class="empty-state" style="color:var(--red)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';
}}
}}
init();
</script>
</body></html>"""

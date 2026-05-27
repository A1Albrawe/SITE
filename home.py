from flask import Blueprint, render_template_string

home_blueprint = Blueprint('home', __name__)

# عزل التنسيقات الفلورسنتية الحركية لمحاكاة ملفك الشخصي بالملي وبدون تداخل الأقواس
HOME_CSS_PART1 = """
<style>
    :root {
        --bg-global: #06090d; --text-main: #c9d1d9; --bg-card: #0d1117; 
        --border-main: #30363d; --border-neon: #3fb950; --border-cyber: #ff007f; --text-white: #fff; --border-sub: #21262d;
    }
    
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 0; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; overflow-x: hidden; }
    
    .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 1200px; margin: 0 auto; padding: 15px 25px; box-sizing: border-box; position: relative; z-index: 1000; border-bottom: 1px solid var(--border-sub); }
    .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 8px var(--border-neon); text-decoration: none; font-family: monospace; cursor: pointer; }
    .menu-btn-trigger { background: var(--bg-card); border: 1px solid var(--border-main); color: var(--border-neon); padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; display: flex; align-items: center; gap: 6px; font-family: inherit; transition: 0.2s; }
    .menu-btn-trigger:hover { background: var(--border-neon); color: #000; box-shadow: 0 0 12px var(--border-neon); }
    
    .profile-master-container { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 15px 40px 15px; box-sizing: border-box; position: relative; z-index: 10; }
    
    /* 🎮 هندسة غلاف الألعاب والاسم المشتعل (Cyber Cover Graphic Header) المستنسخ من صورتك بالملي */
    .cyber-profile-cover { width: 100%; height: 350px; background: linear-gradient(135deg, #1f1a3a 0%, #0d1117 50%, #1a233a 100%); border-radius: 0 0 18px 18px; border: 1px solid var(--border-main); border-bottom: 4px solid var(--border-neon); position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center; overflow: hidden; box-shadow: 0 15px 35px rgba(0,0,0,0.5); }
    .cover-gamepad-icon { font-size: 90px; color: #3fb950; text-shadow: 0 0 25px #3fb950, 0 0 45px #ff007f; animation: gamepadFloat 4s ease-in-out infinite alternate; margin-bottom: 10px; }
    .cover-brand-name { font-size: 55px; font-weight: 900; color: #fff; letter-spacing: 3px; font-family: 'Impact', 'Arial Black', sans-serif; text-transform: uppercase; background: linear-gradient(to bottom, #ffea7f, #ff7b72, #ff5555); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 12px #ff7b72); margin: 0; }
    
    @keyframes gamepadFloat { 0% { transform: translateY(0) rotate(-2deg); } 100% { transform: translateY(-15px) rotate(2deg); } }
    /* 🖼️ هندسة ومقاييس الأفاتار الدائري التداخلي التفاعلي (Overlapping Circular Avatar) */
    .profile-meta-row { display: flex; align-items: flex-end; gap: 30px; margin-top: -65px; padding: 0 40px; box-sizing: border-box; width: 100%; direction: rtl; position: relative; z-index: 100; }
    
    .avatar-wrapper-circle { width: 155px; height: 155px; border-radius: 50%; border: 5px solid var(--bg-global); overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.5); background: #04060a; flex-shrink: 0; transition: transform 0.3s; }
    .avatar-wrapper-circle:hover { transform: scale(1.04) rotate(3deg); }
    .avatar-img-circle { width: 100%; height: 100%; object-fit: cover; }
    
    .profile-identity-zone { flex: 1; text-align: right; padding-bottom: 15px; }
    .user-full-name { font-size: 28px; font-weight: bold; color: var(--text-white); margin: 0 0 5px 0; display: flex; align-items: center; gap: 10px; }
    .user-slug-name { font-size: 18px; color: #8b949e; font-weight: 500; font-family: monospace; }
    
    .followers-badge-line { font-size: 13.5px; color: #8b949e; margin: 8px 0 0 0; font-weight: 500; }
    .followers-count { color: var(--text-white); font-weight: bold; }
    
    /* 🛠️ أجنحة لوحة المعلومات الموثقة لجامعة عين شمس والثانوية */
    .info-dashboard-card { background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 14px; padding: 30px; margin-top: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); text-align: right; direction: rtl; box-sizing: border-box; }
    .dashboard-title-row { display: flex; align-items: center; gap: 8px; font-size: 16px; font-weight: bold; color: #58a6ff; margin-bottom: 20px; border-bottom: 1px solid var(--border-sub); padding-bottom: 10px; }
    
    .meta-info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
    .info-item-box { display: flex; align-items: center; gap: 12px; font-size: 14.5px; color: var(--text-main); line-height: 1.5; }
    .info-item-box i { color: #8b949e; width: 20px; text-align: center; font-size: 16px; }
    .highlight-text-blue { color: #58a6ff; font-weight: bold; text-decoration: none; }
    .highlight-text-blue:hover { text-decoration: underline; }
    
    @media (max-width: 850px) {
        .cyber-profile-cover { height: 220px; } .cover-gamepad-icon { font-size: 55px; } .cover-brand-name { font-size: 32px; }
        .profile-meta-row { flex-direction: column; align-items: center; text-align: center; margin-top: -75px; padding: 0 15px; }
        .profile-identity-zone { text-align: center; padding-bottom: 0; } .user-full-name { justify-content: center; flex-direction: column; gap: 4px; }
        .meta-info-grid { grid-template-columns: 1fr; }
    }
</style>
"""
HOME_HTML_BODY = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>علي احمد البراوي | البوابة المعتمدة</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    """ + HOME_CSS_PART1 + HOME_CSS_PART2 + """
</head>
<body>

    <div class="top-nav">
        <a href="/" class="brand-logo">Albrawe</a>
        <button class="menu-btn-trigger" onclick="loadAndOpenSidebarMenu()"><i class="fas fa-bars"></i> القائمة</button>
    </div>

    <!-- صندوق الاستقبال الشاغر لحقن كود الـ Sidebar المطور المنبثق دائرياً من menu.py حياً -->
    <div id="dynamicMenuInjectionZone"></div>

    <div class="profile-master-container">
        
        <!-- 🎮 الغلاف الفاخر المستنسخ من صورتك بالبكسل حاملا الاسم الكبير المشتعل -->
        <div class="cyber-profile-cover">
            <div class="cover-gamepad-icon"><i class="fas fa-gamepad"></i></div>
            <h2 class="cover-brand-name">ALBRAWE</h2>
        </div>
        
        <!-- 🖼️ صف الهوية البصرية والأفاتار الدائري التداخلي المتطابق كلياً حياً -->
        <div class="profile-meta-row">
            <div class="avatar-wrapper-circle">
                <img class="avatar-img-circle" src="/static/avatar.png" alt="علي احمد البراوي" onerror="this.src='https://flagcdn.com'">
            </div>
            
                <div class="user-full-name">
                    <span>علي احمد البراوي</span>
                    <span class="user-slug-name">(Albrawe)</span>
                </div>
                <div class="followers-badge-line">
                    المتابعون <span class="followers-count">١٧١</span> • يتابع <span class="followers-count">١٥٧</span>
                </div>
            </div>
        </div>
        
        <!-- 🛠️ لوحة المعلومات الموثقة لجامعة عين شمس وابن خلدون كما بالصورة بالملي -->
        <div class="info-dashboard-card">
            <div class="dashboard-title-row">
                <i class="fas fa-info-circle"></i> لوحة المعلومات والنبذة التعريفية المعتمدة
            </div>
            <div class="meta-info-grid">
                <div class="info-item-box">
                    <i class="fas fa-briefcase"></i>
                    <span>منشئ محتوى رقمي حياً بـ <span style="color:var(--text-white); font-weight:bold;">Cairo</span> • عمل حر 💼</span>
                </div>
                <div class="info-item-box">
                    <i class="fas fa-graduation-cap"></i>
                    <span>درس في <span class="highlight-text-blue">Ain Shams University</span> 🎓</span>
                </div>
                <div class="info-item-box">
                    <i class="fas fa-school"></i>
                    <span>درس في <span style="color:var(--text-white); font-weight:bold;">ابن خلدون الثانوية</span> 🏫</span>
                </div>
                <div class="info-item-box" style="border-top:1px dashed var(--border-sub); padding-top:10px; grid-column:1/-1;">
                    <i class="fas fa-user-shield" style="color:#3fb950;"></i>
                    <span><strong style="color:#fff;">نبذة برمجية:</strong> هندسة وتطوير تطبيقات الويب الكاملة باستخدام بايثون (Flask)، وتصميم الواجهات المتكاملة والمعالجات المحلية الفائقة الكفاءة.</span>
                </div>
            </div>
        </div>
        
    </div>

    <div class="global-footer-bar">
        حقوق النشر محفوظة برمجياً وتعود إلى المسؤول البراوي بتاريخ 2026 ©
    </div>
"""
    <script>
        // الخوارزمية التزامنية لسحب الستارة المنبثقة دائرياً من menu.py وحقنها حياً فورا بدون أي تداخل
        function loadAndOpenSidebarMenu() {
            const zone = document.getElementById("dynamicMenuInjectionZone");
            
            if (zone.innerHTML.trim() !== "") {
                toggleSidebarMenu(true);
                return;
            }
            
            fetch('/api/get_sidebar_menu')
            .then(res => res.json())
            .then(data => {
                const styleNode = document.createElement("style");
                styleNode.innerHTML = data.css;
                document.head.appendChild(styleNode);
                
                zone.innerHTML = data.html;
                setTimeout(() => { toggleSidebarMenu(true); }, 20);
            }).catch(() => { alert("❌ عطل طارئ: تعذر جلب مستودع القائمة."); });
        }

        function toggleSidebarMenu(openState) {
            const sidebar = document.getElementById("slidingSidebarMenu");
            if (sidebar) {
                if(openState) sidebar.classList.add("active");
                else sidebar.classList.remove("active");
            }
        }

        function toggleGamesDropdown() {
            const trigger = document.getElementById("gamesMenuTrigger");
            const panel = document.getElementById("gamesDropdownPanel");
            if (panel.style.display === "flex") {
                panel.style.display = "none";
                trigger.classList.remove("open-state");
            } else {
                panel.style.display = "flex";
                trigger.classList.add("open-state");
            }
        }
    </script>
</body>
</html>
"""

@home_blueprint.route('/')
def home_page():
    return render_template_string(HOME_HTML_BODY)

from flask import Blueprint, render_template_string

home_blueprint = Blueprint('home', __name__)

# عزل التنسيقات ثنائية الأجنحة لحماية النواة والـ CSS من التعارض النصي للأقواس خارج الصندوق
HOME_CSS_PART1 = """
<style>
    :root {
        --bg-global: #06090d; --text-main: #c9d1d9; --bg-card: #0d1117; 
        --border-main: #30363d; --border-neon: #58a6ff; --border-cyber: #3fb950; --text-white: #fff; --border-sub: #21262d;
    }
    
    body { font-family: 'Courier New', Courier, monospace; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; overflow-x: hidden; transition: background 0.3s, color 0.3s; }
    
    /* 🌐 شريط الهيدر الموحد القياسي العلوى */
    .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 1200px; margin: 0 auto 35px auto; border-bottom: 2px solid var(--border-sub); padding-bottom: 14px; box-sizing: border-box; position: relative; z-index: 1000; }
    .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 8px var(--border-neon); text-decoration: none; font-family: monospace; cursor: pointer; }
    .menu-btn-trigger { background: var(--bg-card); border: 1px solid var(--border-main); color: var(--border-neon); padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; display: flex; align-items: center; gap: 6px; font-family: inherit; transition: 0.2s ease; }
    .menu-btn-trigger:hover { background: var(--border-neon); color: var(--bg-global); box-shadow: 0 0 12px var(--border-neon); }
    
    .main-container { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; position: relative; z-index: 10; }
    
    /* 💻 الهيكل ثنائي الأجنحة السينمائي الممتد الفخم لتغطية الشاشات الكبيرة بالبكسل دون تعليق */
    .responsive-profile-wrapper { 
        display: flex; flex-direction: row; gap: 40px; width: 100%; max-width: 1200px; 
        background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 18px; 
        padding: 45px; box-shadow: 0 30px 60px rgba(0,0,0,0.4); border-bottom: 4px solid var(--border-neon); 
        box-sizing: border-box; align-items: center; direction: rtl; transition: background 0.3s, border 0.3s;
        position: relative; z-index: 50;
    }
    
    .profile-sidebar-zone { flex: 1; max-width: 280px; display: flex; flex-direction: column; align-items: center; text-align: center; border-left: 2px solid var(--border-sub); padding-left: 30px; box-sizing: border-box; }
    .profile-content-zone { flex: 2; display: flex; flex-direction: column; justify-content: center; text-align: right; box-sizing: border-box; padding-right: 10px; }
    
    .avatar-wrapper { width: 145px; height: 145px; border-radius: 16px; border: 2px solid var(--border-neon); overflow: hidden; box-shadow: 0 0 20px rgba(88,166,255,0.2); margin-bottom: 20px; display: flex; align-items: center; justify-content: center; background: #04060a; }
    .avatar-img { width: 100%; height: 100%; object-fit: cover; display: block; }
    
    .profile-name { font-size: 28px; font-weight: bold; color: var(--text-white); margin: 0 0 8px 0; }
    .profile-title { font-size: 11.5px; font-weight: bold; color: var(--border-neon); margin: 0; text-transform: uppercase; letter-spacing: 0.5px; }
</style>
"""
# 🪐 الجزء الثاني: عزل أنماط لوحة البيانات وتثبيت معايير الانبثاق الدائري المتمدد للستارة الجانبية
HOME_CSS_PART2 = """
<style>
    .details-sub-box { display: flex; flex-direction: column; gap: 16px; font-size: 14.5px; line-height: 1.65; }
    .meta-item { display: block; color: var(--text-main); }
    .meta-label { font-weight: bold; color: var(--text-white); }
    .tech-highlight { color: var(--border-neon); font-weight: bold; font-family: monospace; }
    .global-footer-bar { width: 100%; text-align: center; margin-top: 40px; padding-top: 15px; border-top: 1px solid var(--border-sub); font-size: 12px; color: #8b949e; font-family: monospace; position: relative; z-index: 100; }

    /* 🕹️ تثبيت وتحقيق الانبثاق الدائري للستارة الجانبية بأعلى طبقة منعاً للتعليق */
    .sidebar-overlay { 
        position: fixed !important; top: 0 !important; right: 0 !important; 
        width: 320px !important; height: 100vh !important; 
        background: rgba(8, 12, 20, 0.99) !important; border-left: 2px solid #58a6ff !important; 
        box-shadow: -20px 0 40px rgba(0, 0, 0, 0.9) !important; z-index: 99999999 !important; 
        display: flex !important; flex-direction: column !important; 
        padding: 30px 25px !important; box-sizing: border-box !important; 
        text-align: right !important; direction: rtl !important;
        clip-path: circle(0% at 100% 0%); transition: clip-path 0.45s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .sidebar-overlay.active { clip-path: circle(150% at 100% 0%) !important; }
    
    .close-menu-btn { background: #161b22; border: 1px solid #30363d; color: #ff5555; font-size: 13.5px; font-weight: bold; cursor: pointer; display: flex; align-items: center; gap: 6px; padding: 7px 14px; border-radius: 6px; align-self: flex-start; margin-bottom: 25px; font-family: inherit; }
    .sidebar-links-wrapper { display: flex; flex-direction: column; text-align: right; gap: 5px; }
    .section-menu-divider { font-size: 14.5px; font-weight: bold; display: flex; align-items: center; gap: 8px; justify-content: flex-start; margin-top: 15px; margin-bottom: 8px; border-bottom: 1px dashed #21262d; padding-bottom: 6px; color: #8b949e; }
    .dropdown-trigger-btn { background: none; border: none; font-size: 15.5px; font-weight: bold; width: 100%; padding: 10px 0; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit; color: #3fb950; text-shadow: 0 0 4px rgba(63,185,80,0.2); }
    .dropdown-content-panel { display: none; background: #05070b; border: 1px solid #21262d; border-radius: 8px; padding: 4px 12px; margin-bottom: 10px; flex-direction: column; }
    .game-link-btn { text-decoration: none; font-size: 14px; font-family: inherit; padding: 9px 0; display: block; width: 100%; text-align: right; font-weight: 500; border-bottom: 1px dashed #161b22; }
    .game-link-btn:last-child { border-bottom: none; }
    
    .general-link-item { text-decoration: none; font-size: 15.5px; font-weight: bold; padding: 11px 0; display: block; font-family: inherit; }
    .link-home { color: #8b949e; } .link-projects { color: #a371f7; } .link-about { color: #ff7b72; } .link-scripts { color: #58a6ff; } .link-report { color: #ff5555; }
    
    @media (max-width: 850px) {
        body { padding: 15px; } .top-nav { max-width: 100%; } .responsive-profile-wrapper { flex-direction: column; align-items: center; padding: 25px; max-width: 440px; }
        .profile-sidebar-zone { flex: none; width: 100%; max-width: 100%; border-left: none; border-bottom: 2px solid var(--border-sub); padding-left: 0; padding-bottom: 25px; margin-bottom: 20px; }
        .profile-content-zone { width: 100%; padding-right: 0; }
    }
</style>
"""
# 🪐 الجزء الثالث: دالة سحب وحقن باقة الألعاب وهيكل الـ HTML الصافي ثنائي الأجنحة
def get_embedded_games_html():
    import os
    from flask import current_app
    games_list_nodes = []
    try:
        games_dir = os.path.join(current_app.root_path, 'static', 'my_games')
        if os.path.exists(games_dir):
            for filename in sorted(os.listdir(games_dir)):
                if filename.endswith('.txt'):
                    game_slug = filename.replace('.txt', '').replace('\\n', '').replace('\\r', '').strip()
                    file_path = os.path.join(games_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        raw_lines = f.readlines()
                    lines = [str(line).replace('\\n', '').replace('\\r', '').strip() for line in raw_lines if line.strip()]
                    game_name = lines if len(lines) > 0 else game_slug
                    game_icon = lines if len(lines) > 1 else "fas fa-gamepad"
                    game_color = lines if len(lines) > 2 else "#fff"
                    node_html = f'<a href="/{game_slug}" class="game-link-btn" style="color: {game_color};"><i class="{game_icon}"></i> {game_name}</a>'
                    games_list_nodes.append(node_html)
    except Exception: pass
    return "".join(games_list_nodes) if games_list_nodes else '<p style="color:#8b949e; font-size:12px;">قائمة الألعاب فارغة.</p>'

@home_blueprint.route('/')
def home_page():
    dynamic_games_html = get_embedded_games_html()
    
    HOME_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Albrawe | البوابة الرسمية الموحدة</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    """ + HOME_CSS_PART1 + HOME_CSS_PART2 + """
</head>
<body>

    <div class="top-nav">
        <a href="/" class="brand-logo">Albrawe</a>
        <button class="menu-btn-trigger" onclick="toggleSidebarMenu(true)"><i class="fas fa-bars"></i> القائمة</button>
    </div>

    <!-- 🕹️ الـ Sidebar المنزلق الملوّن والمحمي المدمج صراحة لمنع التعليق البصري نهائياً -->
    <div class="sidebar-overlay" id="slidingSidebarMenu">
        <button class="close-menu-btn" onclick="toggleSidebarMenu(false)"><i class="fas fa-times"></i> إغلاق القائمة</button>
        
        <div class="sidebar-links-wrapper">
            <a href="/" class="general-link-item link-home">البوابة الرئيسية</a>
            
            <button class="dropdown-trigger-btn" id="gamesMenuTrigger" onclick="toggleGamesDropdown()">
                <span>قائمة ألعاب النظام 🎮</span>
                <i class="fas fa-chevron-down arrow-icon"></i>
            </button>
            <div class="dropdown-content-panel" id="gamesDropdownPanel">
                """ + dynamic_games_html + """
            </div>
            
            <div class="section-menu-divider">مسارات إضافية</div>
            <a href="/projects" class="general-link-item link-projects">معرض المشاريع 📁</a>
            <a href="/about" class="general-link-item link-about">(About us) 👤</a>
            <a href="/scripts" class="general-link-item link-scripts">إسكربتات بايثون 💻</a>
            <a href="/report" class="general-link-item link-report">الإبلاغ عن مشكلة (صيانة) 🛠️</a>
            <a href="https://t.me" target="_blank" class="general-link-item link-telegram">حسابي في التليجرام ✈️</a>
        </div>
    </div>

    <div class="main-container">
        <!-- 💻 الهيكل ثنائي الأجنحة الفخم الممتد لتغطية شاشات الكمبيوتر واللاب توب بالبكسل -->
        <div class="responsive-profile-wrapper">
            
            <!-- الجناح الأيمن المطور (صورة الاسم والمسمى) -->
            <div class="profile-sidebar-zone">
                <div class="avatar-wrapper">
                    <img class="avatar-img" src="/static/avatar.png" alt="Albrawe Profile" onerror="this.src='https://flagcdn.com'">
                </div>
                <h1 class="profile-name">Albrawe</h1>
                <div class="profile-title">Architecture & Software Engineer</div>
            </div>
            
            <!-- الجناح الأيسر المطور (الخبرات والتقنيات الأساسية بالملي) -->
            <div class="profile-content-zone">
                <div class="details-sub-box">
                    <span class="meta-item">
                        ⚡ <span class="meta-label">خبراتي:</span> بناء وتطوير تطبيقات الويب الكاملة، وتصميم وتعديل اسكريبتات البايثون. إنشاء وتصميم صفحات الويب المتكاملة، معالجة البيانات المحلية، والواجهات الذكية.
                    </span>
                    <span class="meta-item" style="border-top: 1px dashed var(--border-sub); padding-top: 12px; margin-top: 2px;">
                        🛠️ <span class="meta-label">التقنيات الأساسية:</span>
                        <div style="margin-top: 8px; display: flex; flex-direction: column; gap: 6px;">
                            <div>🔹 <span class="tech-highlight">Python</span></div>
                            <div>🔹 <span class="tech-highlight">JavaScript</span></div>
                        </div>
                    </span>
                </div>
            </div>
            
        </div>
    </div>

    <div class="global-footer-bar">حقوق النشر محفوظة برمجياً وتعود إلى المسؤول البراوي بتاريخ 2026 ©</div>

    <script>
        function toggleSidebarMenu(openState) {
            const sidebar = document.getElementById("slidingSidebarMenu");
            if (sidebar) {
                if(openState) sidebar.classList.add("active");
                else sidebar.classList.remove("active");
            }
        }

        function toggleGamesDropdown() {
            const panel = document.getElementById("gamesDropdownPanel");
            panel.style.display = (panel.style.display === "flex") ? "none" : "flex";
        }
    </script>
</body>
</html>
"""
    return render_template_string(HOME_HTML)

import os
from flask import Blueprint, render_template_string, current_app

projects_blueprint = Blueprint('projects', __name__)

# عزل التنسيقات السيبرانية لحماية بايثون من التعارض النصي للأقواس خارج الصندوق في خوادم فيرسيل
PROJECTS_TERMINAL_CSS = """
<style>
    :root {
        --bg-global: #020406; --text-main: #3fb950; --bg-card: rgba(6, 10, 15, 0.92); 
        --border-main: #1f883d; --border-neon: #a371f7; --border-cyber: #00f0f0; --text-white: #fff; --border-sub: #161b22;
    }
    body { font-family: 'Courier New', Courier, monospace; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; overflow-x: hidden; position: relative; }
    body::before { content: ''; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 255, 0, 0.03)); background-size: 100% 4px, 6px 100%; z-index: 2; pointer-events: none; }
    .cyber-grid-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(rgba(31, 136, 61, 0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(31, 136, 61, 0.05) 1px, transparent 1px); background-size: 20px 20px; z-index: 1; pointer-events: none; }
    
    .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 1200px; margin: 0 auto 30px auto; border-bottom: 2px solid var(--border-main); padding-bottom: 14px; box-sizing: border-box; position: relative; z-index: 1000; }
    .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 10px var(--border-neon), 0 0 20px var(--border-cyber); text-decoration: none; font-family: monospace; letter-spacing: 2px; }
    .menu-btn-trigger { background: var(--bg-card); border: 1px solid var(--border-main); color: var(--border-neon); padding: 8px 18px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 14px; display: flex; align-items: center; gap: 6px; font-family: inherit; box-shadow: 0 0 10px rgba(163,113,247,0.15); }
    
    .main-container { flex: 1; display: flex; flex-direction: column; align-items: center; width: 100%; max-width: 1200px; margin: 0 auto; position: relative; z-index: 10; }
    .proj-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; width: 100%; text-align: right; direction: rtl; }
    
    /* 🛸 هندسة "الكرت الدوار الذكي العائم" المتجاوب للمشاريع الهندسية لعام 2026 */
    .proj-card { 
        background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 12px; padding: 25px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-top: 4px solid var(--border-neon); border-left: 4px solid var(--border-cyber); 
        display: flex; flex-direction: column; gap: 12px; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
        animation: cyberFloat 4s ease-in-out infinite alternate; transition: transform 0.3s, box-shadow 0.3s;
        clip-path: polygon(0 0, 96% 0, 100% 5%, 100% 100%, 4% 100%, 0 95%);
    }
    .proj-card:hover { transform: translateY(-6px) scale(1.01) rotate(0.5deg); border-color: var(--border-cyber); box-shadow: 0 0 20px rgba(0,240,240,0.2); }
    @keyframes cyberFloat { 0% { transform: translateY(0px); } 100% { transform: translateY(-8px); } }
    
    .proj-title { font-size: 17px; font-weight: bold; color: var(--text-white); margin: 0; text-shadow: 0 0 5px rgba(255,255,255,0.2); }
    .proj-desc { font-size: 13.5px; color: var(--text-main); line-height: 1.6; margin: 0; }
    .global-footer-bar { width: 100%; text-align: center; padding: 20px 0; border-top: 1px solid var(--border-main); font-size: 11.5px; color: var(--text-main); font-family: monospace; position: relative; z-index: 100; margin-top: auto; letter-spacing: 1px; }

    /* 🕹️ حقن وتثبيت تصميم ومقاييس الستارة الجانبية المنبثقة دائرياً الموحدة في نفس الملف لمنع الـ 404 */
    .sidebar-overlay { 
        position: fixed !important; top: 0 !important; right: 0 !important; 
        width: 320px !important; height: 100vh !important; 
        background: rgba(4, 6, 9, 0.98) !important; border-left: 2px solid var(--border-cyber) !important; 
        box-shadow: -25px 0 50px #000 !important; z-index: 99999999 !important; 
        display: flex !important; flex-direction: column !important; 
        padding: 30px 25px !important; box-sizing: border-box !important; 
        text-align: right !important; direction: rtl !important;
        clip-path: circle(0% at 100% 0%); transition: clip-path 0.45s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .sidebar-overlay.active { clip-path: circle(150% at 100% 0%) !important; }
    .close-menu-btn { background: #000; border: 1px solid var(--border-cyber); color: var(--border-cyber); font-size: 13px; font-weight: bold; cursor: pointer; display: flex; align-items: center; gap: 6px; padding: 7px 14px; border-radius: 4px; align-self: flex-start; margin-bottom: 25px; font-family: inherit; box-shadow: 0 0 10px rgba(255,0,127,0.15); }
    .close-menu-btn:hover { background: var(--border-cyber); color: #fff; box-shadow: 0 0 15px var(--border-cyber); }
    .sidebar-links-wrapper { display: flex; flex-direction: column; text-align: right; gap: 4px; }
    .section-menu-divider { font-size: 14px; font-weight: bold; display: flex; align-items: center; gap: 8px; justify-content: flex-start; margin-top: 15px; margin-bottom: 8px; border-bottom: 1px dashed var(--border-main); padding-bottom: 6px; color: #8b949e; letter-spacing: 0.5px; }
    .dropdown-trigger-btn { background: none; border: none; font-size: 15.5px; font-weight: bold; width: 100%; padding: 10px 0; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit; color: var(--border-neon); text-shadow: 0 0 6px rgba(163,113,247,0.2); }
    .dropdown-content-panel { display: none; background: #000; border: 1px solid var(--border-main); border-radius: 4px; padding: 4px 12px; margin-bottom: 10px; flex-direction: column; }
    .game-link-btn { text-decoration: none; font-size: 14px; font-family: inherit; padding: 9px 0; display: block; width: 100%; text-align: right; font-weight: 500; border-bottom: 1px dashed #161b22; }
    .game-link-btn:last-child { border-bottom: none; }
    .general-link-item { text-decoration: none; font-size: 15.5px; font-weight: bold; padding: 11px 0; display: block; font-family: inherit; color: var(--text-main); }
    .general-link-item:hover { color: var(--text-white); text-shadow: 0 0 10px var(--border-neon); padding-right: 4px; }
    @media (max-width: 850px) { body { padding: 15px; } .top-nav { max-width: 100%; } .proj-grid { grid-template-columns: 1fr; } .proj-card { clip-path: none !important; } }
</style>
"""
def get_embedded_games_html():
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
                    if len(lines) >= 3:
                        game_name = lines[0]
                        game_icon = lines[1]
                        game_color = lines[2]
                        node_html = f'<a href="/{game_slug}" class="game-link-btn" style="color: {game_color};"><i class="{game_icon}"></i> {game_name}</a>'
                        games_list_nodes.append(node_html)
    except Exception: pass
    return "".join(games_list_nodes) if games_list_nodes else '<p style="color:#1f883d; font-size:12px;">قائمة الألعاب فارغة.</p>'

@projects_blueprint.route('/projects')
def projects_page():
    dynamic_games_html = get_embedded_games_html()
    dynamic_projects_html = ""
    try:
        proj_dir = os.path.join(current_app.root_path, 'static', 'my_projects')
        if os.path.exists(proj_dir):
            for filename in sorted(os.listdir(proj_dir)):
                if filename.endswith('.txt'):
                    file_path = os.path.join(proj_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        raw_lines = f.readlines()
                    
                    # ✅ التطهير البرمجي وقفل الفهارس النصية صراحة لمنع وعزل شاشات الـ 500 حياً للابد
                    lines = [str(line).replace('\\n', '').replace('\\r', '').strip() for line in raw_lines if line.strip()]
                    if len(lines) >= 2:
                        p_title = lines[0]
                        p_desc = lines[1]
                        dynamic_projects_html += f'''
                        <div class="proj-card">
                            <div class="proj-title"><i class="fas fa-drafting-table" style="color:var(--border-cyber); margin-left:6px;"></i> {p_title}</div>
                            <p class="proj-desc">{p_desc}</p>
                        </div>
                        '''
    except Exception: pass

    if not dynamic_projects_html:
        dynamic_projects_html = '<p style="color:#1f883d; text-align:center; grid-column: 1/-1;">لا توجد مشاريع هندسية مرفوعة حالياً.</p>'

    PROJECTS_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>معرض المشاريع الهندسية | Albrawe</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    """ + PROJECTS_TERMINAL_CSS + """
</head>
<body>
    <div class="cyber-grid-overlay"></div>

    <div class="top-nav">
        <a href="/" class="brand-logo">> ALBRAWE_</a>
        <button class="menu-btn-trigger" onclick="toggleSidebarMenu(true)"><i class="fas fa-terminal"></i> CORE_MENU_</button>
    </div>

    <!-- الستارة الجانبية الموحدة المدمجة صراحة من الزاوية لمنع التضارب والـ 404 كلياً -->
    <div class="sidebar-overlay" id="slidingSidebarMenu">
        <button class="close-menu-btn" onclick="toggleSidebarMenu(false)"><i class="fas fa-times"></i> CLOSE_STREAM_</button>
        <div class="sidebar-links-wrapper">
            <a href="/" class="general-link-item">> البوابة الرئيسية 🏠</a>
            <button class="dropdown-trigger-btn" onclick="toggleGamesDropdown()">
                <span>> قائمة ألعاب النظام 🎮</span>
                <i class="fas fa-chevron-down arrow-icon"></i>
            </button>
            <div class="dropdown-content-panel" id="gamesDropdownPanel">
                """ + dynamic_games_html + """
            </div>
            <div class="section-menu-divider">SYS_ROUTING_UNITS</div>
            <a href="/projects" class="general-link-item">> معرض المشاريع 📁</a>
            <a href="/about" class="general-link-item">> الهوية الرقمية 👤</a>
            <a href="/scripts" class="general-link-item">> إسكربتات بايثون 💻</a>
            <a href="/report" class="general-link-item" style="color:var(--border-cyber);">> الإبلاغ عن مشكلة (صيانة) 🛠️</a>
            <a href="https://t.me" target="_blank" class="general-link-item" style="color:#388bfd;">> حسابي في التليجرام ✈️</a>
        </div>
    </div>

    <div class="main-container">
        <div class="proj-grid">
            """ + dynamic_projects_html + """
        </div>
    </div>
    <div class="global-footer-bar">حقوق النشر محفوظة سيبرانياً وتعود إلى المسؤول البراوي بتاريخ 2026 © [STABLE_BUILD]</div>

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
    return render_template_string(PROJECTS_HTML)

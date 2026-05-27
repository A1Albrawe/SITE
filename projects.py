import os
from flask import Blueprint, render_template_string, current_app

projects_blueprint = Blueprint('projects', __name__)

PROJECTS_CSS = """
<style>
    :root { --bg-global: #030508; --text-main: #c9d1d9; --bg-card: rgba(13, 17, 23, 0.8); --border-main: #21262d; --border-neon: #a371f7; --border-cyber: #00f0f0; --text-white: #fff; --border-sub: #30363d; }
    body { font-family: 'Courier New', monospace; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; overflow-x: hidden; position: relative; }
    
    /* 🪐 حقن وحياكة كتل رادار الفضاء العسكري الخلفي الدائم الحركة */
    .radar-background-grid { position: fixed; top: 50%; left: 50%; width: 140vw; height: 140vw; transform: translate(-50%, -50%); border-radius: 50%; border: 1px solid rgba(163, 113, 247, 0.1); pointer-events: none; z-index: 1; animation: radarRotate 25s linear infinite; }
    @keyframes radarRotate { 0% { transform: translate(-50%, -50%) rotate(0deg); } 100% { transform: translate(-50%, -50%) rotate(360deg); } }

    .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 1100px; margin: 0 auto 35px auto; border-bottom: 2px solid var(--border-sub); padding-bottom: 14px; box-sizing: border-box; position: relative; z-index: 100; }
    .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 10px var(--border-neon); text-decoration: none; font-family: monospace; }
    .menu-btn-trigger { background: #161b22; border: 1px solid var(--border-sub); color: var(--border-neon); padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; font-family: inherit; }
    
    .main-container { flex: 1; display: flex; flex-direction: column; align-items: center; width: 100%; max-width: 1100px; margin: 0 auto; position: relative; z-index: 10; }
    .proj-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; width: 100%; text-align: right; }
    
    /* 🛸 هندسة "الكرت الدوار الذكي العائم" (Floating & Rotating Cyber Cards) */
    .proj-card { 
        background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 14px; padding: 25px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.5); border-top: 4px solid var(--border-neon); border-left: 4px solid var(--border-cyber); 
        display: flex; flex-direction: column; gap: 12px; backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
        
        /* حركة الطفو العمودي والاهتزاز الهادئ للكرت الكوني */
        animation: cyberFloat 4s ease-in-out infinite alternate;
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s;
    }
    .proj-card:nth-child(even) { animation-delay: 2s; }
    .proj-card:hover { transform: translateY(-8px) scale(1.02) rotate(1deg); border-color: var(--border-cyber); box-shadow: 0 0 20px rgba(0,240,240,0.2); }
    
    @keyframes cyberFloat { 0% { transform: translateY(0px); } 100% { transform: translateY(-10px); } }
    
    .proj-title { font-size: 17px; font-weight: bold; color: var(--text-white); margin: 0; text-shadow: 0 0 6px rgba(255,255,255,0.1); }
    .proj-desc { font-size: 13.5px; color: var(--text-main); line-height: 1.6; margin: 0; }
    .global-footer-bar { width: 100%; text-align: center; margin-top: 40px; padding-top: 15px; border-top: 1px solid var(--border-sub); font-size: 12px; color: #8b949e; font-family: monospace; position: relative; z-index: 100; }
</style>
"""

@projects_blueprint.route('/projects')
def projects_page():
    dynamic_projects_html = ""
    try:
        proj_dir = os.path.join(current_app.root_path, 'static', 'my_projects')
        if os.path.exists(proj_dir):
            for filename in sorted(os.listdir(proj_dir)):
                if filename.endswith('.txt'):
                    file_path = os.path.join(proj_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = [line.replace('\\n', '').replace('\\r', '').strip() for line in f.readlines() if line.strip()]
                    if len(lines) >= 2:
                        p_title = lines[0]
                        p_desc = lines[1]
                        dynamic_projects_html += f'''
                        <div class="proj-card">
                            <div class="proj-title"><i class="fas fa-drafting-table" style="color:var(--border-neon); margin-left:6px;"></i> {p_title}</div>
                            <p class="proj-desc">{p_desc}</p>
                        </div>
                        '''
    except Exception:
        dynamic_projects_html = '<p style="color:#8b949e;">خطأ فني في جلب مستودع المشاريع الهندسية.</p>'

    if not dynamic_projects_html:
        dynamic_projects_html = '<p style="color:#8b949e; text-align:center; grid-column: 1/-1;">لا توجد مشاريع مرفوعة في المستودع حالياً.</p>'

    PROJECTS_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>معرض المشاريع الهندسية | Albrawe</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    """ + PROJECTS_CSS + """
</head>
<body>
    <div class="radar-background-grid"></div>
    <div class="top-nav">
        <a href="/" class="brand-logo">Albrawe</a>
        <button class="menu-btn-trigger" onclick="loadAndOpenSidebarMenu()"><i class="fas fa-bars"></i> القائمة</button>
    </div>
    <div id="dynamicMenuInjectionZone"></div>
    <div class="main-container">
        <div class="proj-grid">
            """ + dynamic_projects_html + """
        </div>
    </div>
    <div class="global-footer-bar">حقوق النشر محفوظة برمجياً وتعود إلى المسؤول البراوي بتاريخ 2026 ©</div>
    <script>
        function loadAndOpenSidebarMenu() {
            const zone = document.getElementById("dynamicMenuInjectionZone");
            if (zone.innerHTML.trim() !== "") { toggleSidebarMenu(true); return; }
            fetch('/api/get_sidebar_menu').then(res => res.json()).then(data => {
                const styleNode = document.createElement("style"); styleNode.innerHTML = data.css; document.head.appendChild(styleNode);
                zone.innerHTML = data.html; setTimeout(() => { toggleSidebarMenu(true); }, 30);
            });
        }
        function toggleSidebarMenu(openState) { const sidebar = document.getElementById("slidingSidebarMenu"); if(sidebar) { if(openState) sidebar.classList.add("active"); else sidebar.classList.remove("active"); } }
        function toggleGamesDropdown() { const trigger = document.getElementById("gamesMenuTrigger"); const panel = document.getElementById("gamesDropdownPanel"); if(panel.style.display === "flex") { panel.style.display = "none"; trigger.classList.remove("open-state"); } else { panel.style.display = "flex"; trigger.classList.add("open-state"); } }
    </script>
</body>
</html>
"""
    return render_template_string(PROJECTS_HTML)

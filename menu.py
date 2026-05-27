import os
from flask import Blueprint, current_app, jsonify

menu_blueprint = Blueprint('menu', __name__)

@menu_blueprint.route('/api/get_sidebar_menu')
def get_sidebar_menu():
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
                        lines = [line.replace('\\n', '').replace('\\r', '').strip() for line in raw_lines if line.strip()]
                        
                    game_name = lines[0] if len(lines) > 0 else game_slug
                    game_icon = lines[1] if len(lines) > 1 else "fas fa-gamepad"
                    game_color = lines[2] if len(lines) > 2 else "#fff"
                    
                    node_html = f'<a href="/{game_slug}" class="game-link-btn" style="color: {game_color};"><i class="{game_icon}"></i> {game_name}</a>'
                    games_list_nodes.append(node_html)
    except Exception:
        games_list_nodes = ['<p style="color:#8b949e; font-size:12px; padding:8px 0;">خطأ في مواءمة مسارات الألعاب.</p>']

    dynamic_games_html = "".join(games_list_nodes) if games_list_nodes else '<p style="color:#8b949e; font-size:12px; padding:8px 0;">لا توجد ألعاب مكتشفة حالياً.</p>'

    # 🕹️ الهيكل الصافي للستارة الجانبية الموحدة
    MENU_CANVAS_BODY = """
    <div class="sidebar-overlay" id="slidingSidebarMenu">
        <button class="close-menu-btn" onclick="toggleSidebarMenu(false)"><i class="fas fa-times"></i> إغلاق القائمة</button>
        
        <div class="sidebar-links-wrapper">
            <a href="/" class="general-link-item" style="color:#fff;">البوابة الرئيسية 🏠</a>
            
            <button class="dropdown-trigger-btn" id="gamesMenuTrigger" onclick="toggleGamesDropdown()">
                <span><i class="fas fa-gamepad" style="margin-left:5px;"></i> قائمة ألعاب النظام</span>
                <i class="fas fa-chevron-down arrow-icon"></i>
            </button>
            <div class="dropdown-content-panel" id="gamesDropdownPanel">
                """ + dynamic_games_html + """
            </div>
            
            <div class="section-menu-divider"><i class="fas fa-folder-open"></i> مسارات إضافية</div>
            <a href="/projects" class="general-link-item">معرض المشاريع 📁</a>
            <a href="/scripts" class="general-link-item">إسكربتات بايثون 💻</a>
            <a href="/report" class="general-link-item" style="color:#ff7b72;">الإبلاغ عن مشكلة (صيانة) 🛠️</a>
            <a href="https://t.me" target="_blank" class="general-link-item" style="color:#388bfd; border-bottom:none;">حسابي في التليجرام ✈️</a>
        </div>
        
        <div class="theme-toggle-container">
            <button class="theme-toggle-btn" onclick="toggleGlobalThemeMode()">
                <i class="fas fa-adjust"></i> <span id="themeToggleTextBtn">الوضع الفاتح ⚪</span>
            </button>
        </div>
    </div>
    """
    return jsonify({"html": MENU_CANVAS_BODY})

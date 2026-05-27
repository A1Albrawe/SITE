import os
from flask import Blueprint, render_template_string, current_app, jsonify

menu_blueprint = Blueprint('menu', __name__)

# عزل التنسيقات في كتل نصية مضغوطة ومحمية 100% لمنع وميض انهيار السيرفر السحابي
MENU_CSS = """
<style>
    body { font-family: 'Courier New', Courier, monospace; background: #06090d; color: #c9d1d9; margin: 0; padding: 0; box-sizing: border-box; display: flex; justify-content: flex-start; min-height: 100vh; overflow-x: hidden; }
    
    /* 🕹️ المعمارية الطولية الجانبية الفخمة المثبتة صراحة بأقصى يمين الشاشة لتطابق صورتك بالملي */
    .sidebar-container { position: absolute; right: 0; top: 0; width: 100%; max-width: 320px; height: 100vh; background: #0b0f17; border-left: 2px solid #58a6ff; box-shadow: -15px 0 35px rgba(0, 0, 0, 0.8); display: flex; flex-direction: column; padding: 30px 25px; box-sizing: border-box; text-align: right; }
    
    /* زر الإغلاق الأحمر التفاعلي الفاخر X المثبت بأعلى يسار لوحة الستارة */
    .close-menu-link { background: none; border: none; color: #f85149; font-size: 16px; font-weight: bold; cursor: pointer; display: flex; align-items: center; gap: 8px; align-self: flex-start; margin-bottom: 35px; font-family: inherit; text-decoration: none; padding: 4px; }
    .close-menu-link:hover { text-shadow: 0 0 10px #f85149; }
    
    .sidebar-links-wrapper { display: flex; flex-direction: column; text-align: right; gap: 6px; }
    
    /* 📦 هندسة زر المنسدل التفاعلي الفاخر لباقة الألعاب المكتشفة تلقائياً */
    .dropdown-trigger-btn { background: #161b22; border: 1px solid #30363d; color: #3fb950; font-size: 15px; font-weight: bold; width: 100%; padding: 10px 0; border-radius: 0; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit; margin: 5px 0; transition: 0.2s; background: none; border: none; text-shadow: 0 0 4px rgba(63,185,80,0.2); }
    .dropdown-trigger-btn:hover { text-shadow: 0 0 12px #3fb950; }
    .dropdown-trigger-btn i.arrow-icon { transition: transform 0.3s ease; font-size: 12px; margin-right: auto; padding-left: 5px; }
    .dropdown-trigger-btn.open-state i.arrow-icon { transform: rotate(180deg); }
    
    /* لوحة المنسدل الداخلي المنساب للألعاب */
    .dropdown-content-panel { display: none; background: #090d12; border: 1px solid #21262d; border-radius: 8px; padding: 4px 12px; margin-bottom: 10px; flex-direction: column; }
    
    .game-link-btn { text-decoration: none; font-size: 14px; font-family: inherit; padding: 9px 0; display: block; transition: 0.15s ease; width: 100%; text-align: right; font-weight: 500; border-bottom: 1px dashed #161b22; }
    .game-link-btn:last-child { border-bottom: none; }
    .game-link-btn:hover { padding-right: 6px; text-shadow: 0 0 10px currentColor; }
    /* روابط القائمة الملونة المضيئة بالملي تكتيكياً وصيانة التناسق البصري الكلي */
    .general-link-item { text-decoration: none; font-size: 15px; font-weight: bold; padding: 10px 0; display: block; transition: 0.2s; font-family: inherit; }
    
    .link-home { color: #8b949e; }
    .link-home:hover { color: #fff; text-shadow: 0 0 8px #fff; }
    
    .link-projects { color: #a371f7; text-shadow: 0 0 4px rgba(163,113,247,0.2); }
    .link-projects:hover { text-shadow: 0 0 12px #a371f7; }
    
    .link-about { color: #ff7b72; text-shadow: 0 0 4px rgba(255,123,114,0.2); }
    .link-about:hover { text-shadow: 0 0 12px #ff7b72; }
    
    .link-scripts { color: #58a6ff; text-shadow: 0 0 4px rgba(88,166,255,0.2); }
    .link-scripts:hover { text-shadow: 0 0 12px #58a6ff; }
    
    .link-report { color: #ff5555; text-shadow: 0 0 4px rgba(255,85,85,0.2); }
    .link-report:hover { text-shadow: 0 0 12px #ff5555; }
    
    .link-telegram { color: #388bfd; text-shadow: 0 0 4px rgba(56,139,253,0.2); }
    .link-telegram:hover { text-shadow: 0 0 12px #388bfd; }
</style>
"""
@menu_blueprint.route('/menu')
def menu_page():
    # 🧠 تفعيل محرك التوليد التلقائي لـ الألعاب المبرأة تماماً من الـ n\ لتسليط الألوان حياً داخل المنسدل
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
                        
                    game_name = lines if len(lines) > 0 else game_slug
                    game_icon = lines if len(lines) > 1 else "fas fa-gamepad"
                    game_color = lines if len(lines) > 2 else "#fff"
                    
                    node_html = f'<a href="/{game_slug}" class="game-link-btn" style="color: {game_color};"><i class="{game_icon}"></i> {game_name}</a>'
                    games_list_nodes.append(node_html)
    except Exception:
        games_list_nodes = ['<p style="color:#8b949e; font-size:12px; padding:8px 0;">خطأ في مواءمة مسارات الألعاب التلقائية.</p>']

    dynamic_games_html = "".join(games_list_nodes) if games_list_nodes else '<p style="color:#8b949e; font-size:12px; padding:8px 0;">قائمة النظام التلقائية فارغة حالياً.</p>'

    MENU_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>قائمة النظام الموحدة | Albrawe</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    """ + MENU_CSS + """
</head>
<body>

    <div class="sidebar-container">
        <a href="/" class="close-menu-link"><i class="fas fa-times"></i> إغلاق القائمة</a>
        
        <div class="sidebar-links-wrapper">
            <!-- 1️⃣ البوابة الرئيسية يفتح الهوم الصافي -->
            <a href="/" class="general-link-item link-home">البوابة الرئيسية</a>
            
            <!-- 2️⃣ خانة المنسدل التفاعلي الفاخر لألعاب النظام المكتشفة حياً ومطهرة 100% -->
            <button class="dropdown-trigger-btn" id="gamesMenuTrigger" onclick="toggleGamesDropdown()">
                <span>قائمة ألعاب النظام 🎮</span>
                <i class="fas fa-chevron-down arrow-icon"></i>
            </button>
            <div class="dropdown-content-panel" id="gamesDropdownPanel">
                """ + dynamic_games_html + """
            </div>
            
            <!-- 3️⃣ معرض المشاريع -->
            <a href="/projects" class="general-link-item link-projects">معرض المشاريع</a>
            
            <!-- 4️⃣ نبذة عن هويتك المعمارية والبرمجية -->
            <a href="/about" class="general-link-item link-about">(About us)</a>
            
            <!-- 5️⃣ اسكريبتات بايثون -->
            <a href="/scripts" class="general-link-item link-scripts">إسكربتات بايثون</a>
            
            <!-- 6️⃣ الإبلاغ عن مشكلة صيانة المميز الهوية -->
            <a href="/report" class="general-link-item link-report">الإبلاغ عن مشكلة (صيانة)</a>
            
            <!-- 7️⃣ حساب التليجرام القياسي -->
            <a href="https://t.me" target="_blank" class="general-link-item link-telegram">حسابي في التليجرام</a>
        </div>
    </div>

    <script>
        // سكريبت تشغيل وفتح المنسدل للألعاب المستكشفة تلقائياً بنعومة وانسيابية تامة
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
    return render_template_string(MENU_HTML)

from flask import Blueprint, render_template_string

menu_blueprint = Blueprint('menu', __name__)

# 🎨 استنساخ ومطابقة الألوان والخطوط الفلورسنتية للأزرار بدقة كما في صورتك تماماً حياً
MENU_CSS = """
<style>
    body { font-family: 'Courier New', Courier, monospace; background: #06090d; color: #c9d1d9; margin: 0; padding: 0; box-sizing: border-box; display: flex; justify-content: flex-end; min-height: 100vh; overflow-x: hidden; }
    
    /* 🕹️ المعمارية الطولية الجانبية الفخمة لتطابق لقطة الشاشة تماماً بالبكسل */
    .sidebar-container { width: 100%; max-width: 320px; height: 100vh; background: #0b0f17; border-left: 2px solid #58a6ff; box-shadow: -15px 0 35px rgba(0, 0, 0, 0.8); display: flex; flex-direction: column; padding: 30px 25px; box-sizing: border-box; text-align: right; }
    
    /* زر الإغلاق الأحمر المميز X المثبت بأعلى اليسار */
    .close-menu-link { background: none; border: none; color: #f85149; font-size: 16px; font-weight: bold; cursor: pointer; display: flex; align-items: center; gap: 8px; align-self: flex-end; margin-bottom: 35px; font-family: inherit; text-decoration: none; padding: 4px; }
    .close-menu-link:hover { text-shadow: 0 0 10px #f85149; }
    
    .sidebar-links-wrapper { display: flex; flex-direction: column; text-align: right; gap: 12px; }
    .section-menu-divider { font-size: 15px; font-weight: bold; display: flex; align-items: center; gap: 8px; justify-content: flex-start; margin-top: 15px; margin-bottom: 5px; border-bottom: 1px dashed #21262d; padding-bottom: 6px; color: #8b949e; }
    
    /* روابط القائمة الملونة المضيئة بالملي */
    .general-link-item { text-decoration: none; font-size: 15px; font-weight: bold; padding: 8px 0; display: block; transition: 0.2s; font-family: inherit; }
    
    .link-home { color: #8b949e; }
    .link-home:hover { color: #fff; text-shadow: 0 0 8px #fff; }
    
    .link-arcade { color: #3fb950; text-shadow: 0 0 4px rgba(63,185,80,0.2); }
    .link-arcade:hover { text-shadow: 0 0 12px #3fb950; }
    
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

    <!-- العلبة الجانبية الطولية السوداء المستنسخة من صورتك بالملي -->
    <div class="sidebar-container">
        <!-- عند الضغط على إغلاق يعود بالزائر فوراً إلى صفحة الهوم الرئيسية بسلاسة -->
        <a href="/" class="close-menu-link">إغلاق القائمة <i class="fas fa-times"></i></a>
        
        <div class="sidebar-links-wrapper">
            <a href="/" class="general-link-item link-home">البوابة الرئيسية</a>
            
            <div class="section-menu-divider">قائمة ألعاب النظام 🎮</div>
            <a href="/card_game" class="general-link-item link-arcade">مطابقة الكروت</a>
            <a href="/clicker" class="general-link-item link-arcade">الضغط السريع</a>
            <a href="/shooter" class="general-link-item link-arcade">سفينة الفضاء</a>
            <a href="/snake" class="general-link-item link-arcade">لعبة الثعبان</a>
            <a href="/tetris" class="general-link-item link-arcade">tetris</a>
            <a href="/xo" class="general-link-item link-arcade">X-O</a>
            
            <div class="section-menu-divider">مسارات إضافية</div>
            <a href="/projects" class="general-link-item link-projects">معرض المشاريع</a>
            <a href="/about" class="general-link-item link-about">(About us)</a>
            <a href="/scripts" class="general-link-item link-scripts">إسكربتات بايثون</a>
            <a href="/report" class="general-link-item link-report">الإبلاغ عن مشكلة (صيانة)</a>
            <a href="https://t.me" target="_blank" class="general-link-item link-telegram">حسابي في التليجرام</a>
        </div>
    </div>

</body>
</html>
"""

@menu_blueprint.route('/menu')
def menu_page():
    return render_template_string(MENU_HTML)

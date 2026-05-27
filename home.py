from flask import Blueprint, render_template_string

home_blueprint = Blueprint('home', __name__)

HOME_CSS = """
<style>
    body { font-family: 'Courier New', Courier, monospace; background: #06090d; color: #c9d1d9; margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; overflow-x: hidden; }
    
    .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 1200px; margin: 0 auto 35px auto; border-bottom: 2px solid #21262d; padding-bottom: 14px; box-sizing: border-box; }
    .brand-logo { font-size: 24px; font-weight: bold; color: #fff; text-shadow: 0 0 8px #58a6ff; font-family: monospace; text-decoration: none; cursor: pointer; }
    .menu-btn-link { background: #161b22; border: 1px solid #30363d; color: #58a6ff; padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; display: flex; align-items: center; gap: 6px; font-family: inherit; text-decoration: none; }
    .menu-btn-link:hover { background: #58a6ff; color: #06090d; box-shadow: 0 0 12px #58a6ff; }
    
    .main-container { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; }
    .responsive-profile-wrapper { display: flex; flex-direction: row; gap: 40px; width: 100%; max-width: 1200px; background: #0d1117; border: 1px solid #30363d; border-radius: 18px; padding: 45px; box-shadow: 0 30px 60px rgba(0,0,0,0.4); border-bottom: 4px solid #58a6ff; box-sizing: border-box; align-items: center; direction: rtl; }
    
    .profile-sidebar-zone { flex: 1; max-width: 280px; display: flex; flex-direction: column; align-items: center; text-align: center; border-left: 2px solid #21262d; padding-left: 30px; box-sizing: border-box; }
    .profile-content-zone { flex: 2; display: flex; flex-direction: column; justify-content: center; text-align: right; box-sizing: border-box; padding-right: 10px; }
    .avatar-wrapper { width: 145px; height: 145px; border-radius: 16px; border: 2px solid #58a6ff; overflow: hidden; box-shadow: 0 0 20px rgba(88,166,255,0.2); margin-bottom: 20px; display: flex; align-items: center; justify-content: center; background: #04060a; }
    .avatar-img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .profile-name { font-size: 28px; font-weight: bold; color: #fff; margin: 0 0 8px 0; }
    .profile-title { font-size: 11.5px; font-weight: bold; color: #58a6ff; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; }
    .details-sub-box { display: flex; flex-direction: column; gap: 16px; font-size: 14.5px; line-height: 1.65; }
    .tech-highlight { color: #58a6ff; font-weight: bold; font-family: monospace; }
    .global-footer-bar { width: 100%; text-align: center; margin-top: 40px; padding-top: 15px; border-top: 1px solid #21262d; font-size: 12px; color: #8b949e; font-family: monospace; }
    
    @media (max-width: 850px) {
        body { padding: 15px; } .top-nav { max-width: 100%; } .responsive-profile-wrapper { flex-direction: column; align-items: center; padding: 25px; max-width: 440px; }
        .profile-sidebar-zone { flex: none; width: 100%; max-width: 100%; border-left: none; border-bottom: 2px solid #21262d; padding-left: 0; padding-bottom: 25px; margin-bottom: 20px; }
        .profile-content-zone { width: 100%; padding-right: 0; }
    }
</style>
"""

HOME_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Albrawe | البوابة الرسمية الموحدة</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    """ + HOME_CSS + """
</head>
<body>

    <div class="top-nav">
        <a href="/" class="brand-logo">Albrawe</a>
        <!-- التوجيه الصريح المباشر والأصح برمجياً لفتح صفحة المنيو المستقلة الملونة -->
        <a href="/menu" class="menu-btn-link"><i class="fas fa-bars"></i> القائمة</a>
    </div>

    <div class="main-container">
        <div class="responsive-profile-wrapper">
            <div class="profile-sidebar-zone">
                <div class="avatar-wrapper">
                    <img class="avatar-img" src="/static/avatar.png" alt="Albrawe Profile" onerror="this.src='https://flagcdn.com'">
                </div>
                <h1 class="profile-name">Albrawe</h1>
                <div class="profile-title">Architecture & Software Engineer</div>
            </div>
            
            <div class="profile-content-zone">
                <div class="details-sub-box">
                    <span class="meta-item">
                        ⚡ <span class="meta-label">خبراتي:</span> بناء وتطوير تطبيقات الويب الكاملة، وتصميم وتعديل اسكريبتات البايثون. إنشاء وتصميم صفحات الويب المتكاملة، معالجة البيانات المحلية، والواجهات الذكية.
                    </span>
                    <span class="meta-item" style="border-top: 1px dashed #21262d; padding-top: 12px; margin-top: 2px;">
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

</body>
</html>
"""

@home_blueprint.route('/')
def home_page():
    return render_template_string(HOME_HTML)

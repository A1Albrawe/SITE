from flask import Blueprint, render_template_string

home_blueprint = Blueprint('home', __name__)

# حقن التنسيقات الحركية والـ CSS المتجاوب الحاوي لمتغيرات الألوان الثنائية لعام 2026
HOME_CSS = """
<style>
    /* 🌓 معمارية المتغيرات اللونية الحاكمة لقلب الأنماط وانسيابية الألوان */
    :root {
        --bg-global: #06090d;
        --text-main: #c9d1d9;
        --bg-card: #0d1117;
        --border-main: #30363d;
        --border-neon: #58a6ff;
        --text-white: #fff;
        --bg-sub-box: #06090d;
        --border-sub: #21262d;
    }
    
    [data-theme="light"] {
        --bg-global: #f6f8fa;
        --text-main: #24292f;
        --bg-card: #ffffff;
        --border-main: #d0d7de;
        --border-neon: #0969da;
        --text-white: #1f2328;
        --bg-sub-box: #f6f8fa;
        --border-sub: #d0d7de;
    }

    body { font-family: 'Courier New', Courier, monospace; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; overflow-x: hidden; transition: background 0.3s, color 0.3s; }
    
    /* 🌐 شريط الهيدر العلوي القياسي الموحد المبرأ من الانعكاس البصري */
    .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 1200px; margin: 0 auto 35px auto; border-bottom: 2px solid var(--border-sub); padding-bottom: 14px; box-sizing: border-box; }
    .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 8px var(--border-neon); font-family: monospace; text-decoration: none; margin: 0; padding: 0; cursor: pointer; transition: 0.2s; }
    .brand-logo:hover { opacity: 0.8; }
    .menu-btn-trigger { background: var(--bg-card); border: 1px solid var(--border-main); color: var(--border-neon); padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; display: flex; align-items: center; gap: 6px; transition: 0.2s ease; font-family: inherit; margin: 0; }
    .menu-btn-trigger:hover { background: var(--border-neon); color: var(--bg-global); box-shadow: 0 0 12px var(--border-neon); }
    
    .main-container { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; }
    
    /* 💻 الهيكل ثنائي الأجنحة الفخم الممتد لتغطية شاشات الكمبيوتر واللاب توب بالبكسل */
    .responsive-profile-wrapper { display: flex; flex-direction: row; gap: 40px; width: 100%; max-width: 1200px; background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 18px; padding: 45px; box-shadow: 0 30px 60px rgba(0,0,0,0.4); border-bottom: 4px solid var(--border-neon); box-sizing: border-box; align-items: center; direction: rtl; transition: background 0.3s, border 0.3s; }
    
    .profile-sidebar-zone { flex: 1; max-width: 280px; display: flex; flex-direction: column; align-items: center; text-align: center; border-left: 2px solid var(--border-sub); padding-left: 30px; box-sizing: border-box; }
    .profile-content-zone { flex: 2; display: flex; flex-direction: column; justify-content: center; text-align: right; box-sizing: border-box; padding-right: 10px; }
    
    .avatar-wrapper { width: 145px; height: 145px; border-radius: 16px; border: 2px solid var(--border-neon); overflow: hidden; box-shadow: 0 0 20px rgba(88,166,255,0.2); margin-bottom: 20px; display: flex; align-items: center; justify-content: center; background: #04060a; transition: border 0.3s; }
    .avatar-img { width: 100%; height: 100%; object-fit: cover; display: block; }
    
    .profile-name { font-size: 28px; font-weight: bold; color: var(--text-white); margin: 0 0 8px 0; text-shadow: 0 0 5px rgba(255,255,255,0.1); }
    .profile-title { font-size: 11.5px; font-weight: bold; color: var(--border-neon); margin: 0; text-transform: uppercase; letter-spacing: 0.5px; }
    
    .details-sub-box { display: flex; flex-direction: column; gap: 16px; font-size: 14.5px; line-height: 1.65; }
    .meta-item { display: block; color: var(--text-main); }
    .meta-label { font-weight: bold; color: var(--text-white); }
    .tech-highlight { color: var(--border-neon); font-weight: bold; font-family: monospace; }
    
    /* 🔒 الذيل الفوتر الثابت الموحد لحقوق النشر لعام 2026 */
    .global-footer-bar { width: 100%; text-align: center; margin-top: 40px; padding-top: 15px; border-top: 1px solid var(--border-sub); font-size: 12px; color: var(--text-muted, #8b949e); font-family: monospace; transition: border 0.3s; }
    
    @media (max-width: 850px) {
        body { padding: 15px; }
        .top-nav { max-width: 100%; }
        .responsive-profile-wrapper { flex-direction: column; align-items: center; padding: 25px; max-width: 440px; }
        .profile-sidebar-zone { flex: none; width: 100%; max-width: 100%; border-left: none; border-bottom: 2px solid var(--border-sub); padding-left: 0; padding-bottom: 25px; margin-bottom: 20px; }
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
    <link rel="shortcut icon" type="image/x-icon" href="/static/favicon.ico">
    """ + HOME_CSS + """
    <script>
        // 🌓 سكريبت جدار حماية الأنماط اللحظي: يقرأ الكاش فوراً قبل رندر الصفحة لمنع وميض اللون الأبيض
        (function() {
            const savedTheme = localStorage.getItem("albrawe_global_theme_mode") || "dark";
            document.documentElement.setAttribute("data-theme", savedTheme);
        })();
    </script>
</head>
<body>

    <div class="top-nav">
        <!-- الاسم يميناً، يعيد الزائر فوراً للرئيسية عند النقر عليه صيانة للمسارات -->
        <a href="/" class="brand-logo">Albrawe</a>
        <!-- دالة سحب وحقن الستارة الجانبية التلقائية من menu.py حياً وبدون وميض تحميل -->
        <button class="menu-btn-trigger" onclick="loadAndOpenSidebarMenu()"><i class="fas fa-bars"></i> القائمة</button>
    </div>

    <!-- صندوق المطبخ التلقائي لحقن كود الـ Sidebar الجانبي المنفصل حياً بداخل الصفحة -->
    <div id="dynamicMenuInjectionZone"></div>

    <div class="main-container">
        <div class="responsive-profile-wrapper">
            
            <!-- الجناح الأيمن المطور (صورة وشعار الهكر والاسم والمسمى) -->
            <div class="profile-sidebar-zone">
                <div class="avatar-wrapper">
                    <!-- جلب وتأمين صورة الـ Avatar الصافية من جذر مجلد الموارد الثابتة دون أي حجب سحابي -->
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

    <!-- ذيل حقوق النشر الثابت الموحد لعام 2026 لجميع الصفحات -->
    <div class="global-footer-bar">
        حقوق النشر محفوظة برمجياً وتعود إلى المسؤول البراوي بتاريخ 2026 ©
    </div>

    <script>
        // 🚀 خوارزمية الربط المنفصل الذكي: سحب الستارة من menu.py وحقنها وتفعيلها حياً بدون وميض
        function loadAndOpenSidebarMenu() {
            const zone = document.getElementById("dynamicMenuInjectionZone");
            
            if (zone.innerHTML.trim() !== "") {
                toggleSidebarMenu(true);
                updateThemeButtonTextOnSidebar();
                return;
            }
            
            fetch('/api/get_sidebar_menu')
            .then(res => res.json())
            .then(data => {
                const styleNode = document.createElement("style");
                styleNode.innerHTML = data.css;
                document.head.appendChild(styleNode);
                
                zone.innerHTML = data.html;
                updateThemeButtonTextOnSidebar();
                setTimeout(() => { toggleSidebarMenu(true); }, 30);
            }).catch(() => { alert("❌ عطل طارئ: تعذر جلب مستودع الستارة الجانبية الموحدة."); });
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

        // 🌓 محرك قلب وتغيير الألوان المركزي (Dark / Light Theme Toggle Engine) لعام 2026 حياً
        function toggleGlobalThemeMode() {
            const currentTheme = document.documentElement.getAttribute("data-theme") || "dark";
            const newTheme = currentTheme === "dark" ? "light" : "dark";
            
            document.documentElement.setAttribute("data-theme", newTheme);
            localStorage.setItem("albrawe_global_theme_mode", newTheme);
            
            // تحديث الأنماط والمتغيرات داخل حاوية المنيو المنزلقة فوراً حياً
            const sidebar = document.getElementById("slidingSidebarMenu");
            if(sidebar) {
                if(newTheme === "light") {
                    sidebar.style.setProperty("--bg-sidebar", "#ffffff");
                    sidebar.style.setProperty("--border-color", "#d0d7de");
                    sidebar.style.setProperty("--text-muted", "#57606a");
                    sidebar.style.setProperty("--bg-btn", "#f6f8fa");
                    sidebar.style.setProperty("--bg-dropdown", "#f6f8fa");
                    sidebar.style.setProperty("--text-general", "#24292f");
                    sidebar.style.setProperty("--border-dashed", "#d0d7de");
                    sidebar.style.setProperty("--text-home-btn", "#24292f");
                    sidebar.style.setProperty("--text-theme-btn", "#0969da");
                } else {
                    sidebar.style.removeProperty("--bg-sidebar");
                    sidebar.style.removeProperty("--border-color");
                    sidebar.style.removeProperty("--text-muted");
                    sidebar.style.removeProperty("--bg-btn");
                    sidebar.style.removeProperty("--bg-dropdown");
                    sidebar.style.removeProperty("--text-general");
                    sidebar.style.removeProperty("--border-dashed");
                    sidebar.style.removeProperty("--text-home-btn");
                    sidebar.style.removeProperty("--text-theme-btn");
                }
            }
            updateThemeButtonTextOnSidebar();
        }

        function updateThemeButtonTextOnSidebar() {
            const btnText = document.getElementById("themeToggleTextBtn");
            if (btnText) {
                const currentTheme = document.documentElement.getAttribute("data-theme") || "dark";
                btnText.innerText = currentTheme === "dark" ? "الوضع الفاتح ⚪" : "الوضع الداكن ⚫";
            }
        }
    </script>
</body>
</html>
"""

@home_blueprint.route('/')
def home_page():
    return render_template_string(HOME_HTML)

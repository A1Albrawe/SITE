from flask import Blueprint, render_template_string

clicker_blueprint = Blueprint('clicker', __name__)

CLICKER_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>تحدي النقر السريع | Albrawe</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <style>
        :root { --bg-global: #06090d; --text-main: #c9d1d9; --bg-card: #0d1117; --border-main: #30363d; --border-neon: #ffffff; --text-white: #fff; --border-sub: #21262d; }
        [data-theme="light"] { --bg-global: #f6f8fa; --text-main: #24292f; --bg-card: #ffffff; --border-main: #d0d7de; --border-neon: #24292f; --text-white: #1f2328; --border-sub: #d0d7de; }
        body { font-family: 'Courier New', monospace; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; align-items: center; transition: 0.3s; }
        
        .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 500px; margin-bottom: 25px; border-bottom: 2px solid var(--border-sub); padding-bottom: 12px; }
        .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 8px var(--border-neon); text-decoration: none; font-family: monospace; }
        .menu-btn-trigger { background: var(--bg-card); border: 1px solid var(--border-main); color: var(--border-neon); padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; font-family: inherit; }
        
        .game-box { background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 14px; padding: 30px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); border-bottom: 4px solid var(--border-neon); display: flex; flex-direction: column; align-items: center; gap: 20px; width: 100%; max-width: 360px; box-sizing: border-box; }
        .stats-row { display: flex; justify-content: space-between; width: 100%; font-size: 15px; font-weight: bold; color: var(--text-white); font-family: monospace; }
        
        .click-target-btn { width: 140px; height: 140px; border-radius: 50%; background: #161b22; border: 3px solid var(--border-neon); color: var(--text-white); font-size: 18px; font-weight: bold; cursor: pointer; display: flex; align-items: center; justify-content: center; user-select: none; transition: transform 0.05s, box-shadow 0.2s; box-shadow: 0 0 15px rgba(255,255,255,0.05); font-family: inherit; }
        .click-target-btn:active { transform: scale(0.95); box-shadow: 0 0 25px var(--border-neon); }
        .click-target-btn:disabled { opacity: 0.6; cursor: not-allowed; transform: none; box-shadow: none; }
        
        .start-btn { background: var(--bg-global); border: 1px solid var(--border-main); color: var(--text-white); padding: 10px 24px; border-radius: 6px; font-weight: bold; cursor: pointer; font-family: inherit; font-size: 14px; transition: 0.2s; }
        .start-btn:hover { border-color: var(--border-neon); }
        .global-footer-bar { width: 100%; max-width: 500px; text-align: center; margin-top: 30px; padding-top: 15px; border-top: 1px solid var(--border-sub); font-size: 12px; color: var(--text-main); font-family: monospace; }
    </style>
    <script>
        (function() { const savedTheme = localStorage.getItem("albrawe_global_theme_mode") || "dark"; document.documentElement.setAttribute("data-theme", savedTheme); })();
    </script>
</head>
<body>
    <div class="top-nav">
        <a href="/" class="brand-logo">Albrawe</a>
        <button class="menu-btn-trigger" onclick="loadAndOpenSidebarMenu()"><i class="fas fa-bars"></i> القائمة</button>
    </div>
    <div id="dynamicMenuInjectionZone"></div>

    <div class="game-box">
        <div class="stats-row">
            <span>النقاط: <span id="clickCount">0</span></span>
            <span>الوقت: <span id="timerText">10</span>ث</span>
        </div>
        
        <button class="click-target-btn" id="clickerTarget" onclick="registerClick()" disabled>انقر! ⚡</button>
        <button class="start-btn" id="startBtn" onclick="startChallenge()">بدء التحدي 🏁</button>
    </div>

    <div class="global-footer-bar">حقوق النشر محفوظة برمجياً وتعود إلى المسؤول البراوي بتاريخ 2026 ©</div>

    <script>
        let clicks = 0; let timeLeft = 10; let timerInterval = null; let isRunning = false;

        function startChallenge() {
            if(isRunning) return;
            clicks = 0; timeLeft = 10; isRunning = true;
            document.getElementById("clickCount").innerText = clicks;
            document.getElementById("timerText").innerText = timeLeft;
            document.getElementById("clickerTarget").removeAttribute("disabled");
            document.getElementById("startBtn").setAttribute("disabled", "true");
            document.getElementById("startBtn").innerText = "جاري اللعب...";

            timerInterval = setInterval(() => {
                timeLeft--;
                document.getElementById("timerText").innerText = timeLeft;
                if(timeLeft <= 0) {
                    clearInterval(timerInterval); isRunning = false;
                    document.getElementById("clickerTarget").setAttribute("disabled", "true");
                    document.getElementById("startBtn").removeAttribute("disabled");
                    document.getElementById("startBtn").innerText = "إعادة المحاولة 🔄";
                    alert("🏁 انتهى الوقت! إجمالي نقراتك التكتيكية: " + clicks + " نقرة في 10 ثوانٍ!");
                }
            }, 1000);
        }

        function registerClick() { if(isRunning) { clicks++; document.getElementById("clickCount").innerText = clicks; } }

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

@clicker_blueprint.route('/clicker')
def clicker_page():
    return render_template_string(CLICKER_HTML)

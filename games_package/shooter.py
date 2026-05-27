from flask import Blueprint, render_template_string

shooter_blueprint = Blueprint('shooter', __name__)

SHOOTER_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>سفينة الفضاء | Albrawe</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <style>
        :root { --bg-global: #06090d; --text-main: #c9d1d9; --bg-card: #0d1117; --border-main: #30363d; --border-neon: #388bfd; --text-white: #fff; --border-sub: #21262d; }
        [data-theme="light"] { --bg-global: #f6f8fa; --text-main: #24292f; --bg-card: #ffffff; --border-main: #d0d7de; --border-neon: #0969da; --text-white: #1f2328; --border-sub: #d0d7de; }
        body { font-family: 'Courier New', monospace; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; align-items: center; transition: 0.3s; }
        
        .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 500px; margin-bottom: 25px; border-bottom: 2px solid var(--border-sub); padding-bottom: 12px; }
        .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 8px var(--border-neon); text-decoration: none; font-family: monospace; }
        .menu-btn-trigger { background: var(--bg-card); border: 1px solid var(--border-main); color: var(--border-neon); padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; font-family: inherit; }
        
        .game-box { background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 14px; padding: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); border-bottom: 4px solid var(--border-neon); display: flex; flex-direction: column; align-items: center; gap: 15px; width: 100%; max-width: 360px; box-sizing: border-box; }
        canvas { background: #020408; border: 2px solid var(--border-main); border-radius: 8px; display: block; max-width: 100%; }
        .score-board { font-size: 18px; font-weight: bold; color: var(--text-white); font-family: monospace; }
        
        .btn-panel { display: flex; gap: 15px; width: 100%; justify-content: center; margin-top: 5px; }
        .control-btn { background: #161b22; border: 1px solid #30363d; color: #fff; padding: 10px 20px; border-radius: 8px; font-size: 15px; cursor: pointer; flex: 1; }
        .control-btn:active { background: var(--border-neon); color: #000; }
        
        @media (min-width: 850px) { .btn-panel { display: none; } }
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
        <div class="score-board">النقاط الكونية: <span id="shooterScore">0</span></div>
        <canvas id="shooterCanvas" width="300" height="400"></canvas>
        
        <div class="btn-panel">
            <button class="control-btn" onclick="moveShip(-25)"><i class="fas fa-chevron-left"></i> يسار</button>
            <button class="control-btn" onclick="fireLaser()" style="background:var(--border-neon);">إطلاق 🚀</button>
            <button class="control-btn" onclick="moveShip(25)">يمين <i class="fas fa-chevron-right"></i></button>
        </div>
    </div>

    <div class="global-footer-bar">حقوق النشر محفوظة برمجياً وتعود إلى المسؤول البراوي بتاريخ 2026 ©</div>

    <script>
        const canvas = document.getElementById("shooterCanvas");
        const ctx = canvas.getContext("2d");
        let score = 0;

        let ship = { x: 135, y: 360, w: 30, h: 20 };
        let lasers = []; let enemies = [];

        function spawnEnemy() {
            enemies.push({ x: Math.random() * (canvas.width - 20), y: 0, w: 20, h: 20, speed: 2 });
        }
        setInterval(spawnEnemy, 1500);

        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // رسم سفينة الفضاء القياسية المضيئة بالنيون الأزرق
            ctx.fillStyle = "#388bfd"; ctx.shadowBlur = 10; ctx.shadowColor = "#388bfd";
            ctx.fillRect(ship.x, ship.y, ship.w, ship.h);

            // تحديث ورسم الليزرات الفلورسنتية الطائرة
            ctx.fillStyle = "#ff7b72"; ctx.shadowColor = "#ff7b72";
            lasers.forEach((l, lIdx) => {
                l.y -= 5; ctx.fillRect(l.x, l.y, l.w, l.h);
                if(l.y < 0) lasers.splice(lIdx, 1);
            });

            // تحديث الكتل الفضائية المهاجمة حياً
            ctx.fillStyle = "#ffea7f"; ctx.shadowColor = "#ffea7f";
            enemies.forEach((e, eIdx) => {
                e.y += e.speed; ctx.fillRect(e.x, e.y, e.w, e.h);
                
                // رصد ومزامنة حدوث الاصطدام بكتل الليزر
                lasers.forEach((l, lIdx) => {
                    if(l.x < e.x + e.w && l.x + l.w > e.x && l.y < e.y + e.h && l.y + l.h > e.y) {
                        enemies.splice(eIdx, 1); lasers.splice(lIdx, 1);
                        score += 5; document.getElementById("shooterScore").innerText = score;
                    }
                });

                if(e.y > canvas.height) { enemies.splice(eIdx, 1); score = Math.max(0, score - 2); document.getElementById("shooterScore").innerText = score; }
            });
            ctx.shadowBlur = 0; requestAnimationFrame(gameLoop);
        }

        function moveShip(dir) { ship.x = Math.max(0, Math.min(canvas.width - ship.w, ship.x + dir)); }
        function fireLaser() { lasers.push({ x: ship.x + 13, y: ship.y, w: 4, h: 10 }); }

        document.addEventListener("keydown", e => {
            if(e.keyCode === 37) moveShip(-15);
            else if(e.keyCode === 39) moveShip(15);
            else if(e.keyCode === 32) fireLaser();
        });

        gameLoop();

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

@shooter_blueprint.route('/shooter')
def shooter_page():
    return render_template_string(SHOOTER_HTML)

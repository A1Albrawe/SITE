from flask import Blueprint, render_template_string

snake_blueprint = Blueprint('snake', __name__)

SNAKE_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>لعبة الثعبان | Albrawe</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <style>
        :root { --bg-global: #06090d; --text-main: #c9d1d9; --bg-card: #0d1117; --border-main: #30363d; --border-neon: #3fb950; --text-white: #fff; --border-sub: #21262d; }
        [data-theme="light"] { --bg-global: #f6f8fa; --text-main: #24292f; --bg-card: #ffffff; --border-main: #d0d7de; --border-neon: #1f883d; --text-white: #1f2328; --border-sub: #d0d7de; }
        body { font-family: 'Courier New', monospace; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; align-items: center; transition: 0.3s; overflow-x: hidden; }
        
        .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 600px; margin-bottom: 25px; border-bottom: 2px solid var(--border-sub); padding-bottom: 12px; }
        .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 8px var(--border-neon); text-decoration: none; font-family: monospace; }
        .menu-btn-trigger { background: var(--bg-card); border: 1px solid var(--border-main); color: var(--border-neon); padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; font-family: inherit; }
        
        .game-box { background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 14px; padding: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); border-bottom: 4px solid var(--border-neon); display: flex; flex-direction: column; align-items: center; gap: 15px; width: 100%; max-width: 440px; box-sizing: border-box; }
        canvas { background: #04060a; border: 2px solid var(--border-main); border-radius: 8px; box-shadow: inset 0 0 20px rgba(0,0,0,0.8); display: block; max-width: 100%; }
        .score-board { font-size: 18px; font-weight: bold; color: var(--text-white); font-family: monospace; display: flex; gap: 30px; }
        
        .controls-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; width: 180px; margin-top: 5px; }
        .control-btn { background: #161b22; border: 1px solid #30363d; color: #fff; padding: 12px; border-radius: 8px; font-size: 16px; cursor: pointer; text-align: center; transition: 0.1s; }
        .control-btn:active { background: var(--border-neon); color: #000; }
        
        @media (min-width: 850px) { .controls-grid { display: none; } }
        .global-footer-bar { width: 100%; max-width: 600px; text-align: center; margin-top: 30px; padding-top: 15px; border-top: 1px solid var(--border-sub); font-size: 12px; color: var(--text-main); font-family: monospace; }
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
        <div class="score-board">
            <span>النقاط: <span id="currentScore">0</span></span>
            <span>الأعلى: <span id="highScore">0</span></span>
        </div>
        <canvas id="snakeCanvas" width="400" height="400"></canvas>
        
        <div class="controls-grid">
            <div></div><button class="control-btn" onclick="changeDir('up')"><i class="fas fa-chevron-up"></i></button><div></div>
            <button class="control-btn" onclick="changeDir('left')"><i class="fas fa-chevron-left"></i></button>
            <button class="control-btn" onclick="resetGame()"><i class="fas fa-sync"></i></button>
            <button class="control-btn" onclick="changeDir('right')"><i class="fas fa-chevron-right"></i></button>
            <div></div><button class="control-btn" onclick="changeDir('down')"><i class="fas fa-chevron-down"></i></button><div></div>
        </div>
    </div>

    <div class="global-footer-bar">حقوق النشر محفوظة برمجياً وتعود إلى المسؤول البراوي بتاريخ 2026 ©</div>

    <script>
        const canvas = document.getElementById("snakeCanvas");
        const ctx = canvas.getContext("2d");
        const grid = 20;
        let count = 0;
        let score = 0;
        let hScore = localStorage.getItem("snake_high_score") || 0;
        document.getElementById("highScore").innerText = hScore;

        let snake = { x: 160, y: 160, dx: grid, dy: 0, cells: [{x: 160, y: 160}, {x: 140, y: 160}], maxCells: 2 };
        let apple = { x: 320, y: 320 };

        function getRandomInt(min, max) { return Math.floor(Math.random() * (max - min)) + min; }
        
        function loop() {
            requestAnimationFrame(loop);
            if (++count < 6) return;
            count = 0;
            ctx.clearRect(0,0,canvas.width,canvas.height);

            snake.x += snake.dx;
            snake.y += snake.dy;

            if (snake.x < 0) snake.x = canvas.width - grid;
            else if (snake.x >= canvas.width) snake.x = 0;
            if (snake.y < 0) snake.y = canvas.height - grid;
            else if (snake.y >= canvas.height) snake.y = 0;

            snake.cells.unshift({x: snake.x, y: snake.y});
            if (snake.cells.length > snake.maxCells) snake.cells.pop();

            // رسم التفاحة النيونية المضيئة
            ctx.fillStyle = '#ff7b72';
            ctx.shadowBlur = 10; ctx.shadowColor = '#ff7b72';
            ctx.fillRect(apple.x, apple.y, grid-1, grid-1);

            // رسم الثعبان المتوهج بالأخضر السيبراني
            ctx.fillStyle = '#3fb950';
            ctx.shadowBlur = 8; ctx.shadowColor = '#3fb950';
            snake.cells.forEach(function(cell, index) {
                ctx.fillRect(cell.x, cell.y, grid-1, grid-1);
                if (cell.x === apple.x && cell.y === apple.y) {
                    snake.maxCells++; score++;
                    document.getElementById("currentScore").innerText = score;
                    if(score > hScore) { hScore = score; localStorage.setItem("snake_high_score", hScore); document.getElementById("highScore").innerText = hScore; }
                    apple.x = getRandomInt(0, 20) * grid; apple.y = getRandomInt(0, 20) * grid;
                }
                for (let i = index + 1; i < snake.cells.length; i++) {
                    if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) { resetGame(); }
                }
            });
            ctx.shadowBlur = 0;
        }

        function changeDir(dir) {
            if (dir === 'left' && snake.dx === 0) { snake.dx = -grid; snake.dy = 0; }
            else if (dir === 'up' && snake.dy === 0) { snake.dy = -grid; snake.dx = 0; }
            else if (dir === 'right' && snake.dx === 0) { snake.dx = grid; snake.dy = 0; }
            else if (dir === 'down' && snake.dy === 0) { snake.dy = grid; snake.dx = 0; }
        }

        document.addEventListener('keydown', function(e) {
            if (e.which === 37 && snake.dx === 0) { snake.dx = -grid; snake.dy = 0; }
            else if (e.which === 38 && snake.dy === 0) { snake.dy = -grid; snake.dx = 0; }
            else if (e.which === 39 && snake.dx === 0) { snake.dx = grid; snake.dy = 0; }
            else if (e.which === 40 && snake.dy === 0) { snake.dy = grid; snake.dx = 0; }
        });

        function resetGame() {
            score = 0; document.getElementById("currentScore").innerText = score;
            snake = { x: 160, y: 160, dx: grid, dy: 0, cells: [{x: 160, y: 160}, {x: 140, y: 160}], maxCells: 2 };
            apple.x = getRandomInt(0, 20) * grid; apple.y = getRandomInt(0, 20) * grid;
        }

        requestAnimationFrame(loop);

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

@snake_blueprint.route('/snake')
def snake_page():
    return render_template_string(SNAKE_HTML)

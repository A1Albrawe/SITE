from flask import Blueprint, render_template_string

card_game_blueprint = Blueprint('card_game', __name__)

CARD_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>مطابقة البطاقات | Albrawe</title>
    <link rel="stylesheet" href="https://cloudflare.com">
    <style>
        :root { --bg-global: #06090d; --text-main: #c9d1d9; --bg-card: #0d1117; --border-main: #30363d; --border-neon: #58a6ff; --text-white: #fff; --border-sub: #21262d; }
        [data-theme="light"] { --bg-global: #f6f8fa; --text-main: #24292f; --bg-card: #ffffff; --border-main: #d0d7de; --border-neon: #0969da; --text-white: #1f2328; --border-sub: #d0d7de; }
        body { font-family: 'Courier New', monospace; background: var(--bg-global); color: var(--text-main); margin: 0; padding: 25px; box-sizing: border-box; display: flex; flex-direction: column; min-height: 100vh; justify-content: center; align-items: center; transition: 0.3s; }
        
        .top-nav { display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 500px; margin-bottom: 25px; border-bottom: 2px solid var(--border-sub); padding-bottom: 12px; }
        .brand-logo { font-size: 24px; font-weight: bold; color: var(--text-white); text-shadow: 0 0 8px var(--border-neon); text-decoration: none; font-family: monospace; }
        .menu-btn-trigger { background: var(--bg-card); border: 1px solid var(--border-main); color: var(--border-neon); padding: 8px 18px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 14px; font-family: inherit; }
        
        .game-box { background: var(--bg-card); border: 1px solid var(--border-main); border-radius: 14px; padding: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); border-bottom: 4px solid var(--border-neon); display: flex; flex-direction: column; align-items: center; gap: 15px; width: 100%; max-width: 400px; box-sizing: border-box; }
        .card-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; width: 100%; aspect-ratio: 1; }
        
        .mesh-card { background: #161b22; border: 1px solid var(--border-main); border-radius: 6px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 24px; color: transparent; transition: background 0.2s, transform 0.2s; user-select: none; }
        .mesh-card.flipped { background: var(--bg-global); border-color: var(--border-neon); color: var(--text-white); text-shadow: 0 0 8px var(--border-neon); transform: rotateY(180deg); }
        .mesh-card.matched { background: rgba(63,185,80,0.05); border-color: #3fb950; color: #3fb950; text-shadow: 0 0 8px #3fb950; cursor: default; }
        
        .reset-btn { background: var(--bg-global); border: 1px solid var(--border-main); color: var(--text-white); padding: 8px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; font-family: inherit; font-size: 13px; transition: 0.2s; }
        .reset-btn:hover { border-color: var(--border-neon); }
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
        <div style="font-size:15px; font-weight:bold; color:var(--text-white);">تحدي الذاكرة والمطابقة الرقمية</div>
        <div class="card-grid" id="cardGridContainer"></div>
        <button class="reset-btn" onclick="initializeCardsBoard()">إعادة الترتيب 🔄</button>
    </div>

    <div class="global-footer-bar">حقوق النشر محفوظة برمجياً وتعود إلى المسؤول البراوي بتاريخ 2026 ©</div>

    <script>
        const iconsList = [
            "fa-rocket", "fa-rocket", "fa-ghost", "fa-ghost",
            "fa-bolt", "fa-bolt", "fa-cube", "fa-cube",
            "fa-bomb", "fa-bomb", "fa-heart", "fa-heart",
            "fa-star", "fa-star", "fa-shield-alt", "fa-shield-alt"
        ];
        let flippedCards = []; let lockBoard = false;

        function shuffle(array) { return array.sort(() => Math.random() - 0.5); }

        function initializeCardsBoard() {
            const container = document.getElementById("cardGridContainer");
            container.innerHTML = ""; flippedCards = []; lockBoard = false;
            let shuffledIcons = shuffle([...iconsList]);

            shuffledIcons.forEach((icon, index) => {
                const card = document.createElement("div");
                card.classList.add("mesh-card");
                card.dataset.icon = icon;
                card.innerHTML = `<i class="fas ${icon}"></i>`;
                card.addEventListener("click", () => flipCard(card));
                container.appendChild(card);
            });
        }

        function flipCard(card) {
            if (lockBoard || card.classList.contains("flipped") || card.classList.contains("matched")) return;
            card.classList.add("flipped"); flippedCards.push(card);

            if (flippedCards.length === 2) {
                lockBoard = true;
                let isMatch = flippedCards[0].dataset.icon === flippedCards[1].dataset.icon;
                if(isMatch) {
                    flippedCards[0].classList.add("matched"); flippedCards[1].classList.add("matched");
                    flippedCards = []; lockBoard = false;
                } else {
                    setTimeout(() => {
                        flippedCards[0].classList.remove("flipped"); flippedCards[1].classList.remove("flipped");
                        flippedCards = []; lockBoard = false;
                    }, 800);
                }
            }
        }

        initializeCardsBoard();

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

@card_game_blueprint.route('/card_game')
def card_game_page():
    return render_template_string(CARD_HTML)

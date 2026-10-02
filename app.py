import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
page_title="벽돌깨기 게임",
page_icon="🧱",
layout="centered"
)

st.title("🧱 벽돌깨기 게임")
st.write("키보드 ← → 로 패들을 움직이세요!")

game = """

<!DOCTYPE html> <html> <head> <style> body { margin: 0; padding: 0; background: #111; color: white; font-family: Arial, sans-serif; text-align: center; }
#gameCanvas {
    background: #050505;
    border: 3px solid #ffffff;
    display: block;
    margin: 10px auto;
    max-width: 100%;
}

button {
    background: #2196F3;
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    border-radius: 8px;
    cursor: pointer;
    margin: 5px;
}

button:hover {
    background: #1976D2;
}

#info {
    font-size: 18px;
    margin: 10px;
}

</style> </head> <body> <div id="info"> 점수: <span id="score">0</span> &nbsp;&nbsp; 목숨: <span id="lives">3</span> </div>

<canvas id="gameCanvas" width="480" height="600"></canvas>

<button onclick="restartGame()">🔄 다시 시작</button>

<script> const canvas = document.getElementById("gameCanvas"); const ctx = canvas.getContext("2d"); const scoreElement = document.getElementById("score"); const livesElement = document.getElementById("lives"); let score = 0; let lives = 3; let gameRunning = true; const ball = { x: canvas.width / 2, y: canvas.height - 50, radius: 8, dx: 4, dy: -4 }; const paddle = { width: 90, height: 12, x: canvas.width / 2 - 45, y: canvas.height - 30, speed: 7, dx: 0 }; const brick = { rowCount: 5, columnCount: 8, width: 50, height: 20, padding: 8, offsetTop: 50, offsetLeft: 12 }; let bricks = []; function createBricks() { bricks = []; for (let r = 0; r < brick.rowCount; r++) { bricks[r] = []; for (let c = 0; c < brick.columnCount; c++) { bricks[r][c] = { x: 0, y: 0, status: 1 }; } } } createBricks(); document.addEventListener("keydown", keyDownHandler); document.addEventListener("keyup", keyUpHandler); function keyDownHandler(e) { if (e.key === "ArrowRight") { paddle.dx = paddle.speed; } else if (e.key === "ArrowLeft") { paddle.dx = -paddle.speed; } } function keyUpHandler(e) { if ( e.key === "ArrowRight" || e.key === "ArrowLeft" ) { paddle.dx = 0; } } function drawBall() { ctx.beginPath(); ctx.arc( ball.x, ball.y, ball.radius, 0, Math.PI * 2 ); ctx.fillStyle = "#ffffff"; ctx.fill(); ctx.closePath(); } function drawPaddle() { ctx.beginPath(); ctx.rect( paddle.x, paddle.y, paddle.width, paddle.height ); ctx.fillStyle = "#2196F3"; ctx.fill(); ctx.closePath(); } function drawBricks() { for (let r = 0; r < brick.rowCount; r++) { for (let c = 0; c < brick.columnCount; c++) { if (bricks[r][c].status === 1) { const brickX = c * (brick.width + brick.padding) + brick.offsetLeft; const brickY = r * (brick.height + brick.padding) + brick.offsetTop; bricks[r][c].x = brickX; bricks[r][c].y = brickY; ctx.beginPath(); ctx.rect( brickX, brickY, brick.width, brick.height ); const colors = [ "#ff5252", "#ff9800", "#ffeb3b", "#4caf50", "#2196f3" ]; ctx.fillStyle = colors[r]; ctx.fill(); ctx.closePath(); } } } } function collisionDetection() { for (let r = 0; r < brick.rowCount; r++) { for (let c = 0; c < brick.columnCount; c++) { const b = bricks[r][c]; if (b.status === 1) { if ( ball.x > b.x && ball.x < b.x + brick.width && ball.y > b.y && ball.y < b.y + brick.height ) { ball.dy = -ball.dy; b.status = 0; score++; scoreElement.textContent = score; if ( score === brick.rowCount * brick.columnCount ) { gameWin(); } } } } } } function draw() { if (!gameRunning) { return; } ctx.clearRect( 0, 0, canvas.width, canvas.height ); drawBricks(); drawBall(); drawPaddle(); collisionDetection(); // 벽 충돌 if ( ball.x + ball.dx > canvas.width - ball.radius || ball.x + ball.dx < ball.radius ) { ball.dx = -ball.dx; } if ( ball.y + ball.dy < ball.radius ) { ball.dy = -ball.dy; } // 패들과 충돌 if ( ball.y + ball.dy > paddle.y - ball.radius && ball.x > paddle.x && ball.x < paddle.x + paddle.width ) { ball.dy = -ball.dy; } // 바닥 if ( ball.y + ball.dy > canvas.height - ball.radius ) { lives--; livesElement.textContent = lives; if (lives <= 0) { gameOver(); return; } resetBall(); } ball.x += ball.dx; ball.y += ball.dy; paddle.x += paddle.dx; // 패들이 화면 밖으로 나가지 않도록 if (paddle.x < 0) { paddle.x = 0; } if ( paddle.x + paddle.width > canvas.width ) { paddle.x = canvas.width - paddle.width; } requestAnimationFrame(draw); } function resetBall() { ball.x = canvas.width / 2; ball.y = canvas.height - 50; ball.dx = 4; ball.dy = -4; paddle.x = canvas.width / 2 - paddle.width / 2; } function gameOver() { gameRunning = false; setTimeout(() => { alert( "게임 오버!\\n점수: " + score ); }, 100); } function gameWin() { gameRunning = false; setTimeout(() => { alert( "🎉 축하합니다!\\n모든 벽돌을 깼습니다!\\n점수: " + score ); }, 100); } function restartGame() { score = 0; lives = 3; gameRunning = true; scoreElement.textContent = score; livesElement.textContent = lives; createBricks(); resetBall(); draw(); } draw(); </script> </body> </html> """

components.html(game, height=700)

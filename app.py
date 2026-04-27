import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(page_title="Miekkavalaan labyrintti", layout="centered")

def img_to_base64(path):
    data = Path(path).read_bytes()
    return base64.b64encode(data).decode()

orca_b64 = img_to_base64("orca.png")
win_b64 = img_to_base64("xyz.jpg")

st.title("🐋 Orca Labyrinth")
st.write("Raahaa miekkavalas, merten suurin kiusankappale maaliin koskematta seiniin.")

components.html(
f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  body {{
    margin: 0;
    text-align: center;
    font-family: sans-serif;
  }}
  canvas {{
    background: #eef3f7;
    touch-action: none;
    border-radius: 12px;
  }}
  #win {{
    display: none;
  }}
  img {{
    max-width: 80%;
    border-radius: 12px;
  }}
</style>
</head>
<body>

<canvas id="game" width="360" height="480"></canvas>

<div id="win">
  <h2>🎉 Onnittelut!</h2>
  <img src="data:image/png;base64,{win_b64}">
  <br><br>
  <button onclick="restart()" style="font-size:18px;padding:10px 20px;">
    Uudestaan!
  </button>
</div>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const orcaImg = new Image();
orcaImg.src = "data:image/png;base64,{orca_b64}";

let orca = {{ x: 30, y: 30, r: 18 }};
let dragging = false;

const walls = [
 
  {{x: 140, y: 120, w: 20, h: 360}},
  {{x: 210, y: 0,   w: 20, h: 300}},
  {{x: 0,   y: 220, w: 160, h: 20}},
  {{x: 120, y: 400, w: 200, h: 20}},
];

const goal = {{ x: 320, y: 450, r: 20 }};

function reset() {{
  orca.x = 30;
  orca.y = 30;
}}

function collisionRect(w) {{
  return (
    orca.x + orca.r > w.x &&
    orca.x - orca.r < w.x + w.w &&
    orca.y + orca.r > w.y &&
    orca.y - orca.r < w.y + w.h
  );
}}

function winCheck() {{
  const d = Math.hypot(orca.x - goal.x, orca.y - goal.y);
  if (d < orca.r + goal.r) {{
    canvas.style.display = "none";
    document.getElementById("win").style.display = "block";
  }}
}}

function draw() {{
  ctx.clearRect(0,0,canvas.width,canvas.height);

  ctx.fillStyle = "#2c3e50";
  walls.forEach(w => ctx.fillRect(w.x, w.y, w.w, w.h));

  ctx.beginPath();
  ctx.arc(goal.x, goal.y, goal.r, 0, Math.PI * 2);
  ctx.fillStyle = "#27ae60";
  ctx.fill();

  ctx.drawImage(orcaImg, orca.x-orca.r, orca.y-orca.r, orca.r*2, orca.r*2);
}}

canvas.addEventListener("pointerdown", e => dragging = true);
canvas.addEventListener("pointerup", e => dragging = false);
canvas.addEventListener("pointermove", e => {{
  if (!dragging) return;
  const r = canvas.getBoundingClientRect();
  orca.x = e.clientX - r.left;
  orca.y = e.clientY - r.top;

  for (const w of walls) {{
    if (collisionRect(w)) {{
      reset();
      return;
    }}
  }}
  winCheck();
}});

function restart() {{
  document.getElementById("win").style.display = "none";
  canvas.style.display = "block";
  reset();
}}

orcaImg.onload = () => {{
  setInterval(draw, 16);
}};
</script>

</body>
</html>
""",
height=650,
)


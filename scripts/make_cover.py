"""Generate the README cover (assets/cover.svg), 1280x640 so it doubles as the social preview."""
import math
from pathlib import Path

W, H = 1280, 640
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Consolas,'Liberation Mono',monospace"
out = Path(__file__).resolve().parent.parent / "assets" / "cover.svg"

# scope screen geometry
SX, SY, SW, SH = 770, 150, 420, 300


def wave(fn, y0, amp, cycles):
    pts = []
    for i in range(0, 241):
        t = i / 240
        pts.append(f"{SX + 20 + t * (SW - 40):.1f},{y0 - amp * fn(t * cycles * 2 * math.pi):.1f}")
    return "M" + " L".join(pts)


sine = wave(math.sin, SY + 105, 58, 2)
square = wave(lambda a: 1 if math.sin(a) >= 0 else -1, SY + 230, 30, 3)

grid = "".join(
    f'<path d="M{SX + x} {SY}V{SY + SH}"/>' for x in range(0, SW + 1, 42)
) + "".join(f'<path d="M{SX} {SY + y}H{SX + SW}"/>' for y in range(0, SH + 1, 50))

# faint PCB traces along the edges
traces = """
<path d="M0 90 H140 L190 140 H330"/><circle cx="330" cy="140" r="5"/>
<path d="M0 610 H200 L240 570 H420"/><circle cx="420" cy="570" r="5"/>
<path d="M60 0 V40 L100 80 H240"/><circle cx="240" cy="80" r="5"/>
<path d="M1280 70 H1110 L1070 110 H960"/><circle cx="960" cy="110" r="5"/>
<path d="M1280 590 H1140 L1100 550 H900"/><circle cx="900" cy="550" r="5"/>
<path d="M1230 640 V600"/><path d="M720 640 V600 L750 570 H860"/><circle cx="860" cy="570" r="5"/>
"""

chips = [("Fundamentals", "#2f80ed"), ("Analog", "#f2994a"), ("Digital", "#27ae60"), ("Coursework", "#9b51e0")]
chip_svg, x = "", 80
for label, color in chips:
    w = 26 + len(label) * 13.2
    chip_svg += (
        f'<rect x="{x}" y="482" width="{w:.0f}" height="44" rx="22" fill="{color}" fill-opacity=".16" stroke="{color}" stroke-opacity=".7"/>'
        f'<circle cx="{x + 20}" cy="504" r="5" fill="{color}"/>'
        f'<text x="{x + 33}" y="511" font-size="20" font-weight="600" fill="#e8ecf5">{label}</text>'
    )
    x += w + 12

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Electronics Circuit Lab: 183 NI Multisim projects">
  <title>Electronics Circuit Lab</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0a0f1f"/><stop offset="1" stop-color="#141c38"/>
    </linearGradient>
    <radialGradient id="glow" cx=".78" cy=".45" r=".5">
      <stop offset="0" stop-color="#2dd4bf" stop-opacity=".18"/><stop offset="1" stop-color="#2dd4bf" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffb547"/><stop offset=".55" stop-color="#ff4d6d"/><stop offset="1" stop-color="#c026d3"/>
    </linearGradient>
    <pattern id="dots" width="32" height="32" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.3" fill="#8ea3d1" fill-opacity=".14"/>
    </pattern>
    <filter id="blur" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#dots)"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <g fill="none" stroke="#5eead4" stroke-opacity=".22" stroke-width="2.5">{traces}</g>

  <g font-family="{FONT}">
    <path d="M86 150 l-14 26 h12 l-6 22 20 -30 h-12 l8 -18z" fill="#ffb547"/>
    <text x="118" y="182" font-size="20" font-weight="700" letter-spacing="4" fill="#9fb0d6">NI MULTISIM · CIRCUIT LIBRARY</text>
    <text x="76" y="290" font-size="104" font-weight="800" fill="url(#title)" letter-spacing="-2">Electronics</text>
    <text x="76" y="395" font-size="104" font-weight="800" fill="#f5f7fc" letter-spacing="-2">Circuit Lab</text>
    <text x="80" y="450" font-size="28" fill="#b8c4e0"><tspan font-weight="700" fill="#fff">183</tspan> ready-to-simulate .ms13 / .ms14 projects</text>
    {chip_svg}
  </g>

  <!-- oscilloscope -->
  <rect x="{SX - 18}" y="{SY - 46}" width="{SW + 36}" height="{SH + 110}" rx="22" fill="#0d1426" stroke="#2b3b66" stroke-width="2"/>
  <circle cx="{SX + 6}" cy="{SY - 22}" r="6" fill="#ff5f57"/><circle cx="{SX + 26}" cy="{SY - 22}" r="6" fill="#febc2e"/><circle cx="{SX + 46}" cy="{SY - 22}" r="6" fill="#28c840"/>
  <text x="{SX + SW}" y="{SY - 16}" text-anchor="end" font-family="{MONO}" font-size="15" fill="#6f80aa">TRANSIENT · 1 kHz</text>
  <rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="10" fill="#081020"/>
  <g stroke="#1f2d52" stroke-width="1">{grid}</g>
  <path d="{sine}" fill="none" stroke="#2dd4bf" stroke-width="7" stroke-opacity=".45" filter="url(#blur)"/>
  <path d="{sine}" fill="none" stroke="#5eead4" stroke-width="3"/>
  <path d="{square}" fill="none" stroke="#ffb547" stroke-width="6" stroke-opacity=".4" filter="url(#blur)"/>
  <path d="{square}" fill="none" stroke="#ffc46b" stroke-width="2.6"/>
  <g font-family="{MONO}" font-size="15">
    <text x="{SX + 4}" y="{SY + SH + 40}" fill="#5eead4">● CH1 sine</text>
    <text x="{SX + 130}" y="{SY + SH + 40}" fill="#ffc46b">● CH2 square</text>
    <text x="{SX + SW}" y="{SY + SH + 40}" text-anchor="end" fill="#6f80aa">2 V/div</text>
  </g>
</svg>
'''
out.write_text(svg, encoding="utf-8")
print(out)

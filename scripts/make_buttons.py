"""Generate the custom SVG download buttons used in the README."""
import sys
from pathlib import Path

out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "assets" / "buttons"
out.mkdir(parents=True, exist_ok=True)

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

ARROW = (
    '<g fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M0 -9 V5"/><path d="M-6 -1 L0 5 L6 -1"/><path d="M-8 10 H8"/></g>'
)
CHIP = (
    '<g fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round">'
    '<rect x="-7" y="-7" width="14" height="14" rx="2"/>'
    '<path d="M-3 -7v-4M3 -7v-4M-3 7v4M3 7v4M-7 -3h-4M-7 3h-4M7 -3h4M7 3h4"/></g>'
)


def button(name, kicker, label, c1, c2, w=300, h=64, icon=ARROW):
    r = h / 2
    cx = 34
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{kicker} {label}">
  <title>{kicker} {label}</title>
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/>
    </linearGradient>
    <linearGradient id="s" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{r-1}" fill="url(#g)"/>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{r-1}" fill="url(#s)"/>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{r-1}" fill="none" stroke="#fff" stroke-opacity=".25"/>
  <circle cx="{cx}" cy="{h/2}" r="{h/2-10}" fill="#000" fill-opacity=".18"/>
  <g transform="translate({cx} {h/2})">{icon}</g>
  <text x="{cx+32}" y="{h/2-6}" fill="#fff" fill-opacity=".8" font-family="{FONT}" font-size="11" font-weight="600" letter-spacing="1.6">{kicker}</text>
  <text x="{cx+32}" y="{h/2+14}" fill="#fff" font-family="{FONT}" font-size="18" font-weight="700">{label}</text>
</svg>
'''
    (out / f"{name}.svg").write_text(svg, encoding="utf-8")


button("download-all", "DOWNLOAD", "All Circuits (.zip)", "#ff4d4d", "#b3126f", w=340, h=72)
button("download-fundamentals", "DOWNLOAD", "Circuit Fundamentals", "#2f80ed", "#1b4fa8")
button("download-analog", "DOWNLOAD", "Analog Electronics", "#f2994a", "#c0392b")
button("download-digital", "DOWNLOAD", "Digital Logic", "#27ae60", "#0f6e4a")
button("download-coursework", "DOWNLOAD", "Lab &amp; Coursework", "#9b51e0", "#5b2a9e")
button("get-multisim", "GET THE SIMULATOR", "NI Multisim 14.2+", "#3a4150", "#151a22", icon=CHIP)
print("ok")

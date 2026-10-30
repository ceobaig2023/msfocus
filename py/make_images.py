"""Original flat illustrations for the MS Focus site (SVG). Run: python3 make_images.py"""
W, H = 800, 520
SK = ["#f2c9a0", "#e0a878", "#c68642", "#8d5524", "#f7d9bd"]

def kid(x, y, s=1.0, skin=0, hair="#2b1d12", shirt="#e11d48", style="short", arm="up", gog=False):
    sk = SK[skin]
    g = f'<g transform="translate({x},{y}) scale({s})">'
    g += f'<rect x="-34" y="40" width="68" height="80" rx="24" fill="{shirt}"/>'
    if arm == "up":
        g += f'<rect x="26" y="-6" width="14" height="62" rx="7" fill="{sk}" transform="rotate(14 33 56)"/>'
    else:
        g += f'<rect x="-48" y="58" width="16" height="44" rx="8" fill="{sk}" transform="rotate(-20 -40 60)"/><rect x="32" y="58" width="16" height="44" rx="8" fill="{sk}" transform="rotate(20 40 60)"/>'
    g += f'<rect x="-9" y="32" width="18" height="16" fill="{sk}"/><circle cx="0" cy="12" r="30" fill="{sk}"/>'
    if style == "short":
        g += f'<path d="M-31 8 A31 31 0 0 1 31 8 Q10 -4 -31 8Z" fill="{hair}"/>'
    elif style == "long":
        g += f'<path d="M-32 14 A32 32 0 0 1 32 14 L34 52 L24 52 L24 6 Q0 -2 -24 6 L-24 52 L-34 52Z" fill="{hair}"/>'
    elif style == "curly":
        g += "".join(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{hair}"/>' for cx, cy in [(-22,-8),(-8,-16),(8,-16),(22,-8),(-28,6),(28,6)])
    elif style == "bun":
        g += f'<path d="M-31 8 A31 31 0 0 1 31 8 Q10 -4 -31 8Z" fill="{hair}"/><circle cx="0" cy="-22" r="13" fill="{hair}"/>'
    if gog:
        g += '<rect x="-24" y="4" width="48" height="16" rx="8" fill="#bfe9ff" stroke="#1f2937" stroke-width="3" opacity=".9"/>'
    else:
        g += '<circle cx="-11" cy="13" r="3.2" fill="#1f2937"/><circle cx="11" cy="13" r="3.2" fill="#1f2937"/>'
    g += '<path d="M-9 25 Q0 33 9 25" stroke="#7a2e2e" stroke-width="3" fill="none" stroke-linecap="round"/></g>'
    return g

def desk(x, y, w=190, c="#b8793e"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="4" fill="{c}"/><rect x="{x+12}" y="{y+14}" width="9" height="62" fill="#8a5a2b"/><rect x="{x+w-21}" y="{y+14}" width="9" height="62" fill="#8a5a2b"/>'

def svg(body, bg1, bg2):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img">'
            f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#bg)"/><rect y="400" width="{W}" height="120" fill="#d9cfc0"/>{body}</svg>')

def laptop(x, y, c="#334155", screen="#38bdf8"):
    return f'<rect x="{x}" y="{y}" width="64" height="42" rx="4" fill="{c}"/><rect x="{x+5}" y="{y+5}" width="54" height="32" rx="2" fill="{screen}"/><rect x="{x-8}" y="{y+42}" width="80" height="6" rx="3" fill="#94a3b8"/>'

# ---- 1 Smartboard classroom
b = '<rect x="150" y="50" width="500" height="250" rx="14" fill="#1e293b"/><rect x="165" y="65" width="470" height="220" rx="8" fill="#eff6ff"/>'
b += '<rect x="190" y="215" width="40" height="55" fill="#6366f1"/><rect x="245" y="185" width="40" height="85" fill="#22c55e"/><rect x="300" y="150" width="40" height="120" fill="#f59e0b"/><rect x="355" y="120" width="40" height="150" fill="#ef4444"/>'
b += '<circle cx="520" cy="150" r="52" fill="#38bdf8"/><path d="M520 150 L520 98 A52 52 0 0 1 572 150Z" fill="#6366f1"/><rect x="450" y="230" width="150" height="10" rx="5" fill="#94a3b8"/><rect x="450" y="250" width="100" height="10" rx="5" fill="#cbd5e1"/>'
b += '<text x="190" y="102" font-family="Arial" font-weight="700" font-size="22" fill="#1e293b">Smart class</text>'
b += kid(150, 330, 1.05, 0, "#3b2314", "#2563eb", "short", "up") + desk(60, 400, 190)
b += kid(400, 330, 1.05, 3, "#111827", "#f59e0b", "curly", "down") + desk(305, 400, 190)
b += kid(650, 330, 1.05, 1, "#1f1a17", "#16a34a", "long", "up") + desk(555, 400, 190)
open("images/classroom-smartboard.svg", "w").write(svg(b, "#e0f2fe", "#f8fafc"))

# ---- 2 Robotics lab
b = '<rect x="40" y="60" width="200" height="140" rx="8" fill="#1e293b"/>' + "".join(f'<rect x="{50+i*62}" y="{72+j*60}" width="50" height="44" rx="6" fill="{c}"/>' for i,(j,c) in enumerate([(0,"#f97316"),(0,"#22c55e"),(0,"#6366f1"),(1,"#ef4444"),(1,"#38bdf8"),(1,"#eab308")]) if False)
b = '<rect x="40" y="70" width="230" height="12" rx="4" fill="#8a5a2b"/><rect x="40" y="150" width="230" height="12" rx="4" fill="#8a5a2b"/>'
for i, c in enumerate(["#f97316", "#22c55e", "#6366f1"]):
    b += f'<rect x="{60+i*70}" y="34" width="46" height="36" rx="6" fill="{c}"/><rect x="{60+i*70}" y="114" width="46" height="36" rx="6" fill="{c}" opacity=".8"/>'
b += '<circle cx="640" cy="130" r="46" fill="none" stroke="#6366f1" stroke-width="16" stroke-dasharray="14 9"/><circle cx="640" cy="130" r="16" fill="#6366f1"/>'
# robot on table
b += desk(250, 360, 300, "#c08a4a")
b += '<line x1="400" y1="250" x2="400" y2="276" stroke="#334155" stroke-width="5"/><circle cx="400" cy="246" r="9" fill="#ef4444"/><rect x="350" y="276" width="100" height="62" rx="14" fill="#7c3aed"/><circle cx="378" cy="304" r="10" fill="#fff"/><circle cx="422" cy="304" r="10" fill="#fff"/><circle cx="378" cy="304" r="4" fill="#111"/><circle cx="422" cy="304" r="4" fill="#111"/><rect x="340" y="338" width="120" height="14" rx="7" fill="#334155"/><circle cx="362" cy="356" r="11" fill="#1f2937"/><circle cx="438" cy="356" r="11" fill="#1f2937"/>'
b += kid(130, 330, 1.05, 2, "#1a1a1a", "#0ea5e9", "short", "up") + kid(670, 330, 1.05, 4, "#c2410c", "#e11d48", "bun", "down")
b += desk(40, 400, 180) + desk(580, 400, 180)
open("images/robotics-lab.svg", "w").write(svg(b, "#ede9fe", "#faf5ff"))

# ---- 3 Science lab
b = '<rect x="0" y="360" width="800" height="22" fill="#94a3b8"/><rect x="0" y="382" width="800" height="18" fill="#64748b"/>'
def flask(x, c):
    return f'<path d="M{x-12} 300 L{x-12} 330 L{x-40} 372 Q{x-44} 382 {x-30} 382 L{x+30} 382 Q{x+44} 382 {x+40} 372 L{x+12} 330 L{x+12} 300Z" fill="#e0f2fe" stroke="#475569" stroke-width="4"/><path d="M{x-30} 358 L{x+30} 358 L{x+40} 372 Q{x+44} 382 {x+30} 382 L{x-30} 382 Q{x-44} 382 {x-40} 372Z" fill="{c}"/>'
b += flask(430, "#22c55e") + flask(520, "#ef4444") + flask(610, "#a855f7")
b += '<rect x="680" y="320" width="14" height="62" fill="#334155"/><rect x="660" y="372" width="64" height="10" fill="#334155"/><rect x="664" y="318" width="44" height="12" rx="4" fill="#64748b" transform="rotate(-30 686 324)"/><rect x="676" y="300" width="14" height="40" rx="3" fill="#0f172a" transform="rotate(-30 686 324)"/>'
b += '<rect x="60" y="80" width="240" height="14" fill="#8a5a2b"/><rect x="60" y="170" width="240" height="14" fill="#8a5a2b"/>' + "".join(f'<rect x="{80+i*50}" y="{40 if k==0 else 130}" width="30" height="40" rx="5" fill="{c}"/>' for k in (0,1) for i,c in enumerate(["#38bdf8","#facc15","#fb7185","#4ade80"]))
b += kid(200, 290, 1.15, 1, "#1f1a17", "#ffffff", "long", "up", gog=True) + kid(330, 300, 1.05, 0, "#8b5e34", "#ffffff", "short", "down", gog=True)
open("images/science-lab.svg", "w").write(svg(b, "#dcfce7", "#f0fdf4"))

# ---- 4 Coding / STEM
b = '<rect x="230" y="50" width="340" height="190" rx="12" fill="#0f172a"/>' + "".join(f'<rect x="{255+ind}" y="{82+i*26}" width="{w}" height="10" rx="5" fill="{c}"/>' for i,(ind,w,c) in enumerate([(0,120,"#38bdf8"),(24,170,"#a78bfa"),(24,110,"#4ade80"),(48,150,"#fbbf24"),(24,90,"#fb7185"),(0,60,"#38bdf8")]))
b += '<circle cx="110" cy="120" r="46" fill="#fde047"/><circle cx="110" cy="120" r="18" fill="#fff"/><circle cx="690" cy="110" r="40" fill="#fb923c"/><path d="M650 110 A40 40 0 0 1 730 110Z" fill="#f43f5e"/>'
b += desk(80, 380, 270) + desk(450, 380, 270)
b += kid(215, 285, 1.05, 3, "#0b0b0b", "#6366f1", "curly", "down") + laptop(183, 332)
b += kid(585, 285, 1.05, 4, "#9a3412", "#14b8a6", "bun", "down") + laptop(553, 332, "#475569", "#a7f3d0")
open("images/coding-kids.svg", "w").write(svg(b, "#fef9c3", "#fffbeb"))
print("ok")

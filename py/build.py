#!/usr/bin/env python3
"""Generates every HTML page from one shared header/footer so they never drift apart.
Edit the PAGES content below, run `python3 build.py`, and commit the output."""
import html

EMAIL = "focus3to12@gmail.com"
CEO_EMAIL = "ceo@msfocus.in"
PHONE_DISPLAY = "+91 91827 23243"
PHONE_TEL = "+919182723243"
WA = "919182723243"

# ---- FILL THESE IN: sections with no value are left out of the pages automatically ----
YOUTUBE = [("Focus Wallah", "https://www.youtube.com/@focuswallah")]
INSTAGRAM = [("focus_institute_hyd", "https://www.instagram.com/focus_institute_hyd/")]
MAP_EMBED = ""   # Google Maps > Share > Embed a map > copy only the src="..." URL
MAP_LINK = "https://maps.app.goo.gl/J7Fwi3zBtUcybsMx7"  # Google Maps > Share > Copy link
MAP_ADDRESS = "Malakpet, Hyderabad" # Address text shown beside the map
REVIEW_LINK = "" # Google Maps > your place > "Write a review" share link
TEACHERS = [     # ("Name", "Subjects / role", "photo.jpeg or empty")
]
REVIEWS = [      # ("Real review text", "Reviewer name")
]

THEME = {
    "focusinstitute.html": "theme-focus",
    "faraztutorial.html": "theme-faraz",
    "osmaniamodelschool.html": "theme-osmania",
    "sublimeidealschool.html": "theme-sublime",
}
MARK = {  # home-page logo tile colours: (background, text)
    "focusinstitute.html": ("#fde8ea", "#c8102e"),
    "faraztutorial.html": ("#fff1bd", "#c8102e"),
    "osmaniamodelschool.html": ("#e3f5ea", "#12803f"),
}

INSTITUTIONS = [
    ("focusinstitute.html", "Focus Institute", "FI", None,
     "Tuition for Classes 1 to 10 and Intermediate, with practicals and STEM."),
    ("osmaniamodelschool.html", "Osmania Model School", "OM", None,
     "A school where students build strong basics with caring teachers."),
    ("sublimeidealschool.html", "Sublime Ideal School", None, "sublimelogo.jpeg",
     "A school preparing confident students for the future."),
    ("faraztutorial.html", "Faraz Tutorial", "FT", None,
     "Tutoring founded in 1992 by Ms. Ayesha Mehreen."),
]

NAV = [
    ("index.html", "Home"),
    ("Aboutus.html", "About us"),
    ("SUB", "Institutions"),
    ("techcompany.html", "Tech"),
    ("othercources.html", "Courses"),
    ("ourteachers.html", "Our team"),
    ("carriers.html", "Careers"),
]


def e(s):
    return html.escape(s, quote=True)


def social_block():
    groups = []
    if YOUTUBE:
        groups.append(("YouTube channels", YOUTUBE))
    if INSTAGRAM:
        groups.append(("Instagram pages", INSTAGRAM))
    if not groups:
        return ""
    out = ""
    for title, links in groups:
        out += f'<div class="panel"><h3>{title}</h3><ul class="ticks">' + "".join(
            f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a></li>' for n, u in links) + "</ul></div>"
    return f'''<section class="alt"><div class="container"><div class="section-head"><h2>Follow us</h2></div>
<div class="grid-2">{out}</div></div></section>'''


def map_block():
    if not (MAP_EMBED or MAP_LINK):
        return ""
    frame = (f'<iframe title="MS Focus on Google Maps" src="{e(MAP_EMBED)}" width="100%" height="380" style="border:0;border-radius:14px" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'
             if MAP_EMBED else "")
    link = f'<a class="btn outline" href="{e(MAP_LINK)}" target="_blank" rel="noopener">Open in Google Maps</a>' if MAP_LINK else ""
    addr = f"<p>{e(MAP_ADDRESS)}</p>" if MAP_ADDRESS else ""
    return f'''<section><div class="container"><div class="section-head"><h2>Find us</h2>{addr}</div>{frame}<div class="btn-row">{link}</div></div></section>'''


def reviews_block():
    link = REVIEW_LINK or MAP_LINK
    if not REVIEWS and not link:
        return ""
    cards = "".join(
        f'<figure class="panel review"><blockquote>{e(q)}</blockquote><figcaption>{e(n)}</figcaption></figure>'
        for q, n in REVIEWS)
    btn = f'<div class="btn-row"><a class="btn" href="{e(link)}" target="_blank" rel="noopener">Read and write Google reviews</a></div>' if link else ""
    grid = f'<div class="grid-3">{cards}</div>' if cards else ""
    return f'''<section class="alt"><div class="container"><div class="section-head"><h2>What parents and students say</h2></div>{grid}{btn}</div></section>'''


WA_SVG = '<svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true" fill="#fff"><path d="M16 3C9.4 3 4 8.3 4 14.9c0 2.3.7 4.5 1.9 6.4L4 28l6.9-1.8c1.8 1 3.100 1.500 5.100 1.500 6.600 0 12-5.300 12-11.900S22.600 3 16 3zm0 21.800c-1.800 0-3.500-.5-5-1.400l-.4-.2-4 1 1.100-3.900-.3-.4a9.700 9.700 0 0 1-1.500-5.100C5.900 9.500 10.400 5 16 5s10.100 4.500 10.100 9.900S21.600 24.800 16 24.800zm5.500-7.300c-.3-.1-1.800-.9-2.100-1s-.5-.1-.7.100-.8 1-1 1.200-.4.200-.7.100a8.100 8.100 0 0 1-4-3.500c-.3-.5.300-.5.900-1.600.1-.2.100-.4 0-.5l-1-2.300c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.100-.8.400s-1 1-1 2.400 1 2.800 1.200 3 2 3.100 4.900 4.300c1.800.8 2.500.8 3.400.7.5-.1 1.800-.7 2-1.400s.2-1.300.2-1.400-.3-.2-.6-.3z"/></svg>'


def mv_block():
    return '''<section class="mv">
  <div class="container grid-2">
    <div><h2>Our mission</h2>
      <p>To give every student a strong grounding in their subjects and the confidence to use what they know, through clear teaching, hands-on practice and modern technology, in a classroom where learning is also fun.</p></div>
    <div><h2>Our vision</h2>
      <p>To grow a family of schools and learning centres where children from every background learn to think, build and lead, and where technology such as robotics and AI is part of everyday education.</p></div>
  </div>
  <div class="container values">
    <p><strong>Clear teaching.</strong> Concepts explained step by step until they make sense.</p>
    <p><strong>Learning by doing.</strong> Practicals, projects and workshops, not only notes.</p>
    <p><strong>Care for every child.</strong> Teachers who know their students.</p>
  </div>
</section>'''


def circle_row():
    items = [
        ("focusinstitute.html", "Focus Institute", "logo.png", None, "linear-gradient(135deg,#c8102e,#ffc61a)", "contain"),
        ("osmaniamodelschool.html", "Osmania Model School", None, "OM", "linear-gradient(135deg,#0b3d24,#1fa356)", ""),
        ("sublimeidealschool.html", "Sublime Ideal School", "sublimelogo.jpeg", None, "linear-gradient(135deg,#0a2a66,#2b7be4)", "cover"),
        ("faraztutorial.html", "Faraz Tutorial", None, "FT", "linear-gradient(135deg,#ffc61a,#c8102e)", ""),
    ]
    out = ""
    for h, n, img, ini, ring, fit in items:
        inner = (f'<img src="{img}" alt="" class="{fit}" width="120" height="120">' if img
                 else f'<span class="ini" style="color:#fff;background:{ring}">{ini}</span>')
        out += f'<li><a class="circle" href="{h}"><span class="disc" style="background:{ring}">{inner}</span><span class="cname">{n}</span></a></li>'
    return f'<section class="circles"><div class="container"><ul class="circle-row">{out}</ul></div></section>'


def header(current):
    items = []
    for href, label in NAV:
        if href == "SUB":
            inst_current = current in [i[0] for i in INSTITUTIONS]
            subs = "".join(
                f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{e(n)}</a></li>'
                for h, n, *_ in INSTITUTIONS)
            items.append(
                f'<li class="has-sub"><button class="drop" aria-expanded="false" aria-haspopup="true"'
                f'{" style=\"color:var(--violet-700)\"" if inst_current else ""}>{label} &#9662;</button>'
                f'<ul class="submenu">{subs}</ul></li>')
        else:
            cur = ' aria-current="page"' if href == current else ""
            items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    cur = ' aria-current="page"' if current == "contact.html" else ""
    items.append(f'<li class="cta"><a href="contact.html"{cur}>Contact</a></li>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="container nav" aria-label="Main">
    <a class="brand" href="index.html"><img src="logo.png" alt="" width="56" height="44">MS<span>Focus</span></a>
    <button class="menu-btn" id="menu-btn" aria-label="Open navigation menu" aria-expanded="false" aria-controls="nav-links">&#9776;</button>
    <ul class="nav-links" id="nav-links">{"".join(items)}</ul>
  </nav>
</header>'''


def footer():
    inst = "".join(f'<li><a href="{h}">{e(n)}</a></li>' for h, n, *_ in INSTITUTIONS)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div>
        <h3>MS Focus</h3>
        <p>Schools, tutoring, workshops and software from Malakpet, Hyderabad.</p>
      </div>
      <div><h3>Institutions</h3><ul>{inst}</ul></div>
      <div><h3>Explore</h3><ul>
        <li><a href="Aboutus.html">About us</a></li>
        <li><a href="techcompany.html">Tech</a></li>
        <li><a href="othercources.html">Courses</a></li>
        <li><a href="ourteachers.html">Our team</a></li>
        <li><a href="carriers.html">Careers</a></li>
      </ul></div>
      <div><h3>Contact</h3><ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        <li><a href="https://wa.me/{WA}">Message on WhatsApp</a></li>
        {"".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">YouTube: {e(n)}</a></li>' for n, u in YOUTUBE)}
        {"".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">Instagram: {e(n)}</a></li>' for n, u in INSTAGRAM)}
      </ul></div>
    </div>
    <p class="copy">&copy; <span class="year">2026</span> MS Focus. All rights reserved.</p>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{WA}?text=Hello%20MS%20Focus" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{WA_SVG}</a>
<script src="script.js"></script>'''


def page(filename, title, desc, body, current=None):
    theme = THEME.get(filename, "")
    full_title = f"{title} | MS Focus" if title != "MS Focus" else "MS Focus | Education and technology"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="https://www.msfocus.in/msfocuslogo.jpeg">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Hanken+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body class="{theme}">
{header(current or filename)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''


def page_hero(title, sub, crumb):
    return f'''<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / {e(crumb)}</p>
    <h1>{e(title)}</h1>
    <p>{e(sub)}</p>
  </div>
</section>'''


def cta(heading, text, interest=None, label="Send an enquiry"):
    q = f"?interest={interest.replace(' ', '%20')}" if interest else ""
    return f'''<section class="cta-band">
  <div class="container">
    <h2>{e(heading)}</h2>
    <p>{e(text)}</p>
    <div class="btn-row"><a class="btn" href="contact.html{q}">{e(label)}</a></div>
  </div>
</section>'''


PAGES = {}

# ---------------------------------------------------------------- HOME
rows = "".join(
    f'''<div class="row">
      <div class="mark"{f' style="background:{MARK[h][0]};color:{MARK[h][1]}"' if h in MARK else ""}>{f'<img src="{img}" alt="{e(n)} logo" loading="lazy">' if img else ini}</div>
      <div><h3><a href="{h}">{e(n)}</a></h3><p>{e(d)}</p></div>
      <a class="btn outline" href="{h}">View</a>
    </div>'''
    for h, n, ini, img, d in INSTITUTIONS)

PAGES["index.html"] = ("MS Focus",
    "MS Focus connects schools, tutoring, workshops and software development under one vision.",
    f'''<section class="hero">
  <div class="container hero-grid">
    <div>
      <h1>Learn well. Build things. Enjoy it.</h1>
      <p class="lead">From our base in Malakpet, Hyderabad, MS Focus brings sound classroom teaching together with hands-on STEM, robotics and programming for students from Class 1 to Intermediate.</p>
      <div class="btn-row">
        <a class="btn" href="#institutions">See our institutions</a>
        <a class="btn ghost" href="contact.html">Contact us</a>
      </div>
    </div>
    <div class="hero-logo"><img src="msfocuslogo.jpeg" alt="MS Focus logo: a graduation cap on the letter M with a small robot" width="900" height="600"></div>
  </div>
</section>

{circle_row()}

<section id="institutions">
  <div class="container">
    <div class="section-head">
      <h2>Our institutions</h2>
      <p class="lead">Four places of learning, one shared approach: clear teaching, real practice and a welcoming classroom.</p>
    </div>
    <div class="rows">{rows}</div>
  </div>
</section>

{mv_block()}

<section class="alt">
  <div class="container">
    <div class="section-head"><h2>Learning by doing</h2><p class="lead">Smart classrooms, robotics, science labs and coding, so students build and test what they learn.</p></div>
    <div class="grid-2 gallery">
      <figure><img src="images/classroom-smartboard.svg" alt="Students raising their hands in a classroom with a smartboard" loading="lazy"><figcaption>Smart classrooms</figcaption></figure>
      <figure><img src="images/robotics-lab.svg" alt="Students working with a robot in a robotics lab" loading="lazy"><figcaption>Robotics lab</figcaption></figure>
      <figure><img src="images/science-lab.svg" alt="Students in goggles doing a science experiment" loading="lazy"><figcaption>Science practicals</figcaption></figure>
      <figure><img src="images/coding-kids.svg" alt="Students coding on laptops" loading="lazy"><figcaption>Coding and AI</figcaption></figure>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div>
      <h2>Technology that students can touch</h2>
      <p class="lead">Workshops on robotics, AI, programming and science practicals take the subject out of the textbook.</p>
      <ul class="ticks">
        <li>Hands-on robotics and AI workshops for schools</li>
        <li>Programming and science practical sessions</li>
        <li>Website and software development for institutions and businesses</li>
      </ul>
      <a class="btn" href="techcompany.html">What we build and teach</a>
    </div>
    <div class="panel">
      <h3>Led by Mr. Mirza Mohammed Baig</h3>
      <p>Known as Mohd Sir, he is the founder and CEO of MS Focus and the guiding force behind Focus Institute, Osmania Model School and Sublime Ideal School. He is an engineer and data scientist.</p>
      <a href="Aboutus.html">Read about the leadership</a>
    </div>
  </div>
</section>

<section>
  <div class="container split top">
    <div>
      <h2>Partnership with Legacy International School</h2>
      <p class="lead">MS Focus works in partnership with Legacy International School.</p>
    </div>
    <div class="panel">
      <h3>Talk to us</h3>
      <p>Parents, schools and businesses can reach the team directly.</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
    </div>
  </div>
</section>
{reviews_block()}
{social_block()}''')

# ---------------------------------------------------------------- ABOUT
PAGES["Aboutus.html"] = ("About us",
    "Meet the founders and leaders behind MS Focus, Focus Institute, Osmania Model School, Sublime Ideal School and Faraz Tutorial.",
    page_hero("About MS Focus", "A family-led education group in Hyderabad that pairs good teaching with technology.", "About us") + f'''
<section>
  <div class="container split">
    <div class="person">
      <div class="photo"><img src="mohdsirfocus.jpeg" alt="Mr. Mirza Mohammed Baig speaking at an event" width="640" height="601"></div>
    </div>
    <div>
      <h2>Mr. Mirza Mohammed Baig (Mohd Sir)</h2>
      <p class="lead">Founder and CEO of MS Focus.</p>
      <p>He is the visionary leader behind the success of Focus Institute, Osmania Model School and Sublime Ideal School. An engineer and data scientist, he has given workshops on robotics, AI, programming and science practicals at Mesco Idsarimilya MS.</p>
      <p><a href="mailto:{CEO_EMAIL}">{CEO_EMAIL}</a><br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
    </div>
  </div>
</section>

<section>
  <div class="container split top">
    <div><h2>Our story</h2></div>
    <div><p class="lead">MS Focus grew out of a family that has been teaching for decades.</p>
    <p>Faraz Tutorial opened in 1992 under Ms. Ayesha Mehreen. Over the years her work expanded into Focus Institute, Osmania Model School and Sublime Ideal School. Today Mr. Mirza Mohammed Baig leads MS Focus, adding robotics, AI and programming to the classroom so students learn the tools they will use next.</p></div>
  </div>
</section>

{mv_block()}

<section class="alt">
  <div class="container">
    <div class="section-head"><h2>Leadership and founders</h2></div>
    <div class="grid-3">
      <article class="person">
        <div class="initials" aria-hidden="true">AM</div>
        <div class="info"><h3>Ms. Ayesha Mehreen</h3><p class="role">Founder, Faraz Tutorial</p>
        <p>Founded Faraz Tutorial in 1992 and has served as principal of Osmania Model School, Sublime Ideal School and Focus Institute.</p></div>
      </article>
      <article class="person">
        <div class="photo"><img src="Mirza_Liaquat_Ullah_Baig.jpeg" alt="Mr. Mirza Liaquat Ullah Baig" width="640" height="638" loading="lazy"></div>
        <div class="info"><h3>Mr. Mirza Liaquat Ullah Baig (Sajid)</h3><p class="role">Director</p></div>
      </article>
      <article class="person">
        <div class="initials" aria-hidden="true">DM</div>
        <div class="info"><h3>Ms. Dania Mirza</h3><p class="role">Co-founder and teacher</p></div>
      </article>
    </div>
    <div class="grid-3" style="margin-top:1.4rem">
      <article class="person">
        <div class="initials" aria-hidden="true">AB</div>
        <div class="info"><h3>Mr. Mirza Ahmed Baig</h3><p class="role">Co-founder and teacher</p></div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container split top">
    <div><h2>Partnerships</h2><p class="lead">MS Focus works in partnership with Legacy International School.</p></div>
    <div class="panel"><h3>Get in touch</h3><p>Questions about admissions, workshops or partnerships go to the team directly.</p><a class="btn" href="contact.html">Contact us</a></div>
  </div>
</section>''')


# ---------------------------------------------------------------- INSTITUTIONS
def inst_page(fname, name, intro, points, extra_html="", logo=None):
    visual = (f'<div class="hero-logo" style="max-width:300px;transform:none"><img src="{logo}" alt="{e(name)} logo" width="300" height="295"></div>'
              if logo else "")
    return (name, intro,
        page_hero(name, intro, name) + f'''
<section>
  <div class="container split top">
    <div>
      <h2>About {e(name)}</h2>
      {points}
      <div class="btn-row"><a class="btn" href="contact.html?interest={name.replace(" ", "%20")}">Enquire about {e(name)}</a></div>
    </div>
    <div>{visual}{extra_html}</div>
  </div>
</section>
<section class="alt">
  <div class="container">
    <div class="section-head"><h2>Leadership</h2></div>
    <div class="grid-2">
      <div class="panel"><h3>Mr. Mirza Mohammed Baig (Mohd Sir)</h3><p>Founder and CEO of MS Focus, and the visionary leader behind this institution's success.</p></div>
      <div class="panel"><h3>Ms. Ayesha Mehreen</h3><p>Has served as principal of Osmania Model School, Sublime Ideal School and Focus Institute.</p></div>
    </div>
  </div>
</section>
''' + cta("Want to know more?", "Ask about admissions, programmes or visiting in person.", name))


other = lambda cur: '<div class="panel"><h3>Other institutions</h3><ul class="ticks">' + "".join(
    f'<li><a href="{h}">{e(n)}</a></li>' for h, n, *_ in INSTITUTIONS if h != cur) + "</ul></div>"

FOCUS_TEACH = '''
<section class="alt">
  <div class="container">
    <div class="section-head"><h2>What we teach</h2><p class="lead">From primary classes to intermediate, across the boards families choose.</p></div>
    <div class="grid-3">
      <div class="panel"><h3>Classes 1 to 10</h3><p>Coaching for every class from 1 to 10.</p></div>
      <div class="panel"><h3>Boards</h3><ul class="ticks"><li>SSC</li><li>CBSE</li><li>IGCSE</li><li>IB</li><li>TOSS</li></ul></div>
      <div class="panel"><h3>Intermediate</h3><ul class="ticks"><li>MPC</li><li>BIPC</li><li>CEC</li><li>MEC</li></ul></div>
    </div>
  </div>
</section>'''

PAGES["focusinstitute.html"] = inst_page("focusinstitute.html", "Focus Institute",
    "Tuition for Classes 1 to 10 and Intermediate in Malakpet, Hyderabad.",
    '<p class="lead">Learn and fun, from Class 1 to Intermediate.</p><p>Focus Institute in Malakpet, Hyderabad, helps students master their subjects with clear explanations, regular practice and practical work. Alongside the syllabus, students meet STEM and robotics, so ideas move from the page to something they can build and test.</p><p>Mr. Mirza Mohammed Baig leads the institute, and Ms. Ayesha Mehreen has served as its principal. Call or message us for current batches, timings and admissions.</p>',
    other("focusinstitute.html"))
_t, _d, _b = PAGES["focusinstitute.html"]
_b = _b.replace('<div>' + other("focusinstitute.html"), '<div><figure class="gallery"><img src="images/classroom-smartboard.svg" alt="Students in a smart classroom" loading="lazy"></figure>' + other("focusinstitute.html"), 1) + social_block()
PAGES["focusinstitute.html"] = (_t, _d, _b.replace('<section class="alt">\n  <div class="container">\n    <div class="section-head"><h2>Leadership</h2>', FOCUS_TEACH + '\n<section>\n  <div class="container">\n    <div class="section-head"><h2>Leadership</h2>', 1))
PAGES["osmaniamodelschool.html"] = inst_page("osmaniamodelschool.html", "Osmania Model School",
    "A school where students learn with support from experienced teachers.",
    '<p class="lead">Strong basics, taught with care.</p><p>Osmania Model School gives children a steady foundation in the core subjects and the habits that make good students. Teachers focus on understanding rather than memorising, and the school draws on MS Focus for technology and practical learning.</p><p>Mr. Mirza Mohammed Baig is the visionary leader behind its success, and Ms. Ayesha Mehreen has served as its principal. Contact us for classes offered, admissions and timings.</p>',
    other("osmaniamodelschool.html"))
PAGES["sublimeidealschool.html"] = inst_page("sublimeidealschool.html", "Sublime Ideal School",
    "A school focused on student development and readiness for the future.",
    '<p class="lead">A school built around a student’s future.</p><p>Sublime Ideal School combines academic learning with confidence building and exposure to technology, so students are ready for the next stage of their education. The rocket on the school crest says it well: aim high.</p><p>Mr. Mirza Mohammed Baig is the visionary leader behind its success, and Ms. Ayesha Mehreen has served as its principal. Contact us for classes offered, admissions and timings.</p>',
    other("sublimeidealschool.html"), logo="sublimelogo.jpeg")
PAGES["faraztutorial.html"] = inst_page("faraztutorial.html", "Faraz Tutorial",
    "Tutoring founded in 1992 by Ms. Ayesha Mehreen.",
    '<p class="lead">Teaching students since 1992.</p><p>Faraz Tutorial is where the MS Focus story began. Ms. Ayesha Mehreen founded it, and its focus on patient, personal teaching shaped the schools and institute that followed. Contact us for subjects, batches and timings.</p>',
    other("faraztutorial.html"))

# ---------------------------------------------------------------- TECH
PAGES["techcompany.html"] = ("Tech",
    "MS Focus builds websites and software and runs robotics, AI and programming workshops for schools.",
    page_hero("MS Focus Tech", "Software for institutions and businesses, and technology workshops for students.", "Tech") + f'''
<section>
  <div class="container">
    <div class="section-head"><h2>What we do</h2></div>
    <div class="grid-3">
      <div class="panel"><h3>Websites and software</h3><p>Websites, business applications and digital tools for schools, institutes and companies.</p></div>
      <div class="panel"><h3>Edutech</h3><p>Digital learning resources and technology that makes classroom teaching easier to deliver.</p></div>
      <div class="panel"><h3>Workshops</h3><p>Hands-on sessions in robotics, AI, programming and science practicals.</p></div>
    </div>
  </div>
</section>
<section class="alt">
  <div class="container split top">
    <div>
      <h2>Workshops in schools</h2>
      <p>Mr. Mirza Mohammed Baig, an engineer and data scientist, has led workshops on robotics, AI, programming and science practicals, including at Mesco Idsarimilya MS.</p>
      <ul class="ticks"><li>Robotics</li><li>Artificial intelligence</li><li>Programming</li><li>Science practicals</li></ul>
    </div>
    <div><figure class="gallery"><img src="images/robotics-lab.svg" alt="Students working with a robot in a robotics lab" loading="lazy"></figure><div class="panel"><h3>Book a workshop for your school</h3><p>Tell us the class level and the topic you want covered.</p><a class="btn" href="contact.html?interest=Workshops">Request a workshop</a></div></div>
  </div>
</section>''')

# ---------------------------------------------------------------- COURSES
PAGES["othercources.html"] = ("Courses",
    "Courses and workshops from MS Focus: robotics, AI, programming and science practicals.",
    page_hero("Courses and workshops", "Subjects we teach beyond the regular classroom.", "Courses") + f'''
<section>
  <div class="container">
    <div class="grid-2 gallery" style="margin-bottom:1.6rem"><figure><img src="images/science-lab.svg" alt="Students doing a science experiment" loading="lazy"></figure><figure><img src="images/coding-kids.svg" alt="Students coding on laptops" loading="lazy"></figure></div>
    <div class="grid-2">
      <div class="panel"><h3>Robotics</h3><p>Build and program simple robots and learn how sensors and motors work together.</p></div>
      <div class="panel"><h3>Artificial intelligence</h3><p>Understand what AI is, where it is used and how to start working with it.</p></div>
      <div class="panel"><h3>Programming</h3><p>Learn to write code step by step, from first programs onwards.</p></div>
      <div class="panel"><h3>Science practicals</h3><p>Run experiments yourself and see the theory work.</p></div>
    </div>
    <p class="note" style="margin-top:2rem">Dates, fees and age groups change from batch to batch. Send an enquiry and we will reply with the current details.</p>
    <div class="btn-row"><a class="btn" href="contact.html?interest=Courses">Ask about courses</a></div>
  </div>
</section>''')

# ---------------------------------------------------------------- TEAM
def _teacher_cards():
    out = ""
    for n, r, ph in TEACHERS:
        art = (f'<div class="photo"><img src="{e(ph)}" alt="{e(n)}" loading="lazy"></div>' if ph
               else f'<div class="initials" aria-hidden="true">{e("".join(w[0] for w in n.split()[:2]).upper())}</div>')
        out += f'<article class="person">{art}<div class="info"><h3>{e(n)}</h3><p class="role">{e(r)}</p></div></article>'
    return (f'<section class="alt"><div class="container"><div class="section-head"><h2>Our faculty</h2></div><div class="grid-3">{out}</div></div></section>'
            if out else "")


PAGES["ourteachers.html"] = ("Our teachers",
    "Meet the leaders and teachers of MS Focus and learn how we teach.",
    page_hero("Our teachers", "People who know their subjects and know their students.", "Our teachers") + f'''
<section>
  <div class="container">
    <div class="section-head"><h2>Leadership</h2><p class="lead">The family that founded and guides MS Focus.</p></div>
    <div class="grid-3">
      <article class="person"><div class="photo"><img src="mohdsirfocus.jpeg" alt="Mr. Mirza Mohammed Baig" width="640" height="601" loading="lazy"></div>
        <div class="info"><h3>Mr. Mirza Mohammed Baig</h3><p class="role">Founder and CEO (Mohd Sir)</p><p>Engineer and data scientist who leads MS Focus and teaches robotics, AI and programming.</p></div></article>
      <article class="person"><div class="initials" aria-hidden="true">AM</div>
        <div class="info"><h3>Ms. Ayesha Mehreen</h3><p class="role">Founder, Faraz Tutorial</p><p>Principal at Osmania Model School, Sublime Ideal School and Focus Institute.</p></div></article>
      <article class="person"><div class="photo"><img src="Mirza_Liaquat_Ullah_Baig.jpeg" alt="Mr. Mirza Liaquat Ullah Baig" width="640" height="638" loading="lazy"></div>
        <div class="info"><h3>Mr. Mirza Liaquat Ullah Baig</h3><p class="role">Director (Sajid)</p></div></article>
      <article class="person"><div class="initials" aria-hidden="true">DM</div>
        <div class="info"><h3>Ms. Dania Mirza</h3><p class="role">Co-founder and teacher</p></div></article>
      <article class="person"><div class="initials" aria-hidden="true">AB</div>
        <div class="info"><h3>Mr. Mirza Ahmed Baig</h3><p class="role">Co-founder and teacher</p></div></article>
    </div>
  </div>
</section>
{_teacher_cards()}
<section class="alt">
  <div class="container">
    <div class="section-head"><h2>How we teach</h2></div>
    <div class="grid-3">
      <div class="panel"><h3>Explain first</h3><p>Every topic starts with the idea behind it, in plain language, before any formula or answer is memorised.</p></div>
      <div class="panel"><h3>Practise often</h3><p>Regular practice, practicals and short tests show students where they stand and what to fix.</p></div>
      <div class="panel"><h3>Make it fun</h3><p>Activities, experiments and technology keep students curious. Learn and fun go together.</p></div>
    </div>
  </div>
</section>
''' + cta("Want to meet our teachers?", "Visit, call or message us to talk about the right batch for your child.", None, "Contact us"))

# ---------------------------------------------------------------- CAREERS
PAGES["carriers.html"] = ("Careers",
    "Teaching and technology careers at MS Focus.",
    page_hero("Careers at MS Focus", "Teach, build and help students learn.", "Careers") + f'''
<section>
  <div class="container split top">
    <div>
      <h2>Work with us</h2>
      <p class="lead">We look for teachers and technology people who care about students.</p>
      <p>There is no open-positions list online yet. Email your CV and the role you are interested in, and we will contact you when a suitable position opens.</p>
      <div class="btn-row"><a class="btn" href="mailto:{EMAIL}?subject=Careers%20at%20MS%20Focus">Email your CV</a></div>
    </div>
    <div class="panel"><h3>Areas we hire in</h3><ul class="ticks"><li>School and tutorial teaching</li><li>Robotics, AI and programming instruction</li><li>Web and software development</li></ul></div>
  </div>
</section>''')

# ---------------------------------------------------------------- CONTACT
PAGES["contact.html"] = ("Contact",
    "Contact MS Focus by email, phone or the enquiry form.",
    page_hero("Contact us", "Questions about admissions, workshops, software or partnerships.", "Contact") + f'''
<section>
  <div class="container split top">
    <div>
      <h2>Reach the team</h2>
      <ul class="contact-list">
        <li><strong>Location</strong>Malakpet, Hyderabad</li>
        <li><strong>Enquiries email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><strong>Founder and CEO, Mr. Mirza Mohammed Baig</strong><a href="mailto:{CEO_EMAIL}">{CEO_EMAIL}</a></li>
        <li><strong>Phone</strong><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        <li><strong>WhatsApp</strong><a href="https://wa.me/{WA}">Message us</a></li>
      </ul>
    </div>
    <form class="enquiry panel" id="enquiry-form">
      <h3>Send an enquiry</h3>
      <label for="name">Full name</label>
      <input id="name" name="name" type="text" autocomplete="name" required>
      <label for="email">Email address</label>
      <input id="email" name="email" type="email" autocomplete="email" required>
      <label for="phone">Phone (optional)</label>
      <input id="phone" name="phone" type="tel" autocomplete="tel">
      <label for="interest">What is your enquiry about?</label>
      <select id="interest" name="interest" required>
        <option value="">Choose one</option>
        <option>Focus Institute</option><option>Osmania Model School</option>
        <option>Sublime Ideal School</option><option>Faraz Tutorial</option>
        <option>Workshops</option><option>Courses</option>
        <option>Software and websites</option><option>Other</option>
      </select>
      <label for="message">Message</label>
      <textarea id="message" name="message" required></textarea>
      <button class="btn" type="submit">Send enquiry</button>
      <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
{map_block()}
{reviews_block()}
{social_block()}''')

# ---------------------------------------------------------------- 404
PAGES["404.html"] = ("Page not found",
    "This page does not exist.",
    '''<section><div class="container"><h1>Page not found</h1>
<p class="lead">The page you opened does not exist or has moved.</p>
<div class="btn-row"><a class="btn" href="index.html">Go to the home page</a></div></div></section>''')

if __name__ == "__main__":
    for fname, (title, desc, body) in PAGES.items():
        with open(fname, "w", encoding="utf-8") as f:
            f.write(page(fname, title, desc, body))
    pages = [f for f in PAGES if f != "404.html"]
    with open("sitemap.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in pages:
            loc = "https://www.msfocus.in/" + ("" if p == "index.html" else p)
            f.write(f"  <url><loc>{loc}</loc></url>\n")
        f.write("</urlset>\n")
    with open("robots.txt", "w") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: https://www.msfocus.in/sitemap.xml\n")
    print("built", len(PAGES), "pages")

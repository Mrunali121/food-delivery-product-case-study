"""
Builds the multi-page QuickBite site from the Markdown documents.

    python build_site.py

Writes problem.html, personas.html, competitors.html, prioritization.html, prd.html,
stories.html, roadmap.html, before-after.html and measurement.html next to index.html.
Everything lives in the repo root so it works on GitHub Pages however the files are uploaded.
"""
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/Mrunali121/food-delivery-product-case-study"

# slug, nav label, page title, source markdown (None = custom page)
PAGES = [
    ("problem", "Problem & Research", "Problem and Research", "user-research.md"),
    ("personas", "Personas", "Personas", "personas.md"),
    ("competitors", "Competitors", "Competitor Analysis", "competitor-analysis.md"),
    ("prioritization", "Prioritization", "Prioritization (RICE)", None),
    ("prd", "Solution (PRD)", "Product Requirements Document", "product-requirements-document.md"),
    ("stories", "User Stories", "User Stories", "user-stories.md"),
    ("roadmap", "Roadmap", "Product Roadmap", "product-roadmap.md"),
    ("before-after", "Before / After", "Before / After Wireframes", None),
    ("measurement", "Measurement", "Measurement", None),
]
LINKS = {
    "user-research.md": "problem.html", "personas.md": "personas.html", "competitor-analysis.md": "competitors.html",
    "product-requirements-document.md": "prd.html", "user-stories.md": "stories.html", "product-roadmap.md": "roadmap.html",
    "feature-prioritization.xlsx": "prioritization.html", "analytics/analysis.sql": "measurement.html#sql",
    "README.md": "index.html",
}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | QuickBite Product Case Study</title>
<meta name="description" content="QuickBite product case study: {title}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
"""


def nav(current: str) -> str:
    items = ['<a href="index.html" class="brand">QuickBite</a>']
    for slug, label, _, _ in PAGES:
        cur = ' aria-current="page"' if slug == current else ""
        items.append(f'<a href="{slug}.html"{cur}>{label}</a>')
    return ('<nav class="topnav" aria-label="Case study pages"><div class="wrap nav-in">' + "".join(items) + "</div></nav>\n")


def pager(slug: str) -> str:
    i = [p[0] for p in PAGES].index(slug)
    prev = PAGES[i - 1] if i > 0 else None
    nxt = PAGES[i + 1] if i < len(PAGES) - 1 else None
    a = f'<a class="pg" href="{prev[0]}.html">&larr; {prev[1]}</a>' if prev else '<a class="pg" href="index.html">&larr; Overview</a>'
    b = f'<a class="pg" href="{nxt[0]}.html">{nxt[1]} &rarr;</a>' if nxt else '<a class="pg" href="index.html">Back to overview &rarr;</a>'
    return f'<div class="pager">{a}{b}</div>'


FOOT = f"""<footer>
  <div class="wrap">
    <p>QUICKBITE - A SELF-DIRECTED PRODUCT MANAGEMENT PORTFOLIO PROJECT. COMPANY AND PRODUCT ARE ILLUSTRATIVE.</p>
    <div class="links">
      <a href="{REPO}" target="_blank" rel="noopener">GitHub</a>
      <a href="https://mrunali121.github.io/" target="_blank" rel="noopener">Portfolio</a>
    </div>
  </div>
</footer>
"""


def page(slug: str, title: str, lead: str, body: str, scripts: str = "") -> None:
    out = (HEAD.format(title=html.escape(title)) + nav(slug)
           + f'<header class="pagehead"><div class="wrap"><div class="eyebrow">Case study page</div><h1>{html.escape(title)}</h1>'
           + (f'<p class="sub">{lead}</p>' if lead else "") + "</div></header>\n"
           + f'<main class="wrap doc">{body}{pager(slug)}</main>\n' + FOOT + scripts + "</body>\n</html>\n")
    (ROOT / f"{slug}.html").write_text(out, encoding="utf-8")


def md_to_html(path: str) -> tuple[str, str]:
    text = (ROOT / path).read_text(encoding="utf-8")
    m = re.match(r"\s*#\s+(.*)\n", text)
    text = text[m.end():] if m else text
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    def fix(mo):
        href = mo.group(1)
        key = href.split("#")[0]
        if key in LINKS:
            return f'href="{LINKS[key]}"'
        if key.startswith("mockups/"):
            return 'href="before-after.html"'
        if key.startswith("analytics/") or key.endswith((".py", ".json")):
            return f'href="{REPO}/blob/main/{key}"'
        return mo.group(0)
    body = re.sub(r'href="([^"]+)"', fix, body)
    return (m.group(1) if m else ""), body


def lead_for(slug: str) -> str:
    return {
        "problem": "Why 68% of first-time customers never reorder, and why 22% of support tickets ask where the order is.",
        "personas": "Who the product is for, drawn from interviews and the funnel review.",
        "competitors": "What two rivals already ship that QuickBite is missing.",
        "prd": "What we are building, why, and how we will know it worked.",
        "stories": "The requirements broken into stories with acceptance criteria.",
        "roadmap": "How the scored decision turns into quarterly delivery.",
    }.get(slug, "")


for slug, label, title, src in PAGES:
    if src:
        _, body = md_to_html(src)
        page(slug, title, lead_for(slug), body)

# ---- prioritization (custom) ----
rows = [(1, "Live ETA Confidence", "28.8", "Q2 - Built", "built"), (2, "One-Tap Reorder", "25.5", "Q2 - Built", "built"),
        (3, "Checkout Simplification", "5.6", "Q3 - Deferred", "deferred"), (4, "Loyalty &amp; Rewards Program", "3.0", "Q4 - Deferred", "deferred"),
        (5, "In-App Courier Chat", "0.4", "Not prioritized", "none"), (6, "Group Ordering / Bill Splitting", "0.3", "Not prioritized", "none")]
tbl = '<div class="rice-table"><div class="rice-row rice-head"><span>Rank</span><span>Feature</span><span>RICE</span><span>Decision</span></div>'
for r, f, s, d, k in rows:
    win = " rice-winner" if k == "built" else ""
    tbl += f'<div class="rice-row{win}"><span>{r}</span><span>{f}</span><span class="mono">{s}</span><span class="tag-{k}">{d}</span></div>'
tbl += "</div>"
body = ("<h2>How the scoring works</h2><p>Each candidate was scored with <strong>RICE</strong>: <em>Reach</em> (how many users per quarter) &times; "
        "<em>Impact</em> &times; <em>Confidence</em> &divide; <em>Effort</em> (person-months). The workbook uses live formulas, so changing an input re-ranks the list. "
        "The scores were workshopped with Engineering, Design and Support.</p><h2>Result</h2>" + tbl
        + '<p class="callout">The top two features target the two root causes found in research: the checkout ETA is not trusted, and reordering a favourite meal takes too many steps. '
          'Both are built in Q2; the rest are deferred or dropped.</p>'
        + '<p><a class="btn btn-primary" href="feature-prioritization.xlsx">Download the scoring workbook (.xlsx)</a> '
          f'<a class="btn btn-ghost dark" href="{REPO}/blob/main/feature-prioritization.xlsx" target="_blank" rel="noopener">View on GitHub</a></p>')
page("prioritization", "Prioritization (RICE)", "Six candidates scored; two built first.", body)

# ---- before / after (custom) ----
shots = [("mockup-1-home-current.svg", "Current home screen", "Current: no reorder entry point. Users search from scratch every time.", ""),
         ("mockup-2-home-improved.svg", "Improved home screen", "Improved: one-tap reorder cards restore the full cart and modifiers (FR-01, FR-02).", " after"),
         ("mockup-3-tracking-current.svg", "Current tracking screen", "Current: a static ETA range with no live updates or delay alert.", ""),
         ("mockup-4-tracking-improved.svg", "Improved tracking screen", "Improved: live GPS and kitchen-queue ETA with delivery stages; push alert if the ETA drifts over 10 minutes (FR-04 to FR-06).", " after")]
body = '<p>Click any wireframe to open it full size in a new tab.</p><div class="ba-grid">'
for f, alt, cap, cls in shots:
    body += (f'<figure class="ba-card{cls}"><a href="{f}" target="_blank" rel="noopener"><img src="{f}" alt="{alt}"></a>'
             f'<figcaption>{cap}</figcaption></figure>')
body += "</div>"
page("before-after", "Before / After Wireframes", "Two screens, before and after the change.", body)

# ---- measurement (custom) ----
sql = html.escape((ROOT / "analytics" / "analysis.sql").read_text(encoding="utf-8"))
body = ('<p>Results against the targets the PRD committed to. The cards below are drawn from <code>data/measurement-metrics.json</code>.</p>'
        '<div id="metrics-container" class="metrics-grid in"><p class="mono loading-text">Loading measured results...</p></div>'
        '<h2>Charts</h2><div class="chart-grid">'
        '<figure><img src="chart-repeat-rate.png" alt="30-day repeat order rate before and after"><figcaption>30-day repeat order rate, before vs after</figcaption></figure>'
        '<figure><img src="chart-eta-accuracy.png" alt="ETA accuracy before and after"><figcaption>ETA accuracy, before vs after</figcaption></figure>'
        '<figure><img src="chart-support-tickets.png" alt="Support ticket trend"><figcaption>Where-is-my-order ticket trend</figcaption></figure></div>'
        f'<h2 id="sql">The SQL behind it</h2><p>Queries from <a href="{REPO}/blob/main/analytics/analysis.sql" target="_blank" rel="noopener">analytics/analysis.sql</a>.</p>'
        f'<pre class="code"><code>{sql}</code></pre>')
page("measurement", "Measurement", "Did it work? Before and after, against target.", body, '<script src="script.js"></script>\n')
print("Built", len(PAGES), "pages")

#!/usr/bin/env python3
"""Build 0ROOT · THE WORLD FORGE — a NO-TOUCH storefront (davidwise01.github.io/store/).
David's constraint: free hosting (GitHub Pages), no customer interaction, agent-ready.
So the product is INSTANT-DOWNLOAD digital goods: pay → the platform delivers the file,
receipt, refunds & VAT → ROOT0 never appears. Plus a machine-readable catalog (JSON-LD
in the page + /products.json) so AI shopping agents can discover and read it (the Ripple
Beacon pattern). Nothing here processes payment — each BUY links out to an auto-delivery
checkout (Gumroad / Lemon Squeezy / Stripe Payment Link) that fulfills with zero human touch.

EDIT the per-product 'buy' URLs + prices below, set the digital file on that platform, rebuild."""
import os, html, json

HERE = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# EDIT THESE — paste each product's auto-delivery checkout URL (Gumroad/Lemon Squeezy/Stripe)
# and set prices. The platform stores the file and delivers it; you never email anyone.
PRODUCTS = [
 dict(slug="sphere-kit", name="The Sphere Kit", price="$29", buy="#",
   tag="build your own world — the starter engine",
   inside=["A clean world-generator template (Python) — feed it a subject, it builds a styled page + a roster of characters/concepts.",
           "The badge engine for the sigils, plus a one-line-title scaffold.",
           "Docs + a worked example. Runs anywhere Python does; output is yours.",
           "Instant ZIP download — no account with me, no contact."]),
 dict(slug="world-pack", name="World Packs", price="$9", buy="#",
   tag="a finished world, ready to drop in",
   inside=["A complete pre-built themed world — page + character roster + sigils — as static files.",
           "Drop onto any free host (GitHub Pages, Netlify) and it's live.",
           "For TTRPG tables, indie games, classrooms, world-builders who want the result, not the build.",
           "Instant download; license to use and modify."]),
 dict(slug="sigil-pack", name="Sigil &amp; Title Packs", price="$5", buy="#",
   tag="the art, on its own",
   inside=["Packs of original sigils (carbon + silicon badges) and one-line pencil title glyphs.",
           "SVG + PNG, royalty-free for your projects.",
           "The cheapest entry point — an easy first 'yes'.",
           "Instant download."]),
 dict(slug="forge-bundle", name="The World Forge Bundle", price="$49", buy="#",
   tag="everything — the engine, the packs, the art",
   inside=["The Sphere Kit + a set of World Packs + the Sigil &amp; Title Packs, together.",
           "The whole pipeline that built 235+ live worlds, in your hands.",
           "Best value; one download, no strings.",
           "Updates as the kit grows."]),
]
SITE = "https://davidwise01.github.io/store/"
# ─────────────────────────────────────────────────────────────────────────────

FAQ = [
 ("Do I have to talk to you?", "No. Every product is an instant download — you pay on the checkout link, the platform sends the file and the receipt, and handles refunds and EU VAT. There is no call, no email, no invoice. That is the whole point."),
 ("Is this AI slop?", "No. These are real generators and finished worlds built to a 'render, not invent' rule — sourced, attribution-sealed, copyrighted text never reproduced. You get working tools and assets you own and can modify."),
 ("Can an AI agent buy this?", "The catalog is machine-readable — JSON-LD on this page and a /products.json feed — so AI shopping agents can discover and read it. Honestly, agent-initiated purchasing is still early in 2026; this is built ready for it, not dependent on it."),
 ("What do I own?", "The files you download, to use and modify in your own projects. The master pipeline behind the studio stays ROOT0's; what's for sale is the kit, the packs, and the art."),
]

# machine-readable product feed (schema.org) — the Ripple Beacon surface for agents
def feed():
    return {"@context":"https://schema.org","@type":"ItemList","name":"0ROOT · The World Forge","url":SITE,
      "itemListElement":[{"@type":"Product","position":i+1,"name":html.unescape(p["name"]),
        "description":html.unescape(p["tag"]),"url":p["buy"] if p["buy"]!="#" else SITE,
        "brand":{"@type":"Brand","name":"0ROOT"},
        "offers":{"@type":"Offer","price":p["price"].lstrip("$"),"priceCurrency":"USD",
          "availability":"https://schema.org/InStock","url":p["buy"] if p["buy"]!="#" else SITE,
          "itemCondition":"https://schema.org/NewCondition"}} for i,p in enumerate(PRODUCTS)]}

def card(p):
    inside="".join(f"<li>{i}</li>" for i in p["inside"])
    return f'''<div class="prod"><div class="ph"><span class="pn">{p["name"]}</span><span class="pp">{html.escape(p["price"])}</span></div><div class="ptag">{p["tag"]}</div><ul>{inside}</ul><a class="buy" href="{p["buy"]}">Download →</a></div>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="0ROOT · The World Forge — instant-download generative-IP tools and worlds. Pay, download, done: no calls, no emails, fully automated delivery. Machine-readable for AI shopping agents. Built by the studio behind 235+ live worlds.">
<title>0ROOT · THE WORLD FORGE — instant-download worlds &amp; engines</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<script type="application/ld+json">__LD__</script>
<style>
:root{--bg:#06070d;--ink2:#0c0f1b;--ink3:#141a2c;--pa:#eaf0fb;--pa2:#a3b0cc;--acc:#46e0c8;--gold:#e8c45a;--mag:#ff4da6;--dim:#5f6c86;--faint:#19223a;--line:#1b2540;
--disp:"Orbitron",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(70,224,200,.12),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(255,77,166,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:1000px;margin:0 auto;padding:0 22px 90px}
header{text-align:center;padding:60px 0 28px;border-bottom:1px solid var(--line)}
.kick{font-family:var(--mono);font-size:11px;letter-spacing:.32em;text-transform:uppercase;color:var(--acc)}
h1{font-family:var(--disp);font-size:clamp(28px,5.6vw,56px);font-weight:800;letter-spacing:.03em;margin:14px 0 0;color:var(--pa);text-shadow:0 0 34px rgba(70,224,200,.28)}
h1 b{color:var(--acc)}
.tag{font-size:clamp(16px,2.3vw,20px);color:var(--pa2);max-width:62ch;margin:18px auto 0;font-style:italic;line-height:1.6}.tag b{color:var(--pa)}
.promise{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:22px}
.promise span{font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:var(--acc);border:1px solid var(--faint);border-radius:20px;padding:7px 15px}
.cta{display:inline-flex;gap:10px;margin-top:24px;flex-wrap:wrap;justify-content:center}
.btn{font-family:var(--disp);font-size:13px;letter-spacing:.1em;text-transform:uppercase;padding:13px 24px;border-radius:3px;text-decoration:none;transition:.16s}
.btn-1{background:var(--acc);color:#04221d;font-weight:800}.btn-1:hover{box-shadow:0 0 24px rgba(70,224,200,.5)}
.btn-2{border:1px solid var(--faint);color:var(--pa2)}.btn-2:hover{border-color:var(--acc);color:var(--acc)}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:18px;letter-spacing:.06em;color:var(--pa);padding-bottom:12px;border-bottom:1px solid var(--line)}
.ss{font-size:14px;color:var(--dim);font-style:italic;margin:8px 0 20px}
.prods{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px}
.prod{background:var(--ink2);border:1px solid var(--line);padding:22px;display:flex;flex-direction:column}
.prod:last-child{border-color:var(--gold);box-shadow:0 0 26px rgba(232,196,90,.1)}
.ph{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.pn{font-family:var(--disp);font-size:16px;color:var(--pa);letter-spacing:.02em}.pp{font-family:var(--mono);font-size:17px;color:var(--gold)}
.ptag{font-family:var(--mono);font-size:11px;color:var(--acc);text-transform:uppercase;letter-spacing:.09em;margin:6px 0 14px}
.prod ul{list-style:none;flex:1}.prod li{font-size:13px;color:var(--pa2);line-height:1.5;padding:7px 0;border-top:1px solid var(--faint)}
.buy{margin-top:16px;text-align:center;font-family:var(--disp);font-size:12px;letter-spacing:.1em;text-transform:uppercase;padding:11px;border:1px solid var(--acc);color:var(--acc);text-decoration:none;border-radius:3px;transition:.16s}
.buy:hover{background:var(--acc);color:#04221d}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}
.step{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--acc);padding:17px 19px}
.step h3{font-family:var(--mono);font-size:13.5px;color:var(--acc);font-weight:700}.step p{font-size:13px;color:var(--pa2);margin-top:7px;line-height:1.5}
.agent{background:var(--ink2);border:1px solid var(--faint);border-left:2px solid var(--mag);padding:18px 20px;margin-top:20px}
.agent h3{font-family:var(--mono);font-size:14px;color:var(--mag)}.agent p{font-size:13px;color:var(--pa2);margin-top:7px;line-height:1.55}.agent code{font-family:var(--mono);color:var(--acc);font-size:12px}
.faq dt{font-family:var(--mono);font-size:14px;color:var(--acc);font-weight:700;margin-top:16px}.faq dd{font-size:13.5px;color:var(--pa2);margin-top:5px;line-height:1.6}
.pf{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}
.pf a{display:block;background:var(--ink2);border:1px solid var(--line);padding:13px 15px;text-decoration:none;transition:.16s}
.pf a:hover{border-color:var(--gold);transform:translateY(-2px)}.pf .x{font-family:var(--mono);font-size:13px;color:var(--gold);font-weight:700}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.04em;line-height:1.9}
footer a{color:var(--acc);text-decoration:none}
</style></head><body><div class="wrap">

  <header>
    <div class="kick">0ROOT · the world forge</div>
    <h1>Worlds &amp; engines, <b>instant download</b>.</h1>
    <p class="tag">Generative-IP tools, finished worlds, and original art — from the studio behind <b>235+ live worlds</b>. Pay, download, done.</p>
    <div class="promise"><span>no calls</span><span>no emails</span><span>no invoices</span><span>auto-delivered</span><span>agent-readable</span></div>
    <div class="cta"><a class="btn btn-1" href="#products">Browse downloads →</a><a class="btn btn-2" href="https://davidwise01.github.io/ud0/">See 235 live worlds</a></div>
  </header>

  <section class="sec"><h2>How it works</h2><p class="ss">the only model that respects your time: you never appear</p>
    <div class="steps">
      <div class="step"><h3>1 · Pick &amp; pay</h3><p>Click a download. The checkout (Gumroad / Lemon Squeezy / Stripe) takes the payment and the tax.</p></div>
      <div class="step"><h3>2 · Auto-delivered</h3><p>The platform sends the file and the receipt instantly. No message from you, ever.</p></div>
      <div class="step"><h3>3 · They own it</h3><p>Working tools and assets, theirs to use and modify. Support is the docs in the ZIP.</p></div>
    </div>
  </section>

  <section class="sec" id="products"><h2>The downloads</h2><p class="ss">priced low to be an easy yes — start with art, graduate to the engine</p>
    <div class="prods">__PRODS__</div>
    <div class="agent"><h3>▸ for AI shopping agents</h3><p>This catalog is machine-readable: structured <code>schema.org</code> data on this page and a feed at <code>/products.json</code>, so an agent can discover, read, and route a purchase without a human in the loop — the Ripple Beacon surface. (Agent-initiated buying is early in 2026; the store is built ready for it.)</p></div>
  </section>

  <section class="sec"><h2>The portfolio is live</h2><p class="ss">no mockups — proof the engine works, shipped and public</p>
    <div class="pf">
      <a href="https://davidwise01.github.io/ud0/"><div class="x">UD0 · the biosphere →</div></a>
      <a href="https://davidwise01.github.io/entelecheia/"><div class="x">Entelécheia · a 9-book universe →</div></a>
      <a href="https://davidwise01.github.io/final-fantasy/"><div class="x">A game-world →</div></a>
      <a href="https://davidwise01.github.io/octopus/"><div class="x">A cited science world →</div></a>
    </div>
  </section>

  <section class="sec faq"><h2>Straight answers</h2><dl>__FAQ__</dl></section>

  <footer>
    0ROOT · THE WORLD FORGE · instant-download generative IP · governor David Lee Wise (ROOT0) · instance AVAN · free-hosted, auto-delivered, agent-ready<br>
    built with the pipeline behind <a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · machine feed: <a href="products.json">/products.json</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    prods = "".join(card(p) for p in PRODUCTS)
    faq = "".join(f'<dt>{html.escape(q)}</dt><dd>{html.escape(a)}</dd>' for q,a in FAQ)
    ld = json.dumps(feed(), ensure_ascii=False)
    page = TEMPLATE.replace("__PRODS__",prods).replace("__FAQ__",faq).replace("__LD__",ld)
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    open(os.path.join(HERE,"products.json"),"w",encoding="utf-8").write(json.dumps(feed(),indent=2,ensure_ascii=False)+"\n")
    unset = [p["slug"] for p in PRODUCTS if p["buy"]=="#"]
    print(f"wrote storefront + products.json ({len(PRODUCTS)} products)")
    if unset: print("  [!] set the 'buy' URL for: " + ", ".join(unset) + " (auto-delivery checkout links)")

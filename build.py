# Regenerates static SEO pages, sitemap, llms.txt from tools.json. Run: python3 build.py
import json,html,os
S="https://vibepicks.ai"; d=json.load(open('tools.json')); E=html.escape
def page(path,title,desc,body,ld):
  os.makedirs(path or '.',exist_ok=True); url=f"{S}/{path+'/' if path else ''}"
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="VibePicks"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary">
<link rel="stylesheet" href="/style.css"><script type="application/ld+json">{json.dumps(ld)}</script></head><body>
<header class="nav"><a href="/" class="logo">Vibe<span>Picks</span></a><nav><a href="/">Home</a><a href="/#/directory">Directory</a><a href="/releases/">New releases</a><a href="/sponsor/">Sponsor</a></nav></header><main>{body}</main><footer>VibePicks · Rankings are editorial picks · <a href="/sponsor/">Sponsor</a> · <a href="/llms.txt">llms.txt</a></footer></body></html>'''
def tl(t,i): return f'<div class="card tool"><div class="rank">#{i+1}</div><div><h3><a href="{t["url"]}" rel="noopener">{E(t["name"])}</a></h3><div class="muted">Use it for: {E(t["use"])}</div><span class="tag {t["pricing"]}">{t["pricing"]}</span></div></div>'
urls=['/','/releases/']
for c in d['categories']:
  title=f'Best {c["name"]} for Vibe Coders (2026) — VibePicks'
  desc=f'Ranked {c["name"].lower()} for builders shipping apps with AI: '+', '.join(t['name'] for t in c['tools'])+'.'
  ld={"@context":"https://schema.org","@type":"ItemList","name":f'Best {c["name"]}',"itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"SoftwareApplication","name":t["name"],"url":t["url"],"applicationCategory":"DeveloperApplication","description":t["use"]}} for i,t in enumerate(c['tools'])]}
  body=f'<section class="hero" style="padding-bottom:10px"><div style="font-size:2.4rem">{c["icon"]}</div><h1>Best {E(c["name"])}</h1><p>Ranked editorial picks for vibe coders and builders.</p></section><div class="grid" style="grid-template-columns:1fr">'+''.join(tl(t,i) for i,t in enumerate(c['tools']))+'</div><p><a href="/">← All categories</a></p>'
  open(f'{c["id"]}/index.html' if os.makedirs(c['id'],exist_ok=True) is None else '','w').write(page(c['id'],title,desc,body,ld)); urls.append(f'/{c["id"]}/')
rel=''.join(f'<div class="release {"sample" if r.get("sample") else ""}"><span class="tag">{r["date"]}</span> <b>{E(r["tool"])}</b> — {E(r["title"])} <a href="{r["source"]}">source</a></div>' for r in d['releases'])
os.makedirs('releases',exist_ok=True)
open('releases/index.html','w').write(page('releases','New AI Tool Releases for Builders — VibePicks','Verified AI tool and model launches that matter to people shipping apps.','<h1>New releases</h1>'+rel,{"@context":"https://schema.org","@type":"CollectionPage","name":"New AI tool releases"}))
PK=[("Featured Listing","$99","/month","A labeled Sponsored card for your tool on the homepage and directory.","https://buy.stripe.com/test_bJe8wQafc4VM9Pm5wQ83C00"),
("Newsletter Sponsor","$149","/issue","One sponsored block in a VibePicks newsletter issue, labeled Sponsored.","https://buy.stripe.com/test_3cI7sM7303RI4v2aRa83C01"),
("Category Top Spot","$249","/month","A pinned slot above the rankings on one category page, clearly labeled Sponsored.","https://buy.stripe.com/test_8x28wQ5YW1JA6Da1gA83C02")]
cards=''.join(f'<div class="card"><h3>{n}</h3><div style="font-size:1.8rem;font-weight:700">{pr}<span class="muted" style="font-size:1rem">{u}</span></div><p class="muted">{dsc}</p><a class="btn" href="{l}" rel="noopener">Buy {n}</a></div>' for n,pr,u,dsc,l in PK)
sbody=('<div id="thanks" class="card" style="display:none"><b>Thanks! Payment received.</b> We will email you within one business day to set up your placement.</div>'
'<section class="hero" style="padding-bottom:10px"><h1>Sponsor VibePicks</h1><p>Reach vibe coders and builders choosing their AI stack.</p></section>'
'<div class="grid">'+cards+'</div>'
'<h2>Honest audience note</h2><p>VibePicks is a new site and the newsletter is just starting, so our audience is small and growing. That is why these are early-bird prices. Early sponsors keep their rate as we grow.</p>'
'<h2>Our rules</h2><ul><li>Every sponsored spot is clearly labeled <b>Sponsored</b>.</li><li>Sponsorship never changes editorial rankings. Rankings are our own picks.</li><li>We may decline tools that are not a fit for builders.</li></ul>'
'<p>Questions or custom deals: <a href="mailto:news@vibepicks.ai">news@vibepicks.ai</a></p>'
'<script>if(location.search.includes("thanks=1"))document.getElementById("thanks").style.display="block"</script>')
os.makedirs('sponsor',exist_ok=True)
open('sponsor/index.html','w').write(page('sponsor','Sponsor VibePicks — Reach Vibe Coders and Builders','Sponsorship packages for AI and developer tools: featured listings, newsletter sponsorships, and category top spots. Always labeled, never changes rankings.',sbody,{"@context":"https://schema.org","@type":"WebPage","name":"Sponsor VibePicks"}))
urls.append('/sponsor/')
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{S}{u}</loc></url>' for u in urls)+'</urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {S}/sitemap.xml\n')
L=['# VibePicks','> Editorial rankings of the best AI tools for vibe coders and builders shipping apps, grouped by use case. Ranks are editorial picks, not paid placements.','']
for c in d['categories']:
  L+=[f'## {c["name"]} ({S}/{c["id"]}/)']+[f'{i+1}. [{t["name"]}]({t["url"]}): {t["use"]} ({t["pricing"]})' for i,t in enumerate(c['tools'])]+['']
L+=['## Recent releases']+[f'- {r["date"]}: {r["tool"]} — {r["title"]} ({r["source"]})' for r in d['releases']]
L+=['','## Sponsorship',f'Sponsored placements are always labeled and never change editorial rankings. Packages: {S}/sponsor/']
open('llms.txt','w').write('\n'.join(L)+'\n')

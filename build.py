# Regenerates static SEO pages, sitemap, llms.txt from tools.json. Run: python3 build.py
import json,html,os
S="https://vibepicks.ai"; d=json.load(open('tools.json')); E=html.escape
def page(path,title,desc,body,ld):
  os.makedirs(path or '.',exist_ok=True); url=f"{S}/{path+'/' if path else ''}"
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="VibePicks"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary">
<link rel="stylesheet" href="/style.css"><script type="application/ld+json">{json.dumps(ld)}</script></head><body>
<header class="nav"><a href="/" class="logo">Vibe<span>Picks</span></a><nav><a href="/">Home</a><a href="/#/directory">Directory</a><a href="/releases/">New releases</a></nav></header><main>{body}</main><footer>VibePicks · Rankings are editorial picks · <a href="/llms.txt">llms.txt</a></footer></body></html>'''
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
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{S}{u}</loc></url>' for u in urls)+'</urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {S}/sitemap.xml\n')
L=['# VibePicks','> Editorial rankings of the best AI tools for vibe coders and builders shipping apps, grouped by use case. Ranks are editorial picks, not paid placements.','']
for c in d['categories']:
  L+=[f'## {c["name"]} ({S}/{c["id"]}/)']+[f'{i+1}. [{t["name"]}]({t["url"]}): {t["use"]} ({t["pricing"]})' for i,t in enumerate(c['tools'])]+['']
L+=['## Recent releases']+[f'- {r["date"]}: {r["tool"]} — {r["title"]} ({r["source"]})' for r in d['releases']]
open('llms.txt','w').write('\n'.join(L)+'\n')

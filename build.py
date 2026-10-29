# Regenerates static SEO pages, sitemap, llms.txt from tools.json. Run: python3 build.py
# NOTE: /guide/ (Ready, Fire, Aim. sales page) is hand-written; launched Oct 20 2026 (in nav + sitemap). Its download folder stays noindex and out of sitemap/llms.
import json,html,os
S="https://vibepicks.ai"; d=json.load(open('tools.json')); E=html.escape
ICON='<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
PAGES={}  # path -> generated html, used for sitemap lastmod
def catbar(cur=''): return '<nav class="catbar" aria-label="Browse categories"><span class="catbar-l">Browse categories</span>'+''.join(f'<a class="chip{" on" if c["id"]==cur else ""}" href="/{c["id"]}/"'+(' aria-current="page"' if c["id"]==cur else '')+f'>{c["icon"]} {E(c["name"])}</a>' for c in d['categories'])+'</nav>'+('<script>document.querySelector(".catbar .on").scrollIntoView({inline:"center",block:"nearest"})</script>' if cur in [c['id'] for c in d['categories']] else '')
CATIDS={c['id'] for c in d['categories']}
# category pages advertise a plain Markdown copy (/<category>/index.md) so AI agents and answer engines can read the ranking without parsing HTML
def MDALT(path): return f'<link rel="alternate" type="text/markdown" title="{"New releases" if path=="releases" else "This ranking"} as Markdown" href="/{path}/index.md">' if path in CATIDS or path=='releases' else ''
def page(path,title,desc,body,ld):
  os.makedirs(path or '.',exist_ok=True); url=f"{S}/{path+'/' if path else ''}"
  h=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">{ICON}
<meta property="og:type" content="website"><meta property="og:site_name" content="VibePicks"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary">
<link rel="stylesheet" href="/style.css">{MDALT(path)}<link rel="alternate" type="application/rss+xml" title="VibePicks: new AI tool releases" href="/releases/feed.xml"><script type="application/ld+json">{json.dumps(ld)}</script><script>window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};</script><script defer src="/_vercel/insights/script.js"></script></head><body>
<header class="nav"><a href="/" class="logo">Vibe<span>Picks</span></a><nav><a href="/">Home</a><a href="/#/directory">Directory</a><a href="/releases/">New releases</a><a href="/sponsor/">Sponsor</a><a href="/build-it-for-me/">Build it for me</a><a href="/guide/">Guide</a></nav></header>{catbar(path)}<main>{body}</main><footer>VibePicks · Rankings are editorial picks · <a href="/sponsor/">Sponsor</a> · <a href="/llms.txt">llms.txt</a> · <a href="/llms-full.txt">llms-full.txt</a> · <a href="/releases/feed.xml">RSS</a></footer><script src="/signup.js"></script></body></html>'''
  PAGES[f'/{path}/' if path else '/']=h; return h
def tl(t,i): return f'<div class="card tool"><div class="rank">#{i+1}</div><div><h3><a href="{t.get("aff") or t["url"]}" rel="{"sponsored nofollow noopener" if t.get("aff") else "noopener"}">{E(t["name"])}</a></h3><div class="muted">Use it for: {E(t["use"])}</div><span class="tag {t["pricing"]}">{t["pricing"]}</span>{" <span class=\"tag\">Affiliate link</span>" if t.get("aff") else ""}</div></div>'
DISCT='Cursor and Grok are owned by the same company (SpaceXSI), and VibePicks itself is built with Grok Bot. Rankings are based on merit and are never paid for or influenced by that.'
AFFT='Some tool links are affiliate links, labeled Affiliate link. We may earn a commission if you sign up, at no extra cost to you. Affiliate deals never change rankings.'
def disc(own,aff): return '<p class="muted disclosure" style="font-size:.82rem;margin:14px 2px">Disclosure: '+' '.join(x for x in ((DISCT if own else ''),(AFFT if aff else '')) if x)+'</p>' if (own or aff) else ''
DISC=f'<p class="muted disclosure" style="font-size:.82rem;margin:14px 2px">Disclosure: {DISCT}</p>'
urls=['/','/releases/']
LMPH='@@LASTMOD@@'  # placeholder for a page's last-changed date; swapped in after lastmod.json is updated, so it doesn't affect the content hash
CATS=[]
def faq(c):
  T=c['tools']; nl=c['name']; top=T[0]; lc=lambda u: u if (len(u)>1 and u[1].isupper()) else u[0].lower()+u[1:]
  Q=[(f'What is the best pick in {nl} for 2026?',f'{top["name"]} is our #1 pick in {nl}: {lc(top["use"])}. {top["why"]}')]
  fr=next((t for t in T if t['pricing'] in ('Free','Freemium')),None)
  if fr: Q.append((f'Is there a free option in {nl}?',(f'Yes. {fr["name"]} is ' + ('completely free' if fr['pricing']=='Free' else 'free to start, with paid upgrades') + f'. {fr["why"]}') if fr is not top else f'Yes. Our #1 pick, {top["name"]}, is ' + ('completely free.' if top['pricing']=='Free' else 'free to start, with paid upgrades.')))
  if len(T)>1: Q.append((f'What are the best alternatives to {top["name"]}?','In our ranking: '+'; '.join(f'#{i+2} {t["name"]} ({lc(t["use"])})' for i,t in enumerate(T[1:4]))+'.'))
  return Q
for c in d['categories']:
  title=f'Best {c["name"]} for Vibe Coders (2026) — VibePicks'
  desc=f'Ranked {c["name"].lower()} for builders shipping apps with AI: '+', '.join(t['name'] for t in c['tools'])+'.'
  # CollectionPage wrapper adds url, dateModified (filled in after the sitemap step) and a breadcrumb, which help search and AI answer engines cite a fresh, specific page
  cu=f'{S}/{c["id"]}/'
  il={"@type":"ItemList","name":f'Best {c["name"]}',"numberOfItems":len(c['tools']),"itemListOrder":"https://schema.org/ItemListOrderAscending","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"SoftwareApplication","name":t["name"],"url":t["url"],"applicationCategory":"DeveloperApplication","description":t["use"]}} for i,t in enumerate(c['tools'])]}
  ld={"@context":"https://schema.org","@type":"CollectionPage","name":title,"description":desc,"url":cu,"dateModified":LMPH,"isPartOf":{"@type":"WebSite","name":"VibePicks","url":f"{S}/"},"breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"VibePicks","item":f"{S}/"},{"@type":"ListItem","position":2,"name":c["name"],"item":cu}]},"mainEntity":il}
  # Quick answers: short visible Q&A built from the ranking, mirrored as FAQPage JSON-LD, so AI chatbots and answer engines can lift a direct, citable answer to "what's the best/free X?"
  FQ=faq(c); ld={"@context":"https://schema.org","@graph":[{k:v for k,v in ld.items() if k!="@context"},{"@type":"FAQPage","@id":cu+"#quick-answers","url":cu,"mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FQ]}]}
  FAQH='<section class="faq" id="quick-answers" aria-labelledby="qa-h"><h2 id="qa-h" style="font-size:1.15rem;margin:22px 2px 8px">Quick answers</h2>'+''.join(f'<details class="card" style="margin:8px 0;padding:12px 16px"><summary style="cursor:pointer;font-weight:600">{E(q)}</summary><p style="margin:8px 0 0">{E(a)}</p></details>' for q,a in FQ)+'</section>'
  body=f'<section class="hero" style="padding-bottom:10px"><div style="font-size:2.4rem">{c["icon"]}</div><h1>Best {E(c["name"])}</h1><p>Ranked editorial picks for vibe coders and builders.</p><p class="muted" style="font-size:.85rem">Page last updated <time datetime="{LMPH}">{LMPH}</time></p></section><div class="grid" style="grid-template-columns:1fr">'+''.join(tl(t,i) for i,t in enumerate(c['tools']))+'</div>'+FAQH+disc(any(any(k in t['name'] for k in ('Grok','Cursor','xAI')) for t in c['tools']),any(t.get('aff') for t in c['tools']))+'<p><a href="/">← All categories</a></p>'
  open(f'{c["id"]}/index.html' if os.makedirs(c['id'],exist_ok=True) is None else '','w').write(page(c['id'],title,desc,body,ld)); urls.append(f'/{c["id"]}/'); CATS.append(c['id'])
rel=''.join(f'<div class="release {"sample" if r.get("sample") else ""}"><span class="tag">{r["date"]}</span> <b>{E(r["tool"])}</b> — {E(r["title"])} <a href="{r["source"]}">source</a></div>' for r in d['releases'])
os.makedirs('releases',exist_ok=True)
# Releases JSON-LD: description, site link and breadcrumb so search and AI answer engines can place the page and cite it in context
open('releases/index.html','w').write(page('releases','New AI Tool Releases for Builders — VibePicks','Verified AI tool and model launches that matter to people shipping apps.','<h1>New releases</h1>'+rel,{"@context":"https://schema.org","@type":"CollectionPage","name":"New AI tool releases","description":"Verified AI tool and model launches that matter to people shipping apps, newest first, each with a source link.","url":f"{S}/releases/","isPartOf":{"@type":"WebSite","name":"VibePicks","url":f"{S}/"},"breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"VibePicks","item":f"{S}/"},{"@type":"ListItem","position":2,"name":"New releases","item":f"{S}/releases/"}]},"numberOfItems":len(d["releases"]),"dateModified":max((r["date"] for r in d["releases"]),default=None),"mainEntity":{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"NewsArticle","headline":f'{r["tool"]}: {r["title"]}',"datePublished":r["date"],"url":r["source"],"about":{"@type":"SoftwareApplication","name":r["tool"]}}} for i,r in enumerate(d["releases"])]}}))
# RSS feed of verified releases: lets feed readers, aggregators and AI answer engines pick up new launches without crawling the page
from email.utils import format_datetime
import datetime as _dt, hashlib
def _rd(x): return format_datetime(_dt.datetime.fromisoformat(x+'T12:00:00+00:00'))
_items=''.join(f'<item><title>{E(r["tool"])}: {E(r["title"][:120])}{"…" if len(r["title"])>120 else ""}</title><link>{E(r["source"])}</link><guid isPermaLink="false">vibepicks-release-{r["date"]}-{hashlib.sha1((r["tool"]+r["title"]).encode()).hexdigest()[:10]}</guid><pubDate>{_rd(r["date"])}</pubDate><category>{E(r["category"])}</category><description>{E(r["title"])}</description></item>' for r in d['releases'] if not r.get('sample'))
open('releases/feed.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>VibePicks: new AI tool releases</title><link>'+S+'/releases/</link><atom:link href="'+S+'/releases/feed.xml" rel="self" type="application/rss+xml"/><description>Verified AI tool and model launches that matter to people shipping apps, each with a source link.</description><language>en-us</language>'+(f'<lastBuildDate>{_rd(max(r["date"] for r in d["releases"]))}</lastBuildDate>' if d['releases'] else '')+_items+'</channel></rss>\n')
F49="https://buy.stripe.com/5kQ14o0FocjJgoFaBd3VC03"; N75="https://buy.stripe.com/6oU14o3RA97xfkBgZB3VC04"; TOP="https://buy.stripe.com/3cI6oIbk23Nd8WddNp3VC02"
PK=[("Featured listing","$49","/ 30 days","Your tool gets a highlighted card, labeled <b>Sponsored</b>, at the top of its category page for 30 days. Your normal ranking below stays the same.",F49,"Buy a featured listing — $49"),
("Newsletter sponsor","$75","/ issue","One sponsor section, labeled <b>Sponsored</b>, in one weekly issue of the VibePicks newsletter. Founding price, only 3 spots at this rate. The list is new: about 40 subscribers.",N75,"Sponsor the newsletter — $75")]
cards=''.join(f'<div class="card"><h3>{n}</h3><div style="font-size:1.8rem;font-weight:700">{pr}<span class="muted" style="font-size:1rem"> {u}</span></div><p class="muted">{dsc}</p><a class="btn" href="{l}" rel="noopener">{btn}</a></div>' for n,pr,u,dsc,l,btn in PK)
sbody=('<div id="thanks" class="card" style="display:none;border:2px solid #7c3aed"><b>Thanks, your payment went through.</b> We will email you within one business day at the address you used at checkout to get your placement set up.</div>'
'<section class="hero" style="padding-bottom:10px"><h1>Sponsor VibePicks</h1><p>Reach people choosing which AI tools to build with. Pay online in a minute, no back-and-forth.</p></section>'
'<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">'+cards+'</div>'
'<h2>How it works</h2><ol><li>Pick a package and pay through Stripe. Checkout asks for your email and your tool name and URL.</li><li>We email you within one business day to confirm the details and the start date or issue.</li><li>Your placement goes live, clearly labeled Sponsored.</li></ol>'
'<h2>Honest audience note</h2><p>VibePicks launched on October 15, 2026. The newsletter has about 40 subscribers and zero unsubscribes so far, and the site is small and growing. That is why these prices are low. Founding sponsors keep their rate as we grow.</p>'
f'<p class="muted">Also available: a pinned Category Top Spot above the rankings on one category page, $249/month. <a href="{TOP}" rel="noopener">Buy Category Top Spot</a></p>'
'<h2>Our rules</h2><ul><li>Every sponsored spot is clearly labeled <b>Sponsored</b>.</li><li>Some tool links are affiliate links, labeled <b>Affiliate link</b>. We may earn a commission if you sign up, at no extra cost to you. Affiliate deals never change rankings.</li><li>Sponsorship never changes editorial rankings. Rankings are our own picks.</li><li>'+DISCT+'</li><li>We may decline tools that are not a fit for builders, and refund in full if we do.</li></ul>'
'<p>Questions or custom deals: <a href="mailto:news@vibepicks.ai">news@vibepicks.ai</a></p>'
'<script>if(new URLSearchParams(location.search).get("thanks")==="1"){var t=document.getElementById("thanks");t.style.display="block";t.scrollIntoView()}</script>')
os.makedirs('sponsor',exist_ok=True)
open('sponsor/index.html','w').write(page('sponsor','Sponsor VibePicks — Reach Vibe Coders and Builders','Sponsor VibePicks: a $49 featured listing for 30 days or a $75 founding newsletter sponsor slot. Pay online. Always labeled, never changes rankings.',sbody,{"@context":"https://schema.org","@type":"WebPage","name":"Sponsor VibePicks"}))
urls.append('/sponsor/')
os.makedirs('build-it-for-me',exist_ok=True)
BIFM='<h1>Build it for me</h1>\n<p class="muted">For people who\'d rather not dig into AI tools and just want it built.</p>\n<div class="card bifm"><p>Tell us what you want built with AI and we\'ll build it.</p>\n<h2>Things we can build</h2><ul><li>A website</li><li>An online store or checkout</li><li>A newsletter</li><li>Automations that save time (forms, emails, scheduling)</li><li>A simple app or tool</li><li>AI set up for your business</li></ul>\n<h2>Pricing</h2><p>Everything gets a quote after a quick chat. One example:</p><ul><li>A one-page website from <b>$299</b>, one time</li><li>Live in about 48 hours</li><li>You own your domain</li><li>Free hosting</li><li>Optional $15/month if you want us to handle changes</li></ul>\n<p><a class="btn" href="/local/demo-wahmhoff/">See an example website</a></p></div>\n<h2>Tell us what you want built</h2>\n<form id="bifm" class="card bifm-form" novalidate>\n<label>Your name<input name="name" required maxlength="100" autocomplete="name"></label>\n<label>Business name<input name="business" required maxlength="120" autocomplete="organization"></label>\n<label>Email<input name="email" type="email" required maxlength="254" autocomplete="email"></label>\n<label>Phone <span class="muted">(optional)</span><input name="phone" type="tel" maxlength="40" autocomplete="tel"></label>\n<label>Town<input name="town" required maxlength="80"></label>\n<label>What do you want built?<textarea name="message" required maxlength="3000" rows="5"></textarea></label>\n<div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>\n<button class="btn" type="submit">Send</button><p id="bifm-msg" class="muted" role="status"></p>\n</form>\n<div id="bifm-thanks" class="card" style="display:none"><h2>Thanks, we got it.</h2><p>We\'ll get back to you soon.</p><p>VibePicks</p></div>\n<p class="muted">Rather email? <a href="mailto:tech@vibepicks.ai">tech@vibepicks.ai</a></p>\n<script>document.getElementById("bifm").addEventListener("submit",async function(e){e.preventDefault();var f=e.target,m=document.getElementById("bifm-msg"),b=f.querySelector("button");if(!f.reportValidity())return;b.disabled=true;m.textContent="Sending...";try{var r=await fetch("/api/build-request",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(Object.fromEntries(new FormData(f)))});var j=await r.json().catch(function(){return{}});if(r.ok&&j.ok){f.style.display="none";document.getElementById("bifm-thanks").style.display="block";return}m.textContent=j.error||"Something went wrong. Please email tech@vibepicks.ai."}catch(x){m.textContent="Something went wrong. Please email tech@vibepicks.ai."}b.disabled=false})</script>'
open('build-it-for-me/index.html','w').write(page('build-it-for-me','Build It For Me: Tell Us What You Want Built With AI | VibePicks','Rather not dig into AI tools? Tell VibePicks what you want built with AI (a website, store, newsletter, automations, a simple app) and we\'ll build it. One-page websites from $299.',BIFM,{"@context":"https://schema.org","@type":"Service","name":"Build it for me: custom AI builds","provider":{"@type":"Organization","name":"VibePicks"},"offers":{"@type":"Offer","price":"299","priceCurrency":"USD"}}))
urls.append('/build-it-for-me/')
urls.append('/guide/'); PAGES['/guide/']=open('guide/index.html').read()  # hand-written page, hashed for lastmod
# robots.txt never lists the guide download folder (that would publish its private path; it is noindexed via vercel.json headers instead)
# robots.txt names the main AI search and answer-engine crawlers explicitly (all allowed) and points them to llms.txt and the releases feed, so AI assistants can find, cite and recommend VibePicks pages
AIBOTS=['OAI-SearchBot','ChatGPT-User','GPTBot','Claude-SearchBot','Claude-User','ClaudeBot','PerplexityBot','Perplexity-User','Google-Extended','Applebot-Extended','xAI-Bot','DuckAssistBot','Amazonbot','meta-externalagent','MistralAI-User','CCBot']
open('robots.txt','w').write(f'User-agent: *\nAllow: /\n\n# AI search and answer engines are welcome. Plain-text summaries for them: {S}/llms.txt and {S}/llms-full.txt. New releases feed: {S}/releases/feed.xml\n'+''.join(f'User-agent: {b}\n' for b in AIBOTS)+'Allow: /\n\nSitemap: '+S+'/sitemap.xml\n')
L=['# VibePicks','> Editorial rankings of the best AI tools for vibe coders and builders shipping apps, grouped by use case. Ranks are editorial picks, not paid placements.','',f'Full version with every tool, pricing label, plain-English reason and release: {S}/llms-full.txt',f'Each category page also has a plain Markdown copy for AI agents, e.g. {S}/coding-agents/index.md',f'New releases as Markdown: {S}/releases/index.md',f'Agents can also ask for Markdown directly: request any category page (or the homepage) with the header Accept: text/markdown, e.g. curl -H "Accept: text/markdown" {S}/coding-agents/','Last updated: '+max((r['date'] for r in d['releases']),default=''),'']  # freshness signal for AI answer engines
for c in d['categories']:
  L+=[f'## {c["name"]} ({S}/{c["id"]}/)']+[f'{i+1}. [{t["name"]}]({t["url"]}): {t["use"]} ({t["pricing"]})' for i,t in enumerate(c['tools'])]+['']
L+=['## Recent releases']+[f'- {r["date"]}: {r["tool"]} — {r["title"]} ({r["source"]})' for r in d['releases']]
L+=['',f'Releases RSS feed: {S}/releases/feed.xml']
L+=['','## Sponsorship',f'Sponsored placements are always labeled and never change editorial rankings. Packages: {S}/sponsor/','','## Build it for me',f'Tell us what you want built with AI and we\'ll build it: websites, online stores and checkouts, newsletters, automations, simple apps, AI set up for your business. One-page websites from $299, everything else quoted after a quick chat: {S}/build-it-for-me/','','## Guide',f'Ready, Fire, Aim. ($9 PDF, 29 pages): how a machinist with little coding experience got a website, a newsletter and a checkout running with AI, step by step with 29 copy-paste prompts: {S}/guide/']
open('llms.txt','w').write('\n'.join(L)+'\n')
# llms-full.txt: the whole directory in one plain-text file for AI assistants and answer engines
CN={c['id']:c['name'] for c in d['categories']}; UPD=max((r['date'] for r in d['releases']),default='')
F=['# VibePicks (full directory)','> Every VibePicks ranking, tool, plain-English reason, pricing label and verified release in one file. Short index: '+S+'/llms.txt','',
f'Site: {S}/','Last updated: '+UPD,'About: VibePicks ranks AI tools for vibe coders, builders and non-coders by use case. #1 is our top pick in each category.',
'Pricing labels: Free = no paid tier needed; Freemium = usable free plan plus paid upgrades; Paid = paid plan or trial that converts to paid.','Rankings are editorial picks and are never sold. Sponsored placements are always labeled Sponsored.','']
for c in d['categories']:
  F+=[f'## {c["name"]}',f'Page: {S}/{c["id"]}/','']
  for i,t in enumerate(c['tools']):
    F+=[f'### #{i+1} {t["name"]}',f'- Website: {t["url"]}',f'- Pricing: {t["pricing"]}',f'- Use it for: {t["use"]}']+([f'- In plain English: {t["why"]}'] if t.get('why') else [])+['']
F+=['## Verified releases (newest first)',f'Page: {S}/releases/',f'RSS feed: {S}/releases/feed.xml','']+[f'- {r["date"]} | {r["tool"]} ({CN.get(r["category"],r["category"])}): {r["title"]}. Source: {r["source"]}' for r in d['releases']]
F+=['','## Contact','Newsletter and sponsorship: news@vibepicks.ai',f'Sponsor packages: {S}/sponsor/','Build requests: tech@vibepicks.ai',f'Build it for me (custom AI builds; one-page websites from $299): {S}/build-it-for-me/',f'Guide: Ready, Fire, Aim. ($9 PDF) on building a website, newsletter and checkout with AI, step by step: {S}/guide/']
open('llms-full.txt','w').write('\n'.join(F)+'\n')

import re
h=open('index.html').read()
blk='<!--catbar-->'+catbar()+'<!--/catbar-->'
h=re.sub(r'<!--catbar-->.*?<!--/catbar-->',lambda m:blk,h,flags=re.S) if '<!--catbar-->' in h else h.replace('</header>','</header>'+blk,1)
h=h if 'application/rss+xml' in h else h.replace('<link rel="canonical"','<link rel="alternate" type="application/rss+xml" title="VibePicks: new AI tool releases" href="/releases/feed.xml"><link rel="canonical"',1)
h=h if 'rel="icon"' in h else h.replace('<link rel="canonical"',ICON+'<link rel="canonical"',1)
# Home JSON-LD @graph: WebSite + Organization (publisher) + an ItemList of every category page, so search and AI answer engines can see who runs the site and map each use case to its ranked page
HLD={"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":f"{S}/#website","name":"VibePicks","url":f"{S}/","description":"Editorial rankings of the best AI tools for vibe coders and builders shipping apps, grouped by use case.","inLanguage":"en-US","publisher":{"@id":f"{S}/#org"}},{"@type":"Organization","@id":f"{S}/#org","name":"VibePicks","url":f"{S}/","logo":f"{S}/favicon.svg","email":"news@vibepicks.ai"},{"@type":"ItemList","@id":f"{S}/#categories","name":"VibePicks categories","numberOfItems":len(d['categories']),"itemListElement":[{"@type":"ListItem","position":i+1,"name":f'Best {c["name"]}',"url":f'{S}/{c["id"]}/'} for i,c in enumerate(d['categories'])]}]}
h=re.sub(r'<script type="application/ld\+json">.*?</script>',lambda m:'<script type="application/ld+json">'+json.dumps(HLD)+'</script>',h,count=1,flags=re.S)
open('index.html','w').write(h)

# sitemap.xml with <lastmod>: a page's date changes only when its generated content changes (hashes kept in lastmod.json)
import hashlib,datetime
from zoneinfo import ZoneInfo
TODAY=datetime.datetime.now(ZoneInfo('America/New_York')).date().isoformat()
PAGES['/']=h+json.dumps(d,sort_keys=True)  # homepage is rendered client-side from tools.json
LM=json.load(open('lastmod.json')) if os.path.exists('lastmod.json') else {}
for u in urls:
  hx=hashlib.sha256(PAGES[u].encode()).hexdigest()[:16]
  if LM.get(u,{}).get('h')!=hx: LM[u]={'h':hx,'d':TODAY}
open('lastmod.json','w').write(json.dumps({u:LM[u] for u in urls},indent=1)+'\n')
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{S}{u}</loc><lastmod>{LM[u]["d"]}</lastmod></url>' for u in urls)+'</urlset>\n')
# fill in the "last updated" date on category pages (visible text + CollectionPage dateModified)
for cid in CATS:
  fp=f'{cid}/index.html'; ph=open(fp).read(); open(fp,'w').write(ph.replace(LMPH,LM[f'/{cid}/']['d']))
# Markdown copy of each category ranking (linked from the page head via rel="alternate" type="text/markdown"), dated with the page's last-changed date
for c in d['categories']:
  M=[f'# Best {c["name"]} for Vibe Coders (2026)',f'> Ranked editorial picks from VibePicks. #1 is our top pick. Rankings are never sold; sponsored spots are always labeled.','',f'Page: {S}/{c["id"]}/',f'Last updated: {LM[f"/{c["id"]}/"]["d"]}','']
  for i,t in enumerate(c['tools']):
    M+=[f'## #{i+1} {t["name"]}',f'- Website: {t["url"]}',f'- Pricing: {t["pricing"]}',f'- Use it for: {t["use"]}']+([f'- In plain English: {t["why"]}'] if t.get('why') else [])+['']
  M+=['## Quick answers','']+[x for q,a in faq(c) for x in (f'**{q}**',a,'')]
  M+=[f'All categories: {S}/llms.txt',f'Full directory: {S}/llms-full.txt',f'New releases: {S}/releases/']
  open(f'{c["id"]}/index.md','w').write('\n'.join(M)+'\n')

# Markdown copy of the releases feed (/releases/index.md) so AI agents can read every verified launch, newest first, without parsing HTML
_RM=['# New AI tool releases for builders','> Verified AI tool and model launches that matter to people shipping apps, newest first, each with its source link. Curated by VibePicks.','',f'Page: {S}/releases/',f'RSS: {S}/releases/feed.xml','Last updated: '+max((r['date'] for r in d['releases']),default=''),'']
for r in d['releases']:
  if r.get('sample'): continue
  _RM+=[f'## {r["date"]}: {r["tool"]}',r['title'],f'- Category: {r["category"]}',f'- Source: {r["source"]}','']
_RM+=[f'All categories: {S}/llms.txt',f'Full directory: {S}/llms-full.txt']
open('releases/index.md','w').write('\n'.join(_RM)+'\n')

# vercel.json: Markdown content negotiation for AI agents. A request for a category page (or the homepage) whose Accept header asks for text/markdown
# gets the page's Markdown copy (homepage -> llms.txt) at the same URL; browsers still get HTML. Uses "routes" because they run before the static
# filesystem check (plain rewrites never fire for URLs a file already answers). Vary: Accept keeps caches from mixing the two versions.
MDH={"type":"header","key":"accept","value":".*text/markdown.*"}
CRE='|'.join([c['id'] for c in d['categories']]+['releases'])  # ids are lowercase letters and hyphens
MDT='text/markdown; charset=utf-8'
VJ={"routes":[
 {"src":"/guide/dl-0wrpqqzyzgvpzxiztpsw9a/(.*)","headers":{"X-Robots-Tag":"noindex, nofollow","Cache-Control":"private, no-store"},"continue":True},
 {"src":f"/({CRE})/index\\.md","headers":{"Content-Type":MDT,"Link":f'<{S}/$1/>; rel="canonical"'},"continue":True},
 {"src":f"/({CRE})/?","has":[MDH],"dest":"/$1/index.md","headers":{"Content-Type":MDT,"Vary":"Accept","Link":f'<{S}/$1/>; rel="canonical"'}},
 {"src":"/","has":[MDH],"dest":"/llms.txt","headers":{"Content-Type":MDT,"Vary":"Accept","Link":f'<{S}/>; rel="canonical"'}},
 {"src":f"/(({CRE})/?)?","headers":{"Vary":"Accept"},"continue":True},
]}
open('vercel.json','w').write(json.dumps(VJ,indent=2)+'\n')

// POST /api/recommend {q} -> {categories, picks, note}. Limited AI recommender via Vercel AI Gateway (OIDC auth).
// Cost controls are in-memory, best-effort (per instance): 10/hr per IP, 500/day global, LRU cache of identical queries. Stores no user text (cache is keyed by a hash).
const D = require('../tools.json');
const MODELS = (process.env.RECO_MODEL || 'google/gemini-2.5-flash-lite,openai/gpt-4.1-nano,openai/gpt-4o-mini,google/gemini-2.5-flash').split(',');
const NAMES = new Map(); D.categories.forEach(c => c.tools.forEach(t => NAMES.set(t.name.toLowerCase(), { name: t.name, cat: c.id })));
const LIST = D.categories.map(c => `${c.id} (${c.name}): ` + c.tools.map(t => `${t.name} - ${t.why || t.use}`).join('; ')).join('\n');
const SYS = `You are VibePicks' tool picker for non-coders. Only recommend tools from this list, using exact names:\n${LIST}\n
Reply with strict JSON only: {"categories":[slug...],"picks":[{"name":"...","why":"one short plain-English sentence"}],"note":"one plain-English tip sentence"}. Max 4 picks.
Only pick a tool if it truly does what the person wants. If nothing in the list really fits, return no picks and a short honest note saying VibePicks doesn't list a good tool for that yet. For Raspberry Pi (full Linux boards like Pi 4/5/Zero, not the Pi Pico), do not pick Arduino Cloud, Wokwi or Tinkercad; prefer ChatGPT for wiring and Python help, and Cursor or Claude Code for writing Python on the Pi. Wokwi simulates the Pi Pico only. Never write code. Never give build steps, plans or instructions. Never answer off-topic questions. If the request is not about choosing tools to make something, return {"categories":[],"picks":[],"note":"<polite one-sentence note that you only help pick tools>"}.`;
const ipHits = new Map(), cache = new Map(); let day = '', dayCount = 0;
module.exports = async (req, res) => {
  res.setHeader('Content-Type', 'application/json'); res.setHeader('Cache-Control', 'no-store');
  const send = (c, o) => { res.statusCode = c; res.end(JSON.stringify(o)); };
  if (req.method !== 'POST') return send(405, { ok: false });
  let b = req.body; if (typeof b === 'string') try { b = JSON.parse(b) } catch { b = {} }
  const q = String((b && b.q) || '').trim().slice(0, 300); if (!q) return send(400, { ok: false });
  const key = require('crypto').createHash('sha256').update(q.toLowerCase().replace(/\s+/g, ' ')).digest('hex'); if (cache.has(key)) return send(200, { ok: true, cached: true, ...cache.get(key) });
  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim(), now = Date.now();
  const h = (ipHits.get(ip) || []).filter(t => now - t < 3600e3); if (h.length >= 10) return send(429, { ok: false, error: 'rate' }); h.push(now); ipHits.set(ip, h);
  const today = new Date().toISOString().slice(0, 10); if (today !== day) { day = today; dayCount = 0 } if (++dayCount > 500) return send(429, { ok: false, error: 'cap' });
  const tok = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN || req.headers['x-vercel-oidc-token']; if (!tok) return send(503, { ok: false });
  try {
    let r, model;
    for (model of MODELS) {
      r = await fetch('https://ai-gateway.vercel.sh/v1/chat/completions', { method: 'POST', headers: { Authorization: `Bearer ${tok}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({ model, temperature: 0.2, max_tokens: 250, response_format: { type: 'json_object' }, messages: [{ role: 'system', content: SYS }, { role: 'user', content: q }] }) });
      if (r.ok) break;
      const t = await r.text().catch(() => ''); console.error('gateway', model, r.status, t.slice(0, 300));
      if (r.status !== 403 && r.status !== 404 && r.status !== 429) break;
    }
    if (!r.ok) return send(502, { ok: false, status: r.status });
    const j = await r.json(); let o = {}; try { o = JSON.parse(j.choices[0].message.content.replace(/^```(json)?|```$/g, '')) } catch { return send(502, { ok: false }) }
    const picks = (Array.isArray(o.picks) ? o.picks : []).map(p => ({ t: NAMES.get(String(p.name || '').toLowerCase()), why: String(p.why || '').slice(0, 200) })).filter(p => p.t).slice(0, 4).map(p => ({ name: p.t.name, why: p.why }));
    const cats = D.categories.map(c => c.id), categories = [...new Set([...(o.categories || []).filter(c => cats.includes(c)), ...picks.map(p => NAMES.get(p.name.toLowerCase()).cat)])];
    const out = { categories, picks, note: String(o.note || '').slice(0, 240), model };
    if (cache.size > 500) cache.delete(cache.keys().next().value); cache.set(key, out);
    return send(200, { ok: true, ...out });
  } catch (e) { console.error(e); return send(502, { ok: false }); }
};

// POST /api/build-request {name, business, email, phone?, town, message, website(honeypot)} -> emails tech@vibepicks.ai via Resend.
const RE = /^[^\s@]{1,64}@[^\s@]{1,255}\.[a-z]{2,}$/i;
const TO = 'tech@vibepicks.ai', FROM = 'VibePicks Build It For Me <tech@vibepicks.ai>';
const hits = new Map(); // best-effort per-instance rate limit: 5 per IP per hour
async function readBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  if (typeof req.body === 'string') { try { return JSON.parse(req.body); } catch { return Object.fromEntries(new URLSearchParams(req.body)); } }
  let s = ''; for await (const c of req) s += c;
  try { return JSON.parse(s || '{}'); } catch { return Object.fromEntries(new URLSearchParams(s)); }
}
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const clean = (v, n) => String(v || '').replace(/[\r\n]+/g, ' ').trim().slice(0, n);
module.exports = async (req, res) => {
  res.setHeader('Content-Type', 'application/json'); res.setHeader('Cache-Control', 'no-store');
  const send = (code, obj) => { res.statusCode = code; res.end(JSON.stringify(obj)); };
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return send(405, { ok: false, error: 'Method not allowed' }); }
  const body = await readBody(req);
  if (body.website) return send(200, { ok: true }); // honeypot
  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'x', now = Date.now();
  const list = (hits.get(ip) || []).filter(t => now - t < 3600e3);
  if (list.length >= 5) return send(429, { ok: false, error: 'Too many requests. Please email tech@vibepicks.ai instead.' });
  const name = clean(body.name, 100), business = clean(body.business, 120), email = clean(body.email, 254).toLowerCase(),
    phone = clean(body.phone, 40), town = clean(body.town, 80), message = String(body.message || '').trim().slice(0, 3000);
  if (!name || !business || !town || !message) return send(400, { ok: false, error: 'Please fill in your name, business, town and what you need.' });
  if (!RE.test(email)) return send(400, { ok: false, error: 'Please enter a valid email address.' });
  const key = process.env.RESEND_API_KEY;
  if (!key) return send(500, { ok: false, error: 'The form is temporarily unavailable. Please email tech@vibepicks.ai.' });
  list.push(now); hits.set(ip, list);
  const rows = [['Name', name], ['Business', business], ['Email', email], ['Phone', phone || '(none)'], ['Town', town]];
  const text = rows.map(r => `${r[0]}: ${r[1]}`).join('\n') + `\n\nWhat they want built:\n${message}\n\nSent from vibepicks.ai/build-it-for-me/`;
  const html = rows.map(r => `<p><b>${r[0]}:</b> ${esc(r[1])}</p>`).join('') + `<p><b>What they want built:</b></p><p style="white-space:pre-wrap">${esc(message)}</p><p style="color:#888">Sent from vibepicks.ai/build-it-for-me/</p>`;
  try {
    const r = await fetch('https://api.resend.com/emails', { method: 'POST', headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from: FROM, to: [TO], reply_to: email, subject: `Build it for me: ${business}`, text, html }) });
    if (r.ok) return send(200, { ok: true });
    console.error('resend error', r.status, await r.text().catch(() => ''));
  } catch (e) { console.error(e); }
  return send(502, { ok: false, error: 'Could not send right now. Please email tech@vibepicks.ai.' });
};

// POST /api/subscribe  {email, company?}  -> adds contact to the VibePicks Newsletter segment in Resend. Never sends email.
const RE = /^[^\s@]{1,64}@[^\s@]{1,255}\.[a-z]{2,}$/i;
const SEGMENT = process.env.RESEND_SEGMENT_ID || 'a2cf110e-f237-4a91-aa22-d5064d972ed0';
async function readBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  if (typeof req.body === 'string') { try { return JSON.parse(req.body); } catch { return {}; } }
  let s = ''; for await (const c of req) s += c;
  try { return JSON.parse(s || '{}'); } catch { return Object.fromEntries(new URLSearchParams(s)); }
}
module.exports = async (req, res) => {
  res.setHeader('Content-Type', 'application/json'); res.setHeader('Cache-Control', 'no-store');
  const send = (code, obj) => { res.statusCode = code; res.end(JSON.stringify(obj)); };
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return send(405, { ok: false, error: 'Method not allowed' }); }
  const body = await readBody(req);
  if (body.company) return send(200, { ok: true }); // honeypot: pretend success for bots
  const email = String(body.email || '').trim().toLowerCase();
  if (email.length > 254 || !RE.test(email)) return send(400, { ok: false, error: 'Please enter a valid email address.' });
  const key = process.env.RESEND_API_KEY;
  if (!key) return send(500, { ok: false, error: 'Signup is temporarily unavailable.' });
  const h = { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' };
  try {
    let r = await fetch('https://api.resend.com/contacts', { method: 'POST', headers: h, body: JSON.stringify({ email, unsubscribed: false, segments: [{ id: SEGMENT }] }) });
    if (r.ok) {
      // Welcome email: fire the Resend event only for brand-new contacts, and only when WELCOME_ENABLED=1 is set in Vercel.
      // The matching Resend automation ("VibePicks welcome email") must also be enabled for anything to send.
      if (process.env.WELCOME_ENABLED === '1') {
        try {
          await fetch('https://api.resend.com/events/send', { method: 'POST', headers: h, body: JSON.stringify({ event: 'newsletter.subscribed', email, payload: { source: 'site' } }) });
        } catch (e) { console.error('welcome event failed', e); }
      }
      return send(200, { ok: true });
    }
    const err = await r.json().catch(() => ({}));
    if (r.status === 409 || /exist/i.test(err.message || '')) {
      r = await fetch(`https://api.resend.com/contacts/${encodeURIComponent(email)}/segments/${SEGMENT}`, { method: 'POST', headers: h });
      if (r.ok || r.status === 409) return send(200, { ok: true, already: true });
    }
    console.error('resend error', r.status, JSON.stringify(err));
    return send(502, { ok: false, error: 'Could not subscribe right now. Please try again.' });
  } catch (e) {
    console.error(e); return send(502, { ok: false, error: 'Could not subscribe right now. Please try again.' });
  }
};

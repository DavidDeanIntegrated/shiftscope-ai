// ShiftScope AI static site generator. Zero dependencies (Node 18+).
// Usage: node build.mjs            -> dist/ at site root "/"
//        BASE=/shiftscope/ node build.mjs   -> for GitHub Pages project sites
import fs from "node:fs";
import path from "node:path";

const BASE = (process.env.BASE || "/").replace(/\/?$/, "/");
const SITE_URL = (process.env.SITE_URL || "").replace(/\/$/, "");
const OUT = "dist";
const tools = JSON.parse(fs.readFileSync("data/tools.json", "utf8"));
const cats = JSON.parse(fs.readFileSync("data/categories.json", "utf8"));
const catBy = Object.fromEntries(cats.map(c => [c.slug, c]));
const site = JSON.parse(fs.readFileSync("data/site.json", "utf8"));

for (const t of tools) {
  if (!catBy[t.category]) throw new Error(`Unknown category ${t.category} on ${t.slug}`);
  if (t.physician_review !== null || t.ratings !== null) throw new Error(`${t.slug}: physician review/ratings must stay empty until a real review exists`);
}

const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const u = p => BASE + p.replace(/^\//, "");
const host = url => { try { return new URL(url).hostname.replace(/^www\./, ""); } catch { return url; } };

function layout({ title, desc, body, pathName }) {
  const nav = [["", "Directory"], ["categories/", "Categories"], ["methodology/", "How we review"], ["newsletter/", "Newsletter"], ["submit/", "Submit a tool"], ["sponsor/", "Sponsor"], ["about/", "About"]];
  return `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}">
${SITE_URL ? `<link rel="canonical" href="${SITE_URL}${u(pathName)}">` : ""}
<meta property="og:title" content="${esc(title)}"><meta property="og:description" content="${esc(desc)}">
<link rel="icon" href="${u("assets/favicon.svg")}" type="image/svg+xml">
<link rel="stylesheet" href="${u("assets/style.css")}">
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap hdr">
  <a class="logo" href="${u("")}"><span class="logo-mark" aria-hidden="true">◎</span> ShiftScope <b>AI</b></a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav"><ul>${nav.map(([h, l]) => `<li><a href="${u(h)}"${pathName === h ? ' aria-current="page"' : ""}>${l}</a></li>`).join("")}</ul></nav>
</div></header>
<main id="main">${body}</main>
<footer class="site-footer"><div class="wrap">
  <p class="disclaimer"><strong>For clinicians. Not medical advice.</strong> ShiftScope AI is an independent directory for healthcare professionals evaluating software. Listings describe vendor products using public sources and are not endorsements, clinical recommendations, or a substitute for your institution's procurement, privacy, and clinical governance review. Always verify vendor claims, FDA status, and BAA terms directly. <a href="${u("disclaimer/")}">Full disclaimer</a>.</p>
  <p class="small">Sponsors never affect verdicts. Sponsored placements are always labeled. <a href="${u("methodology/")}#ads">Ad &amp; conflict-of-interest policy</a> · Data last verified ${esc(site.lastVerified)} · © ${new Date().getFullYear()} ShiftScope AI</p>
</div></footer>
<script src="${u("assets/app.js")}" defer></script>
</body></html>`;
}

function card(t) {
  const c = catBy[t.category];
  const fda = t.fda_authorized ? `<span class="badge fda" title="Has at least one FDA clearance or De Novo authorization; see listing for scope">FDA-authorized</span>` : "";
  const free = t.free_tier ? `<span class="badge free">Free tier</span>` : "";
  return `<article class="card" data-cat="${t.category}" data-text="${esc([t.name, t.company, t.tagline, c.name, ...t.features, ...t.ehr_integrations].join(" ").toLowerCase())}">
  <div class="card-top"><a class="cat-pill" href="${u(`categories/${c.slug}/`)}">${esc(c.short)}</a>${fda}${free}</div>
  <h3><a href="${u(`tools/${t.slug}/`)}">${esc(t.name)}</a></h3>
  <p class="company">${esc(t.company)}</p>
  <p>${esc(t.tagline)}</p>
  <p class="review-pending">Physician review coming soon</p>
</article>`;
}

const newsletterForm = (id = "nl") => `<form class="newsletter" id="${id}" data-stub="true" onsubmit="return false">
  <label for="${id}-email">Get the weekly <em>What's new in ED AI</em> email</label>
  <div class="row"><input id="${id}-email" type="email" placeholder="you@hospital.org" autocomplete="email" required><button type="submit">Subscribe</button></div>
  <p class="stub-note" role="note">Demo form: not connected yet, so nothing is sent or stored. The newsletter is launching soon.</p>
  <p class="form-msg" aria-live="polite"></p>
</form>`;

const sponsoredSlot = `<aside class="sponsored-slot" aria-label="Sponsored placement">
  <span class="sponsored-label">Sponsored</span>
  <p><strong>This space is open.</strong> Sponsored placements are always labeled like this and never change a verdict, rating, or ranking. <a href="${u("sponsor/")}">Sponsor ShiftScope AI</a></p>
</aside>`;

function home() {
  const chips = [`<button class="chip active" data-filter="all" aria-pressed="true">All (${tools.length})</button>`]
    .concat(cats.map(c => `<button class="chip" data-filter="${c.slug}" aria-pressed="false">${esc(c.short)} (${tools.filter(t => t.category === c.slug).length})</button>`)).join("");
  return layout({
    title: "ShiftScope AI: AI tools for the emergency department, judged by EM physicians",
    desc: "An EM-specific directory of AI scribes, clinical Q&A, ECG AI, imaging triage, POCUS AI and sepsis tools, judged against how a real ED shift works.",
    pathName: "",
    body: `<section class="hero"><div class="wrap">
  <p class="eyebrow">Built by an emergency medicine resident physician</p>
  <h1>AI tools for the ED, judged against a real shift.</h1>
  <p class="lede">Interruptions, six open charts, a trauma in bay 3, a loud room and a clunky EHR. ShiftScope AI lists the AI tools emergency clinicians actually run into and checks them against ED-specific criteria, not marketing copy.</p>
  <div class="hero-stats"><span><b>${tools.length}</b> tools tracked</span><span><b>${cats.length}</b> categories</span><span><b>0</b> paid verdicts, ever</span></div>
</div></section>
<section class="wrap directory" aria-labelledby="dir-h">
  <h2 id="dir-h">Directory</h2>
  <div class="controls">
    <label class="sr" for="q">Search tools</label>
    <input id="q" type="search" placeholder="Search: scribe, Epic, PE, sepsis, free…" autocomplete="off">
    <div class="chips" role="group" aria-label="Filter by category">${chips}</div>
  </div>
  <p class="status" id="count" aria-live="polite">${tools.length} tools</p>
  <div class="grid" id="grid">${tools.map(card).join("")}</div>
  <p class="empty" id="empty" hidden>No tools match. Know one we're missing? <a href="${u("submit/")}">Submit a tool</a>.</p>
</section>
<section class="wrap split">
  <div class="panel">${newsletterForm("nl-home")}</div>
  ${sponsoredSlot}
</section>
<section class="wrap how"><h2>What we look at</h2><ul class="criteria-mini">
${site.criteria.map(c => `<li><b>${esc(c.name)}</b><span>${esc(c.short)}</span></li>`).join("")}
</ul><p><a href="${u("methodology/")}">Read the full review method →</a></p></section>`
  });
}

function list(arr) { return arr && arr.length ? `<ul>${arr.map(x => `<li>${esc(x)}</li>`).join("")}</ul>` : `<p class="unknown">Unknown</p>`; }

function toolPage(t) {
  const c = catBy[t.category];
  const crit = site.criteria.map(cr => `<tr><th scope="row">${esc(cr.name)}</th><td class="pending">${esc(t.ed_criteria[cr.key] || "Not yet evaluated")}</td></tr>`).join("");
  const related = tools.filter(x => x.category === t.category && x.slug !== t.slug).slice(0, 3);
  return layout({
    title: `${t.name} for emergency medicine | ShiftScope AI`,
    desc: `${t.name} by ${t.company}: ${t.tagline}`,
    pathName: `tools/${t.slug}/`,
    body: `<div class="wrap tool">
<nav class="crumbs" aria-label="Breadcrumb"><a href="${u("")}">Directory</a> › <a href="${u(`categories/${c.slug}/`)}">${esc(c.name)}</a> › <span>${esc(t.name)}</span></nav>
<header class="tool-head">
  <h1>${esc(t.name)}</h1>
  <p class="company">by ${esc(t.company)} · <a href="${esc(t.url)}" rel="nofollow noopener" target="_blank">${esc(host(t.url))} ↗</a></p>
  <p class="lede">${esc(t.tagline)}</p>
</header>
<section class="verdict-box" aria-labelledby="v-h">
  <h2 id="v-h">Physician verdict</h2>
  <p class="review-pending big">Physician review coming soon</p>
  <p class="small">No rating has been assigned. We don't publish scores until an EM physician has evaluated the tool against our <a href="${u("methodology/")}">ED criteria</a>.</p>
</section>
<div class="tool-grid">
<section><h2>Key features <span class="src-note">(as described by vendor and sources)</span></h2>${list(t.features)}</section>
<section><h2>Facts at a glance</h2><dl class="facts">
  <dt>Category</dt><dd><a href="${u(`categories/${c.slug}/`)}">${esc(c.name)}</a></dd>
  <dt>EHR integrations</dt><dd>${list(t.ehr_integrations)}</dd>
  <dt>Pricing (public)</dt><dd>${esc(t.pricing)}</dd>
  <dt>HIPAA / BAA</dt><dd>${esc(t.hipaa_baa)}</dd>
  <dt>FDA status</dt><dd>${esc(t.fda_status)}</dd>
  <dt>Last verified</dt><dd>${esc(t.last_verified)}</dd>
</dl></section>
</div>
${t.ed_specific_vendor_claims.length ? `<section><h2>ED-specific claims <span class="src-note">(vendor-stated, not independently verified)</span></h2>${list(t.ed_specific_vendor_claims)}</section>` : ""}
<section><h2>ED criteria scorecard</h2><table class="criteria"><tbody>${crit}</tbody></table></section>
<section><h2>Published evidence</h2>${t.studies.length ? `<ul>${t.studies.map(s => `<li><a href="${esc(s.url)}" rel="noopener" target="_blank">${esc(s.title)}</a></li>`).join("")}</ul>` : `<p class="unknown">No peer-reviewed studies linked yet. Know one? <a href="${u("submit/")}">Tell us</a>.</p>`}</section>
${t.notes ? `<section><h2>Notes</h2><p>${esc(t.notes)}</p></section>` : ""}
<section><h2>Sources</h2><ol class="sources">${t.sources.map(s => `<li><a href="${esc(s)}" rel="noopener nofollow" target="_blank">${esc(s)}</a></li>`).join("")}</ol>
<p class="small">Facts were taken from these public sources on ${esc(t.last_verified)}. Vendors change pricing and features often, so confirm with the vendor before you buy. Spot an error? <a href="${u("submit/")}">Send a correction</a>.</p></section>
${related.length ? `<section><h2>More in ${esc(c.name)}</h2><div class="grid">${related.map(card).join("")}</div></section>` : ""}
</div>`
  });
}

function catPage(c) {
  const ts = tools.filter(t => t.category === c.slug);
  return layout({
    title: `${c.name} for emergency medicine | ShiftScope AI`, desc: c.blurb, pathName: `categories/${c.slug}/`,
    body: `<div class="wrap"><nav class="crumbs"><a href="${u("")}">Directory</a> › <a href="${u("categories/")}">Categories</a> › <span>${esc(c.name)}</span></nav>
<h1>${esc(c.name)}</h1><p class="lede">${esc(c.blurb)}</p><p class="status">${ts.length} tools</p>
<div class="grid">${ts.map(card).join("")}</div></div>`
  });
}

function catIndex() {
  return layout({
    title: "Categories | ShiftScope AI", desc: "Browse ED AI tools by category.", pathName: "categories/",
    body: `<div class="wrap"><h1>Categories</h1><div class="grid">${cats.map(c => `<article class="card"><h3><a href="${u(`categories/${c.slug}/`)}">${esc(c.name)}</a></h3><p>${esc(c.blurb)}</p><p class="small">${tools.filter(t => t.category === c.slug).length} tools</p></article>`).join("")}</div></div>`
  });
}

function mdPage(file, pathName, title, desc, extra = "") {
  const html = fs.readFileSync(`src/pages/${file}`, "utf8").replaceAll("{{BASE}}", BASE)
    .replace("{{NEWSLETTER_FORM}}", newsletterForm("nl-page")).replace("{{SPONSORED_SLOT}}", sponsoredSlot)
    .replace("{{CRITERIA}}", site.criteria.map(c => `<li><b>${esc(c.name)}.</b> ${esc(c.long)}</li>`).join(""))
    .replace("{{TOOL_COUNT}}", String(tools.length));
  return layout({ title: `${title} | ShiftScope AI`, desc, pathName, body: `<div class="wrap prose">${html}${extra}</div>` });
}

// ---- write
fs.rmSync(OUT, { recursive: true, force: true });
const write = (p, s) => { const f = path.join(OUT, p); fs.mkdirSync(path.dirname(f), { recursive: true }); fs.writeFileSync(f, s); };
write("index.html", home());
for (const t of tools) write(`tools/${t.slug}/index.html`, toolPage(t));
write("categories/index.html", catIndex());
for (const c of cats) write(`categories/${c.slug}/index.html`, catPage(c));
const pages = [
  ["methodology.html", "methodology/", "How we review", "Our ED-specific review criteria, physician review process, and ad and conflict-of-interest policy."],
  ["submit.html", "submit/", "Submit a tool", "Suggest an AI tool for emergency clinicians, or send a correction."],
  ["sponsor.html", "sponsor/", "Sponsor / Advertise", "Reach emergency physicians, residents and APPs evaluating AI tools."],
  ["about.html", "about/", "About", "ShiftScope AI is built by an emergency medicine resident physician."],
  ["newsletter.html", "newsletter/", "Newsletter", "What's new in ED AI, weekly."],
  ["disclaimer.html", "disclaimer/", "Disclaimer", "Medical and editorial disclaimer."],
];
for (const [f, p, t, d] of pages) write(`${p}index.html`, mdPage(f, p, t, d));
write("404.html", layout({ title: "Not found | ShiftScope AI", desc: "Page not found", pathName: "404", body: `<div class="wrap prose"><h1>Page not found</h1><p><a href="${u("")}">Back to the directory</a></p></div>` }));
for (const f of fs.readdirSync("src/assets")) write(`assets/${f}`, fs.readFileSync(`src/assets/${f}`));
write("data/tools.json", JSON.stringify(tools));
write("robots.txt", `User-agent: *\nAllow: /\n${SITE_URL ? `Sitemap: ${SITE_URL}${u("sitemap.xml")}\n` : ""}`);
const urls = ["", "categories/", ...cats.map(c => `categories/${c.slug}/`), ...tools.map(t => `tools/${t.slug}/`), ...pages.map(p => p[1])];
write("sitemap.xml", `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(p => `<url><loc>${SITE_URL || ""}${u(p)}</loc></url>`).join("\n")}\n</urlset>\n`);
write(".nojekyll", "");
console.log(`Built ${tools.length} tools, ${cats.length} categories, ${urls.length} URLs -> ${OUT}/ (BASE=${BASE})`);

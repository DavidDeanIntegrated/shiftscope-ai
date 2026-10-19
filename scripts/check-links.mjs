// Verifies every internal href/src in dist/ resolves to a file under the configured BASE path.
// Usage: BASE=/shiftscope-ai/ node scripts/check-links.mjs   (defaults to "/")
import fs from "node:fs"; import path from "node:path";
const BASE = (process.env.BASE || "/").replace(/\/?$/, "/");
const root = "dist"; let bad = 0, n = 0;
const walk = d => fs.readdirSync(d, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(path.join(d, e.name)) : [path.join(d, e.name)]);
for (const f of walk(root).filter(f => f.endsWith(".html"))) {
  const html = fs.readFileSync(f, "utf8");
  for (const m of html.matchAll(/(?:href|src)="(\/[^"#?]*)/g)) {
    n++;
    if (!m[1].startsWith(BASE)) { bad++; console.log(`OUTSIDE BASE ${m[1]} in ${f}`); continue; }
    let p = path.join(root, m[1].slice(BASE.length)); if (m[1].endsWith("/")) p = path.join(p, "index.html");
    if (!fs.existsSync(p)) { bad++; console.log(`BROKEN ${m[1]} in ${f}`); }
  }
}
console.log(`${n} internal links checked under ${BASE}, ${bad} broken`); process.exit(bad ? 1 : 0);

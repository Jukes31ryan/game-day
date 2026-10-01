/* Render an edition's icon.svg to the three PNG sizes a PWA needs.
     node tools/render_icons.mjs editions/liam
   Uses the Playwright Chromium the tests already rely on. */
import { chromium } from '../tests/lib.mjs';
import { readFileSync } from 'node:fs';
const dir = process.argv[2];
if (!dir) { console.error('usage: node tools/render_icons.mjs editions/<name>'); process.exit(2); }
const svg = readFileSync(dir + '/icon.svg', 'utf8');
const b = await chromium.launch();
for (const size of [512, 192, 180]) {
  const p = await (await b.newContext({ viewport: { width: size, height: size } })).newPage();
  await p.setContent('<html><body style="margin:0">' +
    svg.replace('width="512" height="512"', 'width="' + size + '" height="' + size + '"') + '</body></html>');
  await p.screenshot({ path: dir + '/icon-' + size + '.png', clip: { x: 0, y: 0, width: size, height: size } });
}
await b.close();
console.log('rendered icons in ' + dir);

# Regweb hero — dashbord (kilde)

Kilde til `assets/img/regweb-hero-{800,1200,1600}.{webp,jpg}` (grafkort + betalingskort med «Motta betaling»).

- `hero.html` — hele bildet som HTML/CSS/SVG (Inter fra `fonts/`). Grafen tegnes av et lite skript nederst (tallene i `v`-listen er illustrative).
- `render.mjs` — `node render.mjs ut.png` rendrer 2336×1314 (puppeteer-core + Chrome).
- `hero-master-2336x1314.png` — ferdig master. Nettversjonene lages slik: `sips -Z <bredde> -s format jpeg -s formatOptions 88 master.png --out regweb-hero-<bredde>.jpg` og `cwebp -q 84 regweb-hero-<bredde>.jpg -o regweb-hero-<bredde>.webp` (800, 1200, 1600).
- `ekstra/` — tidligere forsøk: laptop-mockup med ekte skjermbilde (r002-delt-hero), skript som fjernet logoen fra variant 14 (polynomflate + korn), folke-utsnitt fra variant 17.

Alle tall, navnet «Kari Nordmann» og «+18 % fra i fjor» er illustrative.

## Innhold i mappen (alt samlet, 2026-10-12)

| Mappe/fil | Hva |
|---|---|
| `hero.html`, `render.mjs`, `fonts/`, `logoer/` | Dashbord-heroet. Logoer: Vipps-ordmerke #FF5B24 (fra Dropbox `BILDER.VIPPS`), Visa-merke (standard betalingsikon), Mastercard-symbol (samme som klopp.no) |
| `hero-master-2336x1314.png` | Ferdig master (rendret av `hero.html`) |
| `varianter/` | De 17 bildene Richard genererte (`Regweb-Forsidebilde-01…17.jpg`) |
| `ekstra/` | Delt hero med bærbar PC (`laptop-mockup.html`, `render-laptop.mjs`, skjermbildet `regweb-medlemseditor-skjermbilde-1995x1065.png` + `editor_1600.png`), folke-utsnitt fra variant 17, skript som fjernet logoen fra variant 14 |

Kopi også i Dropbox: `F_MEDIA/BILDER/Medlemssystem-2026/Regweb-hero-dashbord-kilde/`. Mappen er i git (`.gitignore` åpner kun for denne undermappen; PSD-filer i `design-source/` er fortsatt utelatt). Merk: GitHub Pages publiserer alt i repoet, også denne mappen.

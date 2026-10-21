# regweb-no-web

Nettsiden til regweb.no (Regweb medlemssystem), statisk HTML/CSS/JS, hostet hos Domeneshop (se «Deploy til produksjon»). Samme rammeverk, farger og stil som klopp.no.

Lokal URL: http://regweb-no.example/ (Laradock-vhost, mappe `/Users/boss/development/regweb-no-web`).

## Deploy til produksjon (regweb.no)

Produksjon er Domeneshop-hosting (`/home/5/r/regweb/www/`), ikke GitHub Pages. Et bare-repo på serveren (`/home/5/r/regweb/regweb-no-web.git`) har en `post-receive`-hook som synkroniserer grenen `main` til `www` med `rsync --delete`. Hooken utelater `design-source/`, `.claude/`, `README.md`, `CNAME`, `.nojekyll`, `.gitignore` og `assets/img/original/`.

```bash
git remote add produksjon ssh://regweb@login.domeneshop.no/home/5/r/regweb/regweb-no-web.git   # én gang
git push produksjon <lokal-gren>:main                                                           # deploy
ssh regweb@login.domeneshop.no 'DRYRUN=1 /home/5/r/regweb/regweb-no-web.git/hooks/post-receive' # tørrkjør
```

Verifiser alltid med en fersk spørrestreng (`https://regweb.no/?v=<tid>`): nginx foran serveren bufrer. Kopi av hooken ligger i `design-source/hero-dashbord-2026/ekstra/post-receive`.

## BETA-merke

Merke for funksjoner som er i beta (kolbe + «BETA», lyst turkis ramme, oransje tekst). Brukes mange steder.

| Bruk | Hvordan |
|---|---|
| På et kort (liten, 24 px) | `<span class="beta-badge" title="Beta-funksjon">BETA</span>`. Ligg sammen med andre merker i `<div class="ex-tags">…</div>` øverst til høyre i kortet (se «Telefonkatalog-oppslag» på `/funksjoner/`). |
| Stor (48 px, f.eks. overskrift) | `<span class="beta-badge beta-badge-lg">BETA</span>` |
| Utenfor siden (Canva, Facebook, brosjyre) | `assets/img/beta-merke.svg` (vektor) eller `beta-merke-1680x640.png` / `beta-merke-840x320.png` (gjennomsiktig) |

Merket følger lys og mørk modus (CSS-variablene `--beta-teal`, `--beta-text`, `--beta-bg` i `css/site.css`). Teksten er mørkere oransje (`#b4540a`) i selve siden for å holde 4,5:1 kontrast; SVG/PNG bruker merkevarens oransje `#f08a2c`. Skal merket bak et bilde eller på farget bunn, bruk SVG/PNG-en.

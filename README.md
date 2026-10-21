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

Merke for funksjoner som er i beta (oransje pille med kolbe og hvit «BETA»-tekst). Brukes mange steder.

| Bruk | Hvordan |
|---|---|
| På et kort (liten, 24 px) | `<span class="beta-badge" title="Beta-funksjon">BETA</span>`. Ligg sammen med andre merker i `<div class="ex-tags">…</div>` øverst til høyre i kortet (se «Telefonkatalog-oppslag» på `/funksjoner/`). |
| Stor (48 px, f.eks. overskrift) | `<span class="beta-badge beta-badge-lg">BETA</span>` |
| Utenfor siden (Canva, Facebook, brosjyre) | `assets/img/beta-merke.svg` (vektor) eller `beta-merke-1680x640.png` / `beta-merke-840x320.png` (gjennomsiktig) |

Merket er oransje flate med hvit tekst og kolbe (samme i lys og mørk modus). Liten størrelse bruker `#c2540a` (hvit tekst får 4,6:1 kontrast); stor og SVG/PNG bruker `#e0731a` (stor tekst, 3,2:1). Merkevare-oransjen `#f08a2c` er for lys til hvit tekst (2,5:1).
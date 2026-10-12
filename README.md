# regweb-no-web

Nettsiden til regweb.no (Regweb medlemssystem), statisk HTML/CSS/JS på GitHub Pages. Samme rammeverk, farger og stil som klopp.no.

Lokal URL: http://regweb-no.example/ (Laradock-vhost, mappe `/Users/boss/development/regweb-no-web`).

## Deploy til produksjon (regweb.no)

Produksjon er Domeneshop-hosting (`/home/5/r/regweb/www/`), ikke GitHub Pages. Et bare-repo på serveren (`/home/5/r/regweb/regweb-no-web.git`) har en `post-receive`-hook som synkroniserer grenen `main` til `www` med `rsync --delete`. Hooken utelater `design-source/`, `.claude/`, `README.md`, `CNAME`, `.nojekyll`, `.gitignore` og `assets/img/original/`.

```bash
git remote add produksjon ssh://regweb@login.domeneshop.no/home/5/r/regweb/regweb-no-web.git   # én gang
git push produksjon <lokal-gren>:main                                                           # deploy
ssh regweb@login.domeneshop.no 'DRYRUN=1 /home/5/r/regweb/regweb-no-web.git/hooks/post-receive' # tørrkjør
```

Verifiser alltid med en fersk spørrestreng (`https://regweb.no/?v=<tid>`): nginx foran serveren bufrer. Kopi av hooken ligger i `design-source/hero-dashbord-2026/ekstra/post-receive`.

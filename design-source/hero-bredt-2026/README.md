# Regweb hero, bredt bilde (2026-10-21)

Grå perm med oransje Regweb-etikett og en blyant, studiolys. Brukes som hero på regweb.no og skal kunne brukes i andre sammenhenger.

## Kilde og oppløsning

| Fil | Innhold |
|---|---|
| `regweb-perm-original-studio.jpg` | Originalbildet (1984 × 992, Richards studiobilde). **Dette er den høyeste ekte oppløsningen vi har.** |
| `regweb-perm-og-blyant-utklipp.png` | Perm og blyant utklippet med gjennomsiktig bakgrunn (1984 × 992, samme piksler som originalen). |
| `hero-bredt-master-3200x1242.jpg` | Hero-masteren (originalen utvidet til høyre, 1,25 × oppskalert). |
| `formater/…-native.png/jpg` | Formater beskåret fra originalen uten oppskalering. |
| `formater/…-interpolert.jpg` | Oppskalert (Lanczos) til trykk/storskjerm. Ingen ny detalj: skarphet som 1984 px-originalen. |
| `buildP.py`, `cut.py`, `cut2.py`, `lag-formater.py` | Skriptene som lager utvidelsen, utklippet og alle formatene (Python, OpenCV, Pillow). |

For ekte høyere oppløsning (A4-trykk, stor plakat): be om en ny rendering i minst 4000 px fra samme kilde som `regweb-perm-original-studio.jpg`.

## Formater (`formater/`)

| Bruk | Fil | Størrelse |
|---|---|---|
| Hero på nettsiden (2,58:1) | `regweb-hero-bredt-3200x1242.jpg` (også i `assets/img/regweb-hero-bredt-{1200,1600,2400,3200}.{jpg,webp}`) | 3200 × 1242 |
| Hero, native / stor | `regweb-hero-bredt-2550x989-native.jpg`, `regweb-hero-bredt-6400x2484-interpolert.jpg` | 2550 × 990 / 6400 × 2484 |
| 16:9 (presentasjon, YouTube) | `regweb-hero-16x9-1920x1080.jpg`, `…-3840x2160-interpolert.jpg`, `…-1764x992-native.jpg` | 1920 × 1080 / 3840 × 2160 |
| Kvadrat (profil, innlegg) | `regweb-hero-1x1-1080.jpg`, `…-2048-interpolert.jpg`, `…-992-native.jpg` | 1080 / 2048 |
| 4:5 (Facebook/Instagram) | `regweb-hero-4x5-1080x1350.jpg`, `…-1600x2000-interpolert.jpg`, `…-794x992-native.jpg` | 1080 × 1350 |
| 9:16 (stories) | `regweb-hero-9x16-1080x1920.jpg`, `…-558x992-native.jpg` | 1080 × 1920 |
| Delingsbilde (og:image) | `regweb-hero-delingsbilde-1200x630.jpg` (også i `assets/img/`), `…-2400x1260-interpolert.jpg` | 1200 × 630 |
| Utvidet lerret uten beskjæring | `regweb-hero-utvidet-2550x992-native.png` | 2550 × 992 |
| Utklipp med gjennomsiktig bakgrunn | `regweb-perm-og-blyant-utklipp-gjennomsiktig-native.png` | 1984 × 992 |

## Nettfiler

Produksjon får kun `assets/img/regweb-hero-bredt-*` og `regweb-hero-delingsbilde-1200x630.jpg`; `design-source/` publiseres ikke.

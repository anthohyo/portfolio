# Portfolio — Anthony Bayard

Page unique (HTML/CSS, sans framework) qui présente trois projets en ligne :
KichtApp, Vista et VB Databox, plus un profil et un contact.

## Fichiers

- `public/index.html` — la page finale, autonome (images intégrées en base64). C'est le seul fichier publié.
- `src/template.html` — le texte, la mise en page et le style. **C'est ici qu'on modifie le contenu.**
- `src/img/` — les captures d'écran et le portrait (webp).
- `build.py` — recolle le template et les images pour régénérer `public/index.html`.
- `wrangler.jsonc` — config Cloudflare : publie uniquement le dossier `public/`.

## Modifier la page

1. Éditer `src/template.html` (ou remplacer une image dans `src/img/`, avec le même nom).
2. Lancer `python3 build.py`.
3. Commit + push : le site se met à jour tout seul.

## Publier (Cloudflare Workers)

Le repo est connecté à Cloudflare : chaque push sur `main` redéploie le site automatiquement.
L'adresse est `https://portfolio.anthony-bayard69.workers.dev`.

Seul le dossier `public/` est publié (voir `wrangler.jsonc`). Ne pas remettre `"directory": "."`,
sinon le dossier `.git` et les sources deviennent téléchargeables sur le site.

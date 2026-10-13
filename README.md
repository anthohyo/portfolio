# Portfolio — Anthony Bayard

Page unique (HTML/CSS, sans framework) qui présente trois projets en ligne :
KichtApp, Vista et VB Databox, plus un profil et un contact.

## Fichiers

- `index.html` — la page finale, autonome (images intégrées en base64). C'est ce fichier qui est publié.
- `src/template.html` — le texte, la mise en page et le style. **C'est ici qu'on modifie le contenu.**
- `src/img/` — les captures d'écran et le portrait (webp).
- `build.py` — recolle le template et les images pour régénérer `index.html`.

## Modifier la page

1. Éditer `src/template.html` (ou remplacer une image dans `src/img/`, avec le même nom).
2. Lancer `python3 build.py`.
3. Commit + push : le site se met à jour tout seul.

## Publier (GitHub Pages, gratuit)

Settings → Pages → Source : *Deploy from a branch* → branche `main`, dossier `/ (root)` → Save.
L'adresse sera `https://anthohyo.github.io/portfolio/` (compter 1 à 2 minutes la première fois).

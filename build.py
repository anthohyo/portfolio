"""Régénère index.html à partir de src/template.html + src/img/*.webp.

Usage : python3 build.py
Le résultat (index.html, à la racine) est une page autonome : les images sont
intégrées en base64, il n'y a rien d'autre à héberger.
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"

IMAGES = {
    "{{IMG_ME}}": "moi.webp",
    "{{IMG_KICHT}}": "kicht2.webp",
    "{{IMG_VISTA}}": "vista.webp",
    "{{IMG_VB}}": "vb4.webp",
}

DESC = ("Portfolio d'Anthony Bayard : KichtApp, Vista et VB Databox, "
        "trois projets en ligne, et son profil.")

HEAD_OPEN = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{DESC}">
<meta property="og:title" content="Portfolio Anthony Bayard">
<meta property="og:description" content="{DESC}">
<meta property="og:type" content="website">
"""

html = (SRC / "template.html").read_text(encoding="utf-8")
for placeholder, name in IMAGES.items():
    data = base64.b64encode((SRC / "img" / name).read_bytes()).decode("ascii")
    html = html.replace(placeholder, f"data:image/webp;base64,{data}")

marker = '<header class="top">'
head, body = html.split(marker, 1)
out = HEAD_OPEN + head.rstrip() + "\n</head>\n<body>\n" + marker + body.rstrip("\n") + "\n</body>\n</html>\n"

(ROOT / "index.html").write_text(out, encoding="utf-8")
print(f"index.html écrit ({len(out) // 1024} Ko)")

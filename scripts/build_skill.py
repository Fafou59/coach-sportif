#!/usr/bin/env python3
"""Construit le skill `coach` importable sur claude.ai.

- copie skill/coach/ vers dist/coach/ ;
- copie docs/referentiel/00 à 09 dans dist/coach/references/referentiel/,
  avec un sommaire des règles en tête de chaque fichier de plus de 100 lignes ;
- vérifie le frontmatter de SKILL.md (name, description ≤ 200 caractères),
  sa longueur (< 500 lignes) et que chaque lien relatif pointe vers un fichier ;
- zippe dist/coach/ en dist/coach.zip, dossier coach/ à la racine.

Usage : python scripts/build_skill.py   (Python 3, bibliothèque standard seulement)
"""

import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "skill" / "coach"
REFERENTIEL = ROOT / "docs" / "referentiel"
DIST = ROOT / "dist"
OUT = DIST / "coach"
ZIP = DIST / "coach.zip"

MAX_DESCRIPTION = 200
MAX_LINES = 500
SOMMAIRE_SEUIL = 100
RULE_HEADING = re.compile(r"^\*\*(\d+)\.\s*(.+?)\*\*")
LINK = re.compile(r"\]\(([^)#\s]+)\)")


def fail(message):
    print(f"ÉCHEC : {message}")
    sys.exit(1)


def copy_skill():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(SRC, OUT)


def with_sommaire(text):
    """Insère un sommaire des règles (lignes « **N. ») sous le titre H1."""
    lines = text.splitlines()
    if len(lines) <= SOMMAIRE_SEUIL:
        return text
    rules = [f"- {m.group(1)}. {m.group(2).strip()}"
             for m in (RULE_HEADING.match(line) for line in lines) if m]
    if not rules:
        return text
    sommaire = ["", "## Sommaire", "", *rules, ""]
    title = 1 if lines and lines[0].startswith("# ") else 0
    return "\n".join(lines[:title] + sommaire + lines[title:]) + "\n"


def copy_referentiel():
    target = OUT / "references" / "referentiel"
    target.mkdir(parents=True, exist_ok=True)
    files = sorted(REFERENTIEL.glob("0[0-9]-*.md"))
    if len(files) != 10:
        fail(f"10 fichiers 00 à 09 attendus dans {REFERENTIEL}, {len(files)} trouvés")
    for source in files:
        text = source.read_text(encoding="utf-8")
        (target / source.name).write_text(with_sommaire(text), encoding="utf-8", newline="\n")
    return [f.name for f in files]


def check_skill_md():
    text = (OUT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("frontmatter YAML absent de SKILL.md")
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"').strip("'")
    if fields.get("name") != "coach":
        fail(f"name doit valoir « coach » (trouvé : {fields.get('name')!r})")
    description = fields.get("description", "")
    if not description or len(description) > MAX_DESCRIPTION:
        fail(f"description de {len(description)} caractères (1 à {MAX_DESCRIPTION} attendus)")
    count = len(text.splitlines())
    if count >= MAX_LINES:
        fail(f"SKILL.md fait {count} lignes (moins de {MAX_LINES} attendues)")
    return description, count


def check_links():
    """Chaque lien relatif d'un fichier .md doit pointer vers un fichier du build."""
    missing = []
    for md in OUT.rglob("*.md"):
        for target in LINK.findall(md.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("mailto:"):
                continue
            if not (md.parent / target).resolve().exists():
                missing.append(f"{md.relative_to(OUT).as_posix()} -> {target}")
    return missing


def build_zip():
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(OUT.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(DIST).as_posix())
    with zipfile.ZipFile(ZIP) as archive:
        names = archive.namelist()
    if "coach/SKILL.md" not in names or any("\\" in n or not n.startswith("coach/") for n in names):
        fail("structure du ZIP incorrecte")
    return names


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    copy_skill()
    referentiel = copy_referentiel()
    description, count = check_skill_md()
    missing = check_links()
    # Liens du référentiel vers des notes de recherche ou la cartographie non embarquées :
    # tolérés (signalés), seuls les liens de SKILL.md et des procédures sont bloquants.
    blocking = [m for m in missing if not m.startswith("references/referentiel/")]
    for item in missing:
        print(f"{'ÉCHEC' if item in blocking else 'note'} : lien sans cible {item}")
    if blocking:
        fail("liens cassés dans le skill")
    names = build_zip()
    print(f"OK : SKILL.md {count} lignes, description {len(description)} caractères")
    print(f"OK : {len(referentiel)} fichiers du référentiel copiés")
    print(f"OK : {ZIP.relative_to(ROOT).as_posix()} ({len(names)} fichiers)")
    for name in names:
        print(f"  {name}")


if __name__ == "__main__":
    main()

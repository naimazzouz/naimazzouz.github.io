#!/usr/bin/env python3
"""
Standardise les headers des simulations PC en convertissant les
`background: #XXXXXX` en `background: linear-gradient(135deg, #XXXXXX, #darker)`.

Approche : pour chaque header avec une couleur plate, on calcule une
version 25% plus sombre et on construit le gradient.
"""

from __future__ import annotations

import re
from pathlib import Path

# Sims à traiter (celles identifiées sans gradient)
TARGETS = [
    "atome-couches.html",
    "modeles-atome.html",
    "liaisons-chimiques.html",
    "concentration.html",
    "oxydoreduction.html",
    "pile-electrochimique.html",
    "circuit-electrique.html",
    "ohm.html",
    "puissance.html",
    "transformateur.html",
    "effet-joule.html",
    "redressement.html",
    "moteur.html",
    "transmission-info.html",
    "vitesse-acceleration.html",
    "pression.html",
    "debit.html",
    "boyle-mariotte.html",
    "gaz.html",
    "chaleur.html",
    "transferts-thermiques.html",
    "changement-etat.html",
    "rayonnement.html",
    "sources-lumineuses.html",
    "melangeur.html",
    "son.html",
    "son-2nde.html",
    # atome.html est traité séparément (cas particulier)
]


def darken(hex_color: str, factor: float = 0.75) -> str:
    """Renvoie la couleur hex assombrie (0..1, 0.75 = 25% plus sombre)."""
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r = int(int(h[0:2], 16) * factor)
    g = int(int(h[2:4], 16) * factor)
    b = int(int(h[4:6], 16) * factor)
    return f"#{r:02x}{g:02x}{b:02x}"


# Pattern : header { ... background: #XXXXXX; ... } ou background-color
# On capture la sélection complète du selecteur header pour s'assurer
# qu'on modifie le bon bloc.
HEADER_BLOCK_RE = re.compile(
    r"(header\s*\{[^}]*?background(?:-color)?\s*:\s*)(#[0-9a-fA-F]{3,6})(\s*;)",
    re.IGNORECASE,
)


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    def repl(m):
        prefix, color, suffix = m.group(1), m.group(2), m.group(3)
        # Si le bloc contient déjà un gradient, ne pas toucher
        # (mais le pattern n'aurait pas matché de toute façon)
        darker = darken(color)
        new = f"{prefix}linear-gradient(135deg, {color}, {darker}){suffix}"
        return new

    text = HEADER_BLOCK_RE.sub(repl, text, count=1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    sims_dir = repo_root / "simulations"
    changed = 0
    skipped = 0
    for name in TARGETS:
        path = sims_dir / name
        if not path.exists():
            print(f"  ⚠  {name}: introuvable")
            continue
        if process(path):
            print(f"  ✓ {name}")
            changed += 1
        else:
            print(f"  − {name} (pattern non matché)")
            skipped += 1
    print(f"\n{changed} fichiers modifiés, {skipped} non modifiés")


if __name__ == "__main__":
    main()

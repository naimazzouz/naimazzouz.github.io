#!/usr/bin/env python3
"""
Ajoute le bloc <div class="objectifs"> dans les 15 lecon.html qui n'en ont pas,
avec des objectifs alignés sur les programmes officiels (Maths Seconde Bac Pro,
Maths CAP, Maths BTS).
"""

from __future__ import annotations

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Objectifs par chapitre (curés à partir des programmes officiels)
# ---------------------------------------------------------------------------

OBJECTIVES = {
    # ─── MATHS SECONDE BAC PRO (programme 2019) ──────────────────────────
    "maths/seconde/ch03": [
        "Calculer et interpréter les indicateurs de position : moyenne, médiane, quartiles",
        "Calculer et interpréter les indicateurs de dispersion : étendue, écart-type, écart interquartile",
        "Construire et lire un diagramme en boîte à moustaches",
        "Comparer et interpréter plusieurs séries statistiques",
    ],
    "maths/seconde/ch07": [
        "Reconnaître une fonction définie par une expression, un tableau ou une courbe",
        "Calculer l'image d'un nombre par une fonction",
        "Déterminer un antécédent par lecture graphique ou par calcul",
        "Décrire les variations d'une fonction sur un intervalle",
    ],
    "maths/seconde/ch08": [
        "Reconnaître une fonction linéaire et déterminer son coefficient",
        "Représenter graphiquement une fonction linéaire",
        "Faire le lien entre proportionnalité et fonction linéaire",
        "Résoudre des problèmes de proportionnalité par la fonction linéaire",
    ],
    "maths/seconde/ch10": [
        "Connaître la fonction carré f(x) = x² et tracer sa parabole",
        "Identifier les variations de la fonction carré (décroissante puis croissante)",
        "Reconnaître l'allure d'une fonction du type f(x) = ax² + bx + c",
        "Déterminer graphiquement le sommet d'une parabole",
    ],
    "maths/seconde/ch11": [
        "Calculer le périmètre des figures usuelles (carré, rectangle, triangle, cercle, polygones)",
        "Calculer l'aire des figures usuelles",
        "Convertir les unités d'aire (m², cm², dm²)",
        "Résoudre des problèmes de surface en contexte professionnel",
    ],
    "maths/seconde/ch13": [
        "Reconnaître les configurations de Thalès (directe et papillon)",
        "Appliquer l'égalité des rapports pour calculer une longueur",
        "Utiliser la réciproque du théorème de Thalès pour démontrer un parallélisme",
        "Résoudre des problèmes géométriques en situation professionnelle",
    ],

    # ─── MATHS CAP (programme 2019) ──────────────────────────────────────
    "maths/cap/ch01": [
        "Recueillir et organiser des données statistiques",
        "Calculer la moyenne, la médiane et l'étendue d'une série",
        "Représenter des données par un diagramme adapté (bâtons, secteurs)",
        "Interpréter des indicateurs statistiques en contexte",
    ],
    "maths/cap/ch02": [
        "Distinguer fréquence et probabilité",
        "Calculer la probabilité d'un événement dans un cas simple",
        "Utiliser un tableau ou un arbre pour dénombrer les issues",
        "Interpréter un résultat de probabilité dans la vie quotidienne",
    ],
    "maths/cap/ch03": [
        "Reconnaître une situation de proportionnalité",
        "Compléter un tableau de proportionnalité",
        "Calculer un pourcentage d'une quantité",
        "Appliquer un taux d'évolution (augmentation, réduction)",
    ],
    "maths/cap/ch04": [
        "Tester si un nombre est solution d'une équation",
        "Résoudre une équation du type ax + b = cx + d",
        "Mettre en équation un problème simple",
        "Vérifier la cohérence d'une solution dans le contexte",
    ],
    "maths/cap/ch05": [
        "Lire l'image et l'antécédent sur un graphique",
        "Calculer l'image d'un nombre par une fonction donnée par une expression",
        "Lire et compléter un tableau de valeurs",
        "Reconnaître une fonction linéaire ou affine",
    ],
    "maths/cap/ch06": [
        "Calculer le périmètre et l'aire des figures usuelles",
        "Calculer le volume des solides usuels (pavé, cylindre)",
        "Utiliser le théorème de Pythagore",
        "Résoudre des problèmes géométriques en contexte professionnel",
    ],
    "maths/cap/ch07": [
        "Effectuer des calculs avec nombres décimaux et fractionnaires",
        "Utiliser les puissances de 10 et la notation scientifique",
        "Maîtriser les priorités opératoires sur une calculatrice",
        "Estimer et arrondir un résultat avec un nombre de chiffres significatifs adapté",
    ],

    # ─── MATHS BTS ───────────────────────────────────────────────────────
    "maths/bts/ch07": [
        "Connaître la définition et les propriétés de la transformée de Laplace",
        "Calculer la transformée de fonctions usuelles à l'aide d'un formulaire",
        "Utiliser la linéarité et le théorème du retard",
        "Résoudre une équation différentielle linéaire à l'aide de la transformée de Laplace",
    ],
    "maths/bts/ch09": [
        "Calculer une probabilité conditionnelle",
        "Utiliser la formule des probabilités totales",
        "Reconnaître l'indépendance de deux événements",
        "Modéliser une situation à l'aide d'un arbre pondéré",
    ],
}


def html_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_objectives_div(items: list[str]) -> str:
    items_html = "\n".join(f"  <li>{html_escape(it)}</li>" for it in items)
    return f"""
<div class="objectifs">
  <strong>Objectifs du chapitre :</strong>
  <ul>
{items_html}
  </ul>
</div>
"""


# Pattern : injecter juste après </header>
HEADER_END_RE = re.compile(r"</header>\s*", re.IGNORECASE)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    added = 0
    skipped = 0

    for chapter_path, items in OBJECTIVES.items():
        lecon = repo_root / chapter_path / "lecon.html"
        if not lecon.exists():
            print(f"  ⚠  {chapter_path}: lecon.html introuvable")
            continue

        content = lecon.read_text(encoding="utf-8")

        # Idempotence : si déjà un bloc objectifs, skip
        if re.search(r'<div\s+class="objectifs"', content, re.IGNORECASE):
            print(f"  − {chapter_path}: déjà des objectifs")
            skipped += 1
            continue

        block = build_objectives_div(items)
        m = HEADER_END_RE.search(content)
        if not m:
            print(f"  ⚠  {chapter_path}: pas de </header>")
            continue

        idx = m.end()
        new_content = content[:idx] + block + content[idx:]
        lecon.write_text(new_content, encoding="utf-8")
        print(f"  ✓ {chapter_path}: bloc objectifs ajouté ({len(items)} items)")
        added += 1

    print(f"\n{added} ajouts · {skipped} skippés")


if __name__ == "__main__":
    main()

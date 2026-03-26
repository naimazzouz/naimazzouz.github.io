#!/usr/bin/env python3
"""
check_chapters.py — Vérifie la complétude des chapitres du site.

Pour chaque chapitre, vérifie la présence des fichiers obligatoires et optionnels.
Affiche un rapport avec les fichiers manquants.

Usage :
    python3 scripts/check_chapters.py              # rapport complet
    python3 scripts/check_chapters.py --missing    # seulement les chapitres incomplets
    python3 scripts/check_chapters.py --section maths/terminale  # une section précise
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Fichiers obligatoires pour tous les chapitres (hors BTS)
REQUIRED = ['lecon.html', 'exercices.html', 'ds.html']

# Fichiers recommandés (signalés mais pas bloquants)
RECOMMENDED = ['fiche.html', 'qcm.html', 'interro.html']

# Fichiers optionnels (informatifs uniquement)
OPTIONAL = ['activite.html', 'simulation.html', 'exercices-capacites.html']

# Sections à analyser : (chemin relatif, utilise_diff, label)
SECTIONS = [
    ('maths/seconde',                True,  'Maths Seconde'),
    ('maths/premiere',               True,  'Maths Première'),
    ('maths/terminale',              True,  'Maths Terminale'),
    ('maths/bts',                    False, 'Maths BTS'),
    ('physique-chimie/seconde',      True,  'PC Seconde'),
    ('physique-chimie/premiere-iccer', True, 'PC Première ICCER'),
    ('physique-chimie/premiere-era', True,  'PC Première ERA'),
    ('physique-chimie/terminale-iccer', True, 'PC Terminale ICCER'),
    ('physique-chimie/terminale-era', True, 'PC Terminale ERA'),
]

ONLY_MISSING = '--missing' in sys.argv
FILTER_SECTION = None
if '--section' in sys.argv:
    idx = sys.argv.index('--section')
    if idx + 1 < len(sys.argv):
        FILTER_SECTION = sys.argv[idx + 1]


def check_chapter(chapter_path, required, recommended, optional):
    """Retourne un dict avec les fichiers présents/manquants."""
    files = set(os.listdir(chapter_path))
    return {
        'missing_required':     [f for f in required    if f not in files],
        'missing_recommended':  [f for f in recommended if f not in files],
        'present_optional':     [f for f in optional    if f in files],
        'missing_optional':     [f for f in optional    if f not in files],
        'all_files':            sorted(files),
    }


def check_section(section_path, label, uses_diff):
    """Analyse tous les chapitres d'une section."""
    full_path = os.path.join(ROOT, section_path)
    if not os.path.isdir(full_path):
        return

    chapters = sorted([
        d for d in os.listdir(full_path)
        if os.path.isdir(os.path.join(full_path, d)) and d.startswith('ch')
    ])

    if not chapters:
        return

    total = len(chapters)
    complete = 0
    issues = []

    for ch in chapters:
        ch_path = os.path.join(full_path, ch)
        result = check_chapter(ch_path, REQUIRED, RECOMMENDED, OPTIONAL)

        is_complete = (
            len(result['missing_required']) == 0 and
            len(result['missing_recommended']) == 0
        )
        if is_complete:
            complete += 1

        if result['missing_required'] or result['missing_recommended'] or not ONLY_MISSING:
            issues.append((ch, result))

    # Affichage section
    status = 'OK' if complete == total else f'{complete}/{total}'
    print(f'\n{"="*60}')
    print(f'  {label}  [{status}]')
    print(f'  Chemin : {section_path}')
    if not uses_diff:
        print(f'  (BTS — pas de différenciation)')
    print(f'{"="*60}')

    for ch, result in issues:
        has_issue = result['missing_required'] or result['missing_recommended']
        if ONLY_MISSING and not has_issue:
            continue

        line = f'  {ch} :'
        if not result['missing_required'] and not result['missing_recommended']:
            opt = result['present_optional']
            line += f' OK  [optionnels présents : {", ".join(opt) if opt else "aucun"}]'
        else:
            if result['missing_required']:
                line += f'\n    MANQUANT (obligatoire) : {", ".join(result["missing_required"])}'
            if result['missing_recommended']:
                line += f'\n    manquant (recommandé)  : {", ".join(result["missing_recommended"])}'
            if result['present_optional']:
                line += f'\n    optionnels présents    : {", ".join(result["present_optional"])}'
        print(line)

    return {'total': total, 'complete': complete}


def main():
    print('check_chapters.py — Rapport de complétude des chapitres')
    print(f'Racine : {ROOT}')
    if ONLY_MISSING:
        print('Mode : chapitres incomplets uniquement (--missing)')
    if FILTER_SECTION:
        print(f'Filtre : {FILTER_SECTION}')

    grand_total = 0
    grand_complete = 0

    for section_path, uses_diff, label in SECTIONS:
        if FILTER_SECTION and FILTER_SECTION not in section_path:
            continue
        result = check_section(section_path, label, uses_diff)
        if result:
            grand_total += result['total']
            grand_complete += result['complete']

    print(f'\n{"="*60}')
    print(f'  TOTAL SITE : {grand_complete}/{grand_total} chapitres complets')
    print(f'  (obligatoires + recommandés : lecon, exercices, ds, fiche, qcm, interro)')
    print(f'{"="*60}\n')


if __name__ == '__main__':
    main()

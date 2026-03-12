#!/usr/bin/env python3
"""
add_print_css.py — Ajoute <link rel="stylesheet" href="print.css" media="print">
dans toutes les pages HTML du site qui référencent déjà styles.css.

Usage :
    python3 scripts/add_print_css.py          # mode dry-run (affiche seulement)
    python3 scripts/add_print_css.py --apply   # applique les modifications
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY_RUN = '--apply' not in sys.argv


def get_print_css_href(styles_href):
    """Dérive le chemin vers print.css à partir du chemin vers styles.css."""
    # ../../../styles.css → ../../../print.css
    # ../styles.css → ../print.css
    # styles.css → print.css
    return styles_href.replace('styles.css', 'print.css')


def process_file(filepath):
    """Ajoute la référence à print.css si elle n'y est pas déjà."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Déjà présent ?
    if 'print.css' in content:
        return False

    # Chercher la ligne avec styles.css
    match = re.search(
        r'(<link\s+rel="stylesheet"\s+href="([^"]*styles\.css)"[^>]*>)',
        content
    )
    if not match:
        return False

    styles_tag = match.group(1)
    styles_href = match.group(2)
    print_href = get_print_css_href(styles_href)
    print_tag = f'<link rel="stylesheet" href="{print_href}" media="print">'

    new_content = content.replace(
        styles_tag,
        f'{styles_tag}\n{print_tag}'
    )

    if not DRY_RUN:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return True


def main():
    mode = 'DRY-RUN' if DRY_RUN else 'APPLY'
    print(f'Mode : {mode}')
    print(f'Racine : {ROOT}\n')

    modified = 0
    skipped = 0

    for dirpath, _, filenames in os.walk(ROOT):
        # Ignorer node_modules, .git, pdf/generated
        rel = os.path.relpath(dirpath, ROOT)
        if any(part in ['.git', 'node_modules'] for part in rel.split(os.sep)):
            continue
        if rel.startswith(os.path.join('pdf', 'generated')):
            continue

        for filename in filenames:
            if not filename.endswith('.html'):
                continue

            filepath = os.path.join(dirpath, filename)
            relpath = os.path.relpath(filepath, ROOT)

            if process_file(filepath):
                print(f'  + {relpath}')
                modified += 1
            else:
                skipped += 1

    print(f'\n{modified} fichier(s) {"modifié(s)" if not DRY_RUN else "à modifier"}')
    print(f'{skipped} fichier(s) ignoré(s) (déjà présent ou pas de styles.css)')

    if DRY_RUN and modified > 0:
        print('\nPour appliquer : python3 scripts/add_print_css.py --apply')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Injecte un bloc « Objectifs du chapitre » sur chaque page de ressource
(exercices, DS, QCM, interro, fiche, simulation) qui n'en a pas déjà un.

Stratégie
---------
1. Pour chaque chapitre, extraire les objectifs depuis lecon.html
   (le bloc <div class="objectifs">).
2. Pour chaque page-cible du chapitre, vérifier si elle a déjà un bloc
   d'objectifs. Si non, injecter un bloc compact « .objectifs-rappel »
   après le </header>.
3. Idempotent : on marque l'injection avec un commentaire HTML
   <!-- objectifs-rappel:auto --> pour ne pas dupliquer si on relance.

Pages-cibles : exercices.html, ds.html, qcm.html, interro.html,
              fiche.html, simulation.html
Pages laissées intactes : lecon.html, index.html, activite.html,
                          exercices-capacites.html (objectifs déjà
                          présents et chapitre-spécifiques)
"""

from __future__ import annotations

import glob
import html as _html
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TARGET_PAGES = [
    "exercices.html",
    "ds.html",
    "qcm.html",
    "interro.html",
    "fiche.html",
    "simulation.html",
]

SECTIONS = [
    "maths/seconde",
    "maths/premiere",
    "maths/terminale",
    "maths/lgt-terminale",
    "maths/cap",
    "maths/bts",
    "physique-chimie/seconde",
    "physique-chimie/premiere-iccer",
    "physique-chimie/premiere-era",
    "physique-chimie/terminale-iccer",
    "physique-chimie/terminale-era",
    "physique-chimie/cap",
]

INJECTION_MARKER = "<!-- objectifs-rappel:auto -->"

# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

OBJECTIFS_RE = re.compile(
    r'<div\s+class="objectifs"[^>]*>(.*?)</div>',
    re.DOTALL | re.IGNORECASE,
)
LI_RE = re.compile(r"<li[^>]*>(.*?)</li>", re.DOTALL)


def strip_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = _html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract_objectifs_items(lecon_text: str) -> list[str]:
    """Extrait la liste des items d'objectifs du chapitre depuis lecon.html.

    Cherche le premier <div class="objectifs">…</div> qui contient des <li>.
    """
    for match in OBJECTIFS_RE.finditer(lecon_text):
        inner = match.group(1)
        items = LI_RE.findall(inner)
        if items:
            return [strip_html(li) for li in items]
    return []


def html_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


# ---------------------------------------------------------------------------
# Détection de bloc objectifs existant
# ---------------------------------------------------------------------------

ALREADY_HAS_OBJ_RE = re.compile(
    r'<div\s+class="(?:[^"]*\s)?objectifs(?:\s[^"]*)?"',
    re.IGNORECASE,
)


def has_existing_objectives(content: str) -> bool:
    """Indique si le contenu a déjà un bloc objectifs (de quelque type)."""
    return bool(ALREADY_HAS_OBJ_RE.search(content))


# ---------------------------------------------------------------------------
# Construction du bloc à injecter
# ---------------------------------------------------------------------------


def build_objectives_block(items: list[str]) -> str:
    """Construit le bloc HTML d'objectifs du chapitre, compact et identifiable."""
    if not items:
        return ""

    items_html = "\n".join(f"      <li>{html_escape(it)}</li>" for it in items)
    return f"""
{INJECTION_MARKER}
<details class="objectifs-rappel" style="margin:14px 0 22px;border:1px solid var(--p-border,#bee3f8);border-radius:8px;background:var(--p-bg,#ebf5ff);padding:0">
  <summary style="cursor:pointer;padding:10px 16px;font-weight:600;color:var(--p,#0056b3);list-style:none;display:flex;align-items:center;gap:8px">
    <span style="font-size:1.1em">🎯</span> Objectifs du chapitre
    <span style="margin-left:auto;font-size:.8em;font-weight:400;opacity:.7">cliquer pour développer</span>
  </summary>
  <ul style="margin:0;padding:6px 16px 14px 36px;font-size:.92em;color:#334155">
{items_html}
  </ul>
</details>
"""


# ---------------------------------------------------------------------------
# Injection
# ---------------------------------------------------------------------------

# On injecte juste après </header>
HEADER_END_RE = re.compile(r"</header>\s*", re.IGNORECASE)


def inject_after_header(content: str, block: str) -> tuple[str, bool]:
    """Insère le bloc juste après </header>. Si pas de </header>, fallback
    après <div class="c">."""
    if INJECTION_MARKER in content:
        return content, False

    m = HEADER_END_RE.search(content)
    if m:
        idx = m.end()
        return content[:idx] + block + content[idx:], True

    # Fallback : après l'ouverture <div class="c">
    div_c = re.search(r'<div\s+class="c">\s*', content, re.IGNORECASE)
    if div_c:
        idx = div_c.end()
        return content[:idx] + block + content[idx:], True

    return content, False


# ---------------------------------------------------------------------------
# Boucle principale
# ---------------------------------------------------------------------------


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    chapters_processed = 0
    pages_modified = 0
    pages_skipped_existing = 0
    pages_skipped_no_obj = 0
    chapters_no_obj = 0

    for section in SECTIONS:
        chapter_dirs = sorted((repo_root / section).glob("ch*"))
        for ch_dir in chapter_dirs:
            lecon = ch_dir / "lecon.html"
            if not lecon.exists():
                continue

            lecon_text = lecon.read_text(encoding="utf-8")
            items = extract_objectifs_items(lecon_text)

            if not items:
                chapters_no_obj += 1
                # On peut ne pas traiter ce chapitre faute d'objectifs
                continue

            chapters_processed += 1
            block = build_objectives_block(items)

            for page_name in TARGET_PAGES:
                page = ch_dir / page_name
                if not page.exists():
                    continue

                content = page.read_text(encoding="utf-8")

                if has_existing_objectives(content) and INJECTION_MARKER not in content:
                    # Bloc objectifs déjà présent (manuel ou autre auto), on ne touche pas
                    pages_skipped_existing += 1
                    continue

                new_content, injected = inject_after_header(content, block)
                if injected:
                    page.write_text(new_content, encoding="utf-8")
                    pages_modified += 1
                else:
                    # Aucun point d'insertion trouvé
                    pages_skipped_no_obj += 1

    print(
        f"\n✓ Chapitres traités : {chapters_processed}\n"
        f"  Chapitres sans objectifs dans lecon.html : {chapters_no_obj}\n"
        f"  Pages modifiées (bloc injecté) : {pages_modified}\n"
        f"  Pages déjà munies d'objectifs (intactes) : {pages_skipped_existing}\n"
        f"  Pages sans point d'insertion : {pages_skipped_no_obj}"
    )


if __name__ == "__main__":
    main()

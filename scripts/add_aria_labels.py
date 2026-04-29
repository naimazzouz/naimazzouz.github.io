#!/usr/bin/env python3
"""
Ajoute des aria-label sur les canvas et SVG des simulations qui n'en ont pas.
Labels curés à la main pour décrire ce que l'élément représente.
"""

from __future__ import annotations

import re
from pathlib import Path

# (filename, type, id) → aria-label
LABELS: dict[str, dict[tuple[str, str], str]] = {
    "anisotropie-bois.html": {
        ("canvas", "cv"): "Schéma de la pièce de bois selon les trois directions (radiale, tangentielle, longitudinale)",
        ("canvas", "chartCv"): "Graphique de la variation des dimensions du bois selon la direction de coupe",
    },
    "archimede.html": {
        ("canvas", "cv"): "Animation d'un objet plongé dans un fluide montrant la poussée d'Archimède",
    },
    "atome-couches.html": {
        ("svg", "atom-svg"): "Représentation de l'atome avec son noyau et la répartition des électrons sur les couches K, L, M",
    },
    "atome.html": {
        ("svg", "atom-svg"): "Représentation interactive d'un atome avec protons, neutrons et électrons",
    },
    "attenuation-sonore.html": {
        ("svg", "(no-id)"): "Schéma de l'atténuation d'une onde sonore traversant une cloison",
    },
    "balance.html": {
        ("canvas", "bal"): "Animation d'une balance représentant les deux membres d'une équation du premier degré",
    },
    "boyle-mariotte.html": {
        ("canvas", "canvasCylindre"): "Cylindre avec piston illustrant la compression d'un gaz à température constante",
        ("canvas", "canvasGraphPV"): "Graphique de la pression en fonction du volume (loi de Boyle-Mariotte)",
        ("canvas", "canvasGraphInv"): "Graphique de la pression en fonction de l'inverse du volume",
    },
    "calepinage.html": {
        ("canvas", "canvas"): "Plan de calepinage d'une plaque rectangulaire avec disposition des découpes",
    },
    "ccf-bac-rangement.html": {
        ("canvas", "plaque"): "Plaque rectangulaire avec carrés découpés aux quatre coins pour former un bac",
        ("canvas", "graph"): "Graphique du volume du bac en fonction de la taille des carrés découpés",
    },
    "chaleur.html": {
        ("canvas", "canvasThermo"): "Thermomètre indiquant la température du corps chauffé",
        ("canvas", "canvasRecipient"): "Récipient contenant le corps en cours de chauffage",
        ("canvas", "graphe"): "Graphique de la température en fonction de l'énergie reçue",
        ("canvas", "barChart"): "Comparaison des chaleurs massiques de différents matériaux",
    },
    "changement-etat.html": {
        ("canvas", "cvCourbe"): "Courbe de chauffage avec paliers de fusion et d'ébullition",
    },
    "circuit-electrique.html": {
        ("canvas", "canvas"): "Circuit électrique animé avec déplacement des électrons (montage série ou parallèle)",
    },
    "combustion.html": {
        ("canvas", "combustionAnim"): "Animation de la réaction de combustion (molécules de combustible et oxygène)",
        ("canvas", "energyChart"): "Graphique de l'énergie libérée selon le combustible et la quantité",
    },
    "comparateur-vitrages.html": {
        ("canvas", "cvMain"): "Comparaison schématique des trois types de vitrages (simple, double, triple)",
        ("canvas", "chartCost"): "Graphique des pertes thermiques annuelles selon le type de vitrage",
    },
    "complexes.html": {
        ("canvas", "cvs"): "Plan complexe avec représentation vectorielle des nombres z et w",
    },
    "concentration.html": {
        ("canvas", "beaker"): "Bécher contenant une solution chimique avec son soluté dissous",
        ("canvas", "beakerDil"): "Bécher de la solution diluée après ajout du solvant",
    },
    "conductance-thermique.html": {
        ("canvas", "cvSingle"): "Coupe d'une paroi simple avec gradient de température",
        ("canvas", "cvComposite"): "Coupe d'une paroi multicouche avec gradient de température",
        ("canvas", "chartCompare"): "Comparaison de la conductance thermique des matériaux d'isolation",
    },
    "ctn-etuve-regulation.html": {
        ("canvas", "chart"): "Graphique de la résistance d'une CTN en fonction de la température",
    },
    "ctn-pt100-comparaison.html": {
        ("canvas", "chart"): "Comparaison des courbes R(T) d'une CTN et d'une sonde Pt100",
    },
    "debit-fluide.html": {
        ("svg", "(no-id)"): "Schéma d'une canalisation avec flux du fluide et indication du débit",
    },
    "debit.html": {
        ("canvas", "canvas"): "Animation d'un fluide circulant dans une canalisation avec section variable",
    },
    "dephasage.html": {
        ("canvas", "canvasOnde"): "Courbes de la tension et du courant alternatif avec déphasage angulaire",
        ("canvas", "canvasTri"): "Triangle des puissances active, réactive et apparente",
    },
    "derivee.html": {
        ("canvas", "graph"): "Courbe d'une fonction avec la tangente au point sélectionné",
    },
    "dilatation-parquet.html": {
        ("canvas", "canvas"): "Représentation d'une lame de parquet avec sa dilatation thermique",
    },
    "droite-affine.html": {
        ("canvas", "canvas"): "Tracé d'une droite y = ax + b avec coefficients réglables",
    },
    "eclairage-atelier.html": {
        ("canvas", "canvas"): "Plan d'un atelier avec emplacement des luminaires et carte d'éclairement",
    },
    "effet-joule.html": {
        ("canvas", "canvas"): "Conducteur électrique avec dissipation de chaleur par effet Joule",
        ("canvas", "graphe"): "Graphique de la puissance dissipée en fonction de l'intensité",
    },
    "entrainement-ineq.html": {
        ("canvas", "lCanvas"): "Droite graduée représentant l'ensemble solution de l'inéquation linéaire",
        ("canvas", "qCanvas"): "Représentation graphique de l'inéquation du second degré",
    },
    "escalier-blondel.html": {
        ("canvas", "canvas"): "Coupe d'un escalier montrant giron, hauteur de marche et échappée",
    },
    "exp-log.html": {
        ("canvas", "graphCanvas"): "Courbes de la fonction exponentielle et de la fonction logarithme",
    },
    "figures-planes.html": {
        ("canvas", "cv"): "Figure géométrique plane avec dimensions modifiables",
    },
    "fonction-machine.html": {
        ("canvas", "machineCanvas"): "Animation de la machine à fonctions transformant une valeur d'entrée x en image f(x)",
        ("canvas", "chartFunc"): "Tracé de la fonction sélectionnée",
    },
    "forces.html": {
        ("canvas", "cv"): "Représentation vectorielle des forces appliquées à un objet et de leur résultante",
    },
    "gaz.html": {
        ("canvas", "canvasBoyle"): "Cylindre avec piston pour la loi de Boyle-Mariotte (T constante)",
        ("canvas", "grapheBoyle"): "Graphique P en fonction de V pour la loi de Boyle-Mariotte",
        ("canvas", "canvasGL"): "Bonbonne de gaz pour la loi de Gay-Lussac (V constant)",
        ("canvas", "grapheGL"): "Graphique P en fonction de T pour la loi de Gay-Lussac",
    },
    "graphe-equation.html": {
        ("canvas", "graph"): "Tracé de deux droites avec leur point d'intersection (solution graphique)",
    },
    "inegalite.html": {
        ("canvas", "numberLine"): "Droite graduée avec représentation de l'ensemble solution",
    },
    "integrale.html": {
        ("canvas", "cvs"): "Courbe d'une fonction avec aire sous la courbe entre les bornes a et b",
    },
    "liaisons-chimiques.html": {
        ("svg", "molSvg"): "Représentation de la molécule sélectionnée avec ses atomes et liaisons",
        ("svg", "svgCov"): "Schéma d'une liaison covalente (partage d'électrons)",
        ("svg", "svgIon"): "Schéma d'une liaison ionique (transfert d'électrons)",
    },
    "moments.html": {
        ("canvas", "beamCanvas"): "Poutre en équilibre avec forces appliquées et leur bras de levier",
    },
    "moteur.html": {
        ("canvas", "canvas"): "Schéma d'un moteur électrique avec champ magnétique tournant",
    },
    "mouvement.html": {
        ("canvas", "anim"): "Animation du mobile en mouvement le long d'une trajectoire",
        ("canvas", "graph"): "Graphique de la position en fonction du temps",
    },
    "ohm.html": {
        ("canvas", "ohmChart"): "Caractéristiques U = f(I) tracées pour différentes résistances",
        ("svg", "(no-id)"): "Schéma du circuit électrique avec résistance, ampèremètre et voltmètre",
    },
    "ondes-em.html": {
        ("canvas", "cv"): "Spectre électromagnétique avec longueurs d'onde et applications",
    },
    "oxydoreduction.html": {
        ("canvas", "canvas"): "Réaction d'oxydoréduction avec échange d'électrons entre métal et solution",
    },
    "paroi-multicouche.html": {
        ("canvas", "cvWall"): "Coupe d'une paroi multicouche avec gradient de température et flux thermique",
        ("canvas", "chartR"): "Graphique de la résistance thermique cumulée à travers la paroi",
    },
    "pile-electrochimique.html": {
        ("canvas", "cvPile"): "Pile électrochimique avec deux demi-piles, pont salin et circuit extérieur",
    },
    "polynome3.html": {
        ("canvas", "graphCanvas"): "Courbe d'une fonction polynôme de degré 3 avec points clés (racines, extremums, inflexion)",
    },
    "presse-hydraulique.html": {
        ("canvas", "canvas"): "Schéma d'une presse hydraulique avec deux pistons reliés par un fluide",
    },
    "pression.html": {
        ("canvas", "canvas"): "Colonne de fluide avec pression à différentes profondeurs",
        ("canvas", "canvasPascal"): "Illustration du principe de Pascal (transmission de la pression dans un fluide)",
    },
    "probabilites.html": {
        ("canvas", "dieCanvas"): "Animation du lancer d'un dé",
        ("canvas", "coinCanvas"): "Animation du lancer d'une pièce de monnaie",
        ("canvas", "chartFreq"): "Graphique de la fréquence d'apparition convergeant vers la probabilité théorique",
    },
    "proportionnalite.html": {
        ("canvas", "chartProp"): "Graphique d'une situation de proportionnalité (droite passant par l'origine)",
    },
    "puissance.html": {
        ("canvas", "canvas"): "Diagramme de la puissance électrique consommée selon le temps et le tarif",
    },
    "pythagore.html": {
        ("canvas", "canvas"): "Triangle rectangle avec ses trois côtés et carrés sur chaque côté (illustration de Pythagore)",
    },
    "rayonnement.html": {
        ("canvas", "canvasSerre"): "Échanges de rayonnement entre la Terre, l'atmosphère et l'espace",
    },
    "redressement.html": {
        ("canvas", "canvas"): "Signal alternatif et son redressement à travers le pont de Graetz et le condensateur",
    },
    "refraction.html": {
        ("canvas", "cv"): "Rayon lumineux à l'interface entre deux milieux avec angles d'incidence et de réfraction",
    },
    "scalaire.html": {
        ("canvas", "cvs-geo"): "Deux vecteurs dans le plan avec angle entre eux pour le calcul du produit scalaire",
        ("canvas", "cvs-comp"): "Représentation du produit scalaire par projection",
    },
    "serre.html": {
        ("canvas", "sim"): "Schéma de l'effet de serre avec rayonnement solaire entrant et infrarouge piégé",
    },
    "signal-alternatif.html": {
        ("canvas", "scope"): "Écran d'oscilloscope virtuel affichant un signal sinusoïdal",
    },
    "solides.html": {
        ("canvas", "cv"): "Représentation 3D d'un solide géométrique (pavé, cylindre, cône, sphère ou pyramide)",
    },
    "son-2nde.html": {
        ("canvas", "waveCanvas"): "Forme d'onde du signal sonore avec fréquence et amplitude réglables",
    },
    "son.html": {
        ("canvas", "canvas"): "Onde sonore et indicateurs de fréquence et niveau sonore en décibels",
    },
    "sources-lumineuses.html": {
        ("canvas", "cvSpecInc"): "Spectre continu d'une lampe à incandescence",
        ("canvas", "cvSpecFluo"): "Spectre de raies d'une lampe fluorescente",
        ("canvas", "cvSpecLED"): "Spectre d'une LED blanche",
        ("canvas", "chartCost"): "Graphique de la consommation et du coût des différentes sources lumineuses",
    },
    "statistiques.html": {
        ("canvas", "chartBar"): "Diagramme en bâtons de la série statistique",
        ("canvas", "boxPlot"): "Diagramme en boîte à moustaches (médiane, quartiles, étendue)",
    },
    "stats-2var.html": {
        ("canvas", "scatterChart"): "Nuage de points avec droite d'ajustement linéaire",
    },
    "suites.html": {
        ("canvas", "suiteChart"): "Représentation graphique des termes d'une suite arithmétique ou géométrique",
    },
    "thales.html": {
        ("canvas", "canvas"): "Configuration de Thalès avec deux triangles emboîtés ou opposés par le sommet",
    },
    "traceur.html": {
        ("canvas", "graphCanvas"): "Tracé d'une fonction du second degré avec sommet et axe de symétrie",
    },
    "transferts-thermiques.html": {
        ("canvas", "cvConduction"): "Animation de la conduction thermique à travers une barre",
        ("canvas", "cvConvection"): "Animation de la convection dans un fluide chauffé",
        ("canvas", "cvRayonnement"): "Animation du rayonnement thermique d'un corps chaud",
        ("canvas", "cvEquilibre"): "Mise en équilibre thermique de deux corps en contact",
    },
    "transformateur.html": {
        ("canvas", "cvTransfo"): "Schéma d'un transformateur avec deux bobinages enroulés autour d'un noyau",
        ("canvas", "cvTransport"): "Schéma du transport de l'énergie électrique en haute tension",
    },
    "transmission-info.html": {
        ("canvas", "cvSignal"): "Signal d'information modulé pour la transmission",
        ("canvas", "cvShannon"): "Illustration de la chaîne de transmission selon Shannon",
        ("canvas", "cvQuant"): "Numérisation et quantification d'un signal analogique",
    },
    "vecteurs.html": {
        ("canvas", "cvs"): "Représentation graphique des vecteurs et de leurs opérations dans le plan",
    },
    "vitesse-acceleration.html": {
        ("canvas", "cvAnim"): "Animation du mobile en mouvement rectiligne",
        ("canvas", "chartX"): "Graphique de la position en fonction du temps",
        ("canvas", "chartV"): "Graphique de la vitesse en fonction du temps",
        ("canvas", "chartA"): "Graphique de l'accélération en fonction du temps",
    },
}


CANVAS_RE = re.compile(r'(<canvas\b)([^>]*?)(>)', re.IGNORECASE | re.DOTALL)
SVG_RE = re.compile(r'(<svg\b)([^>]*?)(>)', re.IGNORECASE | re.DOTALL)
ID_RE = re.compile(r'id="([^"]+)"', re.IGNORECASE)


def add_aria(tag_name: str, target_labels: dict[tuple[str, str], str], text: str) -> tuple[str, int]:
    """Pour chaque tag <canvas> ou <svg>, ajoute un aria-label si l'id correspond
    à une entrée dans target_labels et qu'il n'y a pas déjà un aria-label."""
    pattern = CANVAS_RE if tag_name == "canvas" else SVG_RE
    count = 0

    def repl(m):
        nonlocal count
        opening = m.group(1)
        attrs = m.group(2)
        closing = m.group(3)
        if "aria-label" in attrs:
            return m.group(0)
        id_m = ID_RE.search(attrs)
        sim_id = id_m.group(1) if id_m else "(no-id)"
        label = target_labels.get((tag_name, sim_id))
        if not label:
            return m.group(0)
        # Insert aria-label after the tag name, before other attrs
        new_attrs = f' aria-label="{label}"{attrs}'
        count += 1
        return f"{opening}{new_attrs}{closing}"

    new_text = pattern.sub(repl, text)
    return new_text, count


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    sims_dir = repo_root / "simulations"

    total_files = 0
    total_added = 0

    for filename, mapping in LABELS.items():
        path = sims_dir / filename
        if not path.exists():
            print(f"  ⚠  {filename}: fichier introuvable")
            continue

        text = path.read_text(encoding="utf-8")
        text, c1 = add_aria("canvas", mapping, text)
        text, c2 = add_aria("svg", mapping, text)
        added = c1 + c2

        if added > 0:
            path.write_text(text, encoding="utf-8")
            total_files += 1
            total_added += added
            print(f"  ✓ {filename} : {added} aria-label ajoutés")
        else:
            print(f"  − {filename} : déjà à jour ou aucune correspondance")

    print(f"\n✓ {total_added} aria-label ajoutés sur {total_files} fichiers")


if __name__ == "__main__":
    main()

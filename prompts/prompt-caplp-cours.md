# PROMPT — Livret de cours CAPLP Mathématiques (LaTeX)

## OBJECTIF

Produire un livret de cours complet en LaTeX pour la préparation au **CAPLP externe BAC+3 — Section mathématiques-physique chimie, session 2026**.

Le document doit être directement compilable sur Overleaf, structuré comme un manuel de référence de niveau **licence**, rigoureux, démonstratif et orienté concours.

---

## PROGRAMME DE RÉFÉRENCE (A.1 — Partie commune)

Le contenu doit couvrir strictement le programme A.1 du CAPLP 2026.
**Niveau attendu : L2 (première année de licence).** Chaque notion est traitée avec ses hypothèses complètes et ses démonstrations fondamentales.

| Ch. | Domaine | Notions détaillées | Profondeur |
|---|---|---|---|
| 1 | Raisonnement et vocabulaire ensembliste | Propositions, connecteurs (∧,∨,¬,⇒,⟺), tables de vérité ; quantificateurs (∀,∃), négation, ordre ; ensembles, inclusion, égalité, opérations (∪,∩,∁,×) ; lois de De Morgan ; applications, image directe/réciproque, injection, surjection, bijection, composition, réciproque ; raisonnements : direct, contraposée, absurde, disjonction de cas, récurrence simple et forte | L2 complet |
| 2 | Nombres complexes | Forme algébrique, module, argument, conjugué ; exponentielle complexe $e^{i\theta}$, formule d'Euler, formules de Moivre ; formules trigonométriques (addition, duplication, factorisation) ; racines $n$-ièmes de l'unité ; équation du second degré à coefficients réels (discriminant, racines complexes) | L1–L2 |
| 3 | Fonctions d'une variable réelle | Fonctions de référence (polynômes, rationnelles, $\exp$, $\ln$, $\sin$, $\cos$, $\tan$, $x^\alpha$) ; limites (définition ε–δ, théorèmes opératoires) ; continuité, prolongement par continuité ; TVI, corollaire (existence de racines) ; dérivabilité, interprétation géométrique, règles de dérivation ; théorème des accroissements finis, règle de l'Hôpital ; parité, périodicité, convexité (définition, lien avec la dérivée seconde), tangente, position de la courbe | L2 |
| 4 | Courbes paramétrées | Étude complète : domaine, parité/symétries, points singuliers, tangente (direction, équation), branche infinie ; courbes polynomiales (deg ≤ 2), rationnelles, trigonométriques ; schéma global | L2 |
| 5 | Calcul intégral | Intégrale de Riemann (définition, propriétés) ; primitives des fonctions usuelles ; théorème fondamental ; aires entre courbes, valeur moyenne ; intégration par parties (IPP) ; changement de variable ; intégrales impropres (convergence, cas usuels) | L2 |
| 6 | Équations différentielles | ED1 linéaires à coefficients constants (homogène + variation de la constante) ; ED1 séparables ; ED2 à coefficients constants (équation caractéristique, cas des 3 discriminants, solution particulière par identification) ; applications : loi de refroidissement, oscillateur harmonique | L2 |
| 7 | Suites numériques réelles | Suites explicites $u_n=f(n)$ et récurrentes $u_{n+1}=f(u_n)$ ; convergence, divergence, limites usuelles ; théorèmes d'existence : suites monotones bornées, théorème des gendarmes, suite adjacentes ; suites arithmétiques et géométriques ; suites extraites, sous-suites ; point fixe et étude graphique | L1–L2 |
| 8 | Algèbre linéaire (A.1) | Systèmes linéaires $n \leq 3$ équations, $p \leq 3$ inconnues ; méthode du pivot de Gauss ; discussion en fonction d'un paramètre ; matrices $\mathcal{M}_{n,p}(\mathbb{R})$, opérations, produit, transposée ; inverse $2\times 2$ et $3\times 3$ ; rang ; application aux systèmes | L1–L2 |
| 9 | Arithmétique des entiers | Représentation en base 10 et base 2 (conversion, opérations) ; division euclidienne ; divisibilité, nombres premiers, décomposition en facteurs premiers ; PGCD, PPCM, algorithme d'Euclide, identité de Bézout ; congruences (définition, propriétés) | L1 |
| 10 | Calcul vectoriel et espaces euclidiens | Vecteurs dans $\mathbb{R}^2$ et $\mathbb{R}^3$ : addition, combinaison linéaire, norme ; barycentre ; repères cartésiens ; produit scalaire (définition, propriétés, formule en coordonnées, orthogonalité) ; produit vectoriel (définition, propriétés, calcul, interprétation géométrique) ; transformations usuelles (translation, rotation, symétrie) | L1–L2 |
| 11 | Géométrie du plan et de l'espace | Droites et plans : équations cartésiennes et paramétriques, intersection, parallélisme, perpendicularité, distance ; cercles et sphères ; repérage polaire (plan), cylindrique et sphérique (espace) ; configurations géométriques classiques | L1–L2 |
| 12 | Formule du binôme | Coefficients binomiaux $\binom{n}{k}$, triangle de Pascal, formule de Pascal ; formule du binôme $(a+b)^n$ avec démonstration par récurrence ; applications (développements, identités remarquables, calculs combinatoires) | L1 |
| 13 | Probabilités | Espaces probabilisés finis $(\Omega,\mathcal{A},\mathbb{P})$ ; probabilité conditionnelle, formule des probabilités totales, formule de Bayes ; indépendance d'événements ; variables aléatoires discrètes, loi, espérance, variance, écart-type ; loi uniforme, loi de Bernoulli, loi binomiale | L1–L2 |
| 14 | Statistiques à une variable | Série statistique : effectifs, fréquences, représentations graphiques ; médiane, quartiles, étendue, écart interquartile ; moyenne, variance, écart-type (population et échantillon) ; boîte à moustaches | L1 |
| 15 | Statistiques à deux variables et algorithmique | Nuage de points, point moyen ; covariance, coefficient de corrélation linéaire ; ajustement affine par moindres carrés (calcul, interprétation) ; interpolation ; **Algorithmique Python** : variables, types, structures conditionnelles, boucles, fonctions, récursivité, tableaux/listes, algorithmes classiques (tri, pgcd, etc.) | L1 |

---

## PROGRAMME DE RÉFÉRENCE (A.2 — Discipline majeure Mathématiques)

**Niveau attendu : L3 (troisième année de licence).** Ce programme approfondit A.1 et couvre des thèmes de niveau avancé spécifiques à la discipline mathématiques.

| Ch. | Domaine | Notions détaillées | Profondeur |
|---|---|---|---|
| A2.1 | Algèbre linéaire avancée | Espaces vectoriels sur $\mathbb{R}$ (axiomes, exemples) ; sous-espaces vectoriels ; familles libres, génératrices, bases ; dimension ; applications linéaires, noyau, image ; théorème du rang ; endomorphismes ; matrices en dimension quelconque ; déterminants (développement, propriétés, règle de Sarrus) ; inverse par Gauss-Jordan ; valeurs propres, vecteurs propres, polynôme caractéristique ; diagonalisation (condition nécessaire et suffisante) ; trigonalisation ; calcul de $A^n$ | L3 |
| A2.2 | Fonctions de deux variables | Limite en un point (définition ε–δ), piège des chemins ; continuité ; dérivées partielles d'ordre 1 et 2 ; différentiabilité, gradient, plan tangent ; condition $\mathcal{C}^1 \Rightarrow$ différentiable ; matrice hessienne, théorème de Schwarz ; développement de Taylor-Young ordre 1 et 2 ; points critiques : définition et nature via le hessien (min/max/selle) | L3 |
| A2.3 | Développements limités | DL à l'ordre $n$ en $0$ (unicité, formule de Taylor-Young) ; liste des 8 DL usuels à connaître ; opérations (somme, produit, composition, intégration) ; applications : calcul de limites ($0/0$), nature des points critiques, position par rapport à la tangente, branches infinies | L2–L3 |
| A2.4 | Séries numériques | Convergence, sommes partielles ; condition nécessaire ; série géométrique, série de Riemann ; critères pour termes positifs : comparaison, équivalents, d'Alembert, Cauchy ; convergence absolue ; séries alternées (critère de Leibniz) | L3 |
| A2.5 | Dénombrement | Cardinal d'un ensemble fini ; principe d'inclusion-exclusion (2 et $n$ ensembles) ; listes ordonnées avec/sans répétition ; arrangements $A_n^k$, permutations $n!$ ; combinaisons $\binom{n}{k}$ ; formule de Pascal ; formule du binôme (preuve par récurrence) | L1–L2 |
| A2.6 | Probabilités discrètes avancées | Loi géométrique $\mathcal{G}(p)$ : définition, espérance, variance, absence de mémoire ; loi de Poisson $\mathcal{P}(\lambda)$ : définition, espérance, variance (preuves) ; approximation $\mathcal{B}(n,p) \to \mathcal{P}(\lambda)$ ; loi exponentielle $\mathcal{E}(\lambda)$ : densité, fonction de répartition, espérance, variance, absence de mémoire continue | L2–L3 |
| Algorithmique et programmation | Variables, types, tableaux, instructions, fonctions, récursivité, Python |

---

## NIVEAU ET POSTURE

- **Niveau attendu : licence (BAC+3)**
- Rigueur mathématique complète : définitions précises, hypothèses explicites, notations correctes
- Les théorèmes sont énoncés avec leurs hypothèses et leur conclusion clairement séparées
- Les démonstrations importantes sont rédigées intégralement
- Les démonstrations secondaires sont esquissées ou laissées en exercice avec indication
- Pas de simplification abusive : on ne "fait semblant" ni de démontrer ni de définir

---

## STRUCTURE GLOBALE DU DOCUMENT

```
Page de garde (titre, niveau, session)
Table des matières
Pour chaque chapitre :
  - Objectifs du chapitre
  - Corps du cours (voir structure ci-dessous)
  - Bilan / À retenir
  - Exercices types avec corrections
```

---

## STRUCTURE D'UN CHAPITRE (OBLIGATOIRE)

### 1. Objectifs
- Liste des notions maîtrisées à l'issue du chapitre
- Lien avec le programme A.1

### 2. Rappels et prérequis
- Notions supposées connues
- Références aux chapitres antérieurs si nécessaire

### 3. Cours (structure concours)

Pour chaque notion du chapitre, respecter l'ordre suivant :

```
Définition (encadré bleu foncé)
  → énoncé rigoureux avec hypothèses et notations

Remarque (si nécessaire)
  → précision, cas particulier, contre-exemple

Propriété / Théorème (encadré violet)
  → hypothèses explicites + conclusion

Démonstration (encadré gris ou inline)
  → complète pour les théorèmes fondamentaux
  → esquissée ou laissée en exercice pour les secondaires

Corollaire (si pertinent)

Exemple (encadré vert)
  → 1 exemple simple (application immédiate)
  → 1 exemple plus élaboré (mise en œuvre de la méthode)

Erreur fréquente / Piège de concours (encadré rouge)
  → formulation d'une erreur type + correction
```

### 4. Méthodes et savoir-faire
- Démarches types pour les exercices de concours
- Étapes numérotées et explicites
- Stratégies de résolution

### 5. Exercices types (minimum 3 par chapitre)
- Exercice 1 : application directe du cours
- Exercice 2 : exercice intermédiaire (plusieurs étapes)
- Exercice 3 : problème type concours (niveau A.2 ou épreuve écrite)
- Correction complète et rédigée pour chaque exercice

### 6. Bilan — À retenir
- Liste des définitions clés
- Liste des théorèmes fondamentaux
- Pièges à éviter
- Méthodes essentielles

---

## EXIGENCES DE RÉDACTION

- **Définitions** : toujours introduites par « Soit... » ou « On dit que... » avec les hypothèses
- **Théorèmes** : toujours avec « Sous les hypothèses... on a... »
- **Démonstrations** : commencent par « Preuve. » et se terminent par \qed
- **Exemples** : concrets, calculés, avec résultat numérique ou expression explicite
- **Notations** : cohérentes dans tout le document (définir une fois, utiliser partout)
- **Liens entre notions** : expliciter les connexions (ex : « Ce résultat généralise... »)
- **Erreurs fréquentes** : au moins une par section importante

---

## CONTRAINTES LATEX

### Packages obligatoires

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{lmodern}
\usepackage[a4paper,margin=2.2cm]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}
\usepackage{array,booktabs}
\usepackage{enumitem}
\usepackage[dvipsnames,svgnames]{xcolor}
\usepackage[most]{tcolorbox}
\usepackage{pgfplots}
\usepackage{tikz}
\usepackage{fancyhdr}
\usepackage[hidelinks]{hyperref}
```

### Couleurs (palette CAPLP)

```latex
\definecolor{caplpblue}{HTML}{1E3A5F}      % bleu marine — définitions
\definecolor{caplpbluebg}{HTML}{EFF6FF}    % fond bleu clair
\definecolor{caplppurple}{HTML}{5B21B6}    % violet — théorèmes
\definecolor{caplppurplebg}{HTML}{F5F3FF}  % fond violet clair
\definecolor{caplpgreen}{HTML}{15803D}     % vert — exemples
\definecolor{caplpgreenbg}{HTML}{F0FDF4}   % fond vert clair
\definecolor{caplpred}{HTML}{B91C1C}       % rouge — erreurs/attention
\definecolor{caplpredbg}{HTML}{FEF2F2}     % fond rouge clair
\definecolor{caplpgray}{HTML}{374151}      % gris — démonstrations
\definecolor{caplpgraybg}{HTML}{F9FAFB}    % fond gris clair
\definecolor{caplporange}{HTML}{C2410C}    % orange — méthodes
\definecolor{caplporangebg}{HTML}{FFF7ED}  % fond orange clair
```

### Environnements tcolorbox

```latex
% Définition
\newtcolorbox{definitionbox}[1][]{breakable, colback=caplpbluebg,
  colframe=caplpblue, fonttitle=\bfseries,
  title={Définition\ifx\relax#1\relax\else\ — #1\fi}}

% Théorème
\newtcolorbox{theoremebox}[1][]{breakable, colback=caplppurplebg,
  colframe=caplppurple, fonttitle=\bfseries,
  title={Théorème\ifx\relax#1\relax\else\ — #1\fi}}

% Proposition
\newtcolorbox{propositionbox}[1][]{breakable, colback=caplppurplebg,
  colframe=caplppurple!70, fonttitle=\bfseries,
  title={Proposition\ifx\relax#1\relax\else\ — #1\fi}}

% Corollaire
\newtcolorbox{corollairebox}[1][]{breakable, colback=caplppurplebg,
  colframe=caplppurple!50, fonttitle=\bfseries,
  title={Corollaire\ifx\relax#1\relax\else\ — #1\fi}}

% Démonstration
\newtcolorbox{preuvebox}{breakable, colback=caplpgraybg,
  colframe=caplpgray!50, fonttitle=\bfseries\itshape,
  title={Démonstration}}

% Exemple
\newtcolorbox{exemplebox}[1][]{breakable, colback=caplpgreenbg,
  colframe=caplpgreen, fonttitle=\bfseries,
  title={Exemple\ifx\relax#1\relax\else\ — #1\fi}}

% Erreur fréquente
\newtcolorbox{erreurbox}[1][]{breakable, colback=caplpredbg,
  colframe=caplpred, fonttitle=\bfseries,
  title={Erreur fréquente\ifx\relax#1\relax\else\ — #1\fi}}

% Méthode
\newtcolorbox{methodebox}[1][]{breakable, colback=caplporangebg,
  colframe=caplporange, fonttitle=\bfseries,
  title={Méthode\ifx\relax#1\relax\else\ — #1\fi}}

% À retenir
\newtcolorbox{retenirbox}{breakable, colback=white,
  colframe=caplpblue, coltitle=white, colbacktitle=caplpblue,
  fonttitle=\bfseries, title={À retenir}, boxrule=1.5pt}

% Exercice
\newtcolorbox{exercicebox}[1][]{breakable, colback=white,
  colframe=caplpgray, fonttitle=\bfseries,
  title={Exercice\ifx\relax#1\relax\else\ — #1\fi}}

% Correction
\newtcolorbox{correctionbox}[1][]{breakable, colback=caplpgreenbg,
  colframe=caplpgreen!60, fonttitle=\bfseries\itshape,
  title={Correction\ifx\relax#1\relax\else\ — #1\fi}}
```

### Classe et mise en page

```latex
\documentclass[11pt,a4paper,twoside]{book}
% En-têtes : chapitre à gauche, section à droite
% Pied de page : numéro centré
% Marges : 2.2 cm
```

---

## FIGURES ET ILLUSTRATIONS (OBLIGATOIRE)

Chaque chapitre doit contenir **au minimum une figure** illustrant une notion centrale du cours.

### Règles

- Utiliser **TikZ** pour les figures géométriques, graphes, diagrammes (Venn, vecteurs propres, courbes paramétrées, droites, plans…)
- Utiliser **pgfplots** pour les graphes de fonctions, courbes de niveau, surfaces 3D, histogrammes, nuages de points
- Placer les figures **dans le corps du cours**, immédiatement après la notion illustrée (pas en fin de chapitre)
- Utiliser `\captionof*{figure}{...}` (package `caption`) pour les légendes

### Figures recommandées par domaine

| Domaine | Figure suggérée |
|---|---|
| Ensembles | Diagrammes de Venn (∪, ∩, ∁) |
| Complexes | Cercle unité, représentation dans $\mathbb{C}$, racines $n$-ièmes |
| Fonctions 1 var. | Courbe + tangente + convexité (pgfplots) |
| Courbes paramétrées | Tracé de la courbe + points singuliers + tangentes |
| Calcul intégral | Aire sous la courbe (zone grisée, pgfplots) |
| Équations différentielles | Champ de vecteurs, familles de solutions |
| Suites | Suite convergente graphiquement (escalier/toile d'araignée) |
| Algèbre linéaire | Vecteurs propres et droites propres dans $\mathbb{R}^2$ |
| Fonctions 2 variables | Courbes de niveau + surface 3D (pgfplots) |
| DL | Approximations de $\sin x$ à plusieurs ordres (pgfplots) |
| Séries | Sommes partielles et convergence (pgfplots) |
| Probabilités | Histogramme de la loi de Poisson/binomiale (pgfplots) |
| Statistiques 2 var. | Nuage de points + droite de régression (pgfplots) |
| Arithmétique | Algorithme d'Euclide (diagramme de flux, TikZ) |
| Géométrie | Configurations (droites, plans, sphère) en TikZ 3D |

### Contraintes techniques

```latex
\usepackage{caption}   % pour \captionof*{figure}{...}
\usetikzlibrary{arrows.meta,calc,positioning,shapes,3d}
\pgfplotsset{compat=1.18}
```

---

## STRATÉGIE DE GÉNÉRATION

1. **Lire les programmes A.1 et A.2** fournis dans ce prompt
2. **Proposer le plan complet** du livret (Partie I : A.1, 15 chapitres ; Partie II : A.2, 6 chapitres)
3. **Générer le préambule LaTeX complet** (packages, couleurs, environnements, page de garde)
4. **Générer UN chapitre complet** (cours + figure(s) + exercices + corrections)
5. **Attendre validation** avant de continuer au chapitre suivant

---

## FORMAT DE SORTIE

- Code LaTeX uniquement, directement compilable
- Un fichier unique `.tex` (pas de `\input` externes)
- Commenter les grandes sections avec `%% === CHAPITRE X ===`
- Aucun commentaire hors code LaTeX

---

## OBJECTIF FINAL

Produire un **manuel de référence CAPLP** complet, rigoureux et pédagogique, utilisable pour la révision autonome du programme A.1, avec :
- Toutes les définitions et théorèmes du programme
- Les démonstrations fondamentales rédigées
- Des exercices types de niveau concours avec corrections complètes

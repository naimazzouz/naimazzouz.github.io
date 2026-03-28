# Skill : Générer des exercices par capacités (`exercices-capacites.html`)

## Usage

```
/generate-exercices-capacites <chemin-chapitre>
```

Exemple : `/generate-exercices-capacites maths/seconde/ch08`

## Instructions

Tu dois générer une page `exercices-capacites.html` complète pour le chapitre indiqué.

### Étape 1 — Collecter le contexte

1. **Lire `lecon.html`** du chapitre pour identifier les notions enseignées
2. **Lire `prompts/prompt-exercices-capacites.md`** pour les règles de rédaction
3. **Lire le programme officiel** dans `/pdf/` pour le niveau correspondant — extraire les **capacités et connaissances** du tableau officiel pour le module concerné
4. **Lire `exercices.html`** si elle existe — vérifier qu'il n'y a pas de capacité couverte dans l'une mais absente de l'autre
5. **Consulter les audits** dans `/audits/` pour vérifier s'il y a des remarques sur ce chapitre

### Étape 2 — Déterminer le thème couleur

| Dossier | `--p` | `--p-bg` | `--p-border` |
|---|---|---|---|
| `maths/seconde` | `#0056b3` | `#ebf5ff` | `#bee3f8` |
| `maths/premiere` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `maths/terminale` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `maths/bts` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/seconde` | `#6f42c1` | `#f5f0ff` | `#c4b5fd` |
| `physique-chimie/premiere-iccer` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/premiere-era` | `#2da44e` | `#f0fff4` | `#86efac` |
| `physique-chimie/terminale-iccer` | `#0969da` | `#dbeafe` | `#93c5fd` |
| `physique-chimie/terminale-era` | `#2da44e` | `#f0fff4` | `#86efac` |

### Étape 3 — Extraire les capacités du programme

1. **Lire le PDF du programme** correspondant
2. **Extraire les capacités** liées au chapitre (verbes d'action précis)
3. **Numéroter** : C1, C2, C3...
4. **Ne pas inventer** de capacités hors programme

**Exemples de capacités valides :**
- Reconnaître une fonction affine
- Calculer une image ou un antécédent
- Lire et interpréter un graphique
- Calculer un terme d'une suite arithmétique

**Ce qu'une capacité n'est PAS :** compétences transversales génériques (Chercher, Modéliser, Représenter, Raisonner, Calculer, Communiquer).

### Étape 4 — Générer la page

Créer le fichier `exercices-capacites.html` dans le dossier du chapitre.

### Structure HTML obligatoire

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – Exercices par capacités – Titre – Classe</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Chapitre X – Exercices par capacités</h1>
  <p class="sous-titre">Titre du chapitre | Niveau | Matière</p>
</header>

<!-- Liste des capacités du programme -->
<div class="objectifs">
  <strong>Capacités et connaissances du programme :</strong>
  <ul>
    <li>C1 — Nom de la capacité</li>
    <li>C2 — Nom de la capacité</li>
    <li>C3 — Nom de la capacité</li>
  </ul>
</div>

<!-- Boutons de filtre -->
<div class="cap-filtres">
  <button class="btn-cap" data-cap="all">Toutes</button>
  <button class="btn-cap" data-cap="C1">C1</button>
  <button class="btn-cap" data-cap="C2">C2</button>
  <button class="btn-cap" data-cap="C3">C3</button>
</div>

<!-- Section par capacité -->
<div class="cap-section" data-cap="C1">
<h2>C1 — Nom de la capacité</h2>

<div class="exo">
  <h3>Exercice 1</h3>
  <p>Énoncé ciblant uniquement cette capacité...</p>
  <button class="bc" onclick="toggle(this)">Voir la correction</button>
  <div class="corr">Correction détaillée</div>
</div>

<!-- 3 à 6 exercices par capacité -->
</div>

<div class="cap-section" data-cap="C2">
<h2>C2 — Nom de la capacité</h2>
<!-- Exercices pour C2 -->
</div>

</div>
<script src="../../../nav.js"></script>
<script src="../../../comp.js"></script>
<!-- PAS de diff.js — pas de différenciation sur cette page -->
</body>
</html>
```

### Règles de contenu

- **3 à 6 exercices par capacité**, difficulté progressive dans chaque série
- **1 exercice = 1 capacité principale** (ciblage strict, pas de mélange)
- Le premier exercice de chaque capacité doit être **accessible à tous**
- **Corrections complètes** pour tous les exercices (bouton `.bc` + `.corr`)
- **Pas de différenciation** (pas de diff.js, pas de classes diff-*)
- `comp.js` inclus pour le filtrage par capacité
- Ne JAMAIS utiliser les sigles ICCER/ERA-MA/MAMA dans le contenu

### Figures SVG obligatoires

Certaines capacités **exigent** une figure pour être travaillées. Sans figure, l'exercice ne couvre PAS la capacité.

**Règle absolue :** si l'énoncé dit "le graphique ci-dessous", "l'oscillogramme ci-dessous", "le schéma ci-dessous", la figure SVG **DOIT** être présente. Ne JAMAIS décrire textuellement un graphique que l'élève doit lire.

**Style SVG :**
```html
<figure class="schema" style="text-align:center;margin:12px 0">
  <svg width="250" height="170" viewBox="0 0 250 170" xmlns="http://www.w3.org/2000/svg">
    <!-- Contenu -->
  </svg>
  <figcaption style="font-size:0.88em;color:#555;margin-top:4px">Légende</figcaption>
</figure>
```

**Conventions graphiques :**
- Remplissage : `fill="#ebf5ff"`
- Contour principal : `stroke="#0056b3"`, `stroke-width="2"`
- Longueurs inconnues : `stroke-dasharray="6,3"` + couleur `#c53030`
- Labels sommets : `font-size="13"`, `fill="#0056b3"`, `font-weight="bold"`
- Labels dimensions : `font-size="11-12"`, `fill="#555"`
- Grilles : `stroke="#e2e8f0"`, `stroke-width="0.5"`
- Axes : `stroke="#333"`, `stroke-width="1.5"`, flèches aux extrémités
- Deuxième courbe : `stroke="#c53030"`

### Contenus hors programme

Si un exercice dépasse le programme, **ne pas le supprimer** mais :
- Ajouter **(HP)** dans le titre de la capacité
- Ajouter une note : *"Cette notion dépasse le programme de [niveau]."*

### Vérification scientifique

- **Refaire chaque calcul** des corrections
- **Unités SI** cohérentes
- **Valeurs physiques réalistes**
- **Formules conformes au niveau**

### Étape 5 — Vérifier

- Capacités extraites du programme officiel (pas inventées)
- 3 à 6 exercices par capacité
- Difficulté progressive dans chaque série
- Un exercice = une capacité principale
- Corrections complètes pour tous les exercices
- comp.js inclus et fonctionnel
- Pas de diff.js ni classes diff-*
- MathJax inclus si formules
- print.css inclus
- Couleurs CSS conformes au thème
- Lien retour vers le sommaire
- Figures SVG inline pour les exercices graphiques/géométriques/statistiques
- Aucun sigle de filière dans le contenu

# Skill : Générer une simulation interactive

## Usage

```
/generate-simulation <type> <chapitre> <titre>
```

- `<type>` : `illustration`, `tp`, `exploration` ou `modele`
- `<chapitre>` : chemin du chapitre lié (ex: `physique-chimie/seconde/ch07`)
- `<titre>` : titre court de la simulation

Exemple : `/generate-simulation tp physique-chimie/seconde/ch07 loi-ohm`

## Instructions

Tu dois générer une page HTML autonome (single-file) dans le dossier `simulations/`.

### Étape 1 — Collecter le contexte

1. **Lire `prompts/prompt-simulation.md`** pour les règles de création des simulations
2. **Lire `lecon.html`** du chapitre lié pour identifier les notions, formules et objectifs pédagogiques
3. **Lire le programme officiel** dans `/pdf/` pour confirmer que la notion est au programme
4. **Consulter `simulations/index.html`** pour vérifier que la simulation n'existe pas déjà

### Étape 2 — Identifier le type de simulation

| Type | Paramètres | Caractéristiques |
|---|---|---|
| **Type 1 — Illustration** | 1-2 sliders | Interface minimaliste, animation Canvas/SVG, pas de mesures |
| **Type 2 — TP numérique** | 2-4 sliders | Mesures, tableau de données remplissable, zone de résultats |
| **Type 3 — Exploration libre** | 3-6 sliders | Système ouvert, retour visuel immédiat, pas de parcours imposé |
| **Type 4 — Modèle mathématique** | Variable | Équations MathJax dynamiques, graphique Chart.js temps réel |

### Étape 3 — Générer la simulation

Créer le fichier dans `simulations/` avec un nom descriptif en kebab-case (ex: `loi-ohm.html`, `pression-hydro.html`).

### Structure HTML obligatoire

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Titre — Simulation</title>
<!-- MathJax si équations -->
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<!-- Chart.js si graphique -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  /* TOUS les styles sont inline — la simulation est autonome */
  *{margin:0;padding:0;box-sizing:border-box}
  body{font-family:'Segoe UI',system-ui,sans-serif;background:#f4f4f9;color:#333}
  .container{max-width:860px;margin:0 auto;padding:20px}
  header{background:var(--accent);color:white;padding:20px;border-radius:10px;text-align:center;position:relative;margin-bottom:20px}
  .btn-back{position:absolute;left:15px;top:15px;background:rgba(255,255,255,0.2);color:white;text-decoration:none;padding:5px 12px;border-radius:5px;font-size:0.85em}
  .btn-back:hover{background:rgba(255,255,255,0.35)}
  .card{background:white;border-radius:10px;padding:20px;box-shadow:0 2px 10px rgba(0,0,0,0.08);margin-bottom:20px}
  .row{display:grid;grid-template-columns:1fr 1fr;gap:20px}
  @media(max-width:600px){.row{grid-template-columns:1fr}}
  .explication{background:#fff8f0;border-left:4px solid var(--accent);padding:12px 16px;border-radius:0 8px 8px 0;margin-bottom:20px}
  /* ... styles spécifiques à la simulation ... */
</style>
</head>
<body>
<div class="container">
  <header>
    <a href="../simulations.html" class="btn-back">← Retour</a>
    <h1>Titre de la simulation</h1>
    <p>Niveau — Chapitre · Formule clé</p>
  </header>

  <!-- Zone d'explication -->
  <div class="explication">
    Rappel de la loi ou du phénomène...
  </div>

  <!-- Contrôles -->
  <div class="card">
    <!-- Sliders, selects, boutons -->
  </div>

  <!-- Visualisation -->
  <div class="card">
    <canvas id="canvas" width="500" height="350"></canvas>
  </div>

  <!-- Résultats / Graphique -->
  <div class="card">
    <!-- Valeurs calculées, graphique Chart.js, tableau de mesures -->
  </div>
</div>
<script>
  // Logique de la simulation
  function update() {
    // Mise à jour temps réel
  }
  // Appel initial
  update();
</script>
</body>
</html>
```

### Points importants — page autonome

- **Styles inline** : pas de lien vers `styles.css` (la simulation est autonome)
- **Pas de `nav.js`** : navigation autonome via le bouton retour
- **Chemin retour** : `<a href="../simulations.html">← Retour</a>`
- **Responsive** : media query `@media(max-width:600px)` obligatoire
- **MathJax** : inclure uniquement si la simulation affiche des équations
- **Chart.js** : inclure uniquement si la simulation a un graphique dynamique

### Palette de couleurs par domaine

| Domaine | Couleur header / accent |
|---|---|
| Électricité | `#e91e63` (rose) ou `#2563eb` (bleu) |
| Thermique | `#e67e22` (orange) |
| Mécanique | `#0284c7` (bleu) |
| Chimie | `#16a34a` (vert) ou `#6f42c1` (violet) |
| Ondes / Signaux | `#8b5cf6` (violet) |
| Mathématiques | `#2563eb` (bleu) |

### Critères de qualité

1. **Interaction immédiate** : chaque slider déclenche `update()` via `oninput` — pas de bouton "Calculer"
2. **Valeur affichée** : `<span id="vParam">valeur</span>` à côté de chaque slider
3. **Paramètres réalistes** : `min`, `max`, `step` physiquement cohérents, unités affichées
4. **Valeurs par défaut** : donnent un résultat parlant
5. **Canvas/SVG lisible** : 400-600px de large, légendes et annotations directement dessus
6. **Couleurs significatives** : rouge = chaud, bleu = froid, etc.
7. **Performance** : pas de `requestAnimationFrame` inutile — redessiner uniquement quand un paramètre change
8. **Canvas effacé** avant chaque redessin (`ctx.clearRect(...)`)
9. **Nombres formatés** : `toFixed(1)` ou `toFixed(2)` selon la précision utile

### Spécificités par type

**Type 2 — TP numérique :**
- Tableau de données avec bouton "Ajouter la mesure"
- Bouton "Effacer les données" pour recommencer
- Zone de résultats avec valeurs calculées mises en forme

**Type 4 — Modèle mathématique :**
- Équation MathJax avec valeurs numériques injectées dynamiquement
- Graphique Chart.js avec axes titrés et unités
- Mise à jour via `chart.update()` (pas de recréation)
- Point courant visible sur la courbe

### Règle fondamentale — ancrage pédagogique

**Toute simulation doit être en lien direct avec un chapitre et le programme officiel.**

Interdit :
- Créer une simulation déconnectée du contenu pédagogique
- Introduire des notions hors-programme
- Créer une simulation "pour le plaisir" sans ancrage dans un chapitre

### Étape 4 — Vérifier

- La simulation correspond à un chapitre et une classe identifiés
- Les notions sont au programme officiel
- Les sliders et contrôles réagissent immédiatement
- Les valeurs numériques ont les bonnes unités
- Le Canvas/SVG est lisible et bien dimensionné
- Le responsive fonctionne (mobile)
- Le lien retour pointe vers `../simulations.html`
- La formule clé est visible
- Les valeurs par défaut donnent un résultat parlant
- Le JavaScript est propre (pas de console.log)
- MathJax / Chart.js inclus uniquement si utilisés

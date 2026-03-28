# Skill : Générer des exercices (`exercices.html`)

## Usage

```
/generate-exercices <chemin-chapitre>
```

Exemple : `/generate-exercices maths/seconde/ch05`

## Instructions

Tu dois générer une page `exercices.html` complète pour le chapitre indiqué.

### Étape 1 — Collecter le contexte

1. **Lire `lecon.html`** du chapitre pour identifier les notions, définitions, propriétés et méthodes
2. **Lire `prompts/prompt-exercices.md`** pour les règles de rédaction des exercices
3. **Lire le programme officiel** dans `/pdf/` pour le niveau correspondant — extraire les capacités du module
4. **Identifier le prompt de filière** correspondant et le lire :
   - Seconde MAMA : `prompts/prompt-filiere-2mama.md`
   - Première ICCER : `prompts/prompt-filiere-premiere-iccer.md`
   - Première ERA : `prompts/prompt-filiere-premiere-era.md`
   - Terminale ICCER : `prompts/prompt-filiere-ticcer.md`
   - Terminale ERA/MA : `prompts/prompt-filiere-era-ma.md`
   - BTS : `prompts/prompt-bts.md`
5. **Vérifier la cohérence** avec `exercices-capacites.html` si elle existe (même capacités couvertes)
6. **Consulter les audits** dans `/audits/` pour vérifier s'il y a des remarques sur ce chapitre

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

### Étape 3 — Générer les exercices

Créer le fichier `exercices.html` dans le dossier du chapitre avec **3 niveaux de différenciation**.

### Structure HTML obligatoire

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – Exercices – Titre – Niveau Bac Pro</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:BG;--p-border:BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Exercices – Titre du chapitre</h1>
  <p class="sous-titre">Chapitre X | Niveau Bac Pro | Matière</p>
</header>

<!-- Exercices communs (visibles par tous) -->
<div class="exo">
  <h2>Exercice 1</h2>
  <!-- Exercice accessible à tous -->
</div>

<!-- Niveau Socle -->
<div class="exo diff-socle">
  <span class="tag-socle">Socle</span>
  <h2>Exercice X</h2>
  <!-- Exercice très guidé -->
  <button class="bc" onclick="this.nextElementSibling.style.display='block'">Voir la correction</button>
  <div class="corr">Correction détaillée étape par étape</div>
</div>

<!-- Niveau Standard -->
<div class="exo diff-standard">
  <span class="tag-standard">Standard</span>
  <h2>Exercice X</h2>
  <!-- Exercice classique -->
  <button class="bc" onclick="this.nextElementSibling.style.display='block'">Voir la correction</button>
  <div class="corr">Correction complète</div>
</div>

<!-- Niveau Approfondissement -->
<div class="exo diff-appro">
  <span class="tag-appro">Approfondissement</span>
  <h2>Exercice X</h2>
  <!-- Exercice ouvert type BTS -->
  <button class="bc" onclick="this.nextElementSibling.style.display='block'">Voir la correction</button>
  <div class="corr">Correction complète</div>
</div>

</div>
<script src="../../../nav.js"></script>
<script src="../../../diff.js"></script>
</body>
</html>
```

### Différenciation pédagogique — les 3 niveaux

| Niveau | Classe CSS | Tag | Contenu |
|---|---|---|---|
| **Socle** | `.diff-socle` | `.tag-socle` | Exercices très guidés, étape par étape, calculs amorcés, tableaux pré-remplis, contextes du quotidien |
| **Standard** | `.diff-standard` | `.tag-standard` | Exercices du programme, contextes professionnels variés, rédaction attendue |
| **Approfondissement** | `.diff-appro` | `.tag-appro` | Problèmes ouverts, mise en équation autonome, questions type BTS |

### Règles de contenu

- **Chaque capacité du programme** doit être couverte par au moins un exercice
- **Exercices progressifs** au sein de chaque niveau
- **Corrections complètes** pour tous les exercices (bouton `.bc` + `.corr`)
- Les corrections expliquent le **raisonnement**, pas juste le résultat
- **Contextes variés** : professionnel + quotidien + scientifique + sport + énergie
- Ne JAMAIS utiliser les sigles ICCER/ERA-MA/MAMA dans le contenu
- **Valeurs physiques réalistes** et unités SI cohérentes
- **Refaire chaque calcul** des corrections pour vérifier l'exactitude

### Figures SVG obligatoires

Si l'exercice implique une lecture graphique, un schéma géométrique, un diagramme statistique, un oscillogramme, un circuit, etc. : **la figure SVG inline DOIT être présente**.

Ne JAMAIS décrire textuellement un graphique que l'élève doit lire.

**Style SVG :**
```html
<figure class="schema" style="text-align:center;margin:12px 0">
  <svg width="250" height="170" viewBox="0 0 250 170" xmlns="http://www.w3.org/2000/svg">
    <!-- Contenu -->
  </svg>
  <figcaption style="font-size:0.88em;color:#555;margin-top:4px">Légende</figcaption>
</figure>
```

Conventions : fill `#ebf5ff`, stroke `#0056b3`, labels `#555`, inconnues `#c53030` en pointillés.

### Spécificité BTS

Pour les chapitres dans `maths/bts/` :
- **Pas de différenciation** (pas de diff.js, pas de classes diff-*)
- Un seul niveau d'exercices, notation rigoureuse
- Lire `prompts/prompt-bts.md` pour les règles spécifiques

### Étape 4 — Vérifier

- Le fichier est bien formé (HTML valide)
- Les 3 niveaux de différenciation sont présents (sauf BTS)
- Toutes les capacités du programme sont couvertes
- Chaque exercice a une correction complète
- Les calculs des corrections sont exacts
- Les figures SVG sont présentes pour les exercices de lecture graphique
- Le lien retour sommaire est correct
- `nav.js` et `diff.js` sont inclus (sauf BTS : pas de diff.js)
- `print.css` est inclus
- MathJax est inclus si formules
- Les couleurs CSS correspondent au thème matière/niveau
- Aucun sigle de filière dans le contenu pédagogique
- Les valeurs numériques sont réalistes et les unités correctes

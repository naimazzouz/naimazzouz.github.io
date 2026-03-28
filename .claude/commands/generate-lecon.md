# Skill : Générer une lecon (`lecon.html`)

## Usage

```
/generate-lecon <chemin-chapitre>
```

Exemple : `/generate-lecon maths/seconde/ch03`

## Instructions

Tu dois générer une page `lecon.html` complète pour le chapitre indiqué.

### Étape 1 — Collecter le contexte

1. **Lire `prompts/prompt-cours.md`** pour les règles de rédaction des cours
2. **Identifier la matière et le niveau** depuis le chemin
3. **Lire le programme officiel** dans `/pdf/` pour le niveau correspondant — extraire les capacités et connaissances du module concerné
4. **Identifier le prompt de filière** correspondant et le lire :
   - Seconde MAMA : `prompts/prompt-filiere-2mama.md`
   - Première ICCER : `prompts/prompt-filiere-premiere-iccer.md`
   - Première ERA : `prompts/prompt-filiere-premiere-era.md`
   - Terminale ICCER : `prompts/prompt-filiere-ticcer.md`
   - Terminale ERA/MA : `prompts/prompt-filiere-era-ma.md`
   - BTS : `prompts/prompt-bts.md`
5. **Lire les fichiers existants** du chapitre (exercices.html, ds.html...) pour assurer la cohérence
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

### Étape 3 — Générer le cours

Créer le fichier `lecon.html` dans le dossier du chapitre.

### Structure HTML obligatoire

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – Titre – Niveau Bac Pro</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:BG;--p-border:BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Chapitre X – Titre</h1>
  <p class="sous-titre">Niveau | Matière | Module</p>
</header>
<!-- Contenu du cours -->
</div>
<script src="../../../nav.js"></script>
</body>
</html>
```

### Structure du contenu

Le cours suit cette progression obligatoire :

1. **Introduction** — explication simple de la notion + exemple concret (vie réelle ou domaine professionnel)
2. **Notions essentielles** — concepts détaillés, vocabulaire scientifique expliqué simplement, définitions dans des `.def`
3. **Exemples expliqués** — plusieurs exemples détaillés, raisonnement étape par étape
4. **Propriétés et formules** — dans des `.prop` et `.formule-box`, avec MathJax
5. **Illustrations visuelles** — schémas SVG inline, graphiques Chart.js ou Canvas si pertinent
6. **Encadrés pédagogiques** :
   - `.retenir` pour les résumés essentiels
   - `.att` pour les erreurs fréquentes
   - `.meth` pour les méthodes de résolution
7. **Applications concrètes** — lien avec la vie quotidienne et les métiers professionnels (utiliser les vrais noms de métiers, JAMAIS les sigles de filière)
8. **Mini exercices** — quelques questions simples de vérification avec correction (`.exo` + `.corr` + `.bc`)

### Règles de contenu

- **Pas de différenciation** : le cours est identique pour tous les élèves (pas de diff.js, pas de classes diff-*)
- **Phrases simples** : vocabulaire accessible, progression logique
- **Niveau lycée professionnel** : pas de formalisme excessif
- **Chaque capacité du programme** doit être couverte par le cours
- **Formules en MathJax** : `\( ... \)` en ligne, `\[ ... \]` en bloc
- **Figures SVG inline** pour les schémas géométriques, graphiques, circuits, etc.
- **Ne JAMAIS utiliser les sigles ICCER/ERA-MA/MAMA** dans le contenu pédagogique
- **Contextes professionnels variés** : professionnel + quotidien + scientifique
- **Valeurs physiques réalistes** et unités SI cohérentes

### Classes CSS à utiliser (définies dans styles.css)

| Classe | Usage |
|---|---|
| `.def` | Définition |
| `.prop` | Propriété |
| `.att` | Attention / erreur fréquente |
| `.meth` | Méthode |
| `.retenir` | Encadré "À retenir" |
| `.ex` | Exemple expliqué |
| `.exo` | Exercice / mini exercice |
| `.corr` | Correction cachée |
| `.bc` | Bouton "Voir la correction" |
| `.formule-box` / `.formula-box` | Encadré formule |
| `.situation` | Situation professionnelle |
| `.grid2` / `.deux-col` | Grille 2 colonnes |

**Ne JAMAIS redéfinir ces classes dans un `<style>` inline.**

### Spécificité BTS

Pour les chapitres dans `maths/bts/` :
- Pas de différenciation (un seul niveau)
- Notation mathématique rigoureuse
- Vocabulaire plus formel
- Lire `prompts/prompt-bts.md` pour les règles spécifiques

### Étape 4 — Vérifier

- Le fichier est bien formé (HTML valide)
- Toutes les capacités du programme sont couvertes
- Le lien retour sommaire est correct
- `nav.js` est inclus en fin de `<body>`
- `print.css` est inclus dans le `<head>`
- MathJax est inclus si formules
- Les couleurs CSS correspondent au thème matière/niveau
- Aucun sigle de filière dans le contenu pédagogique
- Les formules MathJax sont correctes
- Les figures SVG sont présentes là où nécessaire
- Les valeurs numériques sont réalistes

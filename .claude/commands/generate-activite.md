# Skill : Générer une activité de découverte (`activite.html`)

## Usage

```
/generate-activite <chemin-chapitre>
```

Exemple : `/generate-activite physique-chimie/seconde/ch07`

## Instructions

Tu dois générer une page `activite.html` complète pour le chapitre indiqué.

### Étape 1 — Collecter le contexte

1. **Lire `lecon.html`** du chapitre — la notion cible doit être clairement identifiée
2. **Lire `prompts/prompt-activite.md`** pour les règles de rédaction des activités
3. **Lire le programme officiel** dans `/pdf/` pour le niveau — vérifier que la notion est au programme
4. **Identifier le prompt de filière** correspondant et le lire :
   - Seconde MAMA : `prompts/prompt-filiere-2mama.md`
   - Première ICCER : `prompts/prompt-filiere-premiere-iccer.md`
   - Première ERA : `prompts/prompt-filiere-premiere-era.md`
   - Terminale ICCER : `prompts/prompt-filiere-ticcer.md`
   - Terminale ERA/MA : `prompts/prompt-filiere-era-ma.md`
   - BTS : `prompts/prompt-bts.md`
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

### Étape 3 — Générer l'activité

Créer le fichier `activite.html` dans le dossier du chapitre.

### Structure HTML obligatoire

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>ChXX – Activité – Titre – Classe</title>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<link rel="stylesheet" href="../../../styles.css">
<link rel="stylesheet" href="../../../print.css" media="print">
<style>:root{--p:COULEUR;--p-bg:COULEUR-BG;--p-border:COULEUR-BORDER}</style>
</head>
<body>
<div class="c">
<a href="../../sommaire.html" class="nb">← Retour au sommaire</a>
<header>
  <h1>Activité – Titre de la notion</h1>
  <p class="sous-titre">Chapitre X | Niveau | Matière | ⏱ 30 min</p>
</header>

<div class="objectifs">
  <strong>Objectifs :</strong>
  <ul>
    <li>Découvrir [notion 1]</li>
    <li>Comprendre [notion 2]</li>
  </ul>
</div>

<!-- DOCUMENT D'ACCROCHE -->
<div class="situation">
  <h2>Situation professionnelle</h2>
  <p><em>Contexte : [métier réel], [entreprise fictive], [ville].</em></p>
  <!-- Tableau, texte, données, schéma... -->
</div>

<!-- QUESTIONS PROGRESSIVES -->
<div class="exo">
<h2>Question 1 <span class="badge-blue">APP</span></h2>
<p>Consigne...</p>
<button class="bc" onclick="this.nextElementSibling.style.display='block'">Voir la correction</button>
<div class="corr">Correction...</div>
</div>

<!-- ... autant de questions que nécessaire -->

<!-- SYNTHÈSE -->
<div class="retenir">
  <strong>À retenir</strong>
  <p>[Définition / Propriété construite à partir de l'activité]</p>
</div>

</div>
<script src="../../../nav.js"></script>
</body>
</html>
```

### Philosophie de l'activité

L'activité est une **situation-problème** : l'élève découvre la notion par investigation, pas par transmission directe.

**Ce que l'activité n'est PAS :**
- Pas un cours déguisé (on ne donne pas la définition au départ)
- Pas un exercice d'application (l'élève ne connaît pas encore la méthode)
- Pas un TP numérique (c'est une activité documentaire ou graphique)

**Progression narrative obligatoire :**
```
Situation professionnelle (document d'accroche)
    → Questions de compréhension (S'approprier)
    → Questions d'analyse (Analyser)
    → Questions de calcul / manipulation (Réaliser)
    → Questions d'interprétation (Valider)
    → Synthèse (Communiquer)
    → À retenir (la notion formalisée)
```

### Compétences (badges)

| Compétence | Abréviation | Classe CSS | Usage |
|---|---|---|---|
| S'approprier | `APP` | `.badge-blue` | Lecture, compréhension du contexte |
| Analyser | `ANA` | `.badge-blue` | Analyse, identification des relations |
| Réaliser | `REA` | `.badge-green` | Calculs, constructions |
| Valider | `VAL` | `.badge-green` | Vérification, interprétation |
| Communiquer | `COM` | `.badge-yellow` | Rédaction, synthèse |

Au minimum une compétence par grande étape. Les questions de pur calcul intermédiaire n'ont pas besoin de badge.

### Document d'accroche

Le document peut être : un texte de mise en situation, un tableau de données, un graphique, un schéma légendé, un extrait de notice ou de devis.

**Règles :**
- Ancré dans un **métier réel** (JAMAIS les sigles de filière)
- Contient **toutes les données** nécessaires pour répondre aux questions
- Suffisamment riche pour générer les questions
- Lisible : pas surchargé de données inutiles

### Durée et nombre de questions

- **Durée cible** : 25 à 40 minutes (indiquée dans le sous-titre)
- **Nombre de questions** : libre, déterminé par la notion (4 à 12 questions typiquement)
- Des sous-questions (a, b, c) peuvent subdiviser une étape

### Différenciation (optionnelle)

Par défaut, l'activité est **une base commune** (pas de différenciation).

Si nécessaire :
- **Socle** : aides intégrées dans les questions (rappels, calculs amorcés)
- **Standard** : questions sans aide supplémentaire
- **Approfondissement** : questions bonus à la fin

Utiliser `.diff-socle`, `.diff-standard`, `.diff-appro` et `diff.js` uniquement si la différenciation est activée.

### Règles de rédaction

- **Métiers réels** uniquement (voir CLAUDE.md — jamais ICCER, ERA-MA, MAMA)
- **Contextes variés** : professionnel + quotidien + scientifique
- **Données réalistes** : valeurs numériques cohérentes, unités SI
- **Corrections complètes** pour chaque question (bouton `.bc` + `.corr`)
- **Encadré "À retenir"** aligné avec la formulation du cours (`lecon.html`)
- **Contenu dans le programme** : ne pas introduire du hors-programme

### Étape 4 — Vérifier

- Situation professionnelle avec métier réel nommé
- Toutes les données utiles dans le document d'accroche
- Durée estimée indiquée dans le sous-titre
- Objectifs formulés
- Questions numérotées, progressives, avec verbe de consigne précis
- Badges de compétence sur les questions structurantes
- Correction complète pour chaque question
- Encadré "À retenir" aligné avec `lecon.html`
- Aucun sigle de filière dans le contenu
- Données numériques réalistes
- MathJax inclus si formules
- print.css et nav.js inclus
- Couleurs CSS conformes au thème matière/niveau

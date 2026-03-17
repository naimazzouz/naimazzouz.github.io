# Prompt de référence — Génération de pages d'exercices

Je veux que tu rédiges une page d'exercices complète, très pédagogique et bien structurée, destinée à des élèves de lycée professionnel.

Objectif : produire une page HTML prête à être intégrée dans un site pédagogique.

La page d'exercices doit être claire, progressive et accessible, avec des exercices variés, des explications simples et une correction pédagogique.

---

## STRUCTURE DE LA PAGE

### 1. Titre du chapitre

### 2. Introduction
- rappeler brièvement la notion travaillée
- expliquer l'objectif des exercices
- indiquer que les exercices sont progressifs

### 3. Exercices de base
- exercices simples pour vérifier la compréhension du cours
- questions directes
- application immédiate des définitions et méthodes

### 4. Exercices guidés
- exercices avec raisonnement étape par étape
- progression claire
- aide pédagogique implicite dans l'énoncé si nécessaire

### 5. Exercices d'application
- exercices plus complets
- mobilisation de plusieurs notions du chapitre
- calculs et raisonnements adaptés au niveau lycée professionnel

### 6. Exercices contextualisés
- proposer des exercices liés à la vie réelle ou au domaine professionnel
- utiliser des exemples concrets liés aux métiers professionnels

### 7. Illustrations visuelles
- proposer des schémas explicatifs si c'est utile
- proposer des images pédagogiques si nécessaire
- décrire précisément les images à générer

Pour chaque image, ajouter :

> **Prompt image :** description détaillée de l'image à générer

### 8. Graphiques
- produire des graphiques clairs si le chapitre s'y prête
- si possible générer le code pour :
  - Chart.js
  - SVG
  - ou Canvas

### 9. Encadrés importants
Ajouter des encadrés pédagogiques :
- Méthode
- Attention aux erreurs fréquentes
- À retenir

### 10. Correction
- proposer une correction détaillée
- expliquer les étapes du raisonnement
- corriger de manière pédagogique et progressive
- utiliser des phrases simples

---

## DIFFÉRENCIATION PÉDAGOGIQUE

La différenciation s'applique à **tous les niveaux** (Seconde, Première, Terminale).

### Les 3 niveaux de différenciation

| Niveau | Profil cible | Contenu |
|---|---|---|
| **Socle** | Élèves en difficulté | Exercices très guidés, étape par étape, calculs amorcés, tableaux pré-remplis, contextes du quotidien |
| **Standard** | Majorité de la classe | Exercices du programme, contextes professionnels variés, rédaction attendue |
| **Approfondissement** | Poursuite BTS/MC | Problèmes ouverts, mise en équation autonome, questions type BTS |

### Formes possibles de différenciation

1. **Niveau de difficulté progressif** : exercices de base → intermédiaires → avancés
2. **Variété des contextes** : professionnels, scientifiques, vie quotidienne
3. **Aides pédagogiques** : indices, rappels de méthode, étapes guidées
4. **Parcours possibles** : exercices accessibles à tous + exercices d'approfondissement

### Mise en œuvre technique

Utiliser les classes CSS `diff-socle`, `diff-standard`, `diff-appro` pour tagger les blocs par niveau (voir CLAUDE.md pour les détails techniques).

Le contenu doit rester **lisible, clair et structuré** — la différenciation ne doit pas rendre les pages confuses ou trop chargées.

---

## CONTRAINTES PÉDAGOGIQUES

- niveau lycée professionnel
- phrases simples
- vocabulaire accessible
- progression logique
- exercices progressifs
- correction détaillée et pédagogique

---

## CONTRAINTES TECHNIQUES

- produire une page HTML propre
- utiliser des sections bien structurées
- utiliser des classes CSS simples
- intégrer les graphiques directement dans la page si nécessaire

---

## OBJECTIF FINAL

Produire une page d'exercices riche, claire et très pédagogique, utilisable directement sur un site éducatif.

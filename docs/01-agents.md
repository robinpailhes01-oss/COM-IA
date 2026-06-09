# Les 5 agents — spécifications

> System prompts détaillés à rédiger une fois les exemples de Robin analysés.
> Ce document fige le rôle, les inputs et les outputs de chaque agent.

## Agent 1 — Le Stratège
- **Mission** : idée brute → brief structuré de carousel.
- **Inputs** : idée brute (texte/voice transcrit), historique des derniers posts.
- **Outputs** : type de carousel (cas concret / retour d'expérience / comment j'ai
  fait / découverte / avant-après), message principal, structure des slides
  (nombre + contenu en 1 phrase), audience cible, hook recommandé slide 1.
- **Note** : il structure, il ne rédige pas.

## Agent 2 — Le Copywriter
- **Mission** : brief → textes de chaque slide + caption, dans la voix exacte de Robin.
- **Inputs** : brief du Stratège, guide de voix, exemples de captions passées.
- **Outputs** : texte par slide, caption complète (hook + corps + CTA + hashtags),
  premier commentaire (optionnel).
- **Test de voix** : si Robin ne dirait pas la phrase à un ami autour d'un café, on réécrit.
- **Interdits connus** : pas de « game changer », pas d'emoji en début de ligne, pas de ton guru/marketing.

## Agent 3 — Le Directeur Artistique
- **Mission** : définir le brief visuel précis de chaque slide AVANT génération.
- **Inputs** : textes des slides, charte graphique, grille actuelle (9-12 derniers posts),
  palette du dernier post (pour alterner).
- **Outputs par slide** : palette (Light/Dark), layout, couleur fond (hex), couleur texte
  (hex), police + taille, éléments graphiques, description du visuel si nécessaire,
  position texte/visuel, méthode de rendu recommandée (fond IA + texte couche, ou full couche).
- **Palettes de référence** :
  - Light Premium — fond `#FAFAF8`, texte `#1A1A1A`, accent `#C9A84C`
  - Dark Élégant — fond `#0F1117`, texte `#F0EDE6`, accent `#C9A84C`
- **Règle feed** : alterne les palettes, beaucoup de whitespace, jamais surchargé,
  pense « comment ça rend dans la grille des 9 ».

## Agent 4 — Le Designer
- **Mission** : produire les visuels selon le brief du DA.
- **Rôle corrigé (validé Robin)** : le Designer **ne génère pas d'images “à la main”**.
  Il produit les **prompts Nano Banana** (1 par slide) + la liste des éléments à poser
  en couche nette ensuite (texte si besoin, logos). La génération d'image = Nano Banana.
- **Inputs** : brief visuel par slide, textes à intégrer, dernières images du feed.
- **Outputs** : image par slide (1080x1350 ou 1080x1080).
- **Méthode (décision validée)** : Nano Banana pour le fond/visuel uniquement ;
  le texte est ajouté en couche nette (HTML/CSS → image, ou template) — jamais
  de typo laissée à l'IA seule.
- **Prompts Nano Banana de base** :
  - Slide visuel : `[description], premium lifestyle photography style, warm natural lighting, Mediterranean aesthetic, minimalist composition, editorial quality, 1080x1350 format`
  - Fond texte : `minimalist Instagram background, [light/dark] [#hex], clean modern, generous whitespace, subtle gold accent line, no text, 1080x1350 format`

## Agent 5 — Le Quality Checker
- **Mission** : vérifier le carousel avant envoi à Robin.
- **Inputs** : carousel complet (textes + images, via Vision), charte, guide de voix,
  9-12 derniers posts.
- **Outputs** : score /10 sur Voix / Design / Feed Harmony / Clarté ; liste des
  problèmes si < 7 ; suggestions ; verdict ✅ prêt / 🔄 ajustements.
- **Règle** : exigeant. Mieux vaut ne pas poster que poster du médiocre.

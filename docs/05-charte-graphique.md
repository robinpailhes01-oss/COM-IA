# Charte graphique — @robinpailhes

> Consolidée à partir de 20 références / 9 comptes (cf. `04-analyse-references.md`).
> Positionnement : **partage de cas concrets IA, pas influenceur**. Feed premium,
> minimaliste, **lumineux**. Cette charte pilote les agents DA, Designer, Quality Checker.

---

## 1. Principe directeur

> **Fond clair · typo forte · UN seul accent (or) sur le mot/résultat clé · cas concret · zéro clutter.**

La cohérence du feed vient du **SYSTÈME** (typographie + formule de hook + accent unique),
**pas** d'une couleur de fond uniforme. On peut donc alterner Light/Dark sans casser l'harmonie.

---

## 2. Palettes (2, alternées pour le rythme)

### Light Premium (par défaut, ~60 % du feed)
| Rôle | Hex |
|---|---|
| Fond | `#FAFAF8` (crème / blanc cassé) |
| Texte | `#1A1A1A` |
| Accent | `#C9A84C` (or) |

### Dark Élégant (~40 % du feed)
| Rôle | Hex |
|---|---|
| Fond | `#0F1117` |
| Texte | `#F0EDE6` |
| Accent | `#C9A84C` (or) |

**Règle d'alternance** : si les 2 derniers posts sont Light → le prochain est Dark (et inversement).
Cible globale ~60 % Light / 40 % Dark.

**Accent** : UN seul par slide, réservé au mot/chiffre/résultat clé (highlight ou couleur).
Jamais de multi-couleurs. L'or est la signature qui différencie Robin des références (teal, rose, orange…).

---

## 3. Typographie

- **Hook / titres** : serif éditorial (droit ou italique pour l'emphase) OU sans-serif gras.
  Gros, peu de mots, beaucoup d'air autour.
- **Corps / explications** : sans-serif régulier, lisible, interligne généreux.
- **Hiérarchie forte** : 1 idée dominante par slide, le reste plus petit.
- Polices exactes à figer en Phase 2 (pistes : serif type Canela/Tiempos ; sans type Inter/Söhne).

---

## 4. Les types de slides

| Type | Rôle | Layout |
|---|---|---|
| **Hook** | slide 1, doit accrocher DANS la grille | Photo perso + statement en overlay, OU texte plein sur fond crème (serif) |
| **Contenu** | développer le cas concret | Texte structuré, mockup d'écran réel, listes numérotées (« 01// », « #1 ») |
| **Takeaway** | la chose à retenir | Statement fort, accent or sur le mot clé |
| **CTA** | inviter à l'action | Sobre, 1 phrase, sans agressivité marketing |

### Layouts validés (issus des références)
- **Photo perso + overlay texte** (bas-gauche ou haut-droite) — exploite le dossier photos de Robin.
- **Texte plein fond crème** + serif + 1 mot surligné or (style @karaodesign / @victoriaeverest_).
- **Mockup d'écran réel** + label tracké (« CAS CLIENT », « CE QUE J'AI FAIT ») — crédibilité.
- **Photo à gauche + carte texte à droite** (style @michaelaiacademy, version lumineuse).
- **Format « note »** (capture Notes app) — option authenticité, à doser.

---

## 5. Formule de hook (modèle, calibré sur @karaodesign)

Un hook = **une phrase parlée, concrète, lisible seule dans la vignette.** Patterns qui marchent :
- Cas concret + résultat chiffré → « Un client est passé de 10 à 22 réservations/mois. »
- Opinion tranchée → « Les packs, c'est l'arnaque la mieux habillée du web. »
- Story perso → « Ce week-end, j'ai appris que… »
- Aveu / accroche perso → « J'ai une mauvaise relation à l'argent. »

> À remplacer par les formules issues des VRAIS textes de Robin une fois fournis.

---

## 6. À éviter (interdits visuels confirmés)

- Dark / moody / granuleux (on traduit toujours en **lumineux**).
- Stickers / overlays / emojis 3D en pagaille.
- Highlights multi-couleurs.
- Icônes 3D stock / rendus génériques « AI influencer ».
- Style « miniature YouTube » (caps criards, contours, glow).
- Postures « guru qui pose avec son laptop ».
- Surcharge : toujours du whitespace, jamais plein.

---

## 7. Rendu technique (par type de slide)

Conformément à la décision validée (mix) : **Nano Banana pour le fond/visuel uniquement,
texte ajouté en couche nette** (jamais de typo laissée à l'IA seule).

| Slide | Fond / visuel | Texte |
|---|---|---|
| Texte plein | Fond uni ou papier crème généré/templated | Couche HTML/CSS nette |
| Photo perso + overlay | Photo du dossier Robin (retouche lumineuse si besoin) | Couche HTML/CSS nette |
| Mockup d'écran | Capture réelle du travail de Robin | Couche / annotations nettes |

---

## 8. Cohérence feed — règles automatiques

- Alternance palette : 2 Light d'affilée → Dark ensuite.
- Varier les types de contenu : 3 « cas client » d'affilée → changer de format.
- La slide 1 est pensée **pour la grille**, pas juste pour le post isolé.
- Preview grille (8 derniers posts réels + nouveau en position 1) avant validation Robin.
- Le Quality Checker vérifie le **système** (typo + formule de hook + 1 accent), pas « même couleur ».

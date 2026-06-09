# Brief de calibrage — ce que Robin doit fournir

## ⚠️ Décision voix (mise à jour) — calibrage INCRÉMENTAL

Robin ne fournit pas un corpus de voix figé d'avance. **À chaque idée de post**, il
donne ses mots bruts (texte ou audio), qui servent d'**ancre de voix pour ce post**.
Le Copywriter s'appuie sur ces mots + un corpus de voix qui **grossit au fil des posts**
(chaque texte validé enrichit `brand_config.voice_guide`). La voix se calibre en marchant.

---

## Le reste (références design + photos)

Pour calibrer les agents sur le VRAI style de Robin (et pas un style générique),
j'ai besoin de trois familles d'exemples. Plus c'est concret, mieux c'est.

## 1. Pour le Copywriter — ta voix (le plus important)
- **5 à 10 captions / textes qui sonnent vraiment comme toi.**
- Peu importe la perfection : je veux ton ton naturel, tes tournures, ton premier degré.
- Si tu as des exemples de ce que tu DÉTESTES (ton marketing, guru…), envoie-les
  aussi — ça aide à définir les interdits.

## 2. Pour le DA + le Designer — l'esthétique
- **5 à 10 carousels que tu trouves beaux** (les tiens ou d'autres comptes).
- Idéalement avec une phrase sur ce qui te plaît dans chacun.

## 3. Pour la cohérence feed — ta grille
- **1 screenshot de la grille actuelle de @robinpailhes** (les 9-12 dernières vignettes).

## Comment me les envoyer
- Tu peux les déposer dans ce repo, les coller dans le chat, ou me donner les liens.
- Pour chaque exemple, je te répondrai noir sur blanc **ce que j'en retire**, ex :
  - « De ce post : fond crème, serif large sur le hook, max 3 lignes/slide, accent or sur les chiffres. »
  - « De cette caption : phrases courtes, zéro emoji, ton direct, toujours un exemple concret. »
- Ces analyses iront dans `brand_config.examples` et nourriront chaque agent.

> Tant que je n'ai pas ces exemples, je ne fige aucun system prompt : on calibre
> sur du réel, pas sur des suppositions.

# COM-IA — Usine à Contenu Instagram (@robinpailhes)

Pipeline multi-agents qui transforme une idée brute (envoyée sur Telegram) en
carousel Instagram premium prêt à publier, en gardant l'harmonie du feed.

**Principe directeur : on planifie avant de coder. Robin valide chaque étape.**

## État du projet

- [x] **PHASE 0 — Planification** (en cours)
  - [x] Architecture multi-agents validée
  - [x] Décisions structurantes tranchées (voir ci-dessous)
  - [ ] Exemples de calibrage fournis par Robin
  - [ ] System prompts détaillés rédigés (calibrés sur les exemples)
- [ ] PHASE 1 — Agents texte (Stratège + Copywriter)
- [ ] PHASE 2 — Agent visuel (DA + Designer + cohérence feed)
- [ ] PHASE 3 — Quality Checker + pipeline complet
- [ ] PHASE 4 — Optimisation

## Décisions validées (PHASE 0)

| Sujet | Décision |
|---|---|
| **Visuels** | Mix calibré sur les exemples de Robin : fonds IA (Nano Banana) + texte en couche nette. Feed harmony prioritaire. Jamais de texte typographié laissé à l'IA seule. |
| **Cohérence feed** | Upload manuel de la grille au démarrage (screenshot). Scraping auto repoussé après validation du reste. |
| **Publication** | Manuelle — Robin poste depuis l'iPad. Le système envoie images HD + caption sur Telegram. Aucune publication automatique. |
| **Calibrage** | On part des exemples réels de Robin avant d'écrire les system prompts. Les 10 premières générations = tests, pas publications. |

## Architecture

```
Robin (Telegram) ──> [ORCHESTRATEUR n8n]
                          │
                          ▼
   [1 STRATÈGE]  idée brute → brief structuré (format, message, slides)
                          │
                          ▼
   [2 COPYWRITER] brief → textes des slides + caption (voix Robin)
                          │
                          ▼
   [3 DIRECTEUR ARTISTIQUE] textes + charte + grille → brief visuel/slide
                          │
                          ▼
   [4 DESIGNER] brief → fonds Nano Banana + texte en couche nette
                          │
                          ▼
   [5 QUALITY CHECKER] voix ✓ design ✓ feed harmony ✓ → score /10
                          │
                          ▼
   [ORCHESTRATEUR] carousel + preview grille → Telegram → Robin valide
```

Détail des agents, du schéma Supabase et des workflows n8n dans `docs/`.

## Stack

- **n8n cloud** — orchestration
- **Claude API** — agents Stratège, Copywriter, DA, Quality Checker (Vision)
- **Nano Banana (Gemini Image)** — génération des fonds/visuels
- **Supabase** — base de données + storage (feed, exemples, drafts)
- **Telegram** — interface de Robin (entrée idées, sortie drafts, validation)

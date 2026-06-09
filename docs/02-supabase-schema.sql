-- COM-IA — Schéma Supabase (référence, non encore appliqué)
-- À appliquer en PHASE 1.

-- Posts Instagram (historique)
create table if not exists posts (
  id uuid primary key default gen_random_uuid(),
  instagram_id text,
  type text,                 -- 'cas_client' | 'retour_experience' | 'decouverte' | 'comment_jai_fait' | 'avant_apres'
  palette text,              -- 'light' | 'dark'
  hook_text text,
  caption text,
  slides_text jsonb,         -- [{slide_number, text}]
  slides_images text[],      -- URLs Supabase Storage
  thumbnail_url text,        -- image slide 1 (grille)
  status text,               -- 'draft' | 'validated' | 'published'
  published_at timestamptz,
  engagement jsonb,          -- {likes, comments, saves, shares}
  created_at timestamptz default now()
);

-- Feed history (cohérence visuelle)
create table if not exists feed_snapshots (
  id uuid primary key default gen_random_uuid(),
  snapshot_date date,
  grid_images text[],        -- 12 dernières images du feed
  dominant_colors jsonb,
  palette_sequence text[],   -- ['dark','light','dark',...]
  created_at timestamptz default now()
);

-- Templates de design
create table if not exists design_templates (
  id uuid primary key default gen_random_uuid(),
  name text,
  palette text,              -- 'light' | 'dark'
  slide_type text,           -- 'hook' | 'content' | 'takeaway' | 'cta'
  layout jsonb,
  nano_banana_prompt text,
  created_at timestamptz default now()
);

-- Idées brutes de Robin + sorties des agents
create table if not exists ideas (
  id uuid primary key default gen_random_uuid(),
  raw_input text,
  input_type text,           -- 'text' | 'voice_note' | 'image'
  status text,               -- 'received' | 'processing' | 'draft_ready' | 'validated' | 'published' | 'rejected'
  stratege_output jsonb,
  copywriter_output jsonb,
  da_output jsonb,
  designer_output jsonb,
  quality_score int,
  post_id uuid references posts(id),
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Charte graphique + guide de voix (configuration)
create table if not exists brand_config (
  id uuid primary key default gen_random_uuid(),
  voice_guide jsonb,         -- expressions, ton, interdits
  palette_light jsonb,
  palette_dark jsonb,
  typography jsonb,
  design_rules jsonb,
  examples jsonb,            -- analyses des exemples de référence
  updated_at timestamptz default now()
);

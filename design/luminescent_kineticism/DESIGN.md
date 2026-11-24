---
name: Luminescent Kineticism
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#3f4a37'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#6f7b65'
  outline-variant: '#bfcab1'
  surface-tint: '#306c00'
  primary: '#306c00'
  on-primary: '#ffffff'
  primary-container: '#7ae332'
  on-primary-container: '#2b6100'
  inverse-primary: '#76df2d'
  secondary: '#00668a'
  on-secondary: '#ffffff'
  secondary-container: '#40c2fd'
  on-secondary-container: '#004d6a'
  tertiary: '#a43073'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffb5d6'
  on-tertiary-container: '#982669'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#91fc4a'
  primary-fixed-dim: '#76df2d'
  on-primary-fixed: '#0a2100'
  on-primary-fixed-variant: '#225100'
  secondary-fixed: '#c4e7ff'
  secondary-fixed-dim: '#7bd0ff'
  on-secondary-fixed: '#001e2c'
  on-secondary-fixed-variant: '#004c69'
  tertiary-fixed: '#ffd8e7'
  tertiary-fixed-dim: '#ffafd3'
  on-tertiary-fixed: '#3d0026'
  on-tertiary-fixed-variant: '#85145a'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
  court-volt: '#84F329'
  macaron-lime: '#D9F99D'
  macaron-sky: '#E0F2FE'
  macaron-rose: '#FCE7F3'
  canvas-cream: '#F8FAFC'
  glass-border: rgba(255, 255, 255, 0.75)
  glass-surface: rgba(255, 255, 255, 0.68)
  glass-overlay: rgba(15, 23, 42, 0.40)
  text-primary: '#0F172A'
  text-secondary: '#64748B'
  text-tertiary: '#94A3B8'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '800'
    lineHeight: 40px
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '800'
    lineHeight: 34px
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 30px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '700'
    lineHeight: 24px
  title-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 22px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22.4px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
  label-mini:
    fontFamily: Plus Jakarta Sans
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 12px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 0.5rem
  margin: 0.75rem
  margin-detail: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1rem
  space-xl: 1.25rem
  space-2xl: 1.75rem
---

## Brand & Style

The design system establishes a refreshing, energetic, and luminous aesthetic tailored for urban young professionals engaged in pickleball. Rooted in tactile clarity, modern sports minimalism, and luminous micro-depth, the system translates physical court energy into digital space.

### Personality & Values
- **Vital & Lucid:** High-energy visual presence grounded in electric court greens, balanced by airy translucent surfaces and soft pastel gradients.
- **Unobtrusive & Frictionless:** Zero commercial clutter or transactional pressure. Information hierarchy remains immediate, readable, and respectful of user attention.
- **Physical Softness:** Tactile rounded forms, cushion-like container volumes, and frosted acrylic layers evoking modern athletic gear and smooth polymer ball surfaces.

### Design Language
The design system combines **Glassmorphism** with **Soft Neomorphic Volumes**:
- Surfaces employ high-translucency backdrops (`backdrop-filter: blur(20px)`), frosted micro-borders, and gentle internal highlights to mimic physical frosted acrylic and high-end resin sporting hardware.
- Content containers balance crisp functional typography with pill-shaped chips and expansive corner curves (20px to 28px).

## Colors

The color system captures the electric energy of pickleball courts with sophisticated balance:

### Primary Palette
- **Primary (`#7AE332` / Court Volt):** An energized, chromatic pickleball lime-green providing athletic accenting, active state highlights, primary action pills, and vibrant badges.
- **Secondary (`#38BDF8` / Sky Cyan):** Fresh court-sky tone used for analytical indicators, active course tracking, and cool-spectrum content cards.
- **Tertiary (`#F472B6` / Soft Berry):** Energetic conversational and community accent, applied to interactive callouts and highlighted community items.
- **Neutral (`#0F172A` / Slate Night):** High-density text neutral providing immediate legibility and crisp contrast without visual harshness.

### Atmospheric Glass & Macaron Tints
Cards utilize multi-layer pastel backplates (`macaron-lime`, `macaron-sky`, `macaron-rose`) layered underneath frosted glass (`glass-surface`) to yield luminous, ambient color fields without visual fatigue.

## Typography

The type system is set in **Plus Jakarta Sans**, offering geometric warmth, rounded terminal shapes, and optical legibility on high-density mobile screens.

### Hierarchy & Content Rules
- **Headline Scaling:** Section titles and large data figures use bold to extra-bold weights (`700`–`800`) to anchor scanning eyes immediately.
- **Body Long-Form Line Height:** Standard body text follows a strict line-height multiplier of `1.6` (`22.4px` on `14px` base) for comfortable continuous reading in long article viewports.
- **Mobile Constraints:** Tab bar labels and badge counters support optical scales down to `10px` (`label-mini`) to prevent visual crowding on narrow devices like iPhone SE (320px logical width).
- **Truncation:** Content card titles truncate with an ellipsis after a maximum of 2 lines; summaries and value tags are restricted to single-line display.

## Layout & Spacing

The layout model is crafted specifically for mobile viewports using a 375pt baseline grid (conforming to the Mini-Program 750rpx coordinate framework).

### Structural Metrics
- **Canvas Margins:** Screen boundaries enforce a lateral margin of `12px` (`0.75rem` / `24rpx`) for feeds, dashboards, and category streams. Detail viewports expand margin gutters to `16px` (`1rem` / `32rpx`) for clean reading columns.
- **Masonry Waterfall Gutter:** 2-column masonry grids (venues, equipment) utilize an exact column gutter of `8px` (`0.5rem` / `16rpx`). Card widths dynamically adjust via `calc((100vw - 24px - 8px) / 2)`.
- **Touch Target Enclosure:** All tappable anchors, navigation icons, and actionable pills enforce an envelope of at least `44px × 44px` (`88rpx × 88rpx`), independent of the graphic icon size.
- **Chrome Anchor:** Bottom primary floating navigation maintains a standard clearance of `49px` (`98rpx`) elevated above the native home-indicator safe-area inset.

## Elevation & Depth

Visual depth is achieved through **luminescent translucent layering** rather than opaque drop shadows. Surfaces reflect physical glassmorphism and subtle internal reflections.

### Surface Tiers & Depth Strategies
- **Base Canvas (Level 0):** Soft chromatic white canvas (`#F8FAFC`) with subtle underlaid multi-color radial flares.
- **Frosted Content Cards (Level 1):** Semi-transparent white (`rgba(255, 255, 255, 0.70)`) combined with backdrop blur (`backdrop-filter: blur(20px)`), topped with a crisp internal light stroke (`1px solid rgba(255, 255, 255, 0.85)`). Soft, diffused ambient drop shadow: `0 8px 24px -4px rgba(148, 163, 184, 0.18)`.
- **Elevated Interactive Controls (Level 2):** Floating search anchors, quick action toggles, and detail bottom action bars. Utilizes `rgba(255, 255, 255, 0.88)` blur with dual-ring shadows: a delicate interior bevel (`inset 0 1px 1px 0 rgba(255, 255, 255, 0.9)`) and an exterior cushion shadow (`0 12px 32px -4px rgba(15, 23, 42, 0.12)`).
- **Floating Island Navigation (Level 3):** Detached frosted glass capsule floating above the scroll plane. Bordered by `1px solid rgba(255, 255, 255, 0.65)`, backed by `blur(24px)`, and suspended via `0 16px 36px -6px rgba(15, 23, 42, 0.15)`.
- **System Overlays & Bottom Sheets (Level 4):** Dark scrim overlay (`rgba(15, 23, 42, 0.40)`) with backdrop blur (`blur(8px)`), anchoring clean rounded bottom-sheet cards.

## Shapes

The shape system expresses physical playfulness and sports-equipment ergonomics using pronounced, smooth continuous corner radii.

### Curvature Taxonomy
- **Dashboard & Category Cards:** Enforced corner radius of `24px` to `28px`, creating a tactile cushion effect across all feed containers.
- **Media Containers:** Aspect-ratio locked thumbnails (`1:1` gear, `4:3` venues, `16:9` course video streams) integrate `18px` to `20px` corner radii to seamlessly nest inside parent card containers.
- **Pills, Badges & Action Buttons:** Continuous stadium pill shapes (`rounded-full` / `9999px`) across action buttons, category filters, difficulty tags, and bottom navigation pods.
- **Micro Elements:** Checkbox indicators, icon backing plates, and thumbnail placeholders feature `8px` to `12px` roundedness.

## Components

### Buttons & Interactive Controls
- **Primary Pill Action:** Pill-shaped (`rounded-full`), filled with energetic Lime-Volt (`#7AE332`) or solid Slate Night (`#0F172A`), delivering high-contrast white or deep black typography. Includes an interactive active-touch scale of `0.96` (`100ms ease-out`).
- **Glass Action Pill:** White frosted glass (`rgba(255, 255, 255, 0.85)`) with an internal highlight bevel, supporting secondary options and inline detail page bookmarks.
- **Favorite Heart Action:** Features an optimistic state transition: an outline glyph that pulses with a scale transform (`1.2` to `1.0` over `200ms`) and transitions into a solid lime or coral fill upon activation.

### Cards & Feed Modules
- **Macaron Glass Card:** Tinted translucent background cards (lime, sky blue, soft rose) displaying key session statistics, weather/court alerts, or daily lessons. Topped with multi-layer inner frosted panels with `20px` padding.
- **Dual-Column Masonry Card:** Dedicated to venues and equipment items. Features full-bleed media covers (`4:3` or `1:1`), multi-photo count chips floating at top-right, and tight, structured text stacks below.
- **List News Card:** Horizontal arrangement featuring a `100px × 100px` (`200rpx × 200rpx`) square thumbnail on the left with a `16px` radius, complemented by a 2-line clamped headline and metadata row on the right.

### Navigation Chrome
- **Floating Island Tab Bar:** Detached capsule hovering `12px` above the bottom safe area. Measures `49px` in height with an ergonomic pill silhouette. Contains 6 semantic destinations with responsive label scaling (`10px`–`11px`) and soft active highlight indicators.
- **Top Sticky Search Header:** Frosted header bar that transitions from transparent to blurred acrylic surface upon scroll offset. Houses circular `44px` icon buttons and a rounded pill search input with inline debounced query clearing.

### Progress & Status Indicators
- **Course Segment Bar:** Capsule progress tracker divided into pill-shaped progress segments with energetic color transitions (`#38BDF8` to `#7AE332`), displaying completion status cleanly.
- **Empty States & Skeletons:** Animated skeleton cards with warm gray-to-white shimmer sweeps (`200ms` cross-fade on load), avoiding jarring positional jumps.
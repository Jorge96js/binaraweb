---
name: Sanitary Solutions System
colors:
  surface: '#fcf9f4'
  surface-dim: '#dcdad5'
  surface-bright: '#fcf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ee'
  surface-container: '#f0ede9'
  surface-container-high: '#ebe8e3'
  surface-container-highest: '#e5e2dd'
  on-surface: '#1c1c19'
  on-surface-variant: '#45464e'
  inverse-surface: '#31302d'
  inverse-on-surface: '#f3f0eb'
  outline: '#75777f'
  outline-variant: '#c5c6cf'
  surface-tint: '#4f5e84'
  primary: '#041538'
  on-primary: '#ffffff'
  primary-container: '#1b2a4d'
  on-primary-container: '#8392bb'
  inverse-primary: '#b7c6f1'
  secondary: '#6a5d46'
  on-secondary: '#ffffff'
  secondary-container: '#f0ddc0'
  on-secondary-container: '#6e614a'
  tertiary: '#001b18'
  on-tertiary: '#ffffff'
  tertiary-container: '#00322c'
  on-tertiary-container: '#4ea095'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b7c6f1'
  on-primary-fixed: '#091a3c'
  on-primary-fixed-variant: '#37466a'
  secondary-fixed: '#f2e0c3'
  secondary-fixed-dim: '#d6c4a8'
  on-secondary-fixed: '#231a08'
  on-secondary-fixed-variant: '#514530'
  tertiary-fixed: '#9ff2e4'
  tertiary-fixed-dim: '#83d5c8'
  on-tertiary-fixed: '#00201c'
  on-tertiary-fixed-variant: '#005048'
  background: '#fcf9f4'
  on-background: '#1c1c19'
  surface-variant: '#e5e2dd'
  navy-dark: '#101A33'
  border-subtle: rgba(27, 42, 77, 0.12)
  focus-ring: '#7FD1C4'
typography:
  display-hero:
    fontFamily: Outfit
    fontSize: 52px
    fontWeight: '700'
    lineHeight: 60px
    letterSpacing: -0.02em
  display-hero-mobile:
    fontFamily: Outfit
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Outfit
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Outfit
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Outfit
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
  headline-sm:
    fontFamily: Outfit
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  lead:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  label-md:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.04em
  kicker:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.25rem
  gutter-mobile: 0.75rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
  space-2xl: 4rem
  space-section: 5rem
  space-section-mobile: 3rem
---

## Brand & Style

The design system is engineered for a specialized sanitation logistics service in Baradero and northern Buenos Aires Province. The brand persona centers on reliability, clinical hygiene, prompt operational excellence, and approachable regional familiarity. The UI targets event producers, construction site managers, agricultural operators, and private individuals requiring sanitary infrastructure without administrative friction.

The emotional core is **peace of mind**: the user must immediately perceive that the service is odorless, immaculate, punctual, and operated by local professionals. The aesthetic avoids all toilet tropes, crude humor, or industrial grit, leaning instead toward crisp modernism, organic cleanliness, and approachable utility.

The design movement combines **Modern Utility and Soft Flat Design**:
- Crisp geometric structures paired with friendly, generous corner radii (18px card containers, 999px pills).
- High structural legibility using solid color blocking between deep navy and warm off-white tones.
- Flat surfaces with 1px hairline borders instead of heavy, muddy dropshadows.
- Clear conversion pathways optimized for mobile devices, channeling every customer inquiry straight into a structured WhatsApp conversation (+54 3329 20-1399).

## Colors

The palette establishes an immediate rhythm of clinical sanitation balanced with regional warmth. 

- **Primary (`#1B2A4D`)**: Deep Maritime Navy. Derived directly from the brand insignia background. Acts as the primary structural anchor, used for top navigation, dark hero sections, footer caps, and primary buttons over light surfaces.
- **Secondary (`#EBD9BC`)**: Soft Warm Cream. Originates from the stylized logo isotype. Serves as a soothing alternate section backdrop, trust banners, numerical step badges, and headline text over navy backgrounds.
- **Tertiary / Accent (`#7FD1C4`)**: Clean Mint Aqua. Represents fresh water, sanitization, and immediate clarity. Strictly reserved for high-intent primary CTA buttons, floating contact triggers, interactive highlights, and active status indicators. Never overused (maximum 1–2 key interactions per viewport).
- **Neutral Base (`#FAF7F2`)**: Off-white Warm Base. Replaces harsh `#FFFFFF` to reduce eye fatigue and provide an approachable canvas that blends naturally with the cream accents.
- **Navy Dark (`#101A33`)**: Ultra-dark Navy used exclusively for high-contrast body and heading copy over light surfaces, as well as final ground-level footer bands.

## Typography

The typographic hierarchy is built on a high-legibility geometric pair: **Outfit** for structural headers and primary CTA buttons (providing friendly, rounded modern terminals that match the brand logo), paired with **Inter** for dense UI data, input forms, and descriptive body paragraphs.

- **Kickers / Overlines**: Always in uppercase with `0.08em` letter tracking, colored in Mint Aqua (`#7FD1C4`) over dark backgrounds or Deep Navy (`#1B2A4D`) over light surfaces.
- **Headlines (H1, H2, H3)**: Rendered in Outfit with tight, confident leading (`1.15` to `1.22`) to produce punchy value propositions suitable for Spanish syntax (voseo rioplatense).
- **Body & Forms**: Built on Inter (`400` regular, `500` medium) with an open `1.6` line height to ensure rapid skimming on low-brightness mobile displays in outdoor work settings.

## Layout & Spacing

The layout is fundamentally **mobile-first**, transitioning through a responsive 12-column grid system bounded at a maximum container width of `1120px` for general content and `700px` for calculation forms and conversion cards.

- **Breakpoints**:
  - `Mobile (< 640px)`: 4 columns, single-column vertical stack, `16px` outer gutter margin.
  - `Tablet (640px - 859px)`: 8 columns, 2-column paired layout for service comparisons and value propositions.
  - `Desktop (>= 860px)`: 12 columns, 3 to 4 columns for feature cards and trust grids, horizontal hero with right-side vector graphic.

Vertical section flow alternates background tonality (`#1B2A4D` navy -> `#FAF7F2` warm white -> `#EBD9BC` cream) to create natural pacing without requiring horizontal dividers.

## Elevation & Depth

Visual separation relies on clean surface layering and delicate geometric borders rather than heavy dropshadows:

- **Surface Tonal Stacking**: Depth is achieved via crisp color blocking. Cards placed on warm white (`#FAF7F2`) use pure white fills (`#FFFFFF`) with a 1px solid border set to `rgba(27, 42, 77, 0.12)`.
- **Ghost Outlines**: Interactive secondary controls and outlined badge groups feature a 1.5px border in cream (`#EBD9BC`) or maritime navy (`#1B2A4D`).
- **Targeted Floating Elevation**: Ambient shadows are restricted solely to the persistent mobile WhatsApp floating button and modal dialogues:
  - *Floating WhatsApp Trigger*: `box-shadow: 0 10px 25px -3px rgba(16, 26, 51, 0.28), 0 4px 10px -2px rgba(127, 209, 196, 0.35)`.
- **Focus Rings**: For universal accessibility, all active interactive elements apply an offset outline: `3px solid #7FD1C4` with a `2px` transparent gap.

## Shapes

The design system incorporates intentional organic curves to evoke hygiene and approachability:

- **Cards & Outer Containers**: `18px` border radius (`rounded-lg`). Soft, contemporary, and eliminating harsh industrial corners.
- **Form Controls & Accordions**: `12px` to `14px` border radius (`rounded-md`).
- **Interactive Buttons, Pills & Badges**: Fully rounded `999px` capsule silhouettes. This reinforces the pebble-like soft geometry of the brand's primary logotype.
- **Number Badges**: Pure circular forms (`width: 44px; height: 44px; border-radius: 50%`) with centered medium-weight numerals.

## Components

### Buttons
All buttons maintain a strict minimum tap target of `48px` (height) on mobile.
- **Primary CTA (Over Navy Background)**: Background Mint Aqua (`#7FD1C4`), label in Navy Dark (`#101A33`), weight 600, radius `999px`. Hover shifts to `#6bc4b6`.
- **Primary CTA (Over Light Background)**: Background Navy (`#1B2A4D`), label in Cream (`#EBD9BC`), weight 600, radius `999px`. Hover shifts to `#101A33`.
- **Secondary / Ghost**: Transparent fill, 1.5px outline in Cream (`#EBD9BC`) on dark sections or Navy on light sections.
- **Floating WhatsApp Button (Mobile Only)**: 58px diameter circle fixed `20px` from bottom-right. Mint Aqua background, deep navy WhatsApp icon, elevated shadow.

### Cards & Service Units
- Standard cards use `#FFFFFF` background over `#FAF7F2` canvas, `18px` border radius, `1px` subtle navy border (`rgba(27, 42, 77, 0.12)`).
- Top interior padding is `24px` to `28px`.
- Icons are 28px inline SVG with `1.8px` stroke weight, rounded caps, rendered in Navy Dark or Mint Aqua.

### Chips & Location Badges
- Capsule pills (`999px` radius) with Cream (`#EBD9BC`) or subtle Navy tint fill.
- Font: Inter 13px / 500 weight. Used for geographical coverage tags (Baradero, San Pedro, Zárate, Alsina, etc.).

### Inputs & Quotation Calculator
- Height: `48px`. Radius: `12px`.
- Border: `1.5px solid rgba(27, 42, 77, 0.25)`. Active/Focus state switches border to `#1B2A4D` with `#7FD1C4` glow outline.
- Labels are persistently visible above the field (Inter 14px, weight 500, Navy Dark).
- Form calculates parameter states (Service Type, Duration, Unit Quantity) and compiles a pre-filled WhatsApp URI redirect instead of submitting to a database.

### Trust Banner (Franja de Confianza)
- Background: Soft Cream (`#EBD9BC`).
- 4 items displayed in a 2x2 grid on mobile, resolving into a 4-column horizontal strip on desktop.
- Monochromatic navy iconography accompanied by concise reassurance copy.

### FAQ Accordion
- Full-width tap targets with `14px` radius, background `#FFFFFF`, bordered in `1px rgba(27, 42, 77, 0.12)`.
- Icon toggle uses simple "+" and "–" characters in Outfit 20px, transforming smoothly on open state.
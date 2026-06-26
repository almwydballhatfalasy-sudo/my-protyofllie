---
name: Excellence Diplomatic
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0d0e10'
  surface-container-low: '#1b1b1e'
  surface-container: '#1f1f22'
  surface-container-high: '#292a2c'
  surface-container-highest: '#343537'
  on-surface: '#e4e2e5'
  on-surface-variant: '#c5c6ce'
  inverse-surface: '#e4e2e5'
  inverse-on-surface: '#303033'
  outline: '#8f9098'
  outline-variant: '#44474d'
  surface-tint: '#b6c7ea'
  primary: '#b6c7ea'
  on-primary: '#20314d'
  primary-container: '#071a35'
  on-primary-container: '#7383a3'
  inverse-primary: '#4e5f7d'
  secondary: '#e9c266'
  on-secondary: '#3f2e00'
  secondary-container: '#755800'
  on-secondary-container: '#f8d073'
  tertiary: '#c5c6ca'
  on-tertiary: '#2e3034'
  tertiary-container: '#181a1d'
  on-tertiary-container: '#818286'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b6c7ea'
  on-primary-fixed: '#091b36'
  on-primary-fixed-variant: '#374764'
  secondary-fixed: '#ffdf9a'
  secondary-fixed-dim: '#e9c266'
  on-secondary-fixed: '#251a00'
  on-secondary-fixed-variant: '#5a4300'
  tertiary-fixed: '#e2e2e6'
  tertiary-fixed-dim: '#c5c6ca'
  on-tertiary-fixed: '#1a1c1f'
  on-tertiary-fixed-variant: '#45474a'
  background: '#131315'
  on-background: '#e4e2e5'
  surface-variant: '#343537'
typography:
  display-lg:
    fontFamily: ebGaramond
    fontSize: 64px
    fontWeight: '500'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: ebGaramond
    fontSize: 40px
    fontWeight: '500'
    lineHeight: 48px
  headline-lg-mobile:
    fontFamily: ebGaramond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  headline-md:
    fontFamily: ebGaramond
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
  body-lg:
    fontFamily: hankenGrotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: hankenGrotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: hankenGrotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style
The design system is engineered for the highest echelons of international relations, governance, and executive leadership. It evokes a sense of "Stately Modernism"—combining the traditional weight of an embassy with the digital precision of a global headquarters. 

The aesthetic is characterized by **Executive Minimalism** with a **Glassmorphic** overlay. It utilizes deep, immersive backgrounds to signify stability, accented by metallic tones that suggest heritage and prestige. Subtle Arabic geometric motifs should be used as low-opacity background patterns or masking elements to provide cultural depth and architectural structure without cluttering the interface. The emotional response should be one of absolute trust, quiet power, and formal clarity.

## Colors
The palette is rooted in **Deep Navy Blue**, serving as the primary canvas to establish an authoritative and serious tone. **Royal Gold** is reserved strictly for high-priority interactive elements, call-to-actions, and symbolic accents, ensuring it remains a mark of distinction rather than a primary filler.

**Silver Gray** is utilized for structural dividers and secondary metadata, providing a cool contrast to the warmth of the gold. Background surfaces leverage semi-transparency (Glassmorphism) to create a sense of architectural layers, allowing the deep navy to permeate through various levels of the UI.

## Typography
The typographic hierarchy relies on a high-contrast pairing between **EB Garamond** and **Hanken Grotesk**. 

- **Serif (EB Garamond):** Used for headlines and editorial statements. It conveys history and intellectual authority. Optical sizing should be prioritized to maintain grace at large sizes.
- **Sans-Serif (Hanken Grotesk):** Used for body copy, data, and functional labels. It provides a sharp, contemporary counterpoint that ensures legibility in complex reports or technical documentation.
- **Styling:** Large display text should feature slight negative letter-spacing for a "tight" editorial feel. Labels and small caps should have increased tracking to maintain an airy, premium breathing room.

## Layout & Spacing
The design system follows a **Fixed Grid** philosophy for desktop to maintain a "document-like" feel, transitioning to a fluid model for mobile. 

The rhythm is generous, inspired by the wide margins of official diplomatic communiqués. Use a 12-column grid for desktop with wide 32px gutters to prevent information density from feeling overwhelming. Vertical spacing should be aggressive—allowing sections to breathe to emphasize the importance of the content. 

**Breakpoints:**
- **Mobile (<768px):** 4 columns, 20px margins.
- **Tablet (768px - 1024px):** 8 columns, 40px margins.
- **Desktop (>1024px):** 12 columns, 64px margins, 1280px max-width container.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and **Tonal Layering** rather than traditional drop shadows. 

1. **Base:** The primary Navy background (#071A35).
2. **Elevated Surfaces:** Semi-transparent Navy containers with a 12px-24px backdrop blur and a 1px Silver Gray (#A8A9AD) border at 20% opacity. 
3. **Interactive Depth:** When an element is focused or hovered, the backdrop blur intensity increases, and the border color shifts to Royal Gold.

Avoid heavy shadows; use subtle inner glows or "rim lighting" (1px top border) to suggest physical presence in a digital space.

## Shapes
Shapes are disciplined and architectural. A "Soft" (0.25rem) corner radius is the standard for cards and containers, providing just enough approachability without losing the formal structure of a sharp edge. 

Buttons and specialized interactive chips may use a more pronounced corner radius for ergonomic clarity, but large structural containers must remain strictly within the Soft (radius 1) category to maintain a sense of permanence and gravitas.

## Components
- **Buttons:** Primary buttons use a solid Royal Gold fill with Navy text. Secondary buttons are "Ghost" style with a Silver Gray border and white text. All buttons should have a minimum height of 48px to ensure executive presence.
- **Cards:** Utilize the glassmorphic style—transparent Navy fill, backdrop blur, and a 1px subtle border. No shadows.
- **Inputs:** Fields are defined by a bottom-only border in Silver Gray, moving to a full Royal Gold border on focus. This mimics formal stationery.
- **Geometric Motifs:** Use SVG patterns based on 8-point Arabic stars as decorative backgrounds for headers or section dividers, rendered in a very low-contrast Navy (#0A2242).
- **Navigation:** Top-tier navigation should be centered and airy, using uppercase Label-MD typography.
- **Status Indicators:** Use refined, small circular "pills" with high-contrast icons for indicating diplomatic status or classification levels.
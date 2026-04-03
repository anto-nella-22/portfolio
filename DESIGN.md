# Design System Specification: The Technical Editorial

This design system is a bespoke framework crafted for a high-end freelance presence. It bridges the gap between rigorous engineering and high-fashion editorial design. It is designed to signal "Expert Developer" through precision and "Refined Professional" through a sophisticated, moody atmosphere.

---

### 1. Overview & Creative North Star
**Creative North Star: "The Architectural Indigo"**
This system rejects the "standard SaaS" look of white backgrounds and blue buttons. Instead, it adopts a high-contrast, dark-mode-first aesthetic that feels like a premium terminal or a luxury tech journal. We break the template by using **intentional asymmetry**: large-scale typography paired with generous, "expensive" white space (or "dark space") and elements that bleed off the grid to suggest a world beyond the screen.

---

### 2. Colors: Tonal Depth & Soul
The palette is rooted in deep, nocturnal navies (`surface: #0b1326`) and energized by a "Vibrant Electric Indigo" (`primary: #c0c1ff`).

*   **Primary (Electric Indigo):** Use `#c0c1ff` for core actions and `#4b4dd8` for containers. This isn't a passive blue; it’s a high-energy pulse that signals technical capability.
*   **Tertiary (Refined Gold):** Use `#e9c349` sparingly. This is your "Editorial Gold," reserved for high-level accents like award badges, premium tags, or critical CTAs.
*   **The "No-Line" Rule:** Explicitly prohibit 1px solid borders for sectioning. Structural boundaries must be defined by shifts in background tokens. Transition from `surface` to `surface-container-low` to create a new section.
*   **The "Glass & Gradient" Rule:** To achieve a premium polish, use subtle linear gradients for large backgrounds, moving from `surface` to `surface-container`. Hero areas should utilize a mesh gradient of `primary_container` and `surface` to add "soul" to the darkness.

---

### 3. Typography: The Editorial Voice
We pair the functional clarity of **Inter** with the aggressive, futuristic geometry of **Space Grotesk**.

*   **Display & Headlines (Space Grotesk):** Use `display-lg` (3.5rem) for hero statements. These should be tight-tracked (-2% to -4%) to feel like a high-end magazine cover.
*   **Body & Labels (Inter):** All long-form text uses Inter. Keep `body-lg` (1rem) for readability. The contrast between the eccentric `Space Grotesk` and the "invisible" `Inter` creates the "expert" persona.
*   **Hierarchy as Identity:** Use `tertiary` (`#e9c349`) for small `label-md` overlines above main headlines to establish an authoritative, curated feel.

---

### 4. Elevation & Depth: The Layering Principle
We move away from the flat web. Depth is achieved through **Tonal Layering** and **Glassmorphism**.

*   **Surface Nesting:** 
    *   Base Layer: `surface` (#0b1326)
    *   Section Layer: `surface-container-low` (#131b2e)
    *   Card Layer: `surface-container-high` (#222a3d)
*   **Glassmorphism:** For floating cards or navigation bars, use `surface_bright` with an opacity of 60% and a `backdrop-filter: blur(20px)`. This makes the layout feel integrated and "liquid."
*   **Ambient Shadows:** If a shadow is required for a floating state, use a 40px blur with 8% opacity, tinted with `#07006c`. Never use pure black or grey shadows.
*   **The Ghost Border:** If accessibility requires a stroke, use `outline-variant` at 15% opacity. It should be felt, not seen.

---

### 5. Components: Precision Primitives

#### **Buttons: The Action Signature**
*   **Primary:** Solid `primary` (#c0c1ff) with `on_primary` text. Radius: `md` (0.375rem). Use a subtle glow (outer shadow of the same color at 20% opacity) on hover.
*   **Secondary:** Glassmorphic. `surface_variant` at 20% opacity with a `Ghost Border`.
*   **Tertiary:** Text-only in `primary`, with a custom 2px underline that expands from the center on hover.

#### **Cards & Lists: Structural Air**
*   **The Divider Ban:** Strictly forbid `<hr>` or border-bottom dividers. Separate list items using `spacing-5` (1.7rem) and subtle background shifts.
*   **Hover States:** Cards should lift slightly using a `surface-container-highest` shift and an increase in backdrop-blur intensity.

#### **Inputs: The Technical Interface**
*   **Field Style:** Minimalist. Background: `surface_container_lowest`. Only a bottom border of `outline_variant` at 30% opacity. Focus state transitions the border to `primary` at 100% opacity.

#### **Custom Component: The "Tech Badge"**
*   Small chips used for languages (React, Rust, etc.). Use `secondary_container` with `on_secondary_container` text. Roundedness: `full`. These should feel like small, tactile stones.

---

### 6. Do's and Don'ts

**Do:**
*   **Do** use asymmetrical margins. If a headline is left-aligned, let the body text sit 2 columns to the right to create visual tension.
*   **Do** use `spacing-20` (7rem) or `spacing-24` (8.5rem) between major sections. Generous space is the ultimate sign of a premium brand.
*   **Do** use smooth transitions. Every hover and page entry should have a 400ms "ease-out-expo" timing.

**Don't:**
*   **Don't** use 100% white text. Use `on_surface` (#dae2fd) to reduce eye strain and maintain the sophisticated mood.
*   **Don't** use "default" shadows. If it looks like a standard Material Design drop shadow, it’s too heavy.
*   **Don't** use icons with varying stroke weights. Use a single, high-end icon set (like Phosphor or Lucide) in "Thin" or "Light" weight.

---

### 7. Spacing & Rhythm
Rhythm is dictated by the **1.4x scale**.
*   **Section Padding:** Always use `spacing-16` (5.5rem) or higher.
*   **Stacking:** Use `spacing-3` (1rem) for related elements (Label + Headline) and `spacing-6` (2rem) for unrelated blocks.
*   **Grid:** A 12-column grid is the base, but elements should frequently span "off-center" (e.g., a card spanning from column 3 to 11) to break the boxy feel of standard development portfolios.
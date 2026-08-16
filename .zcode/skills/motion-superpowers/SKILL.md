---
name: motion-superpowers
description: Superpowers-driven Remotion and HyperFrames video engineering workflow. Includes grounded research, MOTION.md style catalogs, reverse engineering from reference videos, frame-accurate TDD, and full audio architecture.
version: 2.0.0
author: ardha27
license: MIT
---

# Motion Superpowers (Remotion and HyperFrames Methodology)

A structured animation engineering methodology built on strict engineering discipline for Remotion (React/TSX) and HyperFrames (HTML/GSAP/DOM).

Key capabilities:
- Fact-grounded research (official primary sources first)
- MOTION.md style catalog (motion design tokens and timing curves)
- Reference video reverse engineering via optical flow and scene detection
- 7-phase production pipeline (Brief -> Storyboard -> Audio -> Code -> Still QA -> Render)
- Complete audio architecture (BGM generation + layered cinematic and UI SFX)

---

## 1. Core Principles and Hard Gates

### 1. Mandatory Official Research and Fact Grounding
- Do not build video scripts or animated slides on assumptions or secondary commentary.
- Every video project starts with live research on primary sources: official documentation, product changelogs, official repositories, technical whitepapers, and verified release notes.
- Use anti-detection browser sessions when needed to bypass bot mitigation on official documentation sites.
- Every metric, benchmark comparison, and architectural claim on screen must be verified.

### 2. Humanized Copy and Zero Slop
- Zero emojis on screen overlays and subtitles.
- Strip AI writing clichés: eliminate em dashes, filler words ("testament", "groundbreaking", "seamless", "pivotal"), and promotional puffery.
- Keep text clear, concise, and direct.

### 3. High-Signal Visual Hierarchy
- Avoid walls of text or repeating card layouts across scenes.
- Represent data visually: interactive benchmark bars, comparison matrices, terminal code blocks, split metric cards, and radial progress gauges.
- When matching a light reference theme (clean studio light, glassmorphism, or neutral paper), use crisp high-contrast palettes that meet WCAG AA standards.
- Anti-static motion polish:
  - Rolling metrics: animate numeric changes toward target values using `power3.out` or `easeOutExpo`.
  - Kinetic typography: reveal headlines and bullet points with structured stagger delays (`0.06s` to `0.1s`).
  - Progress and charts: animate width, scale, or SVG stroke offsets on scene entry.
  - Ambient drift: apply slight translation (for example, `y: -6px` over scene duration) so frames remain lively after landing.
  - Edge highlights: apply clean accent sweeps on primary focal points.

### 4. No Implementation Before Storyboard and Spec
- Do not write TSX or HTML code before locking scene breakdown, shot durations, visual mapping, and audio beats.

### 5. Deterministic Frame Timeline
- Never use non-deterministic timing (`Date.now()`, unbound `Math.random()`, or unclocked `requestAnimationFrame`).
- All animations must be pure functions of `frame` / `useCurrentFrame()` or statically seeded by element index.

### 6. Restrained Motion Hierarchy
- One primary focal movement per scene. Do not animate every element simultaneously.
- Hold for at least `0.3s` to `1.0s` after primary transitions settle so viewers can absorb the content.
- Stick to one signature easing curve per composition (such as `cubic-bezier(0.22, 1, 0.36, 1)` or `power4.out`).

### 7. Dual-Layer Audio Architecture
- Custom BGM: produce instrumental tracks matched to target BPM and vibe using procedural generation.
- Macro transitions: place whooshes, impacts, and risers at major scene transitions.
- Micro interactions: map subtle interface sounds (clicks, pops, snaps) to UI reveals and metric ticks.

---

## 2. MOTION.md Style Catalog

Every project chooses one style definition before development begins. Do not mix competing styles in one composition.

| Style Rulebook | Visual Feel | Primary Use Case |
|---|---|---|
| `motion-linear-snappy.md` | Fast, precise, keyboard-native | SaaS, developer tools, workflows |
| `motion-apple-fluid.md` | Spring-driven, physically grounded | Hardware, consumer tech, premium apps |
| `motion-stripe-polished.md` | Calm, deliberate, high-trust | Fintech, enterprise infrastructure, security |
| `motion-vercel-minimal.md` | Instant, stark, confident | Cloud infra, CLI tools, modern web frameworks |
| `motion-material-expressive.md` | Layered physics, expressive sheets | Mobile applications, dashboard systems |
| `motion-framer-spring.md` | Bouncy springs, dynamic layout shifts | Landing pages, portfolio showcases |
| `motion-gsap-cinematic.md` | Filmic pacing, synchronized timelines | Product reveals, brand narrative reels |
| `motion-game-impact.md` | High-impact punches, snappy snaps | Gaming, esports, high-energy clips |
| `motion-glitch-cyberpunk.md` | Digital distortion, rapid scanlines | Security tooling, Web3 protocols, tech teasers |
| `motion-editorial-scroll.md` | Editorial rhythm, typographic focus | Long-form explainers, technical deep-dives |
| `motion-fluent-productive.md` | Smooth acrylic surfaces, measured motion | Productivity suites, desktop applications |
| `motion-carbon-enterprise.md` | Strict grids, structured acceleration | Data platforms, IBM Carbon design systems |
| `motion-cinematic-product.md` | Floating studio lighting, controlled 2.5D | Flagship hardware and software showcases |
| `motion-linear-style.md` | Crisp snappy transitions (legacy v1) | Fast-paced product updates |

---

## 3. Reverse Engineering Reference Videos

When reproducing a reference video style, extract ground-truth motion metrics:

1. **Shot Segmentation and Optical Flow**:
   Run the analysis script to extract cut points, velocity curves, and primary color palettes:
   ```bash
   python3 scripts/extract_motion_spec.py --video path/to/reference.mp4 --out out/analysis/
   ```
2. **Visual Decomposition**:
   Inspect contact sheets and velocity charts to identify camera behaviors (pan, tilt, 2.5D perspective), hero vs secondary hierarchy, and stagger timing.
3. **Spec Synthesis**:
   Translate extraction data into a project-specific `MOTION.md` definition before writing animation code.

---

## 4. Seven-Phase Production Pipeline

```
[Phase 0: Primary Fact Research] -> Verify data on official sites
               ↓
[Phase 1: Brief and Motion Spec] -> Engine, resolution, frame rate, style book
               ↓
[Phase 2: Shot Recipe Mapping]   -> Map data points to visual patterns
               ↓
[Phase 3: Audio and Beat Grid]   -> Lock BPM, place transitions and UI cues
               ↓
[Phase 4: Implementation]        -> Code atomic components in Remotion or HyperFrames
               ↓
[Phase 5: Visual TDD / Still QA] -> Extract critical still frames to verify layout
               ↓
[Phase 6: Full Render and Probe] -> Render MP4 and verify duration and streams
```

---

## 5. Execution Reference

### Phase 1: Spec Definition
- Target Engine: Remotion (React/TSX) or HyperFrames (HTML/GSAP)
- Canvas: `1920x1080` (16:9), `1080x1920` (9:16), or `1080x1080` (1:1)
- Frame Rate: `30fps` or `60fps`
- Absolute Frames: `totalFrames = durationInSeconds * fps`

### Phase 2: Shot Mapping
- Match key metrics to animated counters (`DigitRoll`).
- Match architectural flows to multi-step node reveals.
- Match feature comparisons to split-screen matrices.

### Phase 3: Audio Grid
- Calculate frame markers for musical beats: `beatFrame = beatSecond * fps`.
- Align entrance keyframes with downbeats.
- Place UI clicks on data reveals.

### Phase 4: Implementation Rules
- Remotion: use `interpolate` and `spring` with explicit `fps` options.
- HyperFrames: configure GSAP timelines driven strictly by the master player timeline.
- Maintain readable typography on mobile screens (pill labels and captions at least `16px` to `24px` on `1080p`).

### Phase 5: Still Frame QA
Inspect still captures at scene transitions before launching full renders:
```bash
# Example Remotion still check
npx remotion still src/index.ts MainComposition out/frame-30.png --frame=30
```

### Phase 6: Final Render and Verification
Render video and verify output streams:
```bash
npx remotion render src/index.ts MainComposition out/video.mp4
ffprobe -v error -show_entries format=duration,size:stream=codec_name -of default=noprint_wrappers=1 out/video.mp4
```

<p align="center">
  <h1 align="center">motion-superpowers</h1>
</p>

<p align="center">
  <b>High-discipline motion graphics and video engineering for AI coding agents.</b><br />
  Compatible with Claude Code, OpenAI Codex, ZCode, and Hermes Agent.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" /></a>
  <a href="#supported-platforms"><img alt="Platforms" src="https://img.shields.io/badge/platforms-Claude%20%7C%20Codex%20%7C%20ZCode%20%7C%20Hermes-black?style=flat-square" /></a>
  <a href="#style-catalogs"><img alt="Styles" src="https://img.shields.io/badge/motion%20styles-14%20rulebooks-22a34a?style=flat-square" /></a>
</p>

---

## Overview

`motion-superpowers` is a production methodology for programmatic video generation with **Remotion** (React/TypeScript) and **HyperFrames** (HTML/GSAP).

Most LLMs write brittle, un-timed animation code with static card layouts, mismatched easing curves, and unstructured audio. This skill enforces:
1. **Fact-first research**: scripts grounded on official documentation and verified benchmarks.
2. **Deterministic timing**: pure frame-based clocking without race conditions.
3. **Motion catalogs (`MOTION.md`)**: pre-tuned easing curves, duration scales, and camera choreography.
4. **Visual test-driven development (TDD)**: still-frame assertions at key transition markers before full renders.
5. **Layered audio sync**: custom background tracks combined with frame-aligned UI sound cues.

---

## Supported Platforms

This repository is formatted for plug-and-play installation across major agent harnesses:

| Agent | Installation Path | Auto-Detection |
|---|---|---|
| **Claude Code** | `.claude/skills/motion-superpowers/SKILL.md` or `~/.claude/skills/` | Native skill registry |
| **OpenAI Codex** | `.codex/skills/motion-superpowers/SKILL.md` or `~/.codex/skills/` | ACP skill catalog |
| **ZCode** | `.zcode/skills/motion-superpowers/SKILL.md` or `~/.zcode/skills/` | Skill discovery |
| **Hermes Agent** | `~/.hermes/skills/motion-superpowers/` | Skill manager |

---

## Quick Start

### 1. Claude Code
Add to your project repository or personal skills folder:
```bash
# In your project root
mkdir -p .claude/skills/motion-superpowers
cp -r references scripts SKILL.md .claude/skills/motion-superpowers/
```

### 2. OpenAI Codex CLI / ZCode
```bash
# In your project root
mkdir -p .codex/skills/motion-superpowers .zcode/skills/motion-superpowers
cp -r references scripts SKILL.md .codex/skills/motion-superpowers/
cp -r references scripts SKILL.md .zcode/skills/motion-superpowers/
```

### 3. Hermes Agent
```bash
hermes skills install ardha27/motion-superpowers
```

---

## Workflow

```
[Phase 0: Fact Research]        -> Extract verified numbers from primary sources
               ↓
[Phase 1: Motion Spec]          -> Choose target resolution, FPS, and MOTION.md style
               ↓
[Phase 2: Shot Breakdown]       -> Map metrics to animated visual recipes
               ↓
[Phase 3: Sound & Beat Grid]    -> Align entrance frames with music downbeats
               ↓
[Phase 4: Implementation]       -> Code atomic components (Remotion/HyperFrames)
               ↓
[Phase 5: Still Frame QA]       -> Verify key frames (TDD) before full rendering
               ↓
[Phase 6: Full Render & Probe]  -> Render MP4 and verify audio/video sync
```

---

## Style Catalogs (`references/`)

Each `MOTION.md` rulebook defines physics parameters, timing curves, and staging patterns:

- `motion-linear-snappy.md`: Keyboard-native velocity for developer tools and workflows.
- `motion-apple-fluid.md`: Physically weighted springs for consumer tech and hardware showcases.
- `motion-stripe-polished.md`: High-trust deliberate motion for fintech and enterprise infra.
- `motion-vercel-minimal.md`: Stark, confident, instant transitions for cloud tooling.
- `motion-material-expressive.md`: Layered material sheets and dynamic elevation.
- `motion-framer-spring.md`: Playful spring physics for web product landing pages.
- `motion-gsap-cinematic.md`: Orchestrated camera choreography for brand showcases.
- `motion-game-impact.md`: High-energy snaps and dynamic screenshakes.
- `motion-glitch-cyberpunk.md`: High-frequency scanline distortions and color channel splits.
- `motion-editorial-scroll.md`: Magazine-style pacing for technical deep dives.
- `motion-fluent-productive.md`: Acrylic layered surfaces for desktop productivity software.
- `motion-carbon-enterprise.md`: Metric-driven grid transitions based on IBM Carbon.
- `motion-cinematic-product.md`: Studio lighting and depth of field for hardware heroes.
- `motion-linear-style.md`: Classic v1 linear timing recipe.

---

## Utility Scripts (`scripts/`)

- `extract_motion_spec.py`: Video reverse-engineering tool utilizing PySceneDetect, Farneback optical flow, and audio beat detection.
- `generate_bgm.py` / `generate_bgm.sh`: Automated BGM generation utility.

---

## Contributing

Contributions, additional style rulebooks, and shot recipes are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on submitting patches.

---

## License

Distributed under the [MIT License](LICENSE).

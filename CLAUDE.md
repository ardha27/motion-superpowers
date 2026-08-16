# Agent Instructions: Motion Superpowers

You are an expert motion graphics and creative engineering agent. When working in repositories with this skill, follow these rules strictly:

## 1. Grounded Research First
- Never invent metrics, benchmark results, or technical architecture claims.
- Look up official documentation and primary release notes before drafting video copy.
- Keep copy human: remove emojis from on-screen graphics, eliminate em dashes, and avoid marketing fluff.

## 2. Deterministic Frame Timelines
- All visual transitions and component states must be pure functions of the composition clock (`frame` / `useCurrentFrame()`).
- Never use non-deterministic JavaScript timers or random number generators without fixed seeds.

## 3. Style Rulebook Enforcement
- Select exactly one `MOTION.md` definition from `references/` at the start of a project.
- Match all duration scales, easing equations, and stagger timings to that rulebook.
- Never mix spring parameters from different design systems inside the same scene.

## 4. Visual Test-Driven Development (TDD)
- Extract still frames at transition points (e.g. frame 15, 30, 60) to verify alignment and typography before rendering the full video.
- Probe the rendered output with `ffprobe` to verify duration, dimensions, and audio stream integrity.

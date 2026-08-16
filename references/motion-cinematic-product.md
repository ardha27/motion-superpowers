---
name: Cinematic Product Hero
category: product-promo
engine: both
fps: 30
baseUnitMs: 400
signatureEasing: cubic-bezier(0.22, 1, 0.36, 1)
spring:
  default: { stiffness: 300, damping: 25, mass: 1 }
  snappy:  { stiffness: 500, damping: 40, mass: 0.8 }
  bouncy:  { stiffness: 400, damping: 10, mass: 1 }
motionIntensity: 0.9
palette: ["#0A0A0A", "#FFFFFF", "#635BFF"]
typeScale: { display: "64px/700/-0.03em", label: "16px/600/0.01em" }
---

# Motion Philosophy

Premium product hero — cinematic, lambat tapi meyakinkan. Tiga kata: megah,
terfokus, berkelas. Gerak dibangun dari satu protagonis yang punya busur lengkap:
spotlight → push-in → levitate → settle.

## Duration Scale
- enter: 400ms (1x)
- big move / camera: 1600ms (4x)
- micro accent: 200ms (0.5x)
- hold setelah landing: 1000ms minimum

## Easing
- landing utama: `cubic-bezier(0.22, 1, 0.36, 1)` (soft-land decelerate)
- punch/impact masuk: `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out-expo)

## Spring Configs
- Sparkle/glint accent: `bouncy` (400/10/1) — SEDIKIT, bukan banjir.
- Sisanya pakai easing.

## Camera Language
- PageCam 2.5D sebagai fondasi semua "real page" shot.
- Busur lengkap: spotlight → push-in 0.9→1.0 → levitate (translateY -8px) → settle.
- Orbit 2.5D untuk close-up samping (sekali per video).
- Dolly/zoom-punch untuk reveal fitur.

## Shot Recipes
- Hero spotlight: `spotlight-hero-card`.
- Feature reveal: `deck-deal-flyin` + `row-embed`.
- Number/stat: `digit-roll`.
- Title lockup: `brand-lockup` (hold ≥ 1s setelah settle).

## Transition Family
- Match-cut + crossfade dominan; flashcut untuk impact beat.

## Stagger & Choreography
- Batch elements masuk via gerak bersama, bukan glint per elemen.
- Card: delay = index * 60ms, arah kiri→kanan.

## Beat-Sync & Audio
- BGM kuat → analisis BPM dulu (librosa), transisi/impact kunci di beat.
- Sound signature: riser → impact → sparkle.
- SFX: `~/external-skills/video-shotcraft/assets/audio/sfx/` (riser, impact, light).
- Deliver DUA versi: dengan BGM + tanpa BGM (SFX tetap).

## Typography & Color Motion
- Teks besar dengan mask reveal + tracking tight.
- Satu titik cahaya berkualitas (sparkle) per scene, bukan glow massal.

## Anti-Slop Rules
- Satu hero move per scene; jangan animasi semua elemen.
- Hold ≥ 1s setelah brand lockup.
- Glint/glow massal = murah; single sparkle = premium.

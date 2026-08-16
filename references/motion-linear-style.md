---
name: Linear-style
category: product-tool
engine: remotion
fps: 30
baseUnitMs: 120
signatureEasing: cubic-bezier(0.16, 1, 0.3, 1)
spring:
  default: { stiffness: 300, damping: 25, mass: 1 }
  snappy:  { stiffness: 500, damping: 40, mass: 0.8 }
  bouncy:  { stiffness: 400, damping: 10, mass: 1 }
motionIntensity: 0.6
palette: ["#08090A", "#E6E8EB", "#5E6AD2"]
typeScale: { display: "48px/650/-0.02em", label: "13px/550/0.01em" }
---

# Motion Philosophy

Fast, precise, physically grounded — terasa native app, bukan website. Tiga kata:
cepat, presisi, low-friction. Gerak ada untuk memberi umpan balik kerja, bukan
dekorasi.

## Duration Scale
- micro (hover/focus): 1x baseUnitMs = 120ms
- enter (muncul elemen): 2x = 240ms
- big (panel/reveal): 4x = 480ms
- hold (jeda setelah landing): 3x = 360ms minimum

## Easing
- enter/landing: `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out-expo)
- exit: `cubic-bezier(0.7, 0, 0.84, 0)` (ease-in-expo)
- HANYA dua kurva ini.

## Spring Configs
- Interaksi langsung (drag, press, toggle): `snappy` (500/40/0.8)
- Popover/pop kecil: `bouncy` (400/10/1)
- Default state-change: gunakan easing, BUKAN spring.

## Camera Language
- Dominan: push-in halus 0.96→1.0 (scale), travel ≤ 24px.
- Zoom-punch hanya untuk konfirmasi aksi penting.
- Tidak ada orbit mewah; kamera "invisible".

## Shot Recipes
- Hero title: fade-slide y:12→0, 240ms, stagger 40ms per baris.
- Data/number: counter roll (DigitRoll), 1200ms easeOutExpo.

## Transition Family
- Match-cut + crossfade saja. Tanpa wipe/spin.

## Stagger & Choreography
- List: delay = index * 40ms, arah atas→bawah.
- Grid: delay = index * 30ms, arah kiri→kanan.

## Beat-Sync & Audio
- Tidak ada BGM beat; SFX hanya umpan balik UI (click, toggle, confirm).
- Sumber: `~/external-skills/uisfx/sounds/minimal/`.

## Typography & Color Motion
- Teks muncul kata-per-kata dengan mask reveal, tanpa glow.
- Warna aksen hanya transisi 150ms saat state berubah.

## Anti-Slop Rules
- Satu hero per frame; support selesai lebih dulu dari hero.
- Hold ≥ 360ms setelah gerak kunci.
- Tidak ada overshoot pada konten serius.

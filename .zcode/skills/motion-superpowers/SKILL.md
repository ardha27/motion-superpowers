---
name: motion-superpowers
description: Superpowers-driven Remotion/HyperFrames video methodology. Research first (Camofox official sources), then MOTION.md style catalog + reverse-engineer from reference video, storyboard spec, frame-accurate TDD, Suno BGM + dual SFX, render verify.
version: 2.0.0
category: "video-production"
---

# Motion Superpowers (Remotion & HyperFrames Methodology)

Metodologi rekayasa animasi terstruktur berbasis disiplin **Superpowers** untuk **Remotion (React/TSX)** dan **HyperFrames (HTML/GSAP/DOM)**. Mencakup: research fact-grounding, katalog `MOTION.md` (style rulebook), reverse-engineer style dari video referensi, pipeline produksi, BGM/SFX, dan verifikasi render.

---

## 1. Filosofi & Hard-Gates
1. **Mandatory Official Research & Fact-Grounded (General Rule)**:
   - Dilarang membuat video/naskah animasi dari asumsi, opini sekunder, atau data usang. Berlaku untuk SEMUA topik (AI tools, SaaS, fintech, Web3, open-source, infra, dll).
   - Setiap project video WAJIB diawali live research langsung ke **sumber resmi (Official Sources)**: official docs, release notes, changelogs, official GitHub repos, model cards/whitepapers, atau situs resmi vendor.
   - Wajib gunakan **Camofox Browser** (port `9377`) untuk mengakses halaman resmi agar terhindar dari bot-detection / Cloudflare wall.
   - Angka, benchmark, arsitektur, dan klaim on-screen teks harus 100% terverifikasi faktual.
2. **Humanizer & Zero AI-Slop Copy (Hard Rule)**:
   - Dilarang memakai emoji di seluruh teks/overlay video (zero emojis).
   - Wajib gunakan kaidah skill `humanizer`: hilangkan em-dash (—), hindari buzzwords AI generik ("boasts", "stands as", "testament", "groundbreaking", "nestled"), dan potong kalimat panjang menjadi punchy/ringkas.
   - Bahasa Indonesia: natural, lugas, mengalir, tanpa bahasa robot.
3. **High-Taste Visual Hierarchy & Rich Dynamic Layouts**:
   - Dilarang membuat video berbasis *wall of text* atau layout kartu monoton yang berulang di setiap scene.
   - Transformasikan data menjadi bentuk visual: **Interactive Benchmark Bar Graphs, Comparison Matrices, Split Price Chips, Interactive UI Windows, Live Terminal Snippets, dan Radial Progress**.
   - Background matching: jika referensi bertema cerah (clean light / glassmorphism / studio cream), gunakan palette cerah yang tajam dengan kontras WCAG AA yang sempurna, jangan default gelap.
   - **Rich Motion Polish (Anti-Static)**:
     - **Digit / Metric Roll**: Animasikan angka dari 0 menuju target (`gsap.to(obj, { value: target, onUpdate: ... })` atau `DigitRoll` Remotion) dengan easing `power3.out` / `easeOutExpo`.
     - **Kinetic Text & Staggered Reveal**: Judul dan sub-point masuk per kata / per elemen dengan delay berjenjang (`stagger: 0.06 - 0.1s`).
     - **Dynamic Progress & Charts**: Bar chart / circular gauge menganimasikan `scaleX` atau `strokeDashoffset` saat mendarat di viewport.
     - **Ambient Drift & Subtle Scale**: Kartu atau container UI diberi micro-scale / subtle float (misal `y: -6px`) agar frame tidak mati/statis setelah landing.
     - **Glint / Glow Accent Sweep**: Berikan aksen highlight pada elemen hero saat mendarat.
4. **No Code Before Storyboard & Spec**:
   - Jangan pernah menulis kode TSX/HTML sebelum naskah visual, durasi per shot, mapping data visual (graph/chart), dan timing beat disepakati.
5. **Deterministic Timeline**:
   - Dilarang keras memakai `Date.now()`, `Math.random()`, atau `window.requestAnimationFrame` tanpa clock terikat frame.
   - Semua pergerakan harus berupa fungsi murni dari `frame` / `useCurrentFrame()` atau seed statis terikat index.
6. **Restraint & Anti-Slop Motion**:
   - 1 hero move per scene. Tidak semua elemen bergerak bersamaan.
   - Hold minimal `0.3s - 1.0s` setelah gerakan kunci mendarat agar visual bernafas.
   - Easing konsisten: pilih 1 kurva signature (misal: `cubic-bezier(0.22, 1, 0.36, 1)` atau `power4.out`).
7. **Complete Audio Architecture (BGM + Dual SFX)**:
   - **BGM Generation (Suno AI)**: Gunakan script tool `scripts/generate_bgm.sh` untuk menghasilkan custom BGM instrumental sesuai BPM & style proyek.
   - **Cinematic & Big Transitions**: Gunakan `~/external-skills/video-shotcraft/assets/audio/sfx/` (149 SFX: impact, whoosh, riser, camera shutter, glitch).
   - **Micro-Interactions & UI Actions**: Gunakan `~/external-skills/uisfx/sounds/` (1.800+ SFX terorganisir dalam 12 tema: *cinematic, studio, minimal, soft, zen, scifi, glass, arcade, mechanical, organic, rubber, dreamy*).

---

## 2. MOTION.md Catalog (Style Rulebooks)

Katalog style siap-pakai, terinspirasi `awesome-design-md` / `awesome-motion-md`.
Setiap style adalah satu file `MOTION.md` yang mendefinisikan *feel* + token gerak
(filosofi, duration scale, easing, spring, camera, shot recipes, transisi,
stagger, beat-sync, anti-slop).

**Cara pakai:**
- Sebelum coding, pilih atau rujuk satu `MOTION.md` dari `references/` sebagai
  *motion language* proyek. Jangan mencampur dua style dalam satu video.
- Baca file-nya lewat `skill_view(name='motion-superpowers', file_path='references/motion-<style>.md')`.

**Katalog tersedia (`references/`):**

| File | Feel |
|---|---|
| `motion-linear-snappy.md` | Fast, precise, keyboard-native (SaaS/dev tools) |
| `motion-apple-fluid.md` | Spring-driven, physically grounded |
| `motion-stripe-polished.md` | Calm, deliberate, trustworthy (fintech) |
| `motion-vercel-minimal.md` | Instant, confident, done |
| `motion-material-expressive.md` | Physics-inspired, expressive |
| `motion-framer-spring.md` | Spring-native bouncy |
| `motion-gsap-cinematic.md` | Timeline cinematic, filmic |
| `motion-game-impact.md` | Punchy, high-impact (gaming) |
| `motion-glitch-cyberpunk.md` | Glitch, cyberpunk aesthetic |
| `motion-editorial-scroll.md` | Scroll-driven editorial |
| `motion-fluent-productive.md` | Calm, purposeful (enterprise) |
| `motion-carbon-enterprise.md` | Disciplined, precise (IBM Carbon) |
| `motion-cinematic-product.md` | Premium product hero (seed) |
| `motion-linear-style.md` | Linear-style (seed, v1) |

---

## 3. Reverse-Engineer Style (Video → MOTION.md)

Saat user minta "copy style/animasi dari video X" atau "bikin motion.md dari
video ini", jalankan pipeline ekstraksi deterministik & vision multi-layer:

### R1. Acquire Reference
- **URL**: download via `yt-dlp` (atau Camofox browser port 9377 bila butuh anti-bot).
- **File lokal**: gunakan path lokal.

### R2. Deterministic Extraction Engine
Jalankan script analisa otomatis yang terintegrasi di skill:
```bash
~/.hermes/skills/motion-superpowers/scripts/extract_motion_spec.py <path_video.mp4> --out-dir /tmp/motion_analysis
```
Script ini mengekstrak data kuantitatif:
1. **Metadata & Scene Cuts**: Menemukan titik potong cut transisi eksak (`ffmpeg scene threshold`).
2. **Optical Flow Motion Vectors (`cv2.calcOpticalFlowFarneback`)**: Menghitung kurva akselerasi pixel per frame untuk membedakan `ease-out` (puncak di awal) vs `ease-in` (puncak di akhir).
3. **Color Palette via K-Means**: Mengelompokkan warna dominan hex (`#HEX`).
4. **Audio BPM & Onset Transients (`librosa`)**: Mendeteksi ketukan musik dan timestamp detik saat SFX impact terjadi.
5. **Keyframe Tiling Contact Sheet**: Menghasilkan gambar matrix frame (tile 4x4) untuk inspeksi visual.

### R3. Visual Layer Vision Inspection (LLM Vision Gate)
Buka contact sheet yang dihasilkan ke `vision_analyze`:
```python
vision_analyze(
  image_url="/tmp/motion_analysis/contact_sheet.png",
  question="Analisis frame-by-frame: 1) Gerakan kamera (PageCam 2.5D, orbit, zoom punch, atau flat), 2) Elemen Hero vs Support, 3) Hierarki dan transisi tipografi, 4) Pola stagger antar elemen."
)
```

### R4. Synthesize & Generate MOTION.md
Gabungkan data kuantitatif dari `extraction_raw.json` dengan analisis visual untuk menghasilkan file `MOTION.md` yang 100% evidence-backed. Simpan ke `references/motion-<nama>.md`.

---

## 4. Pipeline Produksi (7 Fase)

```
[Phase 0: Deep Fact Research & Data Grounding] (Camofox + Sumber Official)
       ↓
[Phase 1: Brief & Motion Spec] (Engine, Dimensi, Durasi, MOTION.md style)
       ↓
[Phase 2: Shot Breakdown & Recipe Mapping] (Mapping ke 152 video-shotcraft recipes)
       ↓
[Phase 3: Sound & Beat-Grid Lock] (Suno AI BGM + Beat-Sync + SFX / UI cues)
       ↓
[Phase 4: Component Implementation] (Remotion / HyperFrames atomic components)
       ↓
[Phase 5: Frame-by-Frame QA & TDD] (Still capture at critical frames)
       ↓
[Phase 6: Verification & Full Render] (MP4 inspection & freeze audit)
```

---

## 5. Detail Eksekusi Tiap Fase

### Fase 0: Live Research & Official Fact Grounding (Wajib Menggunakan Camofox Browser)
Sebelum merancang storyboard (berlaku untuk topik apa pun):
1. **Target Official Sources First**:
   - Selalu cari sumber primer: official documentation, product changelogs, official GitHub repositories, model cards/whitepapers, verified press releases, API reference.
   - Hindari artikel pihak ketiga/agregator kecuali hanya sebagai pointer awal menuju sumber official.
2. **Camofox Anti-Detection Browsing**:
   - Gunakan headless **Camofox Browser** (port `9377`) via tool browser / snapshot API untuk scraping dan investigasi mendalam tanpa terblokir Cloudflare/bot-guards.
   - Buka langsung situs resmi, docs, dan rilis produk untuk mengekstrak konten murni.
3. **Ekstraksi Fakta & Verifikasi Metrik Kunci**:
   - Kumpulkan metrik pasti (angka performa, persentase peningkatan, tanggal rilis, nama fitur spesifik, arsitektur teknis).
   - Buat ringkasan fakta/data terverifikasi yang siap ditransformasikan ke on-screen text, charts, atau shot highlights.

### Fase 1: Brief & Motion Spec
Tentukan parameter dasar sebelum coding:
- **Engine**: `Remotion` (React TSX) atau `HyperFrames` (GSAP / Vanilla DOM).
- **Format**: 16:9 (`1920x1080`), 9:16 Vertical (`1080x1920`), atau Square (`1080x1080`).
- **FPS**: Standar `30fps` atau `60fps`.
- **Duration**: Total detik dan konversi frame mutlak (`totalFrames = durationSec * fps`).
- **MOTION.md style**: Pilih satu style dari `references/` sebagai motion language proyek.
- **UI SFX Theme**: Pilih 1 tema dari `uisfx` agar konsisten (misal: `minimal`, `studio`, atau `glass`).

### Fase 2: Shot Breakdown & Recipe Mapping
Bagi video menjadi segmen scene/shot terisolasi:
- Map setiap scene ke pola teruji (misal: `PageCam`, `SpotlightHero`, `DigitRoll`, `FlashCut`, `VerticalTicker`).
- Pasangkan data hasil research ke visual layer (misal: angka statistik pakai `DigitRoll`, fitur utama pakai `SpotlightHero`).
- Catat durasi in-frame dan out-frame tiap scene secara presisi.

### Fase 3: Audio, BGM & SFX Grid
1. **Generate BGM via Suno AI Tool**:
   ```bash
   ~/.hermes/skills/motion-superpowers/scripts/generate_bgm.sh \
     --style "modern tech house, 124 bpm, punchy bass, pristine production" \
     --title "Project BGM" \
     --output "assets/audio/bgm.mp3"
   ```
2. **Beat-Sync Analysis**: Hitung posisi frame beat (`beat_frame = beat_second * fps`).
3. **SFX Placement**:
   - **Transisi / Camera / Impact**: `~/external-skills/video-shotcraft/assets/audio/sfx/{impact,transition,camera,data,riser}/`
   - **Micro UI (Click, Toggle, Pop, Badge, Connect)**: `~/external-skills/uisfx/sounds/<theme>/<action>.mp3`

### Fase 4: Code Implementation
- **Remotion**: Gunakan `interpolate` / `spring` dengan config terikat `fps`. Impor audio via `<Audio src={staticFile('...')} />`.
- **HyperFrames**: Gunakan GSAP timeline yang disinkronkan dengan frame player.
- Pastikan ukuran tipografi mobile-safe (label/pill minimal `16-24px`).

### Fase 5: Still Frame QA (TDD Visual)
Sebelum merender seluruh video, ekstrak still frame kunci untuk verifikasi:
```bash
# Remotion still check
npx remotion still src/index.ts <CompositionName> out/check-frame-30.png --frame=30
```
Periksa alignment, hierarchy, akurasi data/teks, keterbacaan tipografi, dan ketiadaan glitch rendering.

### Fase 6: Render & Verification
Render video final dan jalankan pemeriksaan durasi/audio stream:
```bash
# Render Remotion
npx remotion render src/index.ts <CompositionName> out/final.mp4
# Probe output
ffprobe -v error -show_entries format=duration,size:stream=codec_name -of default=noprint_wrappers=1 out/final.mp4
```

---

## 6. Referensi & Tools
- **MOTION.md Style Catalog**: `references/motion-*.md` (14 style rulebook)
- **Grounded Research & Citations**: `~/.hermes/skills/research/grounded-citations/` & `deep-research/`
- **Suno BGM Generator**: `~/.hermes/skills/motion-superpowers/scripts/generate_bgm.sh`
- **Shot Recipes (152 Cards)**: `~/.hermes/skills/motion-craft/video-shotcraft/`
- **UI Sound Pack (12 Themes)**: `~/external-skills/uisfx/sounds/`
- **Official Remotion Rules**: `~/.hermes/skills/motion-craft/remotion-best-practices/`
- **Motion Principles & Easing**: `~/.hermes/skills/motion-craft/animation-principles/`
- **awesome-motion-md (upstream)**: `~/external-skills/awesome-motion-md/`

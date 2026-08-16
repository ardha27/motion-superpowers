#!/usr/bin/env python3
"""
Motion Smoothness & Anti-Patah Static Auditor for HyperFrames (HTML/GSAP) and Remotion.

Audits code against 5 proven motion engineering rules:
1. CSS Transition vs GSAP Conflict (causes frame jitter)
2. `preserve-3d` Opacity Flattening Bug (causes 2D->3D snap/patah at opacity 1.0)
3. Seek-Unsafe `gsap.to()` on Entrance/Exit (causes frame jump during seeking)
4. Drift & Exit Temporal Overlap (causes simultaneous tween conflicts)
5. Typography Scale & WCAG AA (ensures mobile-safe font sizes >= 16px)

Usage:
  python3 audit_motion_smoothness.py index.html
  python3 audit_motion_smoothness.py src/Composition.tsx
"""

import sys, os, re, json

def audit_file(filepath):
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    warnings = []
    passes = []

    # --- Rule 1: CSS Transition vs GSAP Conflict ---
    # Look for CSS `transition:` on transform or opacity
    css_transitions = re.findall(r'([\.#]?[\w-]+)\s*\{[^}]*transition:\s*([^;\}]+)', content, re.DOTALL)
    for selector, trans_val in css_transitions:
        if any(prop in trans_val for prop in ['transform', 'all', 'opacity', 'scale', 'rotate', 'translate']):
            # Check if this selector is also used in GSAP
            sel_clean = selector.strip()
            if sel_clean and (f"'{sel_clean}'" in content or f'"{sel_clean}"' in content or f"`{sel_clean}`" in content):
                issues.append({
                    "rule": "CSS Transition Conflict",
                    "severity": "HIGH",
                    "selector": sel_clean,
                    "detail": f"CSS selector `{sel_clean}` defines `transition: {trans_val.strip()}` while being animated by GSAP. This causes frame jitter/patah as CSS and GSAP fight over transform writes."
                })

    # --- Rule 2: preserve-3d Opacity Flattening ---
    # Check if elements with transform-style: preserve-3d also have opacity < 1 or GSAP opacity tween
    p3d_selectors = re.findall(r'([\.#]?[\w-]+)\s*\{[^}]*transform-style:\s*preserve-3d', content)
    for sel in p3d_selectors:
        sel_clean = sel.strip()
        # Check CSS for initial opacity: 0
        css_opacity = re.search(r'' + re.escape(sel_clean) + r'\s*\{[^}]*opacity:\s*([0-9\.]+)', content)
        if css_opacity and float(css_opacity.group(1)) < 1.0:
            issues.append({
                "rule": "preserve-3d Opacity Flattening",
                "severity": "CRITICAL",
                "selector": sel_clean,
                "detail": f"Selector `{sel_clean}` has `transform-style: preserve-3d` AND `opacity: {css_opacity.group(1)}`. CSS forces 3D hierarchy to render FLAT 2D whenever opacity < 1, causing a sudden 3D snap/patah when opacity reaches 1.0. Fix: Move opacity to a parent 2D wrapper element."
            })
        
        # Check GSAP for opacity animation on preserve-3d element
        gsap_opacity = re.findall(r"gsap\.(?:to|fromTo|from)\(\s*['\"`]" + re.escape(sel_clean) + r"['\"`]\s*,\s*\{[^}]*opacity:", content)
        if gsap_opacity:
            issues.append({
                "rule": "preserve-3d Opacity Tween",
                "severity": "HIGH",
                "selector": sel_clean,
                "detail": f"GSAP animates `opacity` directly on `{sel_clean}` which has `transform-style: preserve-3d`. Separate the 2D opacity wrapper from the 3D transform container."
            })

    # --- Rule 3: Seek-Unsafe `.to()` Usage ---
    # Look for gsap.to() or timeline.to() on entrance/exit
    to_tweens = re.findall(r'(\b\w+\.to\(\s*[\'\"`][^\'\"`]+[\'\"`]\s*,\s*\{[^}]*\}\s*\))', content)
    for tween in to_tweens:
        if any(kw in tween for kw in ['opacity:', 'scale:', 'y:', 'x:', 'rotateX:', 'rotateY:']):
            # If it's part of entrance or exit timeline
            if 'dur' in tween or '0.' in tween or '1.' in tween:
                warnings.append({
                    "rule": "Seek-Unsafe GSAP .to()",
                    "severity": "MEDIUM",
                    "snippet": tween[:80] + '...',
                    "detail": "Using `.to()` on entrance/exit tweens relies on lazy-start value capture, which causes frame jumps when headless renderers seek non-monotonically. Prefer `.fromTo()` for seek safety."
                })

    # --- Rule 4: Drift & Exit Overlap ---
    # Check for drift duration vs exit start
    drift_matches = re.findall(r'duration:\s*dur\s*-\s*([0-9\.]+)', content)
    exit_matches = re.findall(r'dur\s*-\s*([0-9\.]+)', content)
    if drift_matches and exit_matches:
        drift_end = float(drift_matches[0])
        # Look for exit start timestamp
        for ex in exit_matches:
            ex_val = float(ex)
            if abs(drift_end - ex_val) < 0.05 and drift_end != ex_val:
                warnings.append({
                    "rule": "Drift/Exit Overlap Potential",
                    "severity": "MEDIUM",
                    "detail": f"Drift tween duration is `dur - {drift_end}` while exit start is `dur - {ex_val}`. Ensure drift end timestamp exactly matches exit start timestamp to prevent simultaneous tween write conflicts."
                })

    # --- Rule 5: Typography Scale (Mobile-Safe < 16px) ---
    small_fonts = re.findall(r'font-size:\s*([0-9]+)px', content)
    tiny_fonts = [int(f) for f in small_fonts if int(f) < 16]
    if tiny_fonts:
        warnings.append({
            "rule": "Small Typography Warning",
            "severity": "LOW",
            "detail": f"Found {len(tiny_fonts)} font-size declarations smaller than 16px (e.g. {set(tiny_fonts)}px). Labels and pills should be >= 16px to remain legible on mobile/1080p outputs."
        })
    else:
        passes.append("Typography scale is mobile-safe (all font-sizes >= 16px).")

    # --- Report Output ---
    print(f"\n==== Motion Smoothness Audit: {os.path.basename(filepath)} ====\n")
    
    if not issues and not warnings:
        print("✅ PASSED: 0 critical issues, 0 warnings found. Motion code is smooth and seek-safe!")
        return 0

    if issues:
        print(f"❌ CRITICAL ISSUES ({len(issues)}):")
        for i in issues:
            print(f"  - [{i['severity']}] {i['rule']} ({i.get('selector', '')})")
            print(f"    {i['detail']}\n")

    if warnings:
        print(f"⚠️  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - [{w['severity']}] {w['rule']}")
            print(f"    {w['detail']}\n")

    if passes:
        print("PASSED CHECKS:")
        for p in passes:
            print(f"  - {p}")

    return len(issues)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 audit_motion_smoothness.py <path-to-html-or-tsx>")
        sys.exit(1)
    sys.exit(audit_file(sys.argv[1]))

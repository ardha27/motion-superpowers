#!/usr/bin/env python3
"""CLI utility to generate background music (BGM) / instrumental tracks using Suno AI Automation credentials."""

import argparse
import os
import sys
import time
from pathlib import Path

# Add sunoai-automation to path
sys.path.insert(0, "/home/rishua/sunoai-automation")

try:
    from src.clients.suno_client import SunoClient
    from src.config import get_settings
except ImportError as e:
    print(f"Error importing sunoai-automation modules: {e}", file=sys.stderr)
    sys.exit(1)


def generate_bgm(
    prompt: str,
    style: str,
    title: str,
    output_path: str,
    instrumental: bool = True,
    model: str = "V5_5",
) -> str:
    print(f"[*] Initializing Suno Client with model {model}...")
    client = SunoClient(model=model)
    
    print(f"[*] Submitting generation task:")
    print(f"    Title: {title}")
    print(f"    Style: {style}")
    print(f"    Instrumental: {instrumental}")
    print(f"    Prompt/Tags: {prompt}")

    result = client.generate_and_wait(
        prompt=prompt,
        style=style,
        title=title,
        instrumental=instrumental,
    )

    out_file = Path(output_path).expanduser().resolve()
    out_file.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"[*] Downloading generated track from {result.audio_url}...")
    client.download_audio(result.audio_url, out_file)
    print(f"[✓] BGM successfully generated & saved to: {out_file}")
    print(f"    Duration: {result.duration_seconds}s | Task ID: {result.task_id}")
    return str(out_file)


def main():
    parser = argparse.ArgumentParser(description="Generate BGM via Suno AI automation.")
    parser.add_argument("--style", required=True, help="Music genre / style tags (e.g. 'cyberpunk synthwave, 120 bpm, upbeat, punchy beat')")
    parser.add_argument("--title", default="Motion BGM", help="Song/track title")
    parser.add_argument("--prompt", default="Instrumental background music for modern product showcase video", help="Music direction prompt / lyrics")
    parser.add_argument("--output", "-o", default="out/suno_bgm.mp3", help="Destination MP3 path")
    parser.add_argument("--vocal", action="store_true", help="Enable vocals (default: instrumental only)")
    parser.add_argument("--model", default="V5_5", help="Suno model version (default: V5_5)")

    args = parser.parse_args()
    generate_bgm(
        prompt=args.prompt,
        style=args.style,
        title=args.title,
        output_path=args.output,
        instrumental=not args.vocal,
        model=args.model,
    )


if __name__ == "__main__":
    main()

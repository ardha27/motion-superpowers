#!/usr/bin/env bash
# Wrapper to execute generate_bgm.py using sunoai-automation virtual environment
VENV_PYTHON="/home/rishua/sunoai-automation/.venv/bin/python"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -f "$VENV_PYTHON" ]; then
    exec "$VENV_PYTHON" "$SCRIPT_DIR/generate_bgm.py" "$@"
else
    exec python3 "$SCRIPT_DIR/generate_bgm.py" "$@"
fi

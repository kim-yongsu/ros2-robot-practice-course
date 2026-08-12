#!/usr/bin/env bash
set -euo pipefail

python -m compileall -q examples tests scripts docs/source/conf.py
ruff format --check examples tests scripts docs/source/conf.py
ruff check examples tests scripts docs/source/conf.py
python -m pytest -q

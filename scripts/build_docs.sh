#!/usr/bin/env bash
set -euo pipefail

python scripts/sync_assets.py
python scripts/content_lint.py
python scripts/check_relative_links.py
python scripts/check_translation_parity.py
python scripts/check_snippet_sync.py
python scripts/check_issue_forms.py
python scripts/sphinx_source_preflight.py
python -m sphinx -W --keep-going -b html docs/source docs/_build/html
python -m sphinx -W --keep-going -b linkcheck docs/source docs/_build/linkcheck

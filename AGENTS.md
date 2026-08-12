# Repository map

## Scope

ROS 2 robot practice course documentation. Burger Volume 1 is the only populated course in this preview.

## Sources of truth

- Korean course text: `docs/source/`
- Executable examples: `examples/`
- Diagram sources: `assets/`
- Version and translation status: `translation_status.yml`

DOCX/PDF files are Release assets, not editable canonical sources.

## Build and tests

```bash
python -m pip install -r docs/requirements.txt -c docs/constraints.txt
python scripts/sync_assets.py
sphinx-build -W --keep-going -b html docs/source docs/_build/html
sphinx-build -W --keep-going -b linkcheck docs/source docs/_build/linkcheck
python -m pytest -q
```

## Boundaries

- Do not add results from tests that were not run.
- Do not claim support for a ROS distribution that was not verified.
- Do not copy example code into documentation; use `literalinclude`.
- Do not commit release PDFs or ZIP files to the main history.
- Do not add private paths, credentials, or unreviewed third-party assets.

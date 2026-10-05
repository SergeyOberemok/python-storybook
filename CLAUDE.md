# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal "storybook" of Python learning notebooks, not an application. Almost everything is a standalone Jupyter notebook (`.ipynb`) exploring one topic. Top-level folders group notebooks by subject: `Types/` (built-in types, strings, lists, dicts, dates, files, Faker), `Flow/` (control flow, generators), `Math/`, `Formulas/`, `Sympy/`, `NumPy/`, `Pandas/`, `Matplotlib/`, `ML/`, `Learning/` (numbered course-section notebooks), `Skanavi/`, `Tasks/`. There is no build, lint config, or dependency manifest.

## Environment

- Notebooks run on the Anaconda `base` kernel (kernelspec `conda-base-py`), which supplies numpy, pandas, sympy, matplotlib, ipywidgets, faker, etc. The system Python (`C:\Python313`) does not have pytest or these libraries, so use the conda environment.
- Some notebooks are paired with a `.py` file via **jupytext** (light format), e.g. `Formulas/Golden_Ration.ipynb` ↔ `Formulas/Golden_Ration.py`, `Jupyter/barrel_export.ipynb` ↔ `Jupyter/barrel_export.py`. When editing a paired notebook, keep both files in sync (edit one and let jupytext sync, or update both).

## Sharing code between notebooks

There is no installed package. Notebooks import reusable code by appending sibling folders to `sys.path` in an early cell, then importing the module by name:

```python
paths = [os.path.abspath(os.path.join("..\\Formulas"))]
for path in (p for p in paths if p not in sys.path):
    sys.path.append(path)
from Golden_Ration import calcGoldenRationX
```

The jupytext-paired `.py` files are what make this work: the `.py` side of a notebook is importable from other notebooks (`Jupyter/barrel_export` / `barrel_import` demonstrate the pattern).

## `Math/math_lib`

The only real library code: helpers used by `Math/` notebooks (imported as `math_lib.icons_utils`, `math_lib.numbers_utils`, `math_lib.html_table`).

- `numbers_utils.py` — digit extraction and random number generation.
- `icons_utils.py` — maps digits/numbers (and numpy matrices) to icon strings; imports `numbers_utils` with a relative import.
- `html_table.py` — `TableHtml` for rendering tables in notebooks.

Tests live in `Math/math_lib/__tests__/` and use pytest. The root `pytest.ini` puts `Math/` on `sys.path`, so tests import the package (`from math_lib.numbers_utils import ...`), matching the relative imports inside `math_lib`:

```
~/anaconda3/python.exe -m pytest
~/anaconda3/python.exe -m pytest Math/math_lib/__tests__/test_numbers_utils.py::test_generateRandomNumbers
```

## Running notebooks headlessly

Use `nbclient` from the conda env with the notebook's own folder as the working directory (notebooks use relative paths like `./data/...`). Notebooks calling `input()` need it stubbed. Running `Flow/Files.ipynb` and `Types/Files/files.create.ipynb` modifies the tracked `Flow/temp.txt` / `Types/Files/test.txt`; restore them afterwards. Known non-runnable: `Math/Addition table.ipynb` (imports `Assessments`/`Strategies` from a missing `../Algorithms/Tuition`), `Types/Images/images.comparison.ipynb` (needs `opencv`), `Finances/Test.ipynb` (needs `nasdaqdatalink` + a local `Finances/api_key`, which is gitignored).

The conda env ships pandas 3.x: use `'ME'` instead of `'M'` for month-end frequencies, and note Copy-on-Write semantics.

When editing `.ipynb` JSON, preserve each file's existing line endings (some are CRLF) and clear outputs of changed cells.

## Conventions

- camelCase is used for functions and variables (e.g. `generateRandomNumbers`, `mapNumberToIcons`) rather than PEP 8 snake_case; follow the existing style.
- `.ipynb_checkpoints`, `.virtual_documents`, `.jupyter`, `anaconda_projects`, `.idea` are ignored and should not be committed.

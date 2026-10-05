# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal "storybook" of Python learning notebooks, not an application. Almost everything is a standalone Jupyter notebook (`.ipynb`) exploring one topic. Top-level folders group notebooks by subject: `types/` (built-in types, strings, lists, dicts, dates, files, Faker), `flow/` (control flow, generators), `math/`, `formulas/`, `sympy/`, `numpy/`, `pandas/`, `matplotlib/`, `ml/`, `learning/` (numbered course-section notebooks), `skanavi/`, `tasks/`. There is no build, lint config, or dependency manifest.

## Environment

- Notebooks run on the Anaconda `base` kernel (kernelspec `conda-base-py`), which supplies numpy, pandas, sympy, matplotlib, ipywidgets, faker, etc. The system Python (`C:\Python313`) does not have pytest or these libraries, so use the conda environment.
- Some notebooks have a `.py` sibling generated from them with **nbconvert** (`nbconvert --to script`), e.g. `formulas/golden_ration.ipynb` → `formulas/golden_ration.py`, `jupyter/barrel_export.ipynb` → `jupyter/barrel_export.py`. The notebook is the source of truth: edit it, then regenerate the `.py` (never hand-edit it). Raw cells must be exported as comments so importing the module has no side effects (convert them to markdown cells in memory with a preprocessor before exporting).

## Sharing code between notebooks

There is no installed package. Notebooks import reusable code by appending sibling folders to `sys.path` in an early cell, then importing the module by name:

```python
paths = [os.path.abspath(os.path.join("..\\formulas"))]
for path in (p for p in paths if p not in sys.path):
    sys.path.append(path)
from golden_ration import calc_golden_ration_x
```

The nbconvert-generated `.py` files are what make this work: the `.py` side of a notebook is importable from other notebooks (`jupyter/barrel_export` / `barrel_import` demonstrate the pattern).

## `math/math_lib`

The only real library code: helpers used by `math/` notebooks (imported as `math_lib.icons_utils`, `math_lib.numbers_utils`, `math_lib.html_table`).

- `numbers_utils.py` — digit extraction and random number generation.
- `icons_utils.py` — maps digits/numbers (and numpy matrices) to icon strings; imports `numbers_utils` with a relative import.
- `html_table.py` — `TableHtml` for rendering tables in notebooks.

Tests live in `math/math_lib/tests/` and use pytest. The root `pytest.ini` puts `math/` on `sys.path`, so tests import the package (`from math_lib.numbers_utils import ...`), matching the relative imports inside `math_lib`:

```
~/anaconda3/python.exe -m pytest
~/anaconda3/python.exe -m pytest math/math_lib/tests/test_numbers_utils.py::test_generate_random_numbers
```

## Running notebooks headlessly

Use `nbclient` from the conda env with the notebook's own folder as the working directory (notebooks use relative paths like `./data/...`). Notebooks calling `input()` need it stubbed. Running `flow/files.ipynb` and `types/Files/files_create.ipynb` modifies the tracked `flow/temp.txt` / `types/Files/test.txt`; restore them afterwards. Known non-runnable: `math/algebra/operations/addition_table.ipynb` (imports `Assessments`/`Strategies` from a missing `../Algorithms/Tuition`), `types/Images/images_comparison.ipynb` (needs `opencv`), `finances/test.ipynb` (needs `nasdaqdatalink` + a local `finances/api_key`, which is gitignored).

The conda env ships pandas 3.x: use `'ME'` instead of `'M'` for month-end frequencies, and note Copy-on-Write semantics.

When editing `.ipynb` JSON, preserve each file's existing line endings (some are CRLF) and clear outputs of changed cells.

## Conventions

- PEP 8 naming: `snake_case` for functions, variables, arguments, methods and module/notebook file names (e.g. `generate_random_numbers`, `map_number_to_icons`, `golden_ration.ipynb`), `PascalCase` for classes. Notebook file names are lowercase snake_case with no spaces, dots or `&` (`&` becomes `and`). Single-letter uppercase names (`A`, `M`) are tolerated in notebooks for mathematical notation (matrices, sympy symbols), not in library code.
- `.ipynb_checkpoints`, `.virtual_documents`, `.jupyter`, `anaconda_projects`, `.idea` are ignored and should not be committed.

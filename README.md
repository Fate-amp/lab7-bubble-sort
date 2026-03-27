# Bubble Sort Lab

A beginner-friendly Python lab for practicing bubble sort and test-driven thinking.

## What This Project Contains

- A bubble sort app in `main.py`
- Automated tests using pytest in `tests/test_main.py`
- Pytest configuration in `pytest.ini`
- Progress log in `JOURNAL.md`

## Prerequisites

- Python 3.10+
- pip

## Setup

1. Create a virtual environment:

```powershell
py -m venv .venv
```

2. Activate it (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install pytest
```

## Run the App

```powershell
python main.py
```

The script runs several built-in examples:
- Unsorted list
- Already sorted list
- Reverse-sorted list
- Single-element list
- Empty list

## Terminal Visualization

The project also includes a terminal animation for bubble sort in `bubble_sort_visual`.

Current frame format:
- `Pass`: current bubble-sort pass (1-based)
- `Comparing index`: left index `j` being compared with `j + 1`
- `Action`: one of `Comparing`, `Swapped`, or `No swap`
- `Swapped this step`: whether the current comparison caused a swap
- `Unsorted end index`: right boundary of the unsorted section

Each frame prints one row per index in the form:

```text
index | ####
```

A caret `^` is shown on the row of the left compared index.

### Enable Visualization Demo

In `main.py`, uncomment the visualization demo lines near the bottom:

```python
# visual_input = [14, 1, 7, 13, 12, 2, 8, 10, 6, 5, 0, 3, 11, 9, 4]
# bubble_sort_visual(visual_input, delay=0.15)
```

Then run:

```powershell
python main.py
```

Tip: Increase `delay` (for example `0.3`) to slow down the animation.

## Run Tests

```powershell
python -m pytest
```

You should see 5 tests pass.

## Current Learning Focus

The `bubble_sort` function includes TODO comments designed for learning. A good next step is to finish or refine these parts:

- Track whether any swap happened during each pass
- Exit early if no swap occurred (already sorted)
- Keep code style consistent and readable

## Suggested Practice Steps

1. Implement the swap-tracking flag.
2. Add early-return optimization.
3. Re-run tests after each change.
4. Add one new test (for duplicates).

## Project Structure

```text
lab7-bubble-sort/
├── main.py
├── pytest.ini
├── tests/
│   └── test_main.py
├── JOURNAL.md
└── REPORT.md
```

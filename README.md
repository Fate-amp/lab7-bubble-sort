# Bubble Sort Lab

A beginner-friendly Python lab for practicing bubble sort and test-driven thinking.

## What This Project Contains

- App orchestration in `main.py`
- Pure sorting logic in `sorting_logic.py`
- Terminal UI in `terminal_ui.py`
- Pygame UI in `pygame_ui.py`
- Automated tests using pytest in `tests/test_main.py`
- Pytest configuration in `pytest.ini`
- Dependency list in `requirements.txt`
- Progress log in `JOURNAL.md`

## Architecture

This project now follows separation of concerns:

- `sorting_logic.py`: contains bubble sort algorithm and visualization step generation.
- `terminal_ui.py`: responsible only for terminal drawing.
- `pygame_ui.py`: responsible only for Pygame drawing.
- `main.py`: imports logic/UI modules and decides what to run.

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
python -m pip install -r requirements.txt
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

The project includes a terminal animation in `terminal_ui.visualize_bubble_sort_terminal`.

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

### Enable Terminal Demo

In `main.py`, uncomment the terminal demo line in `main()`:

```python
# visualize_bubble_sort_terminal(visual_input, delay=0.15)
```

Then run:

```powershell
python main.py
```

Tip: Increase `delay` (for example `0.3`) to slow down the animation.

## Pygame Visualization

The project includes a Pygame visualizer in `pygame_ui.visualize_bubble_sort_pygame`.

Current implementation highlights:
- Window-based animation using bars for each value
- Compared pair highlighted during each step
- Sorted tail highlighted
- Header displays pass/action/swap-step metadata

### Run Pygame Demo

In the current `main.py`, Pygame visualization is enabled by default:

```python
visual_input = [14, 1, 7, 13, 12, 2, 8, 10, 6, 5, 0, 3, 11, 9, 4]
visualize_bubble_sort_pygame(visual_input, fps=20)
```

Run:

```powershell
python main.py
```

Close the Pygame window to end the visualization loop.

### Dependency Note

This project uses `pygame-ce` in `requirements.txt` for compatibility with newer Python versions while keeping `import pygame` in code.

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
├── sorting_logic.py
├── terminal_ui.py
├── pygame_ui.py
├── requirements.txt
├── pytest.ini
├── tests/
│   └── test_main.py
├── JOURNAL.md
└── REPORT.md
```

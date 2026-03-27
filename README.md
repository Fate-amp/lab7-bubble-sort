# Bubble Sort Lab

Small Python project to learn bubble sort with two visualizers:
- terminal renderer
- Pygame renderer

## Quick Start

1. Create a virtual environment:

```powershell
py -m venv .venv
```

2. Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

4. Run tests:

```powershell
python -m pytest
```

5. Run app:

```powershell
python main.py
```

## Run Modes

`main.py` runs sorting examples, then launches a visualizer.

- Pygame mode is enabled by default.
- Terminal mode is available by uncommenting its line and commenting the Pygame line.

In `main.py` inside `main()`:

```python
# Terminal mode
# visualize_bubble_sort_terminal(visual_input, delay=0.15)

# Pygame mode
visualize_bubble_sort_pygame(visual_input, fps=20)
```

## File Layout

```text
lab7-bubble-sort/
├── main.py            # app entrypoint / mode selection
├── sorting_logic.py   # bubble sort logic + step generator
├── terminal_ui.py     # terminal rendering only
├── pygame_ui.py       # pygame rendering only
├── tests/
│   └── test_main.py
├── requirements.txt
├── pytest.ini
├── JOURNAL.md
└── REPORT.md
```

## Notes

- `pygame-ce` is used for Python 3.14 compatibility.
- Code imports `pygame` (compatible with `pygame-ce`).

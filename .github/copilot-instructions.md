# Copilot Instructions for RunTime

## Project Overview
- **Purpose:** Analyze and visualize code frequency data (additions/deletions over time) using Python.
- **Key Data:** Main input is `Code frequency.csv` (date, additions, deletions).
- **Outputs:** Visualizations (PNG) in `output/visualizations/`.

## Architecture
- **src/**: Main Python source code (modules for loading, analyzing, visualizing data)
  - `code_frequency_loader.py`: Loads/parses CSV data
  - `code_frequency_analyzer.py`: Performs analysis on loaded data
  - `code_frequency_visualizer.py`: Generates plots/visualizations
  - `cli.py`: (if present) Entry point for command-line usage
- **output/visualizations/**: Generated PNGs (activity heatmap, timeline, etc.)
- **tests/**: (if present) Test suite, e.g., `test_load.py`

## Developer Workflows
- **Install dependencies:**
  - `pip install -r requirements.txt` (requirements file may need to be created/updated)
  - Core dependencies: pandas, numpy, matplotlib, seaborn
- **Run analysis/visualization:**
  - Typical workflow: load CSV → analyze → visualize
  - Example (Python):
    ```python
    from src.code_frequency_loader import load_data
    from src.code_frequency_analyzer import analyze
    from src.code_frequency_visualizer import plot_timeline
    df = load_data('Code frequency.csv')
    summary = analyze(df)
    plot_timeline(df, output_path='output/visualizations/timeline.png')
    ```
- **Testing:**
  - If `tests/` exists, run with `pytest`
- **VS Code Launch:**
  - `.vscode/launch.json` contains .NET and C++ configs, but Python is primary for this repo

## Conventions & Patterns
- **Data:** Always expect `Code frequency.csv` in root
- **Outputs:** All generated images go in `output/visualizations/`
- **Python version:** 3.9+
- **No monolithic scripts:** Use modular imports from `src/`
- **No hardcoded paths:** Use relative paths for input/output

## Integration & Extensibility
- **Add new visualizations:** Implement in `code_frequency_visualizer.py`, save to `output/visualizations/`
- **Add new analyses:** Extend `code_frequency_analyzer.py`
- **CLI:** If `cli.py` exists, expose main workflows via CLI commands

## References
- Example data: `Code frequency.csv`
- Example outputs: `output/visualizations/*.png`
- Key modules: `src/code_frequency_loader.py`, `src/code_frequency_analyzer.py`, `src/code_frequency_visualizer.py`

---
For questions about missing files or unclear workflows, check for uncommitted or ignored files, or ask the project maintainer.

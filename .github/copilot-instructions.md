---discription': ---

# AI Coding Agent Instructions for RunTime

## Project Overview
RunTime is a production-ready Python toolkit for analyzing and visualizing code frequency data from Git repositories. It is organized for modularity, reproducibility, and extensibility.

## Architecture & Data Flow
- **src/**: Core package with four modules:
  - `code_frequency_loader.py`: Loads and summarizes the root `Code frequency.csv` (2017–2025)
  - `code_frequency_analyzer.py`: Advanced analytics (sprints, churn, trends)
  - `code_frequency_visualizer.py`: All plotting (timeline, heatmap, yearly, dashboard)
  - `cli.py`: Unified CLI for all operations (load, analyze, visualize)
- **Data-driven**: All analysis is based on the root CSV. No external APIs/services.
- **Output**: Visualizations are saved to `output/visualizations/`.
- **Interfaces**: CLI, Python API, and Jupyter notebook (`notebooks/exploration.ipynb`).

## Critical Developer Workflows
- **Testing**: Run `pytest` (see `tests/`). Coverage: `pytest --cov=src`.
- **Analysis**: `python src/cli.py analyze --all` (full), `--top N`, `--sprints`.
- **Visualization**: `python src/cli.py visualize --all`, `--timeline`, `--heatmap`.
- **Interactive**: Use `notebooks/exploration.ipynb` for stepwise, cell-based analysis.
- **Examples**: `python examples/advanced_examples.py` for advanced patterns.
- **Dependencies**: Install with `pip install -r requirements.txt`.

## Project-Specific Conventions
- Always import via `from src import ...` (see `__init__.py`).
- Use pandas for all data manipulation; matplotlib/seaborn for plotting.
- CLI and API share logic—prefer CLI for batch, API for custom/interactive.
- Notebooks mirror CLI/API usage patterns.
- Do not change core module APIs without considering backward compatibility.
- Do not remove or bypass test coverage.
- Add new analysis/visualization features as new methods/classes in `src/`.
- Document new CLI commands in `README.md` and `QUICKSTART.md`.
- Preserve `LICENSE.md` in all derived or published artifacts.

## Integration & Extensibility
- Core dependencies: pandas, numpy, matplotlib, seaborn, pytest.
- No external APIs/services; all analysis is local and reproducible.
- Easy to add new analyzers, visualizations, or CLI commands (see `examples/advanced_examples.py`).

## Reference Patterns & Key Files
- `README.md`, `QUICKSTART.md`, `PROJECT_STATUS.md`: Documentation, usage, and status.
- `examples/advanced_examples.py`: Advanced usage and custom workflows.
- `notebooks/exploration.ipynb`: Interactive, cell-based exploration.
- `tests/test_load.py`: Loader and summary logic tests (7 tests).

## Example: Import Pattern
```python
from src import CodeFrequencyLoader, CodeFrequencyAnalyzer, CodeFrequencyVisualizer
```

## When Adding Features
- Use existing module structure in `src/`.
- Add new CLI commands in `cli.py` and document them.
- Save new visualizations to `output/visualizations/`.
- Add tests in `tests/`.

## If You Need More Context
- See `README.md` for full documentation.
- See `QUICKSTART.md` for usage examples.
- See `PROJECT_STATUS.md` for implementation details.
- Explore `notebooks/exploration.ipynb` for interactive examples.

---
**Status:** All core features implemented, tested, and documented. See `README.md` for details.

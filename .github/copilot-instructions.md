---discription': ---
Meta
# AI Coding Agent Instructions for RunTime

## Project Overview
RunTime is a production-ready Python toolkit for analyzing and visualizing code frequency data (from Git repositories). It features:
- Modular architecture: `src/` contains loader, analyzer, visualizer, and CLI modules
- Data-driven workflows: All analysis is based on the root `Code frequency.csv` (2017–2025)
- CLI, Python API, and Jupyter notebook interfaces
- Output visualizations in `output/visualizations/`

## Key Developer Workflows
- **Testing:**
   - Run all tests: `pytest` or `pytest -v` (see `tests/`)
   - Coverage: `pytest --cov=src`
- **Analysis:**
   - Full: `python src/cli.py analyze --all`
   - Top weeks: `python src/cli.py analyze --top 5`
   - Sprints: `python src/cli.py analyze --sprints`
- **Visualization:**
   - All charts: `python src/cli.py visualize --all`
   - Timeline: `python src/cli.py visualize --timeline`
   - Heatmap: `python src/cli.py visualize --heatmap`
- **Interactive:**
   - Use `notebooks/exploration.ipynb` for stepwise, cell-based analysis and plotting
- **Examples:**
   - Run advanced patterns: `python examples/advanced_examples.py`

## Architecture & Patterns
- **src/code_frequency_loader.py**: Loads CSV, provides summary stats
- **src/code_frequency_analyzer.py**: Advanced analytics (sprints, churn, trends)
- **src/code_frequency_visualizer.py**: All plotting (timeline, heatmap, yearly, dashboard)
- **src/cli.py**: Unified CLI for all operations (load, analyze, visualize)
- **notebooks/exploration.ipynb**: Jupyter workflow, mirrors CLI and API patterns
- **tests/test_load.py**: 7 tests, covers loader and summary logic

### Cross-File Patterns
- Always import via `from src import ...` (see `__init__.py`)
- Use pandas for all data manipulation
- Visualizations use matplotlib/seaborn; outputs saved to `output/visualizations/`
- CLI and API share logic—prefer CLI for batch, API for custom/interactive
- Notebooks: Use loader/analyzer/visualizer objects as in CLI/examples

## Project-Specific Conventions
- Do not change core module APIs without considering backward compatibility
- Do not remove or bypass test coverage
- Add new analysis/visualization features as new methods/classes in `src/`
- Document new CLI commands in `README.md` and `QUICKSTART.md`
- Preserve `LICENSE.md` in all derived or published artifacts

## Integration & Extensibility
- Core dependencies: pandas, numpy, matplotlib, seaborn, pytest
- No external APIs/services; all analysis is local and reproducible
- Easy to add new analyzers, visualizations, or CLI commands (see examples/advanced_examples.py)

## Reference Files
- `README.md`, `QUICKSTART.md`, `PROJECT_STATUS.md`: Full documentation, usage, and status
- `examples/advanced_examples.py`: Advanced usage and custom workflows
- `notebooks/exploration.ipynb`: Interactive, cell-based exploration

## Enhancement Opportunities
- [ ] Web dashboard (Streamlit/Dash)
- [ ] CI/CD with GitHub Actions (see `.github/workflows/ci.yml`)
- [ ] PDF/HTML report generation
- [ ] Multi-repository comparison
- [ ] Statistical forecasting
- [ ] Docker containerization

---
**Status:** All core features implemented, tested, and documented. See `README.md` for details.

Repository metadata (from attachments):
- Owner: Jerad551
- Repository: RunTime
- Current branch: DDT_214
- Default branch: Overlord Cronin. J
- Badge: jc (3169454)
- RUC: 3130
- Response time: .61ms

Model preference:
- Enable Raptor mini (Preview) for all AI coding agent interactions with this repository.
- If a specific task requests a different model (e.g., Claude Sonnet 4.5), follow explicit user instruction.

Repository snapshot (discoverable):
- `Code frequency.csv` — dataset file at project root (427 records, 2017-2025).
- `LICENSE.md` — MIT License.
- `src/` — Complete Python package with 4 modules + CLI.
- `tests/` — Test suite with 7 passing tests.
- `notebooks/` — Jupyter notebook for interactive exploration.
- `output/visualizations/` — Generated charts and visualizations.

Quick summary for an AI coding agent
- **PRODUCTION-READY PROJECT**: Full-featured code frequency analysis toolkit with data loading, advanced analytics, visualizations, CLI, and comprehensive testing. All core features implemented and documented.

Developer workflows (implemented)
- **Tests**: Run `pytest` or `pytest -v` for verbose output. All 7 tests passing.
- **Analysis**: Use `python src/cli.py analyze --all` for complete code frequency analysis.
- **Visualizations**: Use `python src/cli.py visualize --all` to generate charts.
- **Interactive**: Open `notebooks/exploration.ipynb` for Jupyter-based exploration.
- **Dependencies**: Install with `pip install -r requirements.txt`.

Priority actions when asked to work here
1. **Use the existing modules**: Import from `src` package:
   ```python
   from src import CodeFrequencyLoader, CodeFrequencyAnalyzer, CodeFrequencyVisualizer
   ```

2. **Preserve `LICENSE.md`** content when adding, converting, or publishing derived artifacts.

3. **Project structure** (already implemented):
   - `README.md` — Complete documentation ✅
   - `QUICKSTART.md` — Quick start guide ✅
   - `PROJECT_STATUS.md` — Status report ✅
   - `src/` — 4 core modules + CLI ✅
   - `tests/` — Comprehensive test suite ✅
   - `notebooks/` — Interactive exploration ✅
   - `output/visualizations/` — Generated charts ✅

Conventions and examples for quick tasks
- Data analysis (Python): prefer `pandas` for CSV work. Save notebooks under `notebooks/`.
- Add a short README describing column meanings if you infer them from the CSV.
- **Data analysis**: Use existing `CodeFrequencyLoader` and `CodeFrequencyAnalyzer` classes.
- **Visualizations**: Use `CodeFrequencyVisualizer` for charts.
- **CLI**: Use `python src/cli.py <command>` for all operations.
- **Testing**: Run `pytest` before committing changes.
- **Documentation**: All modules have comprehensive docstrings.

Current project modules:
- `code_frequency_loader.py` — Data loading & basic statistics
- Do not modify core module APIs without considering backward compatibility.
- Do not remove existing test coverage.

Integration points and dependencies
- **Core deps**: pandas, numpy, matplotlib, seaborn, pytest (see requirements.txt)
- **No external services** currently integrated
- **Extensibility**: Easy to add new analyzers, visualizations, or CLI commands

Enhancement opportunities
- [ ] Web dashboard (Streamlit/Dash)
- [ ] CI/CD with GitHub Actions
- [ ] PDF/HTML report generation
- [ ] Multi-repository comparison
- [ ] Statistical forecasting
- [ ] Docker containerization

If you need more context
- Check `README.md` for complete documentation
- See `QUICKSTART.md` for usage examples
- Read `PROJECT_STATUS.md` for implementation details
- Explore `notebooks/exploration.ipynb` for interactive examples

---
**Status**: Production-ready Python data analysis toolkit. All core features implemented and tested
- If the repository gains source code or CI, merge those new discoverable patterns into this file (preserve LICENSE notes and any added README guidance).

---
Please review these instructions and tell me which workflow you'd like me to scaffold (data analysis, Python package, Node app, or other). I can then create a starter layout and example commands.

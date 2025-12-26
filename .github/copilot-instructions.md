# Copilot instructions for this repository

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

# Copilot instructions for this repository

Repository metadata (from attachments):
- Owner: Jerad551
- Repository: RunTime
- Current branch: main
- Default branch: Overlord Cronin. J

Repository snapshot (discoverable):
- `Code frequency.csv` — dataset file at project root.
- `LICENSE.md` — repository license.

Quick summary for an AI coding agent
- This repo currently contains only a CSV dataset and a license. There is no source code, build system, tests, or CI configuration to inspect. Before making structural changes, confirm the user's intent.

Priority actions when asked to work here
1. Open and inspect `Code frequency.csv` to understand schema and sample rows. Example (Python):

```py
import pandas as pd
df = pd.read_csv('Code frequency.csv')
print(df.head())
```

2. Preserve `LICENSE.md` content when adding, converting, or publishing derived artifacts.

3. If asked to add code, create a minimal project layout and document it in a new `README.md` at the repo root. Suggested starter layout:

- `README.md` — project purpose and quick run steps
- `data/` — raw dataset copies (if needed)
- `src/` — source code (language-specific subfolders)
- `notebooks/` — exploratory analysis/notebooks
- `tests/` — unit/integration tests

Conventions and examples for quick tasks
- Data analysis (Python): prefer `pandas` for CSV work. Save notebooks under `notebooks/`.
- Add a short README describing column meanings if you infer them from the CSV.
- Suggested commit message pattern for dataset changes: `data: add|update Code frequency.csv — <short reason>`

When adding a new language project
- Include a top-level manifest so workflows are discoverable: `requirements.txt` or `pyproject.toml` for Python, `package.json` for Node, etc.
- Add run/test commands to `README.md` and surface CI config only after the user approves the baseline layout.

What NOT to do autonomously
- Do not delete or relicense `LICENSE.md`.
- Do not fabricate a build/test workflow for the user without confirming which language/runtime they want.

Integration points and external deps
- None discovered in the repository. Ask the user which external services, data sources, or registries (PyPI, npm, Docker Hub) should be used before adding integrations.

If you need more context
- Ask the user for the intended purpose (analysis, library, web service, dataset publication). Provide a proposed minimal scaffold and wait for approval before committing.

Update notes
- If the repository gains source code or CI, merge those new discoverable patterns into this file (preserve LICENSE notes and any added README guidance).

---
Please review these instructions and tell me which workflow you'd like me to scaffold (data analysis, Python package, Node app, or other). I can then create a starter layout and example commands.

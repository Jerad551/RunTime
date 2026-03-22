---
description: Copilot instructions for the RunTime repository
---

# Copilot Instructions for RunTime

## Repository overview
- This repository currently centers on the `Code frequency.csv` dataset at the repository root.
- `.devcontainer/devcontainer.json` defines the Codespaces/dev container image.
- `Jrad.oss.prompt.yml` stores the existing prompt configuration used in this repo.

## Working conventions
- Keep changes minimal and focused on the issue being addressed.
- Prefer updating existing files over adding generated artifacts or editor caches.
- Use root-relative repository paths when documenting files in this repo.
- Do not assume a build, lint, or test command exists unless you verify it in the repository first.

## Review guidance
- Flag malformed JSON or YAML configuration before suggesting behavior changes.
- Treat documentation-only and repository-configuration updates as valid fixes when the issue is about setup, Codespaces, or Copilot behavior.

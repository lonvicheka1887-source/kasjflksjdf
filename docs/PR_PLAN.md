# Initial PR Plan (Python)

## PR #1 — Bootstrap repository foundation

**Goal**
- Set up base project structure and first passing tests.

**Scope**
- Add `src/` layout.
- Add a minimal executable module (`app.main`).
- Add baseline tests using `unittest`.
- Add `README`, `pyproject.toml`, `.gitignore`, and `Makefile`.

**Definition of Done**
- `make test` passes locally.
- New contributor can clone and run tests in one command.

---

## PR #2 — Developer experience

**Goal**
- Improve code quality workflow.

**Scope**
- Add formatting + lint tooling (`ruff`, `black` or one-tool strategy via `ruff format`).
- Add pre-commit hooks.
- Document local setup commands.

**Definition of Done**
- Lint/format commands are documented and reproducible.

---

## PR #3 — CI automation

**Goal**
- Enforce quality in CI.

**Scope**
- Add CI workflow (GitHub Actions).
- Run tests + lint on every push/PR.
- Add badge in README.

**Definition of Done**
- CI runs automatically and blocks failing checks.

---

## PR #4 — Domain foundation

**Goal**
- Begin actual product/domain logic.

**Scope**
- Create first real module (e.g., `services/` or `core/`).
- Add tests around that module.
- Keep architecture notes short in `docs/`.

**Definition of Done**
- At least one domain feature with test coverage is shipped.

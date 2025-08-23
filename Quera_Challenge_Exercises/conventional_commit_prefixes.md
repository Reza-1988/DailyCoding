# Conventional Commit Prefixes

A list of common commit prefixes used to keep git history clean and consistent.

---

## Main Types

- **feat:**  
  A new feature for the codebase.  
  Example: `feat: add user login functionality`

- **fix:**  
  A bug fix.  
  Example: `fix: correct null pointer in GameManager`

- **docs:**  
  Documentation changes only (comments, README, etc.).  
  Example: `docs: add comments to __init__ of GameManager`

- **style:**  
  Code style changes (formatting, whitespace, semicolons, etc.) — no code logic changes.  
  Example: `style: reformat snake.py with Black`

- **refactor:**  
  Code changes that neither fix a bug nor add a feature, but improve structure.  
  Example: `refactor: simplify next_move logic in Snake class`

- **test:**  
  Adding or modifying tests.  
  Example: `test: add unit tests for wraparound logic`

- **chore:**  
  Routine tasks, maintenance, or dependency updates (no production code changes).  
  Example: `chore: update pygame dependency`

---

## Optional Extra Types

- **perf:**  
  Performance improvements.  
  Example: `perf: optimize rendering loop in GameManager`

- **build:**  
  Changes to build system, CI/CD, packaging.  
  Example: `build: add GitHub Actions workflow for tests`

- **ci:**  
  Continuous integration related changes.  
  Example: `ci: fix failing pipeline on main branch`

- **revert:**  
  Revert a previous commit.  
  Example: `revert: undo commit 1a2b3c4 due to regression`

---

## Tips

1. Always use **present tense, imperative mood** (e.g., `add` not `added` or `adds`).  
2. Keep messages concise but clear.  
3. Optionally add a longer description after a blank line.  

---

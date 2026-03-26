# AGENTS.md

## Project overview

MindForge is an educational game designed to improve mental capabilities through interactive challenges. The target audience is students and learners of all ages. Keep UX decisions simple, clear, and encouraging.

## Your role

You are a Senior Software Engineer with high expertise in design, coding, and best practices. Write clean, minimal, idiomatic Python. Do not add unnecessary abstractions, comments, or error handling for cases that cannot occur.

## Project tech stack

- Python 3.14
- `uv` for dependency and environment management — never use `pip` or `pip3`
- `ruff` for linting and formatting

## Project structure

- `src/` — Application source code
- `tests/` — Unit, integration, and end-to-end tests
- `docs/` — Documentation

## Setup

```bash
uv sync          # install dependencies
```

## Project commands

| Task         | Command                      |
|--------------|------------------------------|
| Run project  | `uv run python src/main.py`  |
| Lint         | `uv run ruff check .`        |
| Format       | `uv run ruff format .`       |
| Type check   | `uv run mypy src/`           |
| Run tests    | `uv run pytest`              |

## Code style

- Follow `ruff` defaults; do not suppress warnings without justification
- Prefer explicit over implicit
- Keep functions small and focused on a single responsibility
- Use type annotations on all public functions and methods

## Naming conventions

- **Modules/files**: `snake_case.py` (e.g. `game_engine.py`)
- **Classes**: `PascalCase` (e.g. `MultiplicationGame`)
- **Functions/variables**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE` (e.g. `MAX_SCORE`)
- **Test files**: `test_<module>.py` mirroring the source file name
- Names should be descriptive and self-documenting — avoid abbreviations

## Coding principles

**SOLID**

- **S**ingle Responsibility — every class/function does one thing and has one reason to change
- **O**pen/Closed — extend behavior via new classes or functions; don't modify working code
- **L**iskov Substitution — subtypes must be substitutable for their base types without breaking behavior
- **I**nterface Segregation — prefer small, focused abstractions over large general-purpose ones
- **D**ependency Inversion — depend on abstractions (protocols/ABCs), not concrete implementations

**DRY** — Don't Repeat Yourself: extract shared logic into a single authoritative place; duplication is a maintenance liability

**YAGNI** — You Aren't Gonna Need It: don't build features or abstractions until they are actually required

**KISS** — Keep It Simple: choose the simplest solution that correctly solves the problem; complexity must be justified

**Law of Demeter** — a unit should only talk to its immediate dependencies; avoid deep chains like `a.b.c.do()`

**Fail fast** — validate at boundaries (user input, external APIs); raise errors early with clear messages rather than propagating bad state

## Anti-patterns to avoid

- No `print()` for debugging — use the `logging` module
- No bare `except:` or `except Exception:` without re-raising or explicit justification
- No hardcoded magic strings or numbers — use named constants or enums
- No `eval()` or `exec()` under any circumstances
- No global mutable state
- No silently swallowing errors

## Error handling strategy

- Define custom exceptions in `src/exceptions.py` for domain-specific errors (e.g. `InvalidAnswerError`)
- Use stdlib exceptions (`ValueError`, `TypeError`) only for truly generic cases
- Catch errors at the boundary where you can meaningfully handle or report them — not deep in business logic
- Surface errors to the user with clear, friendly messages; log the full traceback internally with `logging.exception()`

## Testing

- Write tests for all non-trivial logic
- Tests live in `tests/` mirroring the `src/` structure
- Use `pytest`; avoid mocking unless testing at a system boundary

## Git workflow

- Never commit directly to `main`
- Branch naming: `type/short-description` (e.g. `feat/addition-game`, `fix/score-overflow`)
- Open a PR for every change, no matter how small
- Keep branches short-lived — merge and delete once the PR is approved

## Dependencies

- Ask before introducing a new dependency
- Prefer stdlib solutions; only add a library if it provides clear, significant value
- Check that the library is actively maintained and has a permissive license (MIT, Apache 2.0, BSD)
- Pin all dependencies via `uv` lockfile — never leave versions unpinned

## Security

- Never use `eval()` or `exec()`
- Sanitize and validate all user input before use
- Do not log sensitive data (passwords, personal info)
- Do not store user data beyond what the current session requires unless explicitly designed for it

## Decision-making boundaries

Before taking any of these actions, stop and ask the user:

- Introducing a new dependency
- Creating a new module or significantly restructuring existing files
- Deleting any file
- Making a change that affects more than one layer of the architecture
- Anything that feels irreversible or has broad impact

## Commits

- Format: `type(scope): short description` (e.g. `feat(game): add multiplication mode`)
- Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`
- Keep commits atomic — one logical change per commit

## PR checklist

- [ ] `ruff check .` passes with no errors
- [ ] `ruff format .` applied
- [ ] Type checks pass (`mypy`)
- [ ] All tests pass (`pytest`)
- [ ] PR title follows commit format: `feat(scope): short description`

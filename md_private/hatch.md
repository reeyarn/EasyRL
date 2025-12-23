Consider using hatch version or bumpversion to automate version bumps.

Great question! Automating version bumps saves time and reduces errors when releasing new versions of your package. Here are the two most popular and modern ways to do it with your current Hatchling-based setup: **Hatch** (recommended) and `bumpversion` (classic alternative).

### Option 1: Use Hatch (Recommended – Native to Your Build System)

Since you're already using **Hatchling** as the build backend, **Hatch** (the CLI tool) is the perfect companion. It’s built by the same team and integrates seamlessly.

#### Step 1: Install Hatch CLI
```bash
pip install hatch
# or if using uv (faster)
uv tool install hatch
```

#### Step 2: Initialize Hatch (optional but useful)
Run this in your project root:
```bash
hatch init
```
- This creates a `pyproject.toml` with Hatch-specific settings (you can merge it with your existing one).
- It also sets up a `version` field in `pyproject.toml` that Hatch can manage.

Your current `pyproject.toml` already has `version = "0.1.0"`, so you’re good to go.

#### Step 3: Bump the Version
Hatch can bump versions in these ways:

```bash
# Bump patch version (0.1.0 → 0.1.1)
hatch version patch

# Bump minor version (0.1.0 → 0.2.0)
hatch version minor

# Bump major version (0.1.0 → 1.0.0)
hatch version major

# Set a specific version
hatch version 0.2.1

# Show current version
hatch version
```

#### Step 4: Release Workflow (Typical)
```bash
# 1. Update changelog or docs if needed
# 2. Bump version
hatch version patch

# 3. Build the package
hatch build

# 4. Publish to PyPI
hatch publish
# or use twine
python -m build
twine upload dist/*
```

Hatch also supports:
- Version schemes (e.g., `0.1.0.dev1`, `0.1.0a1`)
- Multiple sources (e.g., `__version__` in a file, `pyproject.toml`)
- Pre-commit hooks

### Option 2: Use `bumpversion` (Classic Tool)

If you prefer something simpler and widely used, `bumpversion` is still excellent.

#### Step 1: Install
```bash
pip install bump2version  # modern fork, better than original bumpversion
# or uv tool install bump2version
```

#### Step 2: Create a `.bumpversion.cfg` file
In your project root, create `.bumpversion.cfg`:

```ini
[bumpversion]
current_version = 0.1.0
commit = True
tag = True

[bumpversion:file:pyproject.toml]
search = version = "{current_version}"
replace = version = "{new_version}"
```

This tells `bumpversion` to update the `version` field in `pyproject.toml`.

#### Step 3: Bump the Version
```bash
# Patch
bump2version patch

# Minor
bump2version minor

# Major
bump2version major
```

It will:
- Update `pyproject.toml`
- Commit the change (if `commit = True`)
- Create a git tag (if `tag = True`)

#### Step 4: Release
```bash
git push && git push --tags
python -m build
twine upload dist/*
```

### Comparison: Hatch vs. bump2version

| Feature                        | Hatch (Recommended)               | bump2version                     |
|--------------------------------|-----------------------------------|----------------------------------|
| Built-in with your build tool  | Yes (Hatchling)                   | No                               |
| CLI commands                   | `hatch version patch/minor/major` | `bump2version patch/minor/major` |
| Config file                    | `pyproject.toml`                  | `.bumpversion.cfg`               |
| Supports dev/pre-release       | Yes (e.g., `hatch version 0.2.0a1`) | Yes (with `--new-version`)       |
| Git commit & tag               | Manual                            | Automatic (configurable)         |
| Speed & modern feel            | Excellent                         | Good                             |
| Ecosystem                      | Growing fast                      | Very mature                      |

### Recommendation for EasyRL

**Use Hatch** — since you’re already on Hatchling, it keeps your tooling consistent and modern. It’s also faster and has better integration with `pyproject.toml`.

#### Quick Setup for Hatch

1. Install: `pip install hatch`
2. Add to your `dev` dependencies in `pyproject.toml`:
   ```toml
   [project.optional-dependencies]
   dev = [
       "pytest>=7.0",
       "pytest-cov",
       "ruff",
       "mypy",
       "hatch",  # ← add this
   ]
   ```
3. Use it: `hatch version patch`

That’s it! You now have automated version bumping integrated into your workflow.

Let me know if you want a sample GitHub Actions workflow that uses Hatch to build and publish releases automatically!
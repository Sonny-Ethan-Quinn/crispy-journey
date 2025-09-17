# Crispy Journey

Crispy Journey is a Python package that provides a minimal command-line interface. It is packaged and distributed as a Python wheel and source distribution via GitHub releases with automated CI/CD.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Essential Setup Commands

Bootstrap and prepare the development environment:
- **PREREQUISITE**: Python 3.12+ is available at `/usr/bin/python3`
- **PREREQUISITE**: pip is available and functional
- Install build dependencies: `python3 -m pip install --upgrade pip`
- Install essential build tools: `pip install build wheel twine hatchling` (takes ~6 seconds)
- Install development tools: `pip install pytest flake8 black` (takes ~3 seconds)

### Build Commands

Build the package:
- **PRIMARY BUILD**: `python -m build --no-isolation` (takes ~0.5 seconds, NEVER CANCEL)
- **CRITICAL**: Always use `--no-isolation` flag to avoid network timeout issues with PyPI
- **NETWORK LIMITATION**: Standard build with isolation (`python -m build`) fails due to network timeouts when downloading build dependencies from PyPI. Always use `--no-isolation`.
- Build artifacts are created in `dist/` directory: `crispy_journey-0.1.0.tar.gz` and `crispy_journey-0.1.0-py3-none-any.whl`

### Testing Commands

Run the test suite:
- **PRIMARY TEST**: `PYTHONPATH=src pytest -v` (takes ~0.2 seconds, NEVER CANCEL)
- **FAST TEST**: `PYTHONPATH=src pytest` (basic output, takes ~0.2 seconds)
- **CRITICAL**: Always use `PYTHONPATH=src` to ensure tests can import the package
- Test discovery: pytest automatically finds tests in `tests/` directory
- **MANUAL VALIDATION**: After any changes, always run `PYTHONPATH=src python -c "from crispy_journey.main import main; main()"` to verify basic functionality

### Code Quality Commands

Maintain code quality:
- **LINT CHECK**: `flake8 src/` (takes ~0.2 seconds, should return no output if clean)
- **FORMAT CHECK**: `black --check src/` (takes ~0.2 seconds)
- **AUTO FORMAT**: `black src/` (takes ~0.2 seconds, automatically fixes formatting)
- **CRITICAL**: Always run `flake8 src/` before committing or the CI (.github/workflows/release.yml) may fail

### Installation and Runtime

Install and run the package:
- **INSTALL FROM WHEEL**: `pip install dist/crispy_journey-0.1.0-py3-none-any.whl`
- **CLI EXECUTION**: `/home/runner/.local/bin/crispy-journey` (direct path, always works)
- **CLI WITH PATH**: Add `export PATH=$HOME/.local/bin:$PATH` to use `crispy-journey` command directly
- **DEVELOPMENT MODE**: Use `PYTHONPATH=src python -c "from crispy_journey.main import main; main()"` for development testing without installation
- **EXPECTED OUTPUT**: CLI should print "Welcome to Crispy Journey!" and "This is a minimal Python package."

## Validation

### Manual Validation Scenarios

Always run these scenarios after making changes:

**Scenario 1: Full Build and Test Cycle**
1. Clean build: `rm -rf dist/ && python -m build --no-isolation`
2. Run tests: `PYTHONPATH=src pytest -v`
3. Lint check: `flake8 src/`
4. Install package: `pip install dist/crispy_journey-0.1.0-py3-none-any.whl --force-reinstall`
5. Test CLI: `/home/runner/.local/bin/crispy-journey`
6. Verify output contains "Welcome to Crispy Journey!"

**Scenario 2: Development Mode Testing**
1. Format code: `black src/`
2. Lint check: `flake8 src/`
3. Run tests: `PYTHONPATH=src pytest`
4. Manual function test: `PYTHONPATH=src python -c "from crispy_journey.main import main; main()"`
5. Verify output and return code

**Scenario 3: Package Import Testing**
1. Test import: `python -c "import crispy_journey; print(crispy_journey.__version__)"`
2. Should output: `0.1.0`
3. Test main function: `python -c "from crispy_journey.main import main; result = main(); print(f'Return code: {result}')"`
4. Should output the welcome message and "Return code: 0"

### Critical Timing Information

- **NEVER CANCEL**: All commands listed complete in under 10 seconds
- Build process: ~0.5 seconds (extremely fast due to minimal package)
- Test suite: ~0.2 seconds (only 2 basic tests)
- Linting: ~0.2 seconds (small codebase)
- Dependency installation: 3-6 seconds depending on what's already installed
- **TIMEOUT SETTINGS**: Use minimum 30 seconds timeout for any build command, 60 seconds for pip installations

### Known Limitations and Workarounds

- **CRITICAL LIMITATION**: Network connectivity to PyPI is unreliable. pip install commands may timeout.
- **WORKAROUND**: Always use `--no-isolation` flag with build commands
- **WORKAROUND**: Pre-install build dependencies (`hatchling`, `build`, `wheel`) before building
- Development installs (`pip install -e .`) may fail due to network issues. Use `PYTHONPATH=src` method instead.
- **CI CONSIDERATION**: The GitHub Actions workflow (.github/workflows/release.yml) handles network issues by creating package structure if needed

## Repository Structure

### Key Directories and Files
```
.
├── .github/
│   ├── workflows/
│   │   └── release.yml          # Automated release workflow
│   └── copilot-instructions.md  # This file
├── src/
│   └── crispy_journey/
│       ├── __init__.py          # Package initialization, version info
│       └── main.py              # Main CLI entry point
├── tests/
│   ├── __init__.py              # Test package marker
│   └── test_main.py             # Main test suite
├── pyproject.toml               # Modern Python project configuration
├── .gitignore                   # Standard Python gitignore
└── README.md                    # Basic project description
```

### Important Files to Monitor
- **Always check `src/crispy_journey/main.py`** after making functionality changes
- **Always check `tests/test_main.py`** after adding new features to ensure tests cover the changes
- **Always check `pyproject.toml`** if modifying dependencies or project metadata
- **Monitor `.github/workflows/release.yml`** for CI/CD changes

## Common Commands Reference

### Quick Development Cycle
```bash
# Format and lint
black src/
flake8 src/

# Test
PYTHONPATH=src pytest -v

# Build and validate
rm -rf dist/
python -m build --no-isolation
pip install dist/crispy_journey-0.1.0-py3-none-any.whl --force-reinstall
/home/runner/.local/bin/crispy-journey
```

### Project Information Queries
```bash
# Check Python version
python3 --version  # Expected: Python 3.12.3

# Check package version
python -c "import crispy_journey; print(crispy_journey.__version__)"  # Expected: 0.1.0

# List installed development tools
pip list | grep -E "(pytest|flake8|black|build|hatchling)"
```

### File Outputs for Reference

#### pyproject.toml content:
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "crispy-journey"
version = "0.1.0"
description = "A fully automated journey"
readme = "README.md"
requires-python = ">=3.9"
authors = [
    { name = "Sonny Ethan Quinn" }
]

[project.scripts]
crispy-journey = "crispy_journey.main:main"
```

#### Expected test output:
```
$ PYTHONPATH=src pytest -v
================================================= test session starts ==================================================
platform linux -- Python 3.12.3, pytest-8.4.2, pluggy-1.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/runner/work/crispy-journey/crispy-journey
configfile: pyproject.toml
collecting ... collected 2 items                                                                                                      

tests/test_main.py::test_main_function PASSED                                                                    [ 50%]
tests/test_main.py::test_import PASSED                                                                           [100%]

================================================== 2 passed in 0.01s =================================================
```
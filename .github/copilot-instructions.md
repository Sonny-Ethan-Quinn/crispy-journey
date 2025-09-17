# Crispy Journey - GitHub Copilot Instructions

Crispy Journey is a minimal Python package project with setuptools-based build system and automated GitHub releases. The repository uses Python 3.9+ and follows standard Python packaging conventions.

**ALWAYS follow these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information provided here.**

## Working Effectively

### Quick Start for Development
```bash
# Quick development setup (if dependencies already installed)
python3 -m pip install -e .
python3 -m pytest tests/ -v
black src/ && flake8 src/
```

### Bootstrap and Environment Setup
- **Python Environment**: Python 3.12.3 is available, pip 24.0+ is available
- **NETWORK LIMITATIONS**: PyPI connection timeouts in this environment affect pip installs
- **Install/upgrade pip**: `python3 -m pip install --upgrade pip` -- takes 4 seconds (may timeout due to network)
- **Install build dependencies**: `python3 -m pip install build wheel` -- takes 2 seconds (may timeout due to network)  
- **Install development tools**: `python3 -m pip install pytest black flake8` -- takes 4 seconds (may timeout due to network)
- **If pip installs timeout**: Dependencies are likely already available system-wide; proceed to build

### Building the Package
- **CRITICAL LIMITATION**: Standard isolated builds (`python3 -m build`) FAIL due to PyPI connection timeouts in this environment
- **WORKING BUILD COMMAND**: `python3 -m build --no-isolation` -- takes 1 second. NEVER CANCEL.
- **Package structure**: Create basic structure with `mkdir -p src/crispy_journey && touch src/crispy_journey/__init__.py` -- takes 0 seconds
- **Setup file**: A working `setup.py` file exists in the repository root with basic package metadata

### Testing
- **CRITICAL**: Tests require package installation first. Run `python3 -m pip install -e .` for development.
- **Run tests**: `python3 -m pytest tests/ -v` -- takes 0.01 seconds (extremely fast)
- **Test coverage**: 3 basic tests exist covering hello(), main(), and version validation
- **NEVER CANCEL**: Although tests are very fast, always set timeout to 30+ minutes for test commands as they may grow

### Code Quality and Linting
- **Format code**: `black src/` -- takes 0 seconds (instant)
- **Lint code**: `flake8 src/` -- takes 0 seconds (instant)
- **Always run linting before committing**: Format with black first, then check with flake8

### Installation and Validation
- **Development installation**: `python3 -m pip install -e .` -- takes ~0.5 seconds (BEST for development)
- **Local wheel installation**: `python3 -m pip install dist/crispy_journey-0.1.0-py3-none-any.whl` -- takes 0 seconds
- **Test import**: `python3 -c "import crispy_journey; print('SUCCESS:', crispy_journey.hello())"` -- should print "SUCCESS: Hello from crispy-journey!"
- **Test main function**: `python3 -c "import crispy_journey; result = crispy_journey.main(); print('Result:', result)"` -- should return True

### Installation Options for Development
- **Editable installation** (`pip install -e .`): Changes to source code are immediately reflected without reinstall
- **Wheel installation** (`pip install dist/*.whl`): Requires rebuild and reinstall after each change
- **ALWAYS use editable installation for development workflow**

## Critical Build Timing and Limitations

- **NEVER CANCEL**: Build takes ~1 second with `--no-isolation`. Set timeout to 60+ minutes for safety.
- **NEVER CANCEL**: Test suite takes ~0.01 seconds. Set timeout to 30+ minutes for safety.
- **NETWORK LIMITATIONS**: PyPI connections timeout in isolated builds. Always use `--no-isolation` flag.
- **pip install timeouts**: Network-dependent installs may fail due to firewall/proxy limitations. Local wheel installation always works.
- **Actual measured timings**:
  - `pip install --upgrade pip`: ~3.3 seconds
  - `pip install build wheel`: ~1.1 seconds  
  - `pip install pytest black flake8`: ~3.9 seconds
  - `python3 -m build --no-isolation`: ~1 second
  - `python3 -m pytest tests/ -v`: ~0.01 seconds
  - `black src/`: ~0.18 seconds
  - `flake8 src/`: ~0.13 seconds
  - `pip install -e .`: ~0.5 seconds

## Validation Scenarios

**CRITICAL**: After making any changes, ALWAYS run through this complete validation scenario:

1. **Clean and rebuild**: 
   ```bash
   rm -rf dist/ build/ src/crispy_journey.egg-info/
   python3 -m build --no-isolation
   ```

2. **Install for development and test functionality**:
   ```bash
   python3 -m pip uninstall -y crispy-journey
   python3 -m pip install -e .
   python3 -c "import crispy_journey; print('SUCCESS:', crispy_journey.hello()); result = crispy_journey.main(); print('Main returned:', result)"
   ```

3. **Run full test suite**:
   ```bash
   python3 -m pytest tests/ -v
   ```

4. **Lint and format**:
   ```bash
   black src/
   flake8 src/
   ```

All these steps should complete successfully with the expected outputs shown above.

## Repository Structure

```
.
├── README.md                    # Basic project description
├── setup.py                     # Package configuration and metadata
├── .gitignore                   # Git ignore file for Python projects
├── .github/
│   └── workflows/
│       └── release.yml          # Automated release workflow for tagged versions
├── src/
│   └── crispy_journey/
│       └── __init__.py          # Main package module with hello() and main() functions
└── tests/
    └── test_crispy_journey.py   # Basic test suite (3 tests)
```

## Common Commands Reference

**Repository root listing**:
```
.github/    README.md    setup.py    src/    tests/
```

**Package functionality**:
- `crispy_journey.hello()` returns "Hello from crispy-journey!"
- `crispy_journey.main()` prints hello message and returns True
- `crispy_journey.__version__` is "0.1.0"

## GitHub Workflow Information

- **Release workflow**: `.github/workflows/release.yml` triggers on version tags (v*)
- **Python version**: Workflow uses Python 3.11
- **Build process**: Workflow creates basic package structure if setup.py/pyproject.toml missing
- **Release artifacts**: Builds both wheel and source distribution to `dist/`

## Development Workflow

1. **Install for development**: `python3 -m pip install -e .` (editable installation)
2. **Make changes** to source code in `src/crispy_journey/`
3. **Add tests** in `tests/` directory if needed
4. **Format and lint**: `black src/ && flake8 src/`
5. **Run tests**: `python3 -m pytest tests/ -v`
6. **Build package**: `python3 -m build --no-isolation` (for release)
7. **Commit changes** after all validation passes

**Remember**: NEVER CANCEL long-running commands. Although most commands in this project are very fast (0-4 seconds), always use appropriate timeouts (30-60+ minutes) as the project may grow in complexity.
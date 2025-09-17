# Crispy Journey 🚀

A **fully automated** Python project template with comprehensive CI/CD, code quality, and security automation.

[![CI/CD Pipeline](https://github.com/Sonny-Ethan-Quinn/crispy-journey/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/Sonny-Ethan-Quinn/crispy-journey/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## ✨ Features

This project demonstrates a **fully automated** development workflow with:

### 🔄 Continuous Integration & Deployment
- **Automated testing** across Python 3.9, 3.10, and 3.11
- **Code quality checks** with Black, flake8, isort, and mypy
- **Security scanning** with Bandit and Safety
- **Automated releases** with semantic versioning
- **Dependency updates** with automated pull requests

### 🛠️ Development Tools
- **Pre-commit hooks** for code quality enforcement
- **Comprehensive test suite** with pytest and coverage reporting
- **Type checking** with mypy
- **Documentation** generation ready
- **Package building** and distribution

### 🔒 Security & Quality
- **Automated security vulnerability scanning**
- **Code quality metrics** and reporting
- **Dependency vulnerability checks**
- **Automated code formatting**

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Sonny-Ethan-Quinn/crispy-journey.git
cd crispy-journey

# Install development dependencies
pip install -r requirements-dev.txt

# Install the package in development mode
pip install -e .

# Set up pre-commit hooks
pre-commit install
```

### Usage

```python
from crispy_journey import AutomationManager, logger

# Initialize automation manager
manager = AutomationManager()
manager.setup_automation()

# Run automation tasks
manager.run_task("lint")     # Run code linting
manager.run_task("test")     # Run tests
manager.run_task("format")   # Format code
manager.run_task("security") # Security checks

# List available tasks
print(manager.list_tasks())
```

### Command Line Interface

```bash
# Run individual automation tasks
python -m crispy_journey lint
python -m crispy_journey test
python -m crispy_journey format
python -m crispy_journey security
```

## 🔧 Development

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_automation.py
```

### Code Quality

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/

# Security scan
bandit -r src/
```

### Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality:

```bash
# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

## 🏗️ Project Structure

```
crispy-journey/
├── .github/
│   └── workflows/          # GitHub Actions workflows
│       ├── ci.yml         # Main CI/CD pipeline
│       ├── release.yml    # Automated releases
│       └── dependencies.yml # Dependency updates
├── src/
│   └── crispy_journey/    # Main package
│       ├── __init__.py
│       ├── automation.py  # Automation management
│       └── utils.py       # Utility functions
├── tests/                 # Test suite
│   ├── test_automation.py
│   └── test_utils.py
├── .pre-commit-config.yaml # Pre-commit configuration
├── pyproject.toml         # Project configuration
├── setup.cfg             # Tool configurations
├── requirements-dev.txt   # Development dependencies
└── README.md             # This file
```

## 🤖 Automation Workflows

### CI/CD Pipeline (`.github/workflows/ci.yml`)

Automatically runs on every push and pull request:

1. **Code Quality Checks**
   - Code formatting (Black)
   - Import sorting (isort)
   - Linting (flake8)
   - Type checking (mypy)

2. **Testing**
   - Unit tests across Python 3.9, 3.10, 3.11
   - Coverage reporting
   - Test result artifacts

3. **Security Scanning**
   - Vulnerability scanning (Bandit)
   - Dependency security checks (Safety)

4. **Build & Package**
   - Package building
   - Artifact uploading

### Automated Releases (`.github/workflows/release.yml`)

Triggered when a version tag is pushed:

- Builds the package
- Generates changelog from commits
- Creates GitHub release
- Uploads release artifacts

### Dependency Updates (`.github/workflows/dependencies.yml`)

Runs weekly to keep dependencies up-to-date:

- Updates Python dependencies
- Runs security audits
- Creates automated pull requests
- Includes change summaries

## 📦 Package Configuration

### pyproject.toml

Modern Python packaging with:
- Build system configuration
- Project metadata
- Tool configurations (Black, isort, mypy, pytest)
- Development dependencies

### setup.cfg

Additional tool configurations for:
- flake8 linting rules
- Code complexity limits
- Import and style checks

## 🔒 Security

This project implements multiple security layers:

- **Automated vulnerability scanning** with Bandit
- **Dependency security checks** with Safety and pip-audit
- **Regular security audits** via automated workflows
- **Secure coding practices** enforcement via pre-commit hooks

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the automation checks (`python -m crispy_journey lint`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

The automated CI/CD pipeline will run all checks on your pull request.

## 📊 Monitoring & Metrics

The automation provides:

- **Code coverage** reporting
- **Test result** tracking
- **Security vulnerability** monitoring
- **Dependency health** checks
- **Build status** indicators

## 🎯 Goals

This project demonstrates:

- **Zero-configuration** automation setup
- **Industry best practices** for Python development
- **Comprehensive quality gates** 
- **Security-first** approach
- **Developer experience** optimization

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you have questions or need help:

- Open an [issue](https://github.com/Sonny-Ethan-Quinn/crispy-journey/issues)
- Check the [documentation](https://github.com/Sonny-Ethan-Quinn/crispy-journey/wiki)
- Review the [automation workflows](.github/workflows/)

---

**Made with ❤️ and full automation in mind!**
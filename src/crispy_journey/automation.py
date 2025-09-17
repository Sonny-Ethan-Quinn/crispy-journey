"""Automation management utilities."""

import subprocess
import sys
from typing import Dict, List


class AutomationManager:
    """Manages automation tasks and workflows."""

    def __init__(self) -> None:
        """Initialize the automation manager."""
        self.tasks: Dict[str, callable] = {}

    def register_task(self, name: str, task: callable) -> None:
        """Register a new automation task.

        Args:
            name: The name of the task
            task: The callable task function
        """
        self.tasks[name] = task

    def run_task(self, name: str, *args, **kwargs) -> bool:
        """Run a registered task.

        Args:
            name: The name of the task to run
            *args: Positional arguments to pass to the task
            **kwargs: Keyword arguments to pass to the task

        Returns:
            True if task completed successfully, False otherwise
        """
        if name not in self.tasks:
            print(f"Task '{name}' not found")
            return False

        try:
            self.tasks[name](*args, **kwargs)
            return True
        except Exception as e:
            print(f"Task '{name}' failed: {e}")
            return False

    def list_tasks(self) -> List[str]:
        """List all registered tasks.

        Returns:
            List of task names
        """
        return list(self.tasks.keys())

    def run_command(
        self, command: str, check: bool = True
    ) -> subprocess.CompletedProcess:
        """Run a shell command.

        Args:
            command: The command to run
            check: Whether to raise an exception on non-zero exit code

        Returns:
            CompletedProcess object
        """
        return subprocess.run(
            command, shell=True, check=check, capture_output=True, text=True
        )

    def setup_automation(self) -> None:
        """Set up default automation tasks."""
        self.register_task("lint", self._lint_code)
        self.register_task("test", self._run_tests)
        self.register_task("format", self._format_code)
        self.register_task("security", self._security_check)

    def _lint_code(self) -> None:
        """Run code linting."""
        print("Running flake8...")
        result = self.run_command("flake8 src/", check=False)
        if result.returncode == 0:
            print("✅ Linting passed")
        else:
            print("❌ Linting failed")
            print(result.stdout)

    def _run_tests(self) -> None:
        """Run tests."""
        print("Running tests...")
        result = self.run_command("pytest tests/", check=False)
        if result.returncode == 0:
            print("✅ All tests passed")
        else:
            print("❌ Some tests failed")
            print(result.stdout)

    def _format_code(self) -> None:
        """Format code with black."""
        print("Formatting code with black...")
        result = self.run_command("black src/", check=False)
        if result.returncode == 0:
            print("✅ Code formatted")
        else:
            print("❌ Formatting failed")
            print(result.stdout)

    def _security_check(self) -> None:
        """Run security checks."""
        print("Running security checks...")
        result = self.run_command("bandit -r src/ -c .bandit", check=False)
        if result.returncode == 0:
            print("✅ Security check passed")
        else:
            print("❌ Security issues found")
            print(result.stdout)


def main() -> None:
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python -m crispy_journey <task>")
        print("Available tasks: lint, test, format, security")
        return

    manager = AutomationManager()
    manager.setup_automation()

    task_name = sys.argv[1]
    if not manager.run_task(task_name):
        sys.exit(1)


if __name__ == "__main__":
    main()

"""Tests for the automation module."""

import pytest
from unittest.mock import Mock, patch

from crispy_journey.automation import AutomationManager


class TestAutomationManager:
    """Test cases for AutomationManager."""

    def test_init(self):
        """Test AutomationManager initialization."""
        manager = AutomationManager()
        assert manager.tasks == {}

    def test_register_task(self):
        """Test task registration."""
        manager = AutomationManager()
        mock_task = Mock()
        
        manager.register_task("test_task", mock_task)
        
        assert "test_task" in manager.tasks
        assert manager.tasks["test_task"] == mock_task

    def test_run_task_success(self):
        """Test successful task execution."""
        manager = AutomationManager()
        mock_task = Mock()
        manager.register_task("test_task", mock_task)
        
        result = manager.run_task("test_task", "arg1", key="value")
        
        assert result is True
        mock_task.assert_called_once_with("arg1", key="value")

    def test_run_task_not_found(self, capsys):
        """Test running a non-existent task."""
        manager = AutomationManager()
        
        result = manager.run_task("nonexistent")
        
        assert result is False
        captured = capsys.readouterr()
        assert "Task 'nonexistent' not found" in captured.out

    def test_run_task_exception(self, capsys):
        """Test task execution with exception."""
        manager = AutomationManager()
        mock_task = Mock(side_effect=ValueError("Test error"))
        manager.register_task("failing_task", mock_task)
        
        result = manager.run_task("failing_task")
        
        assert result is False
        captured = capsys.readouterr()
        assert "Task 'failing_task' failed: Test error" in captured.out

    def test_list_tasks(self):
        """Test listing registered tasks."""
        manager = AutomationManager()
        task1 = Mock()
        task2 = Mock()
        
        manager.register_task("task1", task1)
        manager.register_task("task2", task2)
        
        tasks = manager.list_tasks()
        assert set(tasks) == {"task1", "task2"}

    @patch('subprocess.run')
    def test_run_command(self, mock_run):
        """Test running a shell command."""
        manager = AutomationManager()
        mock_process = Mock()
        mock_run.return_value = mock_process
        
        result = manager.run_command("echo test")
        
        assert result == mock_process
        mock_run.assert_called_once_with(
            "echo test",
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )

    def test_setup_automation(self):
        """Test setting up default automation tasks."""
        manager = AutomationManager()
        
        manager.setup_automation()
        
        expected_tasks = {"lint", "test", "format", "security"}
        assert set(manager.list_tasks()) == expected_tasks

    @patch.object(AutomationManager, 'run_command')
    def test_lint_code(self, mock_run_command, capsys):
        """Test lint code task."""
        manager = AutomationManager()
        mock_run_command.return_value = Mock(returncode=0)
        
        manager._lint_code()
        
        mock_run_command.assert_called_once_with("flake8 src/", check=False)
        captured = capsys.readouterr()
        assert "✅ Linting passed" in captured.out

    @patch.object(AutomationManager, 'run_command')
    def test_run_tests(self, mock_run_command, capsys):
        """Test run tests task."""
        manager = AutomationManager()
        mock_run_command.return_value = Mock(returncode=0)
        
        manager._run_tests()
        
        mock_run_command.assert_called_once_with("pytest tests/", check=False)
        captured = capsys.readouterr()
        assert "✅ All tests passed" in captured.out

    @patch.object(AutomationManager, 'run_command')
    def test_format_code(self, mock_run_command, capsys):
        """Test format code task."""
        manager = AutomationManager()
        mock_run_command.return_value = Mock(returncode=0)
        
        manager._format_code()
        
        mock_run_command.assert_called_once_with("black src/", check=False)
        captured = capsys.readouterr()
        assert "✅ Code formatted" in captured.out

    @patch.object(AutomationManager, 'run_command')
    def test_security_check(self, mock_run_command, capsys):
        """Test security check task."""
        manager = AutomationManager()
        mock_run_command.return_value = Mock(returncode=0)
        
        manager._security_check()
        
        mock_run_command.assert_called_once_with("bandit -r src/ -c .bandit", check=False)
        captured = capsys.readouterr()
        assert "✅ Security check passed" in captured.out
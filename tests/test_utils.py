"""Tests for the utils module."""

import logging
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from crispy_journey.utils import (
    setup_logging,
    get_project_root,
    ensure_directory,
    read_file,
    write_file,
)


class TestSetupLogging:
    """Test cases for setup_logging function."""

    def test_setup_logging_default(self):
        """Test setup_logging with default parameters."""
        logger = setup_logging()
        
        assert logger.name == "crispy_journey"
        assert logger.level <= logging.INFO

    def test_setup_logging_with_level(self):
        """Test setup_logging with custom level."""
        logger = setup_logging(level="DEBUG")
        
        assert logger.level <= logging.DEBUG

    def test_setup_logging_with_file(self):
        """Test setup_logging with log file."""
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            logger = setup_logging(log_file=tmp_file.name)
            
            # Check that file handler was added
            handlers = logging.getLogger().handlers
            file_handlers = [h for h in handlers if isinstance(h, logging.FileHandler)]
            assert len(file_handlers) > 0


class TestGetProjectRoot:
    """Test cases for get_project_root function."""

    def test_get_project_root(self):
        """Test getting project root directory."""
        root = get_project_root()
        
        assert isinstance(root, Path)
        assert root.exists()
        # Should contain pyproject.toml
        assert (root / "pyproject.toml").exists()


class TestEnsureDirectory:
    """Test cases for ensure_directory function."""

    def test_ensure_directory_new(self):
        """Test creating a new directory."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_path = Path(tmp_dir) / "new_dir" / "nested"
            
            ensure_directory(test_path)
            
            assert test_path.exists()
            assert test_path.is_dir()

    def test_ensure_directory_existing(self):
        """Test with existing directory."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_path = Path(tmp_dir)
            
            # Should not raise an error
            ensure_directory(test_path)
            
            assert test_path.exists()


class TestReadFile:
    """Test cases for read_file function."""

    def test_read_file_success(self):
        """Test reading an existing file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            test_content = "Hello, World!"
            tmp_file.write(test_content)
            tmp_file.flush()
            
            result = read_file(Path(tmp_file.name))
            
            assert result == test_content

    def test_read_file_not_found(self):
        """Test reading a non-existent file."""
        non_existent_path = Path("/tmp/non_existent_file.txt")
        
        with pytest.raises(FileNotFoundError):
            read_file(non_existent_path)


class TestWriteFile:
    """Test cases for write_file function."""

    def test_write_file_new(self):
        """Test writing to a new file."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_path = Path(tmp_dir) / "test_file.txt"
            test_content = "Test content"
            
            write_file(test_path, test_content)
            
            assert test_path.exists()
            assert test_path.read_text() == test_content

    def test_write_file_with_nested_directory(self):
        """Test writing to a file in a nested directory."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            test_path = Path(tmp_dir) / "nested" / "dir" / "test_file.txt"
            test_content = "Test content"
            
            write_file(test_path, test_content)
            
            assert test_path.exists()
            assert test_path.read_text() == test_content

    def test_write_file_overwrite(self):
        """Test overwriting an existing file."""
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            test_path = Path(tmp_file.name)
            original_content = "Original content"
            new_content = "New content"
            
            # Write original content
            test_path.write_text(original_content)
            
            # Overwrite with new content
            write_file(test_path, new_content)
            
            assert test_path.read_text() == new_content
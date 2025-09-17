"""Utility functions and classes."""

import logging
import sys
from pathlib import Path
from typing import Optional


def setup_logging(
    level: str = "INFO",
    log_file: Optional[str] = None,
    format_string: Optional[str] = None,
) -> logging.Logger:
    """Set up logging configuration.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path
        format_string: Optional custom format string

    Returns:
        Configured logger instance
    """
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=format_string,
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )

    # Add file handler if log_file is specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(format_string))
        logging.getLogger().addHandler(file_handler)

    return logging.getLogger("crispy_journey")


def get_project_root() -> Path:
    """Get the project root directory.

    Returns:
        Path to the project root
    """
    current_file = Path(__file__).resolve()
    # Go up from src/crispy_journey/utils.py to project root
    return current_file.parent.parent.parent


def ensure_directory(path: Path) -> None:
    """Ensure a directory exists, creating it if necessary.

    Args:
        path: Path to the directory
    """
    path.mkdir(parents=True, exist_ok=True)


def read_file(file_path: Path) -> str:
    """Read a file and return its contents.

    Args:
        file_path: Path to the file

    Returns:
        File contents as string

    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def write_file(file_path: Path, content: str) -> None:
    """Write content to a file.

    Args:
        file_path: Path to the file
        content: Content to write
    """
    ensure_directory(file_path.parent)
    file_path.write_text(content, encoding="utf-8")


# Global logger instance
logger = setup_logging()

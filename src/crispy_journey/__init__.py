"""
Crispy Journey - A fully automated project template.

This package provides automation tools and utilities for software development projects.
"""

__version__ = "0.1.0"
__author__ = "Sonny Ethan Quinn"
__email__ = "noreply@github.com"

from .automation import AutomationManager
from .utils import logger

__all__ = ["AutomationManager", "logger"]

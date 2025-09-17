"""
Tests for crispy_journey package.
"""

from crispy_journey.main import main


def test_main_function():
    """Test that main function runs without error."""
    result = main()
    assert result == 0


def test_import():
    """Test that package can be imported."""
    import crispy_journey
    assert hasattr(crispy_journey, "__version__")
    assert crispy_journey.__version__ == "0.1.0"
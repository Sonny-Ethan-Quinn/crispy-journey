"""Tests for crispy_journey package."""

import crispy_journey


def test_hello():
    """Test the hello function."""
    result = crispy_journey.hello()
    assert result == "Hello from crispy-journey!"
    assert isinstance(result, str)


def test_main():
    """Test the main function."""
    result = crispy_journey.main()
    assert result is True


def test_version():
    """Test that version is set."""
    assert hasattr(crispy_journey, "__version__")
    assert crispy_journey.__version__ == "0.1.0"
"""Test Snap Package Template."""

import snapenv_core


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(snapenv_core.__name__, str)

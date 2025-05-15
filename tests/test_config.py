"""
Test suite for the snapenv_core module.

This module contains asynchronous tests for functions within the
bootstrap_python_package, specifically focusing on the `some_function` function.

The tests are written using the pytest framework.

Functions
---------
test_config_manager()
    Asynchronously tests that `SnapEnvCommonSettings` returns the expected value.
"""

import platform
import sys
from unittest import mock

import pytest
from pydantic import computed_field

from snapenv_core.settings.manager import (
    ENVIRONMENT,
    SECRETS_DIR,
    SnapEnvCommonSettings,
    initialize_secret_dir,
)

PLATFORM = {"linux": "Linux", "linux2": "Linux", "win32": "Windows", "darwin": "MacOS"}


@pytest.mark.no_collect
class SettingsForTests(SnapEnvCommonSettings):
    """Test class instantied using `SnapEnvCommonSettings` as base model."""

    env: str = ENVIRONMENT
    platform: str = PLATFORM.get(sys.platform, "other")
    port: int = 5432

    @computed_field  # type: ignore[misc]
    @property
    def server(self) -> str:
        """
        Return local server name stripped of possible domain part.

        Returns
        -------
        str
            Server name in upper case.
        """
        return platform.node()


@pytest.mark.asyncio
async def test_config_manager():
    """
    Test that `SnapEnvCommonSettings` returns the expected string.

    This asynchronous test checks whether the `SnapEnvCommonSettings` from the
    snapenv_core.config module returns correct values.

    Raises
    ------
    AssertionError
        If the class does not return the expected values.
    """
    settings = SettingsForTests()
    assert settings.env == "test"
    assert settings.server == platform.node()
    assert settings.platform == PLATFORM.get(sys.platform, "other")
    assert isinstance(settings.port, int)


@pytest.mark.asyncio
@mock.patch("os.makedirs")
@mock.patch("os.path.exists")
async def test_secret_dir_exists(mock_exists, mock_makedirs):
    """
    Test that `initialize_secret_dir` not create dir.

    This asynchronous test checks whether the config managr module
    not create the SECRET_DIR if it exists.

    Raises
    ------
    AssertionError
        If the class does not return the expected values.
    """
    # Mock `os.path.exists` to return False
    mock_exists.return_value = True

    # Call the function directly
    initialize_secret_dir()

    # Assert that os.makedirs was called with the correct arguments
    mock_makedirs.assert_not_called()


@pytest.mark.asyncio
@mock.patch("os.makedirs")
@mock.patch("os.path.exists")
async def test_secret_dir_not_exists(mock_exists, mock_makedirs):
    """
    Test that `initialize_secret_dir` can create dir.

    This asynchronous test checks whether the config managr module
    can create the SECRET_DIR if it not exists.

    Raises
    ------
    AssertionError
        If the class does not return the expected values.
    """
    # Mock `os.path.exists` to return False
    mock_exists.return_value = False

    # Call the function directly
    initialize_secret_dir()

    # Assert that os.makedirs was called with the correct arguments
    mock_makedirs.assert_called_once_with(SECRETS_DIR, exist_ok=True)

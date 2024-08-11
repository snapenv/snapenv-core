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

import os.path
import platform
from unittest import mock

import pytest

from snapenv_core.config.manager import SECRETS_DIR, SnapEnvCommonSettings, initialize_secret_dir


@pytest.mark.asyncio()
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
    settings = SnapEnvCommonSettings()
    assert settings.env == "test"
    assert settings.server == platform.node()
    assert os.path.exists(SECRETS_DIR) == 1


@pytest.mark.asyncio()
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



@pytest.mark.asyncio()
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

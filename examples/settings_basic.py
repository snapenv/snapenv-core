"""Example usage of SnapEnv settings management with Pydantic and environment-based configuration."""

import platform
import sys
from functools import lru_cache

from pydantic import computed_field

from snapenv_core.settings.manager import ENVIRONMENT, PLATFORM, SnapEnvCommonSettings


class DbSettings(SnapEnvCommonSettings):
    """
    Database settings configuration.

    Attributes
    ----------
    POSTGRES_HOST : str
        The title of the application.
    """

    POSTGRES_HOST: str = "dbhost"


class AppSettings(SnapEnvCommonSettings):
    """
    Application settings configuration.

    Attributes
    ----------
    APP_TITLE : str
        The title of the application.
    LOG_LEVEL : str
        The log level for the application.
    model_config : SettingsConfigDict
        Configuration dictionary for environment settings, initialized with the environment file.
    """

    # constant settings

    # Environment depending settings
    env: str = ENVIRONMENT
    platform: str = PLATFORM.get(sys.platform, "other")

    # App settings
    APP_TITLE: str = "SNAPENV-CORE"
    LOG_LEVEL: str = "DEBUG"
    DB: DbSettings = DbSettings()

    # Computed settings
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


@lru_cache
def get_settings() -> AppSettings:
    """
    Retrieve the application settings with caching.

    This function uses an LRU cache to store the settings so that
    subsequent calls are fast and do not re-initialize the settings.

    Returns
    -------
    AppSettings
        The application settings instance.
    """
    return AppSettings()


settings: AppSettings = get_settings()


print(settings)

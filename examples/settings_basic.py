from functools import lru_cache

from snapenv_core.settings.manager import SnapEnvCommonSettings


class AppSettings(SnapEnvCommonSettings):
    """
    Application settings configuration.

    Attributes
    ----------
    APP_TITLE : str
        The title of the application.
    LOG_LEVEL : str
        The log level for the application.
    """

    APP_TITLE: str
    LOG_LEVEL: str


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

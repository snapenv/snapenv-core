# Settings Module

This page demonstrates how to construct and customize application settings using the `SnapEnv Core` package. The example provided illustrates how to define application-specific settings, utilize caching for efficient access, and integrate these settings into your application.

## Example: Application Settings with Caching

### Step 1: Import Necessary Modules

```python
from functools import lru_cache
from snapenv_core.settings.manager import SnapEnvCommonSettings
```

#### Explanation:

- `functools.lru_cache`: This decorator is used to cache the result of the function it decorates, improving performance by storing the result of expensive function calls and reusing them when the same inputs occur.
- `SnapEnvCommonSettings`: This is a base class provided by the SnapEnv Core package. It serves as the foundation for defining environment-based settings in your application.

### Step 2: Define Application Settings Class

```python
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
```

#### Explanation:

- `AppSettings`: This class inherits from `SnapEnvCommonSettings` and defines the specific settings for your application.
- `APP_TITLE`: A string attribute representing the title of your application.
- `LOG_LEVEL`: A string attribute that determines the logging level (e.g., `DEBUG`, `INFO`, `WARNING`, etc.).

### Step 3: Create a Cached Settings Retrieval Function

```python
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
```

#### Explanation:

- `@lru_cache`: This decorator caches the result of the `get_settings` function, ensuring that the settings are only initialized once and subsequent calls are faster.
- `get_settings`: This function returns an instance of `AppSettings`, which contains the application settings.

### Step 4: Initialize and Use the Settings

```python
settings: AppSettings = get_settings()

print(settings)
```

#### Explanation:

- `settings`: This variable holds the cached instance of `AppSettings`.
- `print(settings)`: This prints the current settings to the console, which is useful for debugging or verifying the configuration.

### Customization Guide

You can customize the `AppSettings` class to include additional settings specific to your application. Here’s how you can do it:

1. **Add New Attributes**:
    - Simply add new attributes to the `AppSettings` class to define additional configuration options.
    
    ```python
    class AppSettings(SnapEnvCommonSettings):
        APP_TITLE: str
        LOG_LEVEL: str
        DATABASE_URL: str  # New attribute for database connection string
    ```

2. **Override Default Values**:
    - You can override default values by setting them directly in the class.
    
    ```python
    class AppSettings(SnapEnvCommonSettings):
        APP_TITLE: str = "My Application"
        LOG_LEVEL: str = "DEBUG"
        DATABASE_URL: str = "sqlite:///mydatabase.db"
    ```

3. **Use Environment Variables**:
    - The `SnapEnvCommonSettings` class is designed to load values from environment variables. Ensure your environment variables are correctly set to allow dynamic configuration.
    
    ```bash
    export APP_TITLE="My Application"
    export LOG_LEVEL="DEBUG"
    export DATABASE_URL="sqlite:///mydatabase.db"
    ```

## Example: Using .env Files

The `SnapEnvCommonSettings` class manages environment-specific configurations, allowing settings to be loaded from an `.env` file. The class uses Pydantic's `BaseSettings` to define environment-dependent parameters, and the `.env` file is determined by the value of the `ENVIRONMENT` environment variable.

### Example `.env` File

To avoid setting environment variables manually using the `export` command, you can define them in an `.env` file, which will be automatically loaded by the `SnapEnvCommonSettings` class.

Here's an example of how to create and customize an `.env` file for the `AppSettings` class:

```bash
# .env file

# The title of the application
APP_TITLE="My Custom Application"

# The log level for the application
LOG_LEVEL="DEBUG"

# Add any other custom settings here
DATABASE_URL="sqlite:///mydatabase.db"
```

### How to Use the `.env` File

1. **Create the `.env` File**: In the root directory of your project, create a file named `.env` or `<ENVIRONMENT>.env` (e.g., `production.env`).

2. **Define Your Settings**: Add your settings as key-value pairs in the `.env` file as shown above.

3. **Load Settings Automatically**: When you create an instance of `AppSettings`, the settings will be automatically loaded from the `.env` file.

### Customization Example in Python

```python
from functools import lru_cache
from snapenv_core.settings.manager import SnapEnvCommonSettings


class AppSettings(SnapEnvCommonSettings):
    """
    Application settings configuration.
    """

    APP_TITLE: str
    LOG_LEVEL: str
    DATABASE_URL: str  # New attribute for database connection string


@lru_cache
def get_settings() -> AppSettings:
    """
    Retrieve the application settings with caching.
    """
    return AppSettings()


settings: AppSettings = get_settings()

print(settings.APP_TITLE)  # Output: My Custom Application
print(settings.LOG_LEVEL)   # Output: DEBUG
print(settings.DATABASE_URL)  # Output: sqlite:///mydatabase.db
```

In this example, the settings are automatically populated from the `.env` file, making it easy to manage configurations across different environments without needing to set environment variables manually.

To run the example with different environment files, you can set the `ENVIRONMENT` environment variable before executing the script. This allows you to specify which `.env` file the `SnapEnvCommonSettings` class should load.

### Using the Default `.env` File

By default, if you don't set the `ENVIRONMENT` variable, the `SnapEnvCommonSettings` class will look for a file named `.env` in the root directory of your project.

To run the example using the default `.env` file, simply execute the script without setting any environment variables:

```bash
python examples/settings_basic.py
```

### Using a Specific Environment File (e.g., `dev.env`)

If you want to use a specific environment file like `dev.env`, you need to set the `ENVIRONMENT` variable to `dev` before running the script. This tells the `SnapEnvCommonSettings` class to load the settings from `dev.env`.

Here's how you can do it:

#### Unix/Linux/MacOS

```bash
ENVIRONMENT=dev python examples/settings_basic.py
```

#### Windows (Command Prompt)

```cmd
set ENVIRONMENT=dev && python examples/settings_basic.py
```

#### Windows (PowerShell)

```powershell
$env:ENVIRONMENT="dev"; python examples/settings_basic.py
```

### Explanation

- **ENVIRONMENT Variable**: This variable controls which `.env` file is used. If `ENVIRONMENT=dev`, the script will look for a `dev.env` file in the root directory.
- **Script Execution**: By setting the `ENVIRONMENT` variable before running the script, the settings are loaded from the specified `.env` file, allowing you to easily switch between different environment configurations.

### Example `.env` Files

**Default `.env` file**:

```bash
# .env
APP_TITLE="My Application"
LOG_LEVEL="INFO"
DATABASE_URL="sqlite:///default.db"
```

**Development environment file (`dev.env`)**:

```bash
# dev.env
APP_TITLE="My Application (Development)"
LOG_LEVEL="DEBUG"
DATABASE_URL="sqlite:///development.db"
```

When running with `ENVIRONMENT=dev`, the settings in `dev.env` will be applied, allowing you to customize your application's behavior based on the environment.


## Conclusion

This example illustrates the core concepts of defining and managing application settings using the SnapEnv Core package. By leveraging inheritance, caching, and environment variables, you can create flexible and efficient configuration management for your applications. Customize the `AppSettings` class to match your specific needs, and ensure your environment is configured correctly to take full advantage of the SnapEnv Core features.fic settings, utilize caching for efficient access, and integrate these settings into your application.


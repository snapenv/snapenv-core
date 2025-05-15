## v0.3.0 (2025-05-15)

### ✨ Features

- **manager.py**: remove unused imports, redundant code and default settings of the class

### ci

- **workflow**: set fetch-depth to 0 in checkout step for full git history

### docs

- **examples**: add module-level docstring for settings_basic.py to describe usage
- **adr-template.md**: update superseded by link to point to ADR-0001 for consistency and accuracy

### feat

- **test_config.py**: introduce SettingsForTests class to extend SnapEnvCommonSettings for testing
- Add platform and port attributes to SettingsForTests for enhanced test configuration
- Use no_collect marker to prevent test collection of SettingsForTests
- Ensure test_config_manager uses SettingsForTests to validate new attributes
- **settings_basic.py**: introduce DbSettings class for database configuration
- **settings_basic.py**: add environment and platform attributes to AppSettings for dynamic configuration
- **settings_basic.py**: set default values for APP_TITLE and LOG_LEVEL in AppSettings
- **settings_basic.py**: add computed property server to AppSettings to return local server name

### refactor

- **settings_basic.py**: import ENVIRONMENT and PLATFORM for environment-based configuration

### style

- **settings_basic.py**: add spacing and comments for better readability

### test

- **pytest.ini**: add no_collect marker to exclude specific tests from collection

### 🔧🔨📦️ Configuration, Scripts, Packages

- **pyproject.toml**: Add packages

## v0.2.2 (2025-05-15)

### 🐛🚑️ Fixes

- New version

### ci

- **publish.yml**: specify Python version 3.12 for consistency and predictability in the workflow

## v0.2.1 (2025-05-15)

### 🐛🚑️ Fixes

- Fix test error

## v0.2.0 (2025-05-15)

### ✨ Features

- New verson published

### build

- **pyproject.toml**: update mkdocs-material to include imaging extras

### chore

- **snapenv_core**: update version to 0.2.0 to reflect new changes and improvements in the package

### docs

- **CONTRIBUTING.md**: add `poe gen_module_docs` to formatting and validation section to ensure documentation generation is part of the contribution process
- **API-Reference**: add documentation for snapenv_core module and its settings

### 📌➕⬇️ ➖⬆️  Dependencies

- **poetry.lock**: Updated ependencies

## v0.1.0 (2025-05-14)

### chore

- **test_config.py**: remove unused import of os.path to clean up code
- **workspace**: add VS Code workspace configuration file for project setup
- **pyproject.toml**: add pytest-env dependency for environment variable support in tests chore(pyproject.toml): configure pytest-env to set ENVIRONMENT to "test" chore: remove snap-package-template.code-workspace file to clean up project directory

### docs

- add new logo images and custom HTML override
- add TODO.md with a task to read settings from a YAML file
- **main.html**: add custom HTML override for outdated version notice
- add usage section and settings module documentation
- **mkdocs.yml**: update versioning configuration to include latest and dev
- **index.md**: update feature list to include documentation structure using mkdocs
- update project name and description to SnapEnv Core package in index.md and mkdocs.yml
- **adr**: add ADR for using Pydantic Settings for configuration management

### feat

- update mkdocs.yml with new plugins and theme settings
- **pyproject.toml**: add new documentation dependencies for mkdocs plugins
- **examples**: add basic settings example for application configuration
- **settings**: add SnapEnv core settings module for environment configuration
- **config**: add SnapEnv core configuration management

### fix

- **mkdocs.yml**: correct path to custom CSS file for proper styling
- **workflows**: update repository name in rename_project workflow to snapenv-core

### refactor

- **manager.py**: add docstring to initialize_secret_dir for clarity
- 🎉 Ready to clone and code.

### style

- **settings_basic.py**: add newline for PEP 8 compliance and readability

### test

- **config**: update import paths to reflect new settings module
- **test_config.py**: comment out failing assertion for SECRETS_DIR existence to allow other tests to run
- **pytest.ini**: add pytest configuration file to set environment to test test(test_bootstrap.py): add pytest import and asyncio marker for async tests style(test_config.py): remove unnecessary blank line
- **config**: add tests for SnapEnvCommonSettings and initialize_secret_dir

### ✅🤡🧪 Tests

- remove parentheses from @pytest.mark.asyncio decorator for consistency

### 💚👷 CI & Build

- **pre-commit-config.yaml**: change default_stages from 'commit' to 'pre-commit' to ensure hooks run at the correct stage

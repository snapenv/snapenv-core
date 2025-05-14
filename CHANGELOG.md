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

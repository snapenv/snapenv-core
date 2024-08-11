---
status: accepted
date: 2024-08-11
---
# Use Pydantic Settings for Configuration Management

## Context and Problem Statement

In developing our Python package, we need a reliable way to manage configuration settings, including reading environment variables and validating them. The configuration should be easy to maintain, extend, and integrate well with other components of the package. The following options were considered:

## Considered Options

- [Pydantic Settings](https://pypi.org/project/pydantic-settings/)
- [Dynaconf](https://www.dynaconf.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [environs](https://pypi.org/project/environs/)
- Reading environment variables using `os.environ`.

## Decision Outcome

We decided to use `pydantic_settings` as the primary configuration management tool in our package.

## Consequences

### Positive Consequences:
- **Data Validation**: `pydantic_settings` leverages Pydantic's powerful data validation, ensuring that all configuration values are of the expected type and format.
- **Ease of Use**: It provides a declarative approach to defining settings, making the code more readable and maintainable.
- **Type Safety**: The use of Pydantic models ensures type safety across the configuration.
- **Extensibility**: Easily integrates with other Pydantic features, such as nested models and complex data structures.
- **Environment Management**: Supports reading from environment variables out-of-the-box, which aligns with the need to manage settings in different environments (e.g., development, staging, production).
- **Consistency Across Projects**: Since we extensively use Pydantic in our applications, utilizing `pydantic_settings` maintains consistency across the codebase, reducing the learning curve and increasing development efficiency.

### Negative Consequences:
- **Learning Curve**: Requires familiarity with Pydantic, which might be a barrier for new contributors not experienced with this library.
- **Dependency**: Adds a dependency on the Pydantic library, which may increase the package size and complexity.

## Pros and Cons of the Options

### Option 1: `os.environ`
- **Pros**:
  - Minimal dependencies.
  - Direct access to environment variables.
- **Cons**:
  - No built-in validation or type conversion.
  - Manual error handling and type casting required.

### Option 2: `Dynaconf`
- **Pros**:
  - Flexible and supports multiple sources (e.g., `.env`, environment variables, settings files).
  - Built-in support for different environments (development, production, etc.).
- **Cons**:
  - Additional complexity and larger dependency footprint.
  - Can be overkill for simpler projects.

### Option 3: `python-dotenv`
- **Pros**:
  - Simple and lightweight.
  - Easy to use for loading environment variables from a `.env` file.
- **Cons**:
  - No built-in validation or type safety.
  - Limited to environment variable management.

### Option 4: `environs`
- **Pros**:
  - Similar simplicity to `python-dotenv` but with added type validation.
  - Supports nested structures and more complex configurations.
- **Cons**:
  - Less feature-rich compared to `pydantic_settings`.
  - Another dependency to manage, though smaller than Pydantic.

### Option 5: `pydantic_settings`
- **Pros**:
  - Combines configuration management with robust validation and type safety.
  - Seamless integration with the rest of the package, especially when using Pydantic models.
- **Cons**:
  - Dependency on Pydantic.
  - Requires understanding of Pydantic’s data modeling.

## References

- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Dynaconf Documentation](https://www.dynaconf.com/)
- [python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
- [environs Documentation](https://github.com/sloria/environs)

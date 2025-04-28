# MCP Tool Server Template

A cookiecutter template for creating Model Context Protocol (MCP) tool servers with FastAPI, uv, and Docker support.

## Features

- FastAPI-based REST server
- Model Context Protocol (MCP) tool support
- Sample weather tool implementation
- Modern Python tooling (uv, ruff, mypy)
- Type hints and comprehensive testing
- Docker support for containerization
- Kubernetes deployment configuration

## Requirements

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- [cookiecutter](https://github.com/cookiecutter/cookiecutter) 2.5.0 or higher

## Usage

### Creating a New Project

```bash
cookiecutter gh:mibexx/mbxai-mcp-server-template
```

Follow the prompts to configure your project:

- `project_name`: The name of your project
- `project_slug`: The slug for your project (used in paths and imports)
- `package_name`: The name of your Python package
- `description`: A short description of your project
- `author_name`: Your name
- `author_email`: Your email
- `open_source_license`: The license for your project
- `python_version`: The Python version to use
- `use_pytest`: Whether to include pytest for testing
- `use_mypy`: Whether to include mypy for type checking
- `use_ruff`: Whether to include ruff for linting

### Project Structure

The template creates a well-organized project structure:

```
your-project/
├── src/
│   └── your_package/
│       ├── api/                  # Core API functionality
│       ├── clients/              # Client libraries
│       ├── project/              # Project-specific code
│       │   └── weather.py        # Sample weather tool
│       ├── config.py             # Configuration management
│       └── __init__.py           # Package initialization
├── tests/                        # Test suite
├── data/                         # Data storage
├── logs/                         # Log files
├── kubernetes/                   # Kubernetes deployment files
├── Dockerfile                    # Docker configuration
├── docker-compose.yml            # Docker Compose configuration
├── pyproject.toml                # Project metadata and dependencies
└── README.md                     # Project documentation
```

## Development

### Running Locally

```bash
cd your-project
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
uv pip install -e .
uv run service
```

### Running with Docker

```bash
cd your-project
docker-compose up -d
```

### Deploying to Kubernetes

```bash
cd your-project
kubectl apply -f kubernetes/mbxai_resource.yaml
```

## Adding New Tools

See the project README.md for detailed instructions on adding new tools to your MCP server.

## License

This template is licensed under the MIT License - see the LICENSE file for details.

## About

Created by [Mibexx](https://mibexx.com)

# Development environment

## Important links

- Code repository: 
	- https://github.com/time-link/timelink-py
	- Instructions for contributors: https://github.com/time-link/timelink-py/blob/main/## 
- Pypi package:
	- https://pypi.org/project/timelink/0.2.8/
- ReadTheDocs (package and source code documentation)
	- [https://timelink-py.readthedocs.io/](https://timelink-py.readthedocs.io/)
	- The documentation is produced by `make docs` 

## Source directory layout

### Project Directory Layout: `timelink-py`

The Timelink package used as a template the `cookiecutter-pypackage`. Check the documentation at https://github.com/audreyfeldroy/cookiecutter-pypackage on how to install various tools used. 


> [!NOTE] Old version of `cookiecutter-pypackage` 
> The template used at the time of project start has been checked, namely usage of Travis seems to have been replaced by github actions in the most current versions.


The root directory contains standard Python project files, with the main code in `timelink/` and tests in `tests/`. Below is a high-level overview of the key directories and files based on the project's structure.
#### Root Directory (`timelink-py/`)

- **`timelink/`**: source code for the `timelink` package.
- **`tests/`**: Directory for unit and integration tests (e.g., `test_*.py` files like `test_020_database.py`).
	- This directory contain a `timelink-home` directory that is used to have a base for testing file reflita operations, web services, notebook integration, etc... Inside there are reference projects containing `Kleio`  sources and example notebooks. Also a tutorial.
- **`requirements.txt`**: Lists Python dependencies for the project, i.e. necessary to run `timelink`.
- **`requirements_dev.txt`** Lists Python dependencies for running the various development tools, e.g., tests, linting, documentation generation, etc...
- **`tox.ini`**: Configuration for Tox, a tool for running local tests and linting in isolated Python environments (e.g., for Python 3.10/3.11 and Flake8).  Run is used by `make test-all`.
-  `.travis.yml` Configuration file for the Tavis continuous integration service. This file is used to configure the deployment of a new version of`timelink` to Pypi and ReadTheDocs, when a "push" is done in the main branch of the github repository.  It defines the installation of requirements and the version of Python against which the tests will be run. If tests are successful the package is build and deployed to PyPi.  In future github CI will be used and this file deprecated. See the "Testing" heading in 
- **`setup.cfg`**: configuration for version number generation (`bump2version` ), packaging and `flake8` linter. 
- **`pyproject.toml`**: Configuration for `Black` code formatter, `poetry` (current not used) and `pylance` 
- **`.gitignore`**: Specifies files and directories to ignore in Git (e.g., `__pycache__/`, `*.sqlite`, virtual environments).
- **`README.md`**, **`LICENSE`**, etc.: Documentation and licensing files.

#### Main Package Directory (`timelink/`)

- **`cli.py`**: Command-line interface using Typer, for commands like database setup and server management.
- **`api/`**: Core API modules, including models (e.g., `entity.py`, `database.py`), schemas, and CRUD operations.
- **`web/`**: Web application components, including pages (e.g., `display_id_page.py`, `tables_page.py`) and utilities for the NiceGUI-based web interface.
- **`networks/`**: Modules for network analysis (e.g., `network_generation.py`).
- **`kleio/`**: Kleio server integration and utilities (e.g., `kleio_server.py`).
- **`app/`**: Application-specific code, including models (e.g., `project.py`) and templates (e.g., Jinja2 templates in `templates/`).
- **`mhk/`**: MHK (historical data) utilities.
- **`migrations/`**: Database migration scripts.
- **`__init__.py`**: Package initialization.

## Linting and code formatting

Linting is the process of analysing source code to flag potential errors. In `VSCode` linting signals visually problematic lines and changes the color of the filename in the file browser to red.

We used `Fake8` for linting, so it should be enable inthe workspace settings. Currently we do not use `pylint` so it should be disabled in workspace settings to avoid spurious warnings and errors.

Code can be formatted to abide to `Flake8` requirements using `Black` .  Code can be formatted using `black timelink` in the terminal or in VSCode by setting the default formatter to "Black formatter".

These are set in Workspace settings in the project.



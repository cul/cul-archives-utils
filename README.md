# cul-archives-utils
Python utility module for archives and collection data

## Requirements
* Python 3.7+
* Requests module
* Responses module (to run tests)


## Functionality

* CLIO utils: Utilities to get data from CLIO, the Columbia Libraries Catalog
* Data utils: Perform actions on lists
* File utils: Perform actions on files
* XML utils: Saxon and Jing utilities to work with XML data

## Contribution standards

#### Style

This project uses the Python PEP8 community style guidelines. To conform to these guidelines, the following linters are part of the pre-commit:

* black formats the code automatically
* flake8 checks for style problems as well as errors and complexity
* isort sorts imports alphabetically, and automatically separated into sections and by type

After locally installing pre-commit, install the git-hook scripts in the project directory: ```pre-commit install```  

#### Documentation

This project adheres to [Google’s docstring style guide](https://google.github.io/styleguide/pyguide.html#381-docstrings). There are two types of docstrings: one-liners and multi-line docstrings. A one-line docstring may be perfectly appropriate for obvious cases where the code is immediately self-explanatory. Use multiline docstrings for all other cases.

#### Tests

New code should  have unit tests. Tests are written in unittest style and run using [tox](https://tox.readthedocs.io/). To run the unit tests, specify the Python version using the `e` flag (see `tox.ini` for supported versions).

# A Collection of Design Patterns in Python

All 23 GoF (Gang of Four) Design Patterns In Python ([source](https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25231942#overview)).

### Creational Design Patterns
- [Factory Pattern](https://sbcode.net/python/factory/)
- [Abstract Factory Pattern](https://sbcode.net/python/abstract_factory/)

## Requirements

The code runs on Python 3.

## Setup

### Conda Environment

Create a [Conda](https://docs.conda.io/projects/miniconda/en/latest/index.html#quick-command-line-install) environment with Python 3.10:

```bash
conda create --name py310 python=3.10
```

Activate the Conda environment:

```bash
conda activate py310
```

### Virtual Environment

If you prefer using your own virtual environment(optional):

```bash
cd python/
python -m venv .venv
source .venv/bin/activate
```

## Installation

Install project dependencies:

```bash
pip install -r requirements.txt
```

## Code Quality

### Linter

Run the linter to check for code quality:

```bash
pylint
```

### Code Formatting

Use Black for code formatting:

```bash
black .
```

## Usage

This folder is for keeping and explaining different design patterns in Python. It's here to help developers with effective solutions for various projects.

## Future improvements

* Might be overkill.
* Integrate [Poetry](https://python-poetry.org)
* Integrate [Pre-Commit](https://pre-commit.com/#install)

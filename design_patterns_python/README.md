# A Collection of Design Patterns in Python

This repository contains implementations of all 23 GoF (Gang of Four) Design Patterns in Python. You can find the source course [here](https://www.udemy.com/course/design-patterns-in-python/learn/lecture/25231942#overview).

## Design Patterns

### Creational Design Patterns

- [Factory Pattern](https://sbcode.net/python/factory/)
- [Abstract Factory Pattern](https://sbcode.net/python/abstract_factory/)
- [Builder Pattern](https://sbcode.net/python/builder/)
- [Prototype Pattern](https://sbcode.net/python/prototype/)
- [Singleton Pattern](https://sbcode.net/python/singleton/)

### Structural Design Patterns

- [Decorator Pattern](https://sbcode.net/python/decorator/)
- [Adapter Pattern](https://sbcode.net/python/adapter/)

## Requirements

- Python 3.x

## Setup

### Conda Environment

1. Create a Conda environment with Python 3.x:
    ```bash
    conda create --name py3x python=3.x
    ```
2. Activate the Conda environment:
    ```bash
    conda activate py3x
    ```

### Virtual Environment

1. Navigate to the project directory:
    ```bash
    cd python/
    ```
2. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
3. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

## Installation

Install the project dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Code Quality

### Pre-commit

This project uses pre-commit for static code analysis and formatting.

1. Install pre-commit hooks:
    ```bash
    pre-commit install
    pre-commit installed at .git/hooks/pre-commit
    ```

2. To run pre-commit on all files:
    ```bash
    pre-commit run --all-files
    ```

Feel free to contribute or report any issues you encounter. Happy coding!

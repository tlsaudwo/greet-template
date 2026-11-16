# Contributing to {{ cookiecutter.package_distribution_name }}

## Set up for development

Activate a Python 3.11+ virtual environment and run:

```sh
python -m pip install -e .
```

## Run the tests

```sh
python -c "from {{ cookiecutter.package_import_name }} import greet; print(greet('Hee'))"
```

Expected output: `Hello, Hee!`

## Send a change

Create a branch from `main`, commit your change, push that branch, and open a pull request targeting `main`.

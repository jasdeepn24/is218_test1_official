# IS 218 Test 1
Jasdeep Nagra

Test to set up, build, test, and make Python calculator with Git

requirements.txt is committed so another developer knows which dependencies/versions the project needs.

.venv stays local because it contains machine-specific installed packages and can be recreated from requirements.txt.

## Purpose

This project is a Python calculator created for IS 218 Test 1. It includes addition and subtraction functions and uses pytest to make sure the functions return the correct results.

## Setup

Create the virtual environment using Python 3.13:

```bash
~/.pyenv/versions/3.13.15/bin/python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file is committed so another developer knows which dependencies are needed to run and test the project. The `.venv` directory is ignored because it contains packages installed for my local environment and can be recreated using `requirements.txt`.

## Testing

Run the six student tests:

```bash
python -m pytest
```

Run the student tests and supplied acceptance checks:

```bash
python -m pytest tests checks -v
```

The first command should run all six student tests. The second command also runs the six supplied acceptance checks.

## Test Explanation

The `test_add` test uses `2` and `3` as inputs and expects the result to be `5`. The assertion checks that the `add` function returns `5` when those two values are passed to it.

## Issues

- [Issue #1 - Set up a reproducible Python project](https://github.com/jasdeepn24/is218_test1_official/issues/1)
- [Issue #2 - Implement and test addition](https://github.com/jasdeepn24/is218_test1_official/issues/2)
- [Issue #3 - Implement and test subtraction](https://github.com/jasdeepn24/is218_test1_official/issues/3)
- [Issue #4 - Document, verify, and deliver](https://github.com/jasdeepn24/is218_test1_official/issues/4)
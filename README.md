[![Python 3.12](https://github.com/tiagomdpereira/demo-CI-github-actions/actions/workflows/main_python_3_12.yml/badge.svg)](https://github.com/tiagomdpereira/demo-CI-github-actions/actions/workflows/main_python_3_12.yml) [![Python 3.11](https://github.com/tiagomdpereira/demo-CI-github-actions/actions/workflows/main_python_3_11.yml/badge.svg)](https://github.com/tiagomdpereira/demo-CI-github-actions/actions/workflows/main_python_3_11.yml)

# Demo CI with GitHub Actions

## Project Overview

This repository is a small Python calculator used to practice core DevOps habits that are essential for MLOps.

The project was created while working through exercises 1 and 2 from Practical MLOps by Noah Gift and Alfredo Deza (O’Reilly, 2021, ISBN 978-1-098-10301-9).

## Why This Project

The objective was to build a simple codebase and apply professional engineering practices around it:

- automated testing
- linting and formatting
- reproducible local setup
- Continuous Integration (CI) validation on two Python versions


## Features

- Basic arithmetic operations: add, subtract, multiply, divide
- Unit tests for normal and edge cases
- Division-by-zero guard with explicit assertion
- CI pipelines for Python 3.11 and 3.12 with GitHub Actions

## Project Structure

- `calculator.py`: calculator functions
- `test_calculator.py`: automated tests with pytest
- `requirements.txt`: development dependencies
- `Makefile`: common development commands

## Local Setup

1. Create a virtual environment.

```bash
python3 -m venv .venv
```

2. Activate the environment.

```bash
source .venv/bin/activate
```

3. Install dependencies.

```bash
make install
```

## Development Commands

Run lint checks:

```bash
make lint
```

Run tests with coverage:

```bash
make test
```

Format Python files:

```bash
make format
```

## CI

GitHub Actions runs linting and tests on Python 3.11 and 3.12 for each change, helping keep the codebase stable and consistent.

## Learning Outcome

This project demonstrates a practical first step from software engineering into MLOps.

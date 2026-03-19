SHELL := /bin/bash

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C calculator.py

test:
	python -m pytest -vv --cov=calculator test_calculator.py

format:
	black *.py


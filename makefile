-include .env

install:
	python -m pip install poetry coverage
	poetry config virtualenvs.create true
	poetry install --no-root

run:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file .env

.PHONY: tests

tests:
	poetry run python -m unittest

cover:
	poetry run coverage run -m unittest
	poetry run coverage report
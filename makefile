-include .env

install:
	python -m pip install poetry
	poetry config virtualenvs.create true
	poetry install --no-root

run:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload

.PHONY: tests

tests:
	poetry run python -m unittest
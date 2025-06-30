-include .env

install:
	python -m pip install poetry
	poetry config virtualenvs.create true
	poetry install --no-root

run:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file .env

.PHONY: tests

tests:
	poetry run python -m unittest tests.unit

integration:
	make run & \
	sleep 1 && \
	poetry run python -m unittest tests.integration && \
	pkill -f "uvicorn main:app"

cover:
	poetry run coverage run -m unittest tests.unit
	poetry run coverage report
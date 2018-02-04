.PHONY: lint test

lint:
	pipenv run flake8

test:
	pipenv run py.test --cov=expynent

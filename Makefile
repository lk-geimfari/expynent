.PHONY: lint test
lint:
	flake8

test:
	pipenv run py.test --cov=expynent
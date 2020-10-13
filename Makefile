install:
	pip install -q -e .[dev]
lint:
	black --config pyproject.toml .

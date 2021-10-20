test:
	mypy src
	mypy tests

	flake8 src
	flake8 tests

	pytest --durations=5

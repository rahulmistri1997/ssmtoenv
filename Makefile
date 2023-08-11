test:
	pytest -v --cov=ssmtoenv --disable-pytest-warnings &&\
		readme-cov

testhtml:
	pytest -v --cov=ssmtoenv --cov-report=html --disable-pytest-warnings &&\
		readme-cov

install:
	poetry install

install-requirements:
	pip install -r requirements.txt

requirements:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

mkdocs-serve:
	mkdocs serve

mkdocs-build:
	mkdocs build

pre-commit-file:
	pre-commit install
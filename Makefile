.PHONY: freeze
# TODO: Maybe update to make everything remove the 3 in python/pip 
# (only damoster dev env has 2 different pythons...and python2 is no longer supported...)
PYTHON=python3
PIP=pip3

# TODO: Get this to work propery
# clean-pyc:
# 	find . -name '*.pyc' -exec rm --force {}
# 	find . -name '*.pyo' -exec rm --force {}

# Running
init:
	$(PIP) install -Ur requirements.txt

run:
	$(PYTHON) main.py

# TODO: Get this to work propery
# # Development
# freeze:
# 	$(PIP) freeze | grep -v "pkg-resources" > requirements.txt

test:
	pytest

lint:
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=env/*
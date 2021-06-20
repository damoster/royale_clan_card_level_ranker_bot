# TODO: Maybe update to make everything remove the 3 in python/pip 
# (only damoster dev env has 2 different pythons...and python2 is no longer supported...)
PYTHON=python3
PIP=pip3

init:
	$(PIP) install -Ur requirements.txt

run:
	$(PYTHON) main.py

test:
	pytest

lint:
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude=env/*
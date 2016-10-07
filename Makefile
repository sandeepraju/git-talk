.PHONY: all clean build install uninstall pylint test push

all: clean

clean:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	find . -name \*~ -delete
	rm -rf dist gittalk.egg-info

build:
	python setup.py sdist

install:
	pip install dist/gittalk-*.tar.gz

uninstall:
	yes | pip uninstall gittalk

pylint: ; @for py in gittalk/*.py; do echo "Linting $$py"; pylint --list-msgs -rn $$py; done

test:
	python -m unittest discover -s ./tests -p 'test_*.py'

push:
	python setup.py sdist upload -r pypi

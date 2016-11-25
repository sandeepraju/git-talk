.PHONY: all clean build install uninstall test upload

all: clean

clean:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	find . -name \*~ -delete
	rm -rf dist git-talk.egg-info

build:
	python setup.py sdist

install:
	pip install dist/git-talk-*.tar.gz

uninstall:
	yes | pip uninstall git-talk

test:
	python -m unittest discover -s ./tests -p 'test_*.py'

upload:
	python setup.py sdist upload -r pypi

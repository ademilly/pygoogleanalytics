# Simple MAKEFILE for python project

VENV=venv
VENV_PYTHON_BIN=venv/bin/python
VENV_PIP_BIN=venv/bin/pip
VENV_PYTEST_BIN=venv/bin/pytest
PACKAGE=pygoogleanalytics

default: run

help:
	@echo "Makefile for $(PACKAGE) python project"
	@echo
	@echo "Following commands are available:"
	@echo "    clean"
	@echo "        Remove python artifacts."
	@echo "    test"
	@echo "        Run py.test"
	@echo "    install"
	@echo "        Setup local virtualenv"

clean:
	rm -f *.pyc $(PACKAGE)/*.pyc tests/*.pyc
	rm -rf $(PACKAGE)/__pycache__ tests/__pycache__

test: clean
	$(VENV_PYTEST_BIN) --verbose --color=yes tests/

install:
	virtualenv venv
	$(VENV_PIP_BIN) install -U google-api-python-client
	$(VENV_PIP_BIN) install -U .

.PHONY: clean

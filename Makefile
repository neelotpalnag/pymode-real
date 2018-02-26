python_version = 3

venv/bin/python$(python_version) venv/bin/pip venv/bin/pserve venv/bin/py.test venv/bin/devpi:
	tox -e develop --notest

clean:
	git clean -fXd

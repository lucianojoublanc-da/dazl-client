pip := .venv/bin/pip
python := .venv/bin/python3
pip-compile := .venv/bin/pip-compile
version := $(shell python3 setup.py --version)


.PHONY: wheel
wheel: dist/dazl_pb-$(version)-py3-none-any.whl

$(python):
	python3 -m venv .venv

$(pip): $(python)

$(pip-compile): $(pip)
	$(pip) install pip-tools

requirements.txt: setup.py
	CUSTOM_COMPILE_COMMAND="make $@" $(pip-compile) --generate-hashes

dist/dazl_pb-$(version)-py3-none-any.whl:
	$(pip) wheel . --no-deps -w dist

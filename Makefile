# Название проекта
project = py_proj
# Папка с тестами
tests = tests

.PHONY: all
all: format verify

.PHONY: format
format: yapf isort

.PHONY: verify
verify: lint test

.PHONY: yapf
yapf:
	yapf -i -r $(project) $(tests)

.PHONY: isort
isort:
	isort -rc $(project) $(tests)

.PHONY: lint
lint:
	flake8 $(project) $(tests)

.PHONY: test
test:
	py.test $(tests) -rw -x --cov $(project) --cov-report html --junit-xml junit.xml

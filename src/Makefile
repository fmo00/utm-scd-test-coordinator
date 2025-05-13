.PHONY: setup
setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip setuptools wheel pip-tools
#.venv/bin/pip-compile --generate-hashes --output-file=requirements.txt requirements.in 
	.venv/bin/pip install -r requirements.txt

.PHONY: run-locally
run-locally:
	.venv/bin/pytest ./tests/test_plan/operational_intent_reference/conflicted_injection.py

.PHONY: format
format:
	.venv/bin/black .
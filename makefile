##CI/CD
ci-setup:
	pip install -r requirements.txt

ci-test:
	python -m pytest
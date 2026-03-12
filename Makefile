.PHONY: test run

test:
	python3 -m unittest discover -s tests -p 'test_*.py' -v

run:
	python3 -m src.app.main

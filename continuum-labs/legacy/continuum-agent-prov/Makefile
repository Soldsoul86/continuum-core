.PHONY: install test clean

install:
	python3 -m pip install --user -r requirements.txt

test:
	python3 -m pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +


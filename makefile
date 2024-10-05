.PHONY: install format lint test

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black .

lint:
	pylint --disable=R,C sql_interaction.py
	pylint --disable=R,C sql_test.py

test:
	pytest sql_test.py
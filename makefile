install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

format:
		black .

lint:
		pylint *.py

test:
		pytest sql_test.py
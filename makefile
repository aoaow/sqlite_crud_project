- name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.12

install:
		pip install --upgrade pip
		pip install -r requirements.txt
		pip install databricks-sql-connector

format:
		black .

test:
	pytest sql_test.py
	pytest test_complex_sql_query.py
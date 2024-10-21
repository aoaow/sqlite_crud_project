from databricks import sql
import os

def connect_db():
    # Get connection details from environment variables or replace with hardcoded values
    server_hostname = os.getenv('DATABRICKS_SERVER_HOSTNAME')
    http_path = os.getenv('DATABRICKS_HTTP_PATH')
    access_token = os.getenv('DATABRICKS_ACCESS_TOKEN')

    try:
        # Establish a connection to Databricks SQL
        conn = sql.connect(
            server_hostname=server_hostname,
            http_path=http_path,
            access_token=access_token
        )
        return conn
    except Exception as e:
        print(f"Error connecting to Databricks: {e}")
        return None

def complex_query(conn):
    cursor = conn.cursor()

    # Complex query to rank the highest salary descendingly by departments
    cursor.execute('''USE my_databse;''')
    cursor.execute('''SELECT d.name as dpt_name, SUM(e.salary) as total_salary
                      FROM employees e LEFT JOIN departments d ON e.dpt_id = d.id
                      GROUP BY d.id
                      ORDER BY total_salary DESC''')
    results = cursor.fetchall()
    for row in results:
        print(row)

    return results

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        complex_query(conn)
        conn.close()

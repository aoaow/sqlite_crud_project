from databricks import sql
import os

def connect_db():
    # Get connection details from environment variables or replace with hardcoded values
    server_hostname = os.getenv('DATABRICKS_SERVER_HOSTNAME', 'https://dbc-c95fb6bf-a65d.cloud.databricks.com')
    http_path = os.getenv('DATABRICKS_HTTP_PATH', '/sql/1.0/warehouses/2d6f41451e6394c0')
    access_token = os.getenv('DATABRICKS_ACCESS_TOKEN', '4f2543799d210db9cfe0c07e634b135653c02539b885ec143f0b2d8374c729c0')

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

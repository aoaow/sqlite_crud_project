from sql_interaction import connect_db

    
def complex_query(conn):
    cursor = conn.cursor()
    # create table 'employees'
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees 
                   (id INTEGER PRIMARY KEY, 
                   name TEXT NOT NULL, 
                   dpt_id INTEGER NOT NULL,
                   salary INTEGER NOT NULL);''')
    # insert employees
    cursor.execute('''INSERT INTO employees (id, name, dpt_id, salary) VALUES 
                   (1, 'Amy', 1, 89000),
                   (2, 'Bob', 1, 70000),
                   (3, 'Cindy', 1, 66000),
                   (4, 'David', 3, 100000),
                   (5, 'Eleanor', 3, 240000),
                   (6, 'Frya', 2, 120000);''')
    # create table "department"
    # records the corresponding departments
    cursor.execute('''CREATE TABLE IF NOT EXISTS departments 
                   (id INTEGER PRIMARY KEY, 
                   name TEXT NOT NULL);''')
    cursor.execute('''INSERT INTO departments (id, name) VALUES 
                   (1, 'marketing'),
                   (2, 'clinical'),
                   (3, 'research');''')
    # complex query to rank the highest salary descendingly by departments
    cursor.execute('''SELECT d.name AS dpt_name, SUM(e.salary) AS total_salary
                   FROM employees e LEFT JOIN departments d ON e.dpt_id=d.id
                   GROUP BY d.id
                   ORDER BY total_salary DESC''')
    # we left join employees and departments to get the department name
    # and then we group by department id so that we could get the department total salaries
    # rank the total salaries by deparment descendingly

    results = cursor.fetchall()
    for row in results:
        print(row)

    conn.commit()

    return results



if __name__ == "__main__":

    conn = connect_db()
    if conn:
        complex_query(conn)
        conn.close()
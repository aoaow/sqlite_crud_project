import unittest
from complex_sql_query import connect_db, complex_query
from dotenv import load_dotenv
import os

class TestComplexQuery(unittest.TestCase):
    def setUp(self):
        # Set up connection
        server_hostname = os.getenv('DATABRICKS_SERVER_HOSTNAME')
        http_path = os.getenv('DATABRICKS_HTTP_PATH')
        access_token = os.getenv('DATABRICKS_ACCESS_TOKEN')
        load_dotenv()
        self.conn = connect_db(server_hostname, http_path, access_token)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the connection after each test
        self.conn.close()

    def test_complex_query(self):
        # Execute the complex query function
        results = complex_query(self.conn)
        # Validate the results
        expected_results = [
            ('research', 340000),
            ('marketing', 225000),
            ('clinical', 120000)
        ]
        self.assertEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
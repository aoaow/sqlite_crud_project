import unittest
from complex_sql_query import connect_db, complex_query
import os

class TestComplexQuery(unittest.TestCase):
    def setUp(self):
        # Set up connection
        # Only load .env locally
        if os.getenv('CI') and not os.getenv('DATABRICKS_ACCESS_TOKEN'):
            self.skipTest("Skipping test: Databricks credentials not available.")
        self.conn = connect_db()
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
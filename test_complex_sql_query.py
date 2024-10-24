import unittest
from unittest.mock import patch, MagicMock
from complex_sql_query import connect_db, complex_query

class TestComplexQuery(unittest.TestCase):
    @patch('complex_sql_query.connect_db')
    def setUp(self, mock_connect_db):
        # Create a mock connection object
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

        # Configure the mock to return our mock connection
        mock_connect_db.return_value = self.mock_conn

        # No need to set up environment variables or actual connection
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the mock connection
        self.conn.close()

    def test_complex_query(self):
        # Set up expected results
        expected_results = [
            ('research', 340000),
            ('marketing', 225000),
            ('clinical', 120000)
        ]

        # Configure the mock cursor to return expected results
        self.mock_cursor.fetchall.return_value = expected_results

        # Execute the complex query function
        results = complex_query(self.conn)

        # Validate the results
        self.assertEqual(results, expected_results)

if __name__ == "__main__":
    unittest.main()

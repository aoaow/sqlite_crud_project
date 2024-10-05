import unittest
from sql_interaction import connect_db, create_table, insert_user, read_users, update_user_age, delete_user

class TestCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up an in-memory database for testing
        cls.conn = connect_db(':memory:')
        create_table(cls.conn)

    @classmethod
    def tearDownClass(cls):
        # Close the connection after all tests are done
        cls.conn.close()

    def test_insert_user(self):
        insert_user(self.conn, "TestUser", 25)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = 'TestUser'")
        user = cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], "TestUser")
        self.assertEqual(user[2], 25)

    def test_update_user_age(self):
        insert_user(self.conn, "UpdateUser", 20)
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM users WHERE name = 'UpdateUser'")
        user_id = cursor.fetchone()[0]
        
        update_user_age(self.conn, user_id, 30)
        cursor.execute("SELECT age FROM users WHERE id = ?", (user_id,))
        new_age = cursor.fetchone()[0]
        self.assertEqual(new_age, 30)

    def test_delete_user(self):
        insert_user(self.conn, "DeleteUser", 40)
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM users WHERE name = 'DeleteUser'")
        user_id = cursor.fetchone()[0]

        delete_user(self.conn, user_id)
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        self.assertIsNone(cursor.fetchone())

    def test_read_users(self):
        insert_user(self.conn, "ReadUser", 28)
        insert_user(self.conn, "ReadUser2", 32)
        users = read_users(self.conn)
        self.assertEqual(len(users), 2)

if __name__ == '__main__':
    unittest.main()


import unittest
from credentials import Cridentials #import credential class

class TestCridentials (unittest.TestCase):

    def setUp(self):
        self.new_credentials =Cridentials ("Facebook","peter_p@gmail.com", "peterpan","12345pp")

    def test_init(self):
        self.assertEqual(self.new_credentials.user_acc,"Facebook")
        self.assertEqual(self.new_credentials.email,"peter_p@gmail.com")
        self.assertEqual(self.new_credentials.username,"peterpan")
        self.assertEqual(self.new_credentials.password,"12345pp")








if __name__ == '__main__':
    unittest.main()
"""
TDD 
- Create an account
     * Args:
          -Username -Password
- Save user account
"""

import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("petermain","P@n_main")

    def tearDown(self):
        User.user_list = [] 

    def test_init(self):
        '''
        Testcase 1 - checks for proper initialization of object.
        '''
        self.assertEqual(self.new_user.username, "petermain")
        self.assertEqual(self.new_user.password, "P@n_main")
        

    #testcase2 save user
    def test_save_user(self):
        self.new_user.save_user()
        test_user = User("petermain","P@n_main")
        test_user.save_user()

    # test3 delete user
    def test_delete_user(self):
        self.new_user.save_user()
        test_user =User("petermain","P@n_main")
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    #test4 find user by usename
    def test_find_by_username(self):
        self.new_user.save_user()
        test_user =User("petermain","P@n_main")
        test_user.save_user()

        found_user = User.find_by_username("petermain")
        self.assertEqual(found_user.username ,test_user.username)


if __name__ == '__main__':
    unittest.main()
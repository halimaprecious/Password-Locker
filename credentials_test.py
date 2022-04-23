"""
TDD 
- Create a credential
     * Args:
        -account name  -Username    -Email    -Password
- Save a credential
- Save more than one credential
- Display credential
- Delete credential  
"""
import unittest
from credentials import Credentials #import credential class

class TestCredentials (unittest.TestCase):

    def setUp(self):
        #new credential object
        self.new_credentials =Credentials ("Facebook","peter_p@gmail.com", "peterpan","12345pp") 

    
    # Teardown mthd resets credential list after every testcase
    def tearDown(self):
        Credentials.credential_list = []    

    def test_init(self):
        '''
        test case for proper initialization of objects
        '''
        self.assertEqual(self.new_credentials.user_acc,"Facebook")
        self.assertEqual(self.new_credentials.email,"peter_p@gmail.com")
        self.assertEqual(self.new_credentials.username,"peterpan")
        self.assertEqual(self.new_credentials.password,"12345pp")


    def test_save_cridential(self):
        '''
        test case to check for saved cridentials.
        '''
        #saving new credential
        self.new_credentials.save_cridentials() 
        self.assertEqual(len(Credentials.credential_list),1)









if __name__ == '__main__':
    unittest.main()
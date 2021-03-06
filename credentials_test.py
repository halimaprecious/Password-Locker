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

    
    # Teardown resets credential list after every testcase
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


    def test_save_credential(self):
        '''
        test case2 to check for saved cridentials.
        '''
        #saving new credential
        self.new_credentials.save_credentials() 
        self.assertEqual(len(Credentials.credential_list),1)

    def test_save_multiple_credentials(self):
        '''Test case3 checks if we can save multiple credentials'''

        self.new_credentials.save_credentials()
        test_credential =Credentials("Instagram","peter_p@gmail.com","peter-pan","P!3t3rp@n")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)


    def test_delete_credentials(self):
        '''
        Test case4 tests if we can delete existing credentials
        '''

        self.new_credentials.save_credentials()
        test_credentials =Credentials("Instagram","peter_p@gmail.com","peterp","P!3t3rp@n")
        test_credentials.save_credentials()
        #Deleting credentials
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_by_username(self):
        '''
        Testcase5:tests to find cridentials by user account 
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram","peter_p@gmail.com","peterp","P!3t3rp@n")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_username("peterp")
        self.assertEqual(found_credentials.username, test_credentials.username)


    def test_credentials_exist(self):
        '''
        Testcase 6- checks if credentials exist
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram","peter_p@gmail.com","peterp","P!3t3rp@n")
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist("Instagram")
        self.assertTrue(credentials_exist)


    def test_display_credentials(self):
        '''
        Testcase 7 - returns all saved credentials
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)



if __name__ == '__main__':
    unittest.main()
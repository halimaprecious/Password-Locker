
class Credentials:
    '''
    Class that generates new instances of user credentials.
    '''

    #new credential
    def __init__(self, user_acc, email ,username, password) :
        self.user_acc = user_acc
        self.email = email
        self.username = username
        self.password = password

    #empty cridential list
    credential_list = []
      
    def save_credentials(self):
        '''
        Saves credentials into cridential_list
        '''
        Credentials.credential_list.append(self)


    def delete_credentials(self):
        '''
        delete method deletes saved credentials
        '''
        Credentials.credential_list.remove(self)


    @classmethod
    def find_by_username(cls,username):
        for user in cls.credential_list:
            if user.username == username:
                return user


    @classmethod
    def credentials_exist(cls,user_acc):
        for account in cls.credential_list:
            if account.user_acc == user_acc:
                return True
        return False


    @classmethod
    def display_credentials(cls):
        return cls.credential_list
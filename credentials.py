
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

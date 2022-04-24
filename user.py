
class User:
    '''
    Class generates new instances of a user
    '''

    user_list = []

    def __init__(self, username ,password ):
        self.username = username
        self.password = password
       

    def save_user(self):
        '''saves new user'''
        User.user_list.append(self)


    def delete_user(self):
        '''Deletes saved user'''
        User.user_list.remove(self)

    
    @classmethod
    def find_by_username(cls,username):
        for user in cls.user_list:
             if user.username == username:
                return user


#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import random 

#generating random password

passwrd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-?/"
passwrd_len = int(input("Enter the length of the password"))
p = " ".join(random.sample(passwrd,passwrd_len))
print(f"Your password is:{p}")


# # User methods
# def create_user(username, password):
#     '''Function to create a new user'''

#     new_user = User(username, password)
#     return new_user

# def save_users(user):
#     '''saves new user'''
#     user.save_user()

# def del_user(user):
#     '''deletes user'''
#     user.delete_user()

# def find_user(username):
#     '''search a user by username'''
#     return User.find_by_username(username)

# def check_existing_user(username):
#     '''search if a user exists'''
#     return User.user_exists(username)

# def display_details():
#     '''Displays user info'''
#     return User.display_details()

# # Credential methods
# def create_credential(user_acc,email,username, password):
#     '''creates new credentials'''
#     new_credentials = Credentials(user_acc,email,username,password)
#     return new_credentials

# def save_credentials(credentials):
#     '''Saves new credentials '''
#     Credentials.save_credentials(credentials)

# def del_credentials(credentials):
#     '''deletes credentials'''
#     Credentials.delete_credentials(credentials)

# def find_credentials(username):
#     '''search a credentials by username'''
#     return Credentials.find_by_username(username)

# def check_existing_credentials(user_acc):
#     '''search if credentials exists'''
#     return Credentials.credentials_exist(user_acc)

# def display_details():
#     '''Displays credentials details'''
#     return Credentials.display_credentials()





# if __name__ == '__main__':

#     main()
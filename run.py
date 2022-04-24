#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import random 

#generating random password
def passwrdgen():
    passwrd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-?/"
    passwrd_len = int(input("Enter the length of the password"))
    p = " ".join(random.sample(passwrd,passwrd_len))
    print(f"Your password is:{p}")


# User methods
def create_user(username, password):
    '''Function to create a new user'''

    new_user = User(username, password)
    return new_user

def save_users(user):
    '''saves new user'''
    user.save_user()

def del_user(user):
    '''deletes user'''
    user.delete_user()

def find_user(username):
    '''search a user by username'''
    return User.find_by_username(username)

def check_existing_user(username):
    '''search if a user exists'''
    return User.user_exists(username)

def display_details():
    '''Displays user info'''
    return User.display_details()

# Credential methods
def create_credential(user_acc,email,username, password):
    '''creates new credentials'''
    new_credentials = Credentials(user_acc,email,username,password)
    return new_credentials

def save_credentials(credentials):
    '''Saves new credentials '''
    Credentials.save_credentials(credentials)

def del_credentials(credentials):
    '''deletes credentials'''
    Credentials.delete_credentials(credentials)

def find_credentials(username):
    '''search a credentials by username'''
    return Credentials.find_by_username(username)

def check_existing_credentials(user_acc):
    '''search if credentials exists'''
    return Credentials.credentials_exist(user_acc)

def display_details():
    '''Displays credentials details'''
    return Credentials.display_credentials()


''' Main function that calls other class methods'''

def main():
    
    print("Welcome to Password Locker!!!")
    print("."*60)
    print("\n")

    while True:
        print("Use these short codes : ca - create a new account, lg - login to your account or ex - to exit")
        print("."*60)
        print("\n")
        short_code = input().lower()
        print("\n")

        if short_code == "ca":
            print("Create username")
            created_username = input()

            print("Create password")
            created_password = input()

            print("Confirm password")
            confirm_password = input()

            while confirm_password != created_password:
                print("Invalid password!")
                print("Enter your password")
                created_password = input()
                print("Confirm password")
                confirm_password = input()




if __name__ == '__main__':

    main()
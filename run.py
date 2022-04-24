#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import random 

#generating random password
def passwrdgen():
    passwrd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-?/"
    passwrd_len = int(input("Enter the length of the password"))
    p = " ".join(random.sample(passwrd,passwrd_len))
    # print(f"Your password is:{p}")
    return p


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

                save_users(create_user(username, password)) 

            else:
                print("\n")
                print(f" Conratulations {created_username}! Account creation  was successful.") 
                print("."*60)

                print("Proceed to login")
                print("."*60)
    
        elif short_code == "lg":
            entered_username = input("Enter username...")
            entered_password = input("Your password...")
            confirm_password = input("Confirm password...")
            print("\n")
            if entered_username != created_username or  entered_password != created_password:

                print("Invalid username or password")
                entered_username = input("Enter username...")
                entered_password = input("Your password...")
                confirm_password = input("Confirm password...")
                print("."*60)
                
            else:
                print(f" Welcome { entered_username} to your Account.") 
                print("."*60)        
            while True:
                print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list")

                short_code = input().lower()
                if short_code == "cc":
                    print("New Credentials")
                    print("."*60)
                    user_acc = input("Enter account type e.g snapchat:... ")
                    email = input("Enter email account used for account registration:... ")
                    username = input("Enter username for account:... ")

                    print(f"Would you like to generate a password for your {user_acc} account? yes or no")
                    response = input().lower()
                    if response == "yes":
                        password =(passwrdgen())
                        print("."*60)
                        print(f" your password is: {password}")

                        save_credentials(create_credential(user_acc,email,username, password))

                    elif response == "no":
                        passwrd_len = int(input("Enter the length of the password:..."))
                        password = input("Enter password for the account:... ")
                    
                        save_credentials(create_credential(user_acc,email,username, password))
                        print("\n")
                        print(f"Your {user_acc} account credentials have been saved.") 
                    else:
                        print("."*60)

                elif short_code == "dc":
                    if display_details():
                        print("Your saved credentials: ")
                        print("."*60)
                        for credentials in Credentials.credential_list:
                            print(f"Account: {user_acc} , Email: {email} , Username: {username} , Password: {password}")

                        print("."*60)
                        print(" Would you like to delete credentials? yes or no")
                        response = input().lower()
                        if response == "yes":
                            del_credentials(credentials)
                            print("Credentials deleted successfully")
                        elif response == "no":
                            print("Deletion cancelled.")
                        else:
                             print("."*60)
                    else:
                        print("No credentials found")
                        print("."*60)

                elif short_code == "fc":
                        find = input("Enter account name you are trying to find: ").lower()
                        if find_credentials(username):
                            find = find_credentials(username)
                            print("."*60)
                            print(f"Account:{find.user_acc}, Username:{find.username},Email:{find.email}, Password:{find.password}")
                            print("."*60)

                        else:
                            print("Credentials do not exist")


                elif short_code == "ex":
                            print("Have a lovely Day")
                            break
                        
                else:
                            print("I really didn't get that. Please use the short codes")
                        

if __name__ == '__main__':
    main()
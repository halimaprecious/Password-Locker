# Password Locker

## Built By 
Halima Precious

## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./run.py** | Welcome, choose an option: ca-Create Account, lg-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: lg** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Exit application | **Enter: ex** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* pyperclip
* xclip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/halimaprecious/Password-Locker.git
        $ cd Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x password_locker.py
        $ ./run.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.9 user_test.py
        $ python3.9 credentials_test.py
        
## Technologies Used
* Python3.9

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 **Precious Halima**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
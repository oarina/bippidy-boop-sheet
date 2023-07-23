# --------------------------1---------------------SECTION THAT LINKS PY AND SHEET 

# !!! Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread #imports intire gspread library
from google.oauth2.service_account import Credentials
# imports the credentials class which is part of service accont functions

# Now we need to set our scope - it is what the user has access to
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# SCOPE is a constant meaning it's a variable that will not change!
"""
 This variable is a list that defines the set of permissions (scopes)
  the application is requesting. The scopes determine what actions the 
  application can perform when accessing Google Sheets and Google Drive.
"""

CREDS = Credentials.from_service_account_file('creds.json')

"""
CREDS = Credentials.from_service_account_file('creds.json'): 
This line creates a Credentials object using the service account 
file (creds.json). The service account file contains the necessary 
credentials and information to authenticate the application.
"""

SCOPED_CREDS = CREDS.with_scopes(SCOPE)

"""
SCOPED_CREDS = CREDS.with_scopes(SCOPE): This line creates a new 
Credentials object (SCOPED_CREDS) based on the original credentials 
(CREDS) but with the specified scopes (SCOPE). The with_scopes method 
is used to add the requested scopes to the credentials.

"""
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

"""
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS): 
This line authorizes the gspread client with the scoped credentials 
(SCOPED_CREDS). It creates an instance of the gspread client that can 
interact with Google Sheets using the provided credentials and scopes.
"""

SHEET = GSPREAD_CLIENT.open('bippidy_boop_sheet')

"""
SHEET = GSPREAD_CLIENT.open('bippidy_boop_sheet'): This line opens 
the Google Sheet named 'bippidy_boop_sheet' using the authorized 
gspread client (GSPREAD_CLIENT). The open method allows you to access 
a specific Google Sheet by its title.
"""


bippidy = SHEET.worksheet('bippidy')
# bippidy is actually a first tab in the linked sheet: 
# https://docs.google.com/spreadsheets/d/1SB1IVrH-dtkq-SUiHCtJOxlckCZPszbmLZ-SuvRS6V4/edit#gid=0

# --------------------------2---------------------SECTION THAT WORKS WITH LINKED TATA

def characters_background_fill():

'''
function to fill the space in the terminal that is 24 characters long and 80 characters wide

Reason: want to see how it would look like.
'''
    characters ="*" 
    rows = 24 // len(characters)
    columns = 80

    for i in range(rows):
        print(characters * columns)

characters_background_fill()

'''
def print_I_in_columns():
    characters = "/"
    rows = 24 // len(characters)  # Calculate how many "I" characters fit in each row
    columns = 80

    for i in range(rows):
        print(characters * columns)

# Example usage:
print_I_in_columns()
'''
# attempt at getting a user name . did not work so far
def get_user_name(prompt):
    return input(prompt)

def greet_user(user_name):
    print(f"Sup {user_name}. Welcome aboard!")

print("Hello there ✋🏻! What is your name?")
user_name = get_user_name("")
greet_user(user_name)

data = bippidy.get_all_values() # we calling all data from the sheet
print(data) # printing all data
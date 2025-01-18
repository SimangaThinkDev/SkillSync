import pyrebase
import time
from key import firebase
from database import update_dashboard


"""
Create an Authentication Object
"""

def authenticate_email():
    """
    Authentication of email
    """

    auth = firebase.auth()

    print("WELCOME TO LOGIN PAGE\n\n")
    time.sleep(1.5)
    email = input("Enter your Username: ")
    password = input("Enter your password: ")
    try:
        auth.sign_in_with_email_and_password(email, password)
        print(f"Welcome back to Skillsync {email}"), update_dashboard()
    except:
        print("Account or Email does not exist")

def create_account():
    """
    Email Sign-Up
    """
    print("WELCOME TO SIGN UP PAGE\n\n")
    auth = firebase.auth()
    time.sleep(1.5)
    
    while True:
        email = input("Enter your Username: ")
        password = input("Enter your password: ")
        confirm = input("Confirm your password: ")
        if password == confirm:
            auth.create_user_with_email_and_password(email, password)
            print("\nYou have been signed up")
            print(f"Welcome to SkillSync {email}")
            break
        else:
            print("Passwords do not match\nTry Again\n")
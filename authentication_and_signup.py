import pyrebase
import time
from key import firebase
from database import update_dashboard, add_user_to_db


def role_picker():

    roles = ["Student", "Mentor"]

    for i, each_role in enumerate(roles):
        print(i+1, each_role)
    
    while True:
        try:
            choice = (int(input("\nPlease Select role: ")) - 1)
            break
        except:
            print("Please enter a Valid Role Number")
    
    return roles[choice]


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
        print(f"Welcome back to Skillsync {email}\n")
        
        
        print("How can we help you?")
        dashboard_options = ["Update my information"]
        [print(i+1, option) for i, option in enumerate(dashboard_options)]
        choice = int(input("Choose: ")) -1
        while True:
            if dashboard_options[choice] == "Update my information":
                update_dashboard()
            elif choice + 1 == 0:
                print("Thanks for visiting SkillSync, Pay Us a Visit again soon")

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
        name = input("Name(s): ").title()
        surname = input("Surname: ").title()
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        confirm = input("Confirm your password: ")
        age = int(input("Age: "))
        print()
        [print(i + 1) for i, campus in enumerate(["cpt", "jhb"])]
        camp_choice = int(input("Select your campus: "))
        role = role_picker()
        if password == confirm:
            auth.create_user_with_email_and_password(email, password)
            print("\nYou have been signed up")
            print(f"Welcome to SkillSync {email}\n")
            break
        else:
            print("Passwords do not match\nTry Again\n")
    
    signup_dict = {
        "Name(s)": name,
        "Surname": surname,
        "Email": email, 
        "Age": age,
        "Role": role,
        "Campus": camp_choice
    }

    # add the data to the firebase database
    add_user_to_db(signup_dict)
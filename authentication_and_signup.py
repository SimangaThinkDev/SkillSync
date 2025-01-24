from database import *
from dashboard import dashboard
from tools import *
from create_events import create_event
from calendar_1 import initiate_calendar
from get_events import print_events, get_events
# "👽👾🤖🎃🫶🏾🧠🫂🙇‍♂️👨‍🍼👊👑🚧📥📤🐙🐝🐐"

def role_picker():

    roles = ["Student", "Mentor"]

    print("\nRoles:")
    [print("    ", i + 1, each_role) for i, each_role in enumerate(roles)]
    
    while True:
        try:
            choice = (int(input("Please Select role: ")) - 1)
            break
        except:
            print("Please enter a Valid Role Number")
    
    return roles[choice]


"""
Create an Authentication Object
"""

auth = firebase.auth()
def authenticate_email():
    """
    Authentication of email
    """


    print("WELCOME TO LOGIN PAGE\n\n")
    time.sleep(1.5)
    email = input("Enter your Username: ")
    password = pwinput("Enter your password: ")

    clear()
    try:
        auth.sign_in_with_email_and_password(email, password)
        print(f"Welcome back to Skillsync {email}\n")
        login_console(email, password)
    except:
        print("Wrong Email or Password, Sign Up Maybe?")
        print("\nRedirecting to Home Page\n")
        clear()
        dashboard()


def login_console(sign_in_info):
    email, password = sign_in_info

    print("How can we help you?")
    dashboard_options = ["Update my information", "Make Bookings", "View Bookings", "Exit"]
    [print(i+1, option) for i, option in enumerate(dashboard_options)]
    while True:
        try:
            choice = int(input("Choose: [0 to exit]")) -1
            break
        except ValueError:
            print("Please enter a valid option: ")
            authenticate_email()
    clear()
    if dashboard_options[choice] == "Update my information":
        update_dashboard()
    elif dashboard_options[choice] == "Make Bookings":
        print("\n\nWelcome to the Bookings Console")
        create_event(initiate_calendar(), get_events(initiate_calendar()))
    elif dashboard_options[choice] == "View Bookings":
        print("\n\nWelcome to the Bookings Console")
        print_events(initiate_calendar())

    elif dashboard_options[choice] == "Exit":
        print("Thanks for visiting SkillSync, Pay Us a Visit again soon")
        print("🫂 Thanks Bye 🫂")
        time.sleep(1.5)
        clear()
        sys.exit()
    else:
        print("Invalid Input ")
        login_console()

    dashboard()
        




def create_account():
    """
    Email Sign-Up
    """
    print("\n\nWELCOME TO SIGN UP PAGE\n\n")
    time.sleep(1.5)

    while True:
        name = input("Name(s): ").title()
        surname = input("Surname: ").title()
        email = input("Enter your email: ")
        password = pwinput("Enter your password: ")
        confirm = pwinput("Confirm your password: ")
        age = int(input("Age: "))
        print()
        print("Possible Campuses:")
        campuses = ["JHB", "CPT"]
        [print("    ", i + 1, campus) for i, campus in enumerate(campuses)]
        camp_choice = int(input("Select your campus: ")) - 1
        camp_choice = campuses[camp_choice]
        role = role_picker()
        clear()
        if password == confirm and is_password_secure(password):
            auth.create_user_with_email_and_password(email, password)
            print("\nYou have been signed up")
            print(f"🫂  Welcome to SkillSync Mr/Mrs {surname} 🫂\nYour new username is: {email.split("@")[0]}\n")
            break
        else:
            print("Passwords do not match or Password is not strong enough\nTrying Again")
            create_account()

    signup_dict = {
        "Name(s)": name,
        "Surname": surname,
        "Email": email, 
        "Age": age,
        "Role": role,
        "Campus": camp_choice,
        "Email" : email
    }

    # add the data to the firebase database
    add_user_to_db(signup_dict)
    dashboard()
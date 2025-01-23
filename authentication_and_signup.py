from database import update_dashboard, add_user_to_db
from dashboard import dashboard
from tools import *
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

def authenticate_email():
    """
    Authentication of email
    """

    auth = firebase.auth()

    print("WELCOME TO LOGIN PAGE\n\n")
    time.sleep(1.5)
    email = input("Enter your Username: ")
    password = pwinput("Enter your password: ")
    clear()
    try:
        auth.sign_in_with_email_and_password(email, password)

    except:
        print("Wrong Email or Password, Sign Up Maybe?")
        print("\nRedirecting to Home Page\n")
        clear()
        # dashboard()


    print(f"Welcome back to Skillsync {email}\n")
    print("How can we help you?")
    dashboard_options = ["Update my information", "Make Bookings", "Exit"]
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
    elif dashboard_options[choice] == "Bookings":
        print("\n\nWelcome to the Bookings Console")
        # TODO: This whole code block
        if "s" == "Student":
            print("This is All of your booked sessions:")
            # TODO: Use The Google cal api here
        else:
            print("This is all the sessions you've been booked for:")
                # TODO: Use The google cal api here aswell
    elif dashboard_options[choice] == "Exit":
        print("Thanks for visiting SkillSync, Pay Us a Visit again soon")
        sys.exit()
    else:
        print("Invalid Input ")

    dashboard()
        




def create_account():
    """
    Email Sign-Up
    """
    print("\n\nWELCOME TO SIGN UP PAGE\n\n")
    auth = firebase.auth()
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
        "Campus": camp_choice
    }

    # add the data to the firebase database
    add_user_to_db(signup_dict)
    dashboard()
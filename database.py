from tools import *
db = firebase.database()

def role_picker():

    roles = ["Student", "Mentor"]

    print("\nRoles:")
    [print("    ", i + 1, each_role) for i, each_role in enumerate(roles)]
    
    while True:
        try:
            choice = (click.prompt("Please Select role: ", type=int)) - 1
            break
        except:
            print("Please enter a Valid Role Number")
    
    return roles[choice]


"""
Create an Authentication Object
"""

auth = firebase.auth()
def authenticate_user():
    """
    Authentication of email
    """


    echo("WELCOME TO LOGIN PAGE\n\n")
    time.sleep(1.5)
    email = click.prompt("Email: ", type=str)
    password = click.prompt("Password: ", hide_input=True)

    clear()
    from Home import main
    try:
        auth.sign_in_with_email_and_password(email, password)
        echo(f"Welcome back to Skillsync {email.split("@")[0]}\n")
        time.sleep(3)
    except:
        echo("Wrong Email or Password, Sign Up Maybe?")
        echo("\nRedirecting to Home Page\n")
        time.sleep(3)
        clear()
    
    main()


def add_user_to_db(data:dict):

    email = data["Email"]
    role = data["Role"]

    mail_name = email.split("@")[0]

    db.child(f"{role}s").child(f"{role} id> {mail_name}").set(data)

def create_account():
    """
    Email Sign-Up
    """
    time.sleep(1.5)

    while True:
        name = click.prompt("Name: ").title()
        email = click.prompt("Email: ")
        age = click.prompt("Age: ", type=int)
        echo()
        
        role = role_picker()
        password = click.prompt("Password: ", hide_input=True)
        confirm = click.prompt("Confirm: ", hide_input=True)
        clear()
        if password == confirm:
            auth.create_user_with_email_and_password(email, password)
            echo("\nYou have been signed up")
            echo(f"🫂  Welcome to SkillSync {name} 🫂\nYour new username is: {email.split("@")[0]}\n")
            break
        else:
            echo("Passwords do not match")
            create_account()

    signup_dict = {
        "Name(s)": name,
        "Email": email, 
        "Age": age,
        "Role": role,
        "Email" : email
    }

    # add the data to the firebase database
    add_user_to_db(signup_dict)

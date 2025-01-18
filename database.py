import pyrebase
from key import firebase
import time

"""
DataBase
"""

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



def add_user_to_db(data:dict):
    db = firebase.database()

    email = data["Email"]
    role = data["Role"]

    mail_name = email.split("@")[0]

    db.child(f"{role}s").child(f"{role} id> {mail_name}").set(data)


def update_dashboard():

    user_id = input("Enter User Id, type 0 if forgotten: ")
    if user_id.strip() == "0":
        print("BRAIN ERROR: 🧠Brain Not Found")
        time.sleep(1)
        print("mxm, why you forget the id tho!\n Worry not I'm here for you ")
        email = input("Enter Email [🙏, may it be correct]: ")
        user_id = email.split("@")[0]
        print("Make sure you don't forget again cause I don't have the time for this")
        print("Your user id is:",user_id)
        update_dashboard()
        #TODO: Validate if the user ID really exists
    # 



    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() == "yes":
        update_db(user_id)
    else:
        print("🫶🏾 Thank you for using SkillSync 🫶🏾")
        return


def update_db(user_id):
    db = firebase.database()

    role = role_picker()

    print("What would you like to update: \n")
    values = ["Name", "Surname", "Age", "Role"]

    [print(i+1, value) for i, value in enumerate(values)]

    choice = int(input("\nchoose: ")) - 1
    new_data = input(f"Enter new {values[choice]} ")
    db.child(f"{role}s").child(f"{role} id> {user_id}").update({values[choice]: new_data})
    print("Information Updated Successfully")



def main():
    update_dashboard()
    pass

if __name__ == "__main__":
    main()
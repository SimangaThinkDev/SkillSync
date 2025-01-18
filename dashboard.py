import time
import authentication_and_signup

def dashboard():

    time.sleep(1.5)
    print("\nSKILLSYNC")

    opts = ["Log in", "Sign Up", "Exit"]
    for i, opt in enumerate(opts):
        print(i + 1, opt)
    while True:
        try:
            choice = int(input("Select what you would like to do: ")) -1
            break
        except ValueError:
            print("Please Enter A Valid Option")
    time.sleep(1.5)

    if opts[choice] == "Log in":
        authentication_and_signup.authenticate_email()
    elif opts[choice] == "Sign Up":
        authentication_and_signup.create_account()
    elif opts[choice] == "Exit":
        print("🫂 Thanks Bye 🫂")
    else:
        print("🙇‍♂️ Enter valid option 🙇‍♂️")




def main():
    print("WELCOME TO SKILLSYNC\n")
    dashboard()

if __name__ == "__main__":
    main()
import time
import app

def dashboard():

    print("WELCOME TO SKILLSYNC\n\n")
    time.sleep(1.5)
    print("SKILLSYNC")

    opts = ["Log in", "Sign Up"]
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
        app.authenticate_email()
    elif opts[choice] == "Sign Up":
        app.create_account()
    else:
        print("Enter valid option")




def main():
    dashboard()
    app

if __name__ == "__main__":
    main()
from tools import *
from database import *

def login():
    
    echo("""
Choose One:
1. Log In
2. Sign Up
""")
    choice = click.prompt(">", type=int)
    
    if choice ==  1:
        authenticate_user()
    elif choice == 2:
        create_account()
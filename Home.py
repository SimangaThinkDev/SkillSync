# Hello, And Welcome to the CPU of my code

import click
from click import echo # To reduce redundancy


@click.command()
def main():
    
    click.echo("""
\nOPTIONS:
1. Login
2. View Workshops
3. Request Meeting
4. View Bookings
5. Cancel Booking
""")
    
    choice = click.prompt(">", type=int)
    echo(f"You have chosen {choice}.")
    
    if choice == 1:
        login()
    elif choice ==  2:
        view_workshops()
    elif choice ==  3: 
        request_meeting()
    elif choice == 4:
        view_bookings()
    elif choice == 5:
        cancel_booking()
    else:
        echo("Invalid choice, Input should be between [1-5]")
        main()

if __name__ == "__main__":
    echo("WELCOME TO SKILLSYNC")
    main()
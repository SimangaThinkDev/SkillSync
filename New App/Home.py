# Hello, And Welcome to the CPU of my code

import click
from click import echo # To reduce redundancy


@click.command()
def main():
    
    click.echo("""
WELCOME TO SKILLSYNC
\nOPTIONS:
1. Login
2. View Workshops
3. Request Meeting
4. View Bookings
5. Cancel Booking
""")
    
    choice = click.prompt(">", type=int)
    echo(f"You have chosen {choice}.")
    
if __name__ == "__main__":
    main()
    

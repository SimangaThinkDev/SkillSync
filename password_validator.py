import string

def is_password_secure(password):

    ratings, length, upper, lower, special, numbers = 0,0,0,0,0,0

    if len(password) >= 8:
        length = True
    
    for char in password:
        if str(char) in string.digits:
            numbers = True
        elif char in string.ascii_uppercase:
            upper = True
        elif char in string.ascii_lowercase:
            lower = True
        elif char in string.punctuation:
            special = True
    
    if numbers is True and length is True and upper is True and lower is True and special is True:
        return True
    else:
        return False
import re
import getpass

def check_policy(password):
    expr = re.compile('(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%&])[\S]{8,}')
    result = expr.match(password)
    if result is not None:
        return True
    else:
        return False

password = getpass.getpass("Enter your password: ")
if (check_policy(password)):
    print('password matches')
else:
    print('password does not match')
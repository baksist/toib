import re

def check_policy(password):
    expr = re.compile('(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%&])[\S]{8,}')
    result = expr.match(password)
    if result is not None:
        return True
    else:
        return False

with open('./passwords.lst') as passlist:
    passwords = passlist.read().splitlines()
    
for current_pass in passwords:
    if (check_policy(current_pass)):
        print(f'password {current_pass} matches')
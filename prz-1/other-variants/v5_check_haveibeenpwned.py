import requests
import hashlib

def api_call(credential):
    [ username, password ] = credential.split(',')
    pass_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    hash_prefix = pass_hash[:5]
    r = requests.get(f'https://api.pwnedpasswords.com/range/{hash_prefix}')
    results = r.text
    for line in results.split('\r\n'):
        hash_suffix = line.split(':')[0]
        hash_counter = line.split(':')[1]
        if pass_hash == hash_prefix + hash_suffix:
            result = f'Hit! Password {password} of user {username} been pwned {hash_counter} times'
            return result
    result = f'Password {password} hasn\'t been pwned, user {username} is safe'
    return result

with open('./credentials.lst') as file:
    creds = file.read().splitlines()
    
for current_user in creds:
    print(api_call(current_user))
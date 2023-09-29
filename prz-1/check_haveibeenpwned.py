import requests
import hashlib

def api_call(password):
    pass_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    hash_prefix = pass_hash[:5]
    r = requests.get(f'https://api.pwnedpasswords.com/range/{hash_prefix}')
    results = r.text
    for line in results.split('\r\n'):
        hash_suffix = line.split(':')[0]
        hash_counter = line.split(':')[1]
        if pass_hash == hash_prefix + hash_suffix:
            result = f'Hit! Password {password} been pwned {hash_counter} times'
            return result
    result = f'Password {password} hasn\'t been pwned'
    return result

with open('./passwords.lst') as passlist:
    passwords = passlist.read().splitlines()
    
for current_pass in passwords:
    print(api_call(current_pass))
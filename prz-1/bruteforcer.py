import string
import itertools

alphabet = [*(string.ascii_lowercase)]

password = input("Enter lowercase ascii password to bruteforce: ")

combinations = list(itertools.permutations(alphabet, len(password)))
wordlist = []
for combo in combinations:
    wordlist.append(''.join(combo))

for item in wordlist:
    print(f'Trying {item}...')
    if item == password:
        print(f'Success! Password is indeed {item}')
        break
# collect user preferences for the password
# Get a length of the password for user
# Ensure that it contains special digits
# Allow for it to contain capital letters
# Allow for it to contain normal digits.

# get all available characters for the password
# randomly select them so that they fit into the length of the password
# Ensure we have at least one of each character type
# Double check length with the criteria to see if it's valid

import random
import string #Gives access to all characters that are lowercase, uppercase, digits or special

def gen_password():
    length = int(input("Give a length to your password: "))
    include_upper = input("Would you like to include uppercase for the password? (Y/N): ").strip().lower()
    include_special = input("Would you like to include special digits for the password? (Y/N): ").strip().lower()
    include_digits = input("Would you like to include digits for the password? (Y/N): ").strip().lower()
    
    if length < 5:
        print("Password length must be at least 5 characters long.")
        return
    # This gives a string of all lowercase letters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_upper == 'y' else ''
    spec = string.punctuation if include_special == 'y' else ''
    digits = string.digits if include_digits == 'y' else ''
    chars = lower + upper + spec + digits
    
    req_chars = []
    if upper:
        req_chars.append(random.choice(upper))
    if spec:
        req_chars.append(random.choice(spec))
    if digits:
        req_chars.append(random.choice(digits))
        
    remaining_len = length - len(req_chars)
    for _ in range(remaining_len):
        req_chars.append(random.choice(chars))
    
    random.shuffle(req_chars)
    password = ''.join(req_chars)
    print(password)
    
gen_password()
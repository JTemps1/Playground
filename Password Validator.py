'''
Simple password validator program that will ask the user for a password, 
then check if it obeys the following conditions:
- Must be between 5 and 10 characters long
- Must not contain spaces
- Must contain at least one number
- Must contain at least one special character
'''
import string

caps = list(string.ascii_uppercase)
letters = list(string.ascii_lowercase)
ints = list(map(str, range(10)))
password = input('Password: ')

if len(password) > 10:
    print('Password too long.\n')
elif len(password) < 5:
    print('Password too short.\n')
elif password.count(' ') != 0:
    print('Password must not contain spaces.\n')
else:
    integers = 0
    capitals = 0
    specials = 0
    for char in password:
        if char in ints:
            integers += 1
            
        elif char in caps:
            capitals += 1
            
        elif char not in letters:
            specials += 1
        
        else:
            pass
    
    if integers == 0:
        print('Password must contain at least one number.\n')
    elif capitals == 0:
        print('Password must contain at least one upper case letter.\n')
    elif specials == 0:
        print('Password must contain at least one special character.\n')
    else:
        print('Password valid!\n')
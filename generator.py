import random
from os import system, name

def clear():
    #This allows for the screen to be cleared during first iteration
    #and works for both Windows and mac/linux
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def shuffle(tempList):
    #Shuffles and joins list of characters into a string
    random.shuffle(tempList)
    tempList.insert(0,chr(random.randint(97,122)))
    return "".join(tempList)

password = []
clear()
print('Welcome to the Secure Random Password Generator!\n')
print('What type of password do you want to generate?\n')
while True:
    print('Type "Normal" for a 9-character password.')
    print('Type "Secure" for a 13-character password')
    pw_type = input()

    if pw_type == 'Normal' or pw_type == 'normal':
        char_amt = 2
        break
    elif pw_type == 'Secure' or pw_type == 'secure':
        char_amt = 3
        break
    else:
        print('Invalid choice, please try again')

#Generates the characters
for num in range(char_amt):
    password.append(chr(random.randint(65,90))) # Uppercase
    password.append(chr(random.randint(97,122))) # Lowercase
    password.append(chr(random.randint(48,57))) # Numbers
    password.append(chr(random.randint(33,46))) # Special

password = shuffle(password)

print(f'\nYour Password is: {password}')

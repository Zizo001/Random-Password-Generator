"""
Author:         Zeyad E
Description:    random password generator that uses characters, numbers, and symbols
Last Modified:  6/9/2021
"""
import random
import string
import pyperclip    #external library used to copy/paste to clipboard

def randomPassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation  #characters will consist of letters,numbers, and symbols
    return ''.join(random.choice(characters) for i in range(length))        #creates a string of characters that is as long as the chosen length by the user

print("""---------------------------------------------------------------
|     Hi there, welcome to Z's random password generator!     |
|        How long you would like your password to be?         |
| Please keep in mind that it must be at least 12 characters  |
---------------------------------------------------------------\n""")
print('Password length: ', end='')

while True:     #checks if length is long enough. If less than 12, ask the user again
    passwordLength = int(input())
    if passwordLength >= 12:
        break
    print("ERROR: password is too short. Please try again\n")
    print('Password length: ', end='')

generatedPassword = randomPassword((passwordLength))    #generate the password and assign it to the variable
print("\nYour secure random password is:")
print(generatedPassword)                                #can be commented out for security concerns (i.e. password visible on screen)
pyperclip.copy(generatedPassword)                       #copies the password to clipboard
print("\nThe password has been copied to your clipboard. Enjoy")


#Todo
'''
Ensure length input is an integer, otherwise ask the user again
Ask the user if they would like the password to be copied to their clipboard
GUI
'''
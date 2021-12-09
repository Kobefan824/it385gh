#!/usr/bin/env python3
testPassword = 'goodPasswprd007!'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upperCaseTest = False
SpecialCharacters = ['$','@', '!', '#', '%', '&', '*']

for t in testPassword:
    if t in UPPERCASE:
        upperCaseTest = True
        break

if upperCaseTest == True:
    print('Your Password Passed the Uppercase Test')
else:
    print('Your Password FAILED the Uppercase Test')
if len(testPassword) < 8: 
    print ('Your Password Failed the character Test')
else:
    print('Your Password Passed the Character Test')
if any(char.isdigit()for char in testPassword):
    print ('Your Password Passed the Number Test')
else: 
    print ('Your Password Failed the Number Test')
if any(char.islower()for char in testPassword):
    print ('Your Password Passed the lowercase Test')
else:
    print ('Your Password Failed the lowercase Test')
if any(char in SpecialCharacters for char in testPassword):
    print('Your Password Passed the Special Character Test')
else:
    print('Your Password Failed the Special Character Test')

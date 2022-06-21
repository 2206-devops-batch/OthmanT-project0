from operator import length_hint
import re
import string
import random

def createPassword():
    sp_ch = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    print('Do you want us to generate a password for you, Y/N. Enter Y if yes other wise N: ')
    choose = input()
    if choose in ['n', 'N', 'no', 'No', 'NO']:
        while True:
            password=input('Please Enter your password: ')
            password2=input('Confirm your password: ')
            if ( sp_ch.search(password) != None) :
                if len(password) < 8:
                    print('Your password is too short')
                elif password != password2:
                    print('Please confirm your password Again')
                else:
                    return password 
            else:
                print('The password must contain at least three character like: [@_!#$%^&*()<>?/\|}{~:]')
    else :
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        length = int(input('Please Enter the length of you password (it should contain more 8 characters: )'))
        temp = random.sample(characters,length)
        password = "".join(temp)
        while True:
            if len(password) < 8:
                print('Your password is too short')
            else :
                print('This is your password, do you like it : '+ password + 'Please answer Y/N. Enter Y if yes other wise N: ')
                YesOrNo = input()
                if YesOrNo in ['n', 'N', 'no', 'No', 'NO']:
                    print('Please Enter your Own Password')
                    return createPassword()
                else :
                    return password
            
            
            

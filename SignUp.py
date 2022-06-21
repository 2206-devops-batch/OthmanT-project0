from createUsername import *
from createPassword import *
from AddAccount import *



def SignUp():
    user_name=createUsername()
    password=createPassword()
    AddAccount('Register.csv', user_name, password)
    print("User has been created succesfully !!")
    


#SignUp()
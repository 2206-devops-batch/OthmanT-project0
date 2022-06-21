from AddAccount import *
from createUsername import *
from createPassword import *

def store_data():
    user_name=createUsername()
    password=createPassword()
    AddAccount('Register.csv', user_name, password)
import csv  
import pandas as pd

def createUsername():
    column_names = ["User_Name", "Password"]
    data = pd.read_csv('Register.csv', names=column_names)
    Name_list = data["User_Name"].tolist()
    while True:
        user_name=input('Please Enter a user name: ')
        if user_name in Name_list:
            print("This user name is used by another user, Please Enter a new User name: ")
        else:
            return user_name  
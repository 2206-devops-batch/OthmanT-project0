import pandas as pd

df = pd.read_csv('./Register.csv')

user_name = df['user_name']
password = df['password']

def RetrievePassword():
    User = input('Please Enter your User name: ')
    if User in user_name.values :
        print(df.loc[df['user_name'] == User])
    else :
        print("The user is not exist")
        
#RetrievePassword()
        
        
        

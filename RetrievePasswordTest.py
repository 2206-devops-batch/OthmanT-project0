import pandas as pd

df = pd.read_csv('./Register.csv',index_col=False)

user_name = df['user_name']
password = df['password']

def RetrievePasswordTest(User):
    #User = input('Please Enter your User name: ')
    if User in user_name.values :
        passd = df.loc[df['user_name'] == User]
        passd = str(passd['password'].values)
        return passd
    else :
        print("The user is not exist")
        
#RetrievePasswordTest("Othman")
        
        
        

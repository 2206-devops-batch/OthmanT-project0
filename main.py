from SignUp import *
from SignIn import *
from RetrievePassword import *

user = int(input("Enter 1 if you want to Sign in Or Enter 2 if you want to Retrieve your password, Otherwise We will sign you up: "))
if user == 1 :
    if __name__ == '__main__':
       SignIn()
elif user == 2 :
    if __name__ == '__main__':
           RetrievePassword()
else :
    if __name__ == '__main__':
        SignUp()

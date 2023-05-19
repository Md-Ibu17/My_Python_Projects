#logic
'''
1) Ask user if they want to generate password or not
2) If yes, ask for the length of the password
3) generate password
4) print password
5) If No, exit the program 
'''
import string
import random

character = list(string.ascii_letters+string.digits+"!@#$%^&*()")

def random_password_generator():
    password_length = int(input("Enter the length of the password: "))
    random.shuffle(character)
    password=[]
    for i in range(password_length):
        password.append(random.choice(character))
    random.shuffle(character)
    password="".join(password)
    print(password)

choose = input("Do you want to generate password? (Yes/No): ")
if choose == "Yes" or choose=="yes":
    random_password_generator()
elif choose =="No" or choose=="no":
    print("Program Ended!!")
    quit()
else:
    print("Invalid input Enter the Yes/No!!")
    quit()

def addition(num1,num2):
    result=num1+num2
    print("Addition: "+str(num1) +"+"+ str(num2)+"="+str(result))

def subtraction(num1,num2):
    result=num1-num2
    print("Subtraction: "+str(num1) +"-"+ str(num2)+"="+str(result))

def multiplication(num1,num2):
    result=num1*num2
    print("Multiplication: "+str(num1) +"*"+ str(num2)+"="+str(result))

def division(num1,num2):
    result=num1/num2
    print("Division: "+str(num1) +"/"+ str(num2)+"="+str(result))

def modulus(num1,num2):
    result=num1%num2
    print("Remainder: "+str(num1)+"%"+str(num2)+"="+str(result))


while True:
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Modulus")
    choice=int(input("Enter the choice: "))

    if choice==1:
        num1=int(input("Enter the 1st number: "))
        num2=int(input("Enter the 2nd number: "))
        addition(num1,num2)
    elif choice==2:
        num1=int(input("Enter the 1st number: "))
        num2=int(input("Enter the 2nd number: "))
        subtraction(num1,num2)
    elif choice==3:
        num1=int(input("Enter the 1st number: "))
        num2=int(input("Enter the 2nd number: "))
        multiplication(num1,num2)
    elif choice==4:
        num1=int(input("Enter the 1st number: "))
        num2=int(input("Enter the 2nd number: "))
        division(num1,num2)
    elif choice==5:
        num1=int(input("Enter the 1st number: "))
        num2=int(input("Enter the 2nd number: "))
        modulus(num1,num2)
    else:
        print("Enter the valid number!!")
        break
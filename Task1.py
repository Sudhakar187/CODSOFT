print("Calculator ON")
string="ON"
while(string!="OFF"):
    num1=int(input("Enter the Value 1 : "))
    num2=int(input("Enter the Value 2 : "))
    operator=input("Enter the operator : ")
    if operator=='+':
        print("The Addition of the two numbers is : ",num1+num2)
    elif operator=='-':
        print("The Subtraction of the two numbers is : ",num1-num2)
    elif operator=='*':
        print("The Multiplication of the two numbers is : ",num1*num2)
    elif operator=='/':
        print("The Division of the two numbers is : ",num1/num2)
    elif operator=='//':
        print("The Floor Division of the two numbers is : ",num1//num2)
    elif operator=='%':
        print("The Modules of the two numbers is : ",num1%num2)
    else:
        print("Invalid Operator")
    string=input("Enter any key to continue or enter OFF to exit the operation : ")
print("Thankyou")
    

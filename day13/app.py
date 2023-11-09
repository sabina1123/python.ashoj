from cal import *
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
operator=input("Enter a operator")
if operator=="+":
    print(sum(number1,number2))
elif operator=="*":
    print(multiplication(number1,number2))
elif operator=="-":
    print(subtraction(number1,number2))
elif operator=="/":
    print(division(number1,number2))
else:
    print(modulus(number1,number2))

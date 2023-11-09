"""def number(numbers):
    print(numbers)
number(1) """

""" def number(number1,number2):
    print(number1,number2)
number(1,2) """

def sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    print(total)
sum(1,2,3,4,5,6,7,8,9,10)

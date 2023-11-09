def function(a,b):

    operator=input("Enter you operator:")
    if operator=="+":
        print("The sum of a and b is:", a+b)
    elif operator=="-":
        print("The difference of a and b is:", a-b)
    elif operator=="*":
        print("The multiply of a and b is:",a*b)
    elif operator=="/":
        print("The division of a and b is:", a/b)
    elif operator=="%":
        print("The remember of a and b is :", a%b)
    else:
        print("The square of a is :", a**b)
    while(a<b):
        print("a is smaller than b")
function(10,5)
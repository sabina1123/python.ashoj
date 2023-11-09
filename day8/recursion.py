"""def hello():
    print("hello, world")
    hello()
hello()
def number(n=0):
    print(n)
    if n == 10:
        return 
    number(n+1)
number()"""
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return(n*factorial(n-1))
print(factorial(2))
print(list(range(2)))
    
    
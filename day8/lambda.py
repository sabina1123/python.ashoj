"""def sum(a,b):
    return a+b

sum=lambda a,b:a+b
print(sum(2,3))

def fun(n):
    return lambda a:a*n
doubler=fun(2)
print(doubler(4))
print(doubler(5))"""

def fun(n):
    return lambda a:a*n
tripler=fun(3)
print(tripler(10))
print(tripler(20))


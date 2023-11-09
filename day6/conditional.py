"""i=10
if i<5:
    print("i is less than 5")
elif i==15:
    print("i is equal to 15")
else:
    print("i is greater than 5")"""

name=input("Enter your name:")
print(f"Hello,{name}")  
age=int(input("Enter your age:"))
if age<10:
    print(f"{name} is child")
elif age>10 and age<18:
    print(f"{name} is teenager")
elif age>18 and age<40:
    print(f"{name} is adult")
else:
    print(f"{name} is old")

     
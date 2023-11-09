pie=3.14
int_pie=int(pie)
print(int_pie)
 
a="123"
print(type(a))
b=int(a)
print(type(b))

color=("red", "yellow", "green","blue")
print("Before")
print(color)
color=list(color)
color[0]="Orange"
color=tuple(color)
print("After")
print(color)

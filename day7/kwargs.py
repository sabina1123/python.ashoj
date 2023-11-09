#keywoard arguments
"""def person(**detail):
    print(detail['name'],detail['age'])
person(name="ram",age=20,gender="male") """

def person(**detail):
    print(f"My name is {detail['name']} and my age is {detail['age']} and my hobbies are {detail['hobbies'][0]},{detail['hobbies'][1]}")
person(name="ram",age=20,hobbies=("shopping","Running"))
person(name="shyam",age=30,hobbies=("dancing","singing"))
person(name="sita",age=25,hobbies=("dancing","reading"))
person(name="geeta",age=21,hobbies=("writing","singing"))
person(name="hari",age=30,hobbies=("sleeping","eating"))


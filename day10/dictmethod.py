dict={
    "name":"ram",
    "age":12
}
dict2={
    "name":"shyam",
    "age":12
}
print(dict.keys())
print(dict.values())
print(dict.items()) #gives key and value pair in tuple
for key,value in dict.items():
    print(f"the key is {key} and the value is {value}")
    
    
"""user:input("Enter your name:")

dict={
    "father":{"name":"Shailendra",
              "age":44,
    },
    "Mother":{"name":"Pratima",
              "age":44},
    "Brother":{"name":"sabin",
               "age":20}
}
print(dict.items())
print(dict.split())"""
print(dict.get("name","hari"))
print(dict.pop("name"))
dict.update(dict2)
print(dict)

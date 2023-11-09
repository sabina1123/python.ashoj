person={
    'name':'Sabina',
    'age':'23',
    'hobbies':('coding','reading books'),
    'family_member':(
        {
        'father':'Shailendra',
        'Mother':'pratima',
        'Brother':'sabin'
        }
        
    )
}
print(person)
print(person["name"])
print(person["age"])
print(person["hobbies"][0])
print(person["hobbies"][1][8::])
print(person["hobbies"][1][8:-1])
print(person["family_member"]["father"])
print(person["family_member"]["Mother"])
print(person["family_member"]["Brother"])
print(person["family_member"])



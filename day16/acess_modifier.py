class Person:
    def __init__(self) -> None:
        self.name="ram"
        self._age=12 #protected
        self.__salary="17k" #private
        
    def get_salary(self):
           return self.__salary
    def set_salary(self,salary):
        self.__salary=salary
    salary=property(get_salary,set_salary)
    """@property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        self.__salary=salary"""
person=Person()
person.name="hari"
print(person.name)
print(person._age)
#print(person.get_salary())
#person.set_salary("19k")
#print(person.get_salary())
person.salary="19k"
print(person.salary)


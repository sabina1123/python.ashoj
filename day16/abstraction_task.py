from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
       return 0
    def run(self):
        self.printarea()
class Rectangle(Shape):
    def __init__(self) -> None:
        self.length=4
        self.breath=5
    def printarea(self):
        print(f"The area of Rectangle is {self.length*self.breath}")
class Square(Shape):
    def __init__(self) -> None:
        self.length=5
    def printarea(self):
        print(f"The area of Square is {self.length*self.length}")
rectangle=Rectangle()
rectangle.run()
square=Square()
square.run()

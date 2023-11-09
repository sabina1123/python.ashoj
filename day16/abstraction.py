from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self,app):
        pass
    def run(self,app):
        self.process(app)
class Laptop(Computer):
    def process(self,app):
        print(f"{app} is running in laptop")
class Mobile(Computer):
    def process(self,app):
        print(f"{app} is running in Mobile")
laptop=Laptop()
laptop.run("Youtube")
mobile=Mobile()
mobile.run('PUBG')
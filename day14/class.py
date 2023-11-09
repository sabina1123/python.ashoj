class House: #blue print
    color="red"
    window=12
    door=8
    def __init__(self,color,window,door) :
        self.color=color
        self.window=window
        self.door=door
    def __str__(self) -> str:
        return f"(self.color)House"
    def get_color(self):
       return self.color
    def set_color(self,color):
        self.color=color
ramko_ghar=House("red",12,1)
print(ramko_ghar.color)
#ramko_ghar.set_color("black")
#print(ramko_ghar.get_color())



"""syamko_ghar=House()
syamko_ghar.window=10
syamko_ghar.window=13
print(ramko_ghar.color)
print(syamko_ghar.window)"""
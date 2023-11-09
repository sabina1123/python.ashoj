class GrandFather:
    def __init__(self) :
        print(f"GrandFather owns {self.car}")
    car="lambo"
class Father(GrandFather):
    def __init__(self) :
        car="ferrari"
        super().__init__()
        print(f"father owns {self.car}")
    house="luxery house"
class Mother:
    jewellary="dimond necklace"
class Son(Father,Mother):
    game_boy="ps5"
son=Son()
#father=Father()
"""print(isinstance(son,Father))
print(son.house)
print(son.car)
print(son.game_boy)
print(son.jewellary)"""

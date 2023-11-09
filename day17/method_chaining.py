class Burger:
    
    def bun(self):
        print("bun")
        return self
    def patty(self):
        print("patty")
        return self
    def sauce(self):
        print("sauce")
        return self
burger=Burger()
burger.bun()\
    .patty() \
    .sauce() \
    .patty() \
    .bun()
    
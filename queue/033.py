class Toy:
    def __init__(self, price = float, size = str, collor = str):
        self.__price = price
        self.size = size
        self.collor = collor
    @property
    def price(self):
        return self.__price
class Girls_Toy(Toy):
    pass
class Boys_Toy(Toy):
    pass
tank = Boys_Toy(1500, "средний", "зеленый")
doll = Girls_Toy(800, "маленький", "розовый")
print(f"Размер танка: {tank.size}")
print(f"Цена танка: {tank.price}")
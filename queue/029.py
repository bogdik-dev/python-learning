class Car:
    def __init__(self, brend, color, strana):
        self.brend = brend
        self.color = color
        self.__strana = strana
    def strana(self):
        return f"Авто произведено в {self.__strana}"
my_car = Car("mitsu", "red", "japan")
my_car2 = Car("ferrari", "black", "italy")
print(my_car2.strana(), my_car2.color, my_car2.brend)

'''
class Car:
    def __init__(self, brend, color, strana):
        self.brend = brend
        self.color = color
        self.__strana = strana
    @property
    def strana(self):
        return f"Авто произведено в {self.__strana}"
my_car = Car("mitsu", "red", "japan")
my_car2 = Car("ferrari", "black", "italy")
print(my_car2.strana, my_car2.color, my_car2.brend)
'''

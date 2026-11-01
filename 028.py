class Car:
    name = "auto"
    def get_sound(self):
        return "bibi"
my_car = Car()
my_2car = Car()
print(my_car.name, my_2car.name, my_2car.get_sound())
my_car.brend = "Mitsubisi"
my_car.color = "silver"
my_2car.brend = "Lancer_10_evo"
my_2car.color = "red"
print(my_car.brend, my_car.color, my_2car.brend, my_2car.color, my_2car.get_sound())
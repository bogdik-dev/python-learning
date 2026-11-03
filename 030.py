class Dog:
    def __init__(self, color, poroda, age):
        self.color = color
        self.poroda = poroda
        self.__age = age
    @property
    def age(self):
        return f"Собаке {self.__age} лет"
    def deistvie(self):
        print("Гав - гав!")
my_dog = Dog("red", "taxa", "100")
print(my_dog.poroda, my_dog.age)
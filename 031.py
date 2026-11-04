class Cat:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def meaw(self):
        print(f"{self.__name} - Мяууу")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: int):
        #if new_age <= self.__age:
            #raise ValueError("Неверный возраст котика!")

        self.__age = new_age 
class RussiaCat(Cat):
    pass
cat1 = Cat("Tom", 1)
cat1.meaw()
#print(cat1.age)
#cat1.age = 3
#print(cat1.age)

    
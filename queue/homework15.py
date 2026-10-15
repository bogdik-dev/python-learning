'''
class Pat: #Это пример наследования в ООП
    def __init__(self, name): #Родительский класс
        self.name = name

    def speak(self):  #Метод родителя
        return "Издает звук"

class Cat(Pat): #Дочерний класс (наследует Pet)

    def speak(self): #Переопределяем метод
        return "Мяу"

cat = Cat("Барсик")
print(f"Кот {cat.name}: говорит {cat.speak()}")

class Pat:
    def __init__(self, name):
        self.name = name

class Cat(Pat):
    def __init__(self, name, mice_caught):
        super().__init__(name)
        self.mice_caught = mice_caught

cat = Cat("Рыжик", 5)
print(f"{cat.name} поймал {cat.mice_caught} мышей")

class Pet:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Питомец: {self.name}"

class SuperCat(Pet):
    def info(self):
        return f"{super().info()} (Режим АКМ активирован!!!)"

cat = SuperCat("Кися")
print(cat.info())

class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "Мяу-мяу"

class Dog(Animal):
    def speak(self):
        return "Гав-гав"

koska_i_sobaka = [Cat("Мурка"), Dog("Шарик")]
for i in koska_i_sobaka:
    print(f"{i.name}: {i.speak()}")
'''
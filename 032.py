class Cat:
    desc =  "это кошка"
    sound = "Meow"
    name = "Кошка"

    def get_name(self):
        print(self.name)

    def get_sound(cls):
        print(cls.sound)

    def get_name2(cls):
        print(cls.name)

cat1 = Cat()
cat2 = Cat()
cat1.get_name2()
cat1.name = "Tom"
cat2.name = "Murka"
cat1.get_name()
cat1.get_sound()
cat2.get_name()
cat2.get_sound()

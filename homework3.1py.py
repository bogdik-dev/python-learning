'''
num = input("введите число: ")
if num[-1] != "5":
    print("не подходит")
else:
    print(num)
'''
'''
s = "PythonProgramming"
print(s[1])
print(s[-1])
print(s[::-1])
'''
'''
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)
type(numbers)
print(type(numbers))
'''
def greet_user(name):
    print("Хай", name)
greet_user("Богдик")
greet_user("Кирилл")

def square(num):
    return num * num 
print(square(5))
'''
'''
def syka(num):
    if num % 2 == 0:
        print("четко")
    else:
        print("не четко")
user_1823 = input("введи число боууу")
num =  int(user_1823)
syka(num)

def jon():
    print("Привет друг")
jon()

def Zажигалка (name):
    print(f"дорова бандит, {name}")
Zажигалка ("Кирилл")

def Патирот_слушает(a, b):
    return(a + b)
результат = Патирот_слушает(10, 20)
print (результат)

def uno(name = "посетитель"):
    print(f"привет, {name}!")
uno("воробей")
uno("ceperb")

def smoant(x, y):
    if x > y:
        return x
    else:
        return y
knight_80 = smoant(50, 60)
print(knight_80)

def summa(*args):
    return sum(args)
числа = summa(1, 3, 10)
print(числа)

def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
person(name = "Боря", age = "18", city = "Белэтгород")

cpicok1 = [1, 22, 10]
cpicok2 = [2, 17, 69]


try:
    name = "Bogdan"
    age = 20
    mmm = name + age
except TypeError:
    print("ошибочка")

try:
    age = int("десять")
except ValueError as err:
    print(f"Произошла ошибка: {err}")

try:
    DxD = 44
    print(DzD)
except NameError as err:
    print(f"Поймал ошибку: {err}")
else:
    print("Ошибок не было")

try:
    list = [1, 3, 10]
    print(list[4])
except IndexError as err:
    print("ыыы ошибка")
finally:
    print("омагад")

try:
    result = 67 / 0
except ZeroDivisionError as err:
    print("поймал опять ошибкууу")
    raise

try:
    eval("2" + "print")
except SyntaxError:
    print("ошибка")
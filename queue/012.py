def f(x, y):
    return [x for x in range(x, y + 1) if x % 3 != 0]
print(f(10, 20))
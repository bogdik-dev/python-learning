import random
numbers = []
for _ in range(10):
    numbers.append(random.randint(100,1000))
#print(numbers)

print([random.randint(100,1000) for _ in range(10)])

for i in range(1,4):
    for i2 in range(1,4):
        c = i + i2
        print(c**2)

print([i*i2 for i in range(1,4) for i2 in range(1,4)])
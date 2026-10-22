import random

nums = [random.randint(10,99) for i in range(10)]
print(nums)
my_list = []
i = 0

while i < (len(nums) - 1):
    if (nums[i] + nums[i + 1]) % 5 == 0:
        my_list.append(nums[i])
    i += 1
print(my_list)

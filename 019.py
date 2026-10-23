
def f (nums, num):
    nums = str(nums)
    num = str(num)
    for i in nums:
        for i2 in i:
            if i2 == num:
                return True
    return False
print(f([100, 102, 120, 246], 2))


'''
def check_num(a, b):
    a = str(a)
    b = str(b)
    for i in a:
        if i == b:
            return True
    return False

print(check_num(246, 2)) # True
print(check_num(346, 2)) # False
    
print(f([100, 102, 120, 246], 2))
#102 120 246
'''
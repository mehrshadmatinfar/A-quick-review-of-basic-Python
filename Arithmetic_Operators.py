import math
import random

# Sum
a = 2 + 2
print("2 + 2 = " + str(a))

# Subtraction
a = 8 - 2
print("8 - 2 = " + str(a))

# Multiplication
a = 3 * 4
print("3 * 4 = " + str(a))

# Division
a = 4 / 2
b = 1 / 3
print("4 / 2 = " + str(a))
print("int(4 / 2) = " + str(int(a)))
print("1 / 3 = " + str(b))

a = 4 // 2
b = 1 // 3
print("4 // 2 = " + str(a))
print("1 // 3 = " + str(b))

# Divide remaining
a = 4 % 2
b = 7 % 2
print("4 % 2 = " + str(a))
print("7 % 2 = " + str(b))

# Power
a = 2 ** 3
print("2 ** 3 = " + str(a))

# math library
print('--- math ---')
print(math.sqrt(16))       # 4.0
print(math.trunc(4.9))     # 4
print(int(4.9))            # 4
print(math.factorial(3))   # 6
print(math.log2(16))       # 4.0
print(math.fmod(17, 2))    # 1.0
print(17 % 2)              # 1
print(math.fabs(-5))       # 5.0
print(math.pow(2, 4))      # 16.0
print(math.pi)             # 3.141592653589793

# random library
print('--- random ---')
print(random.randint(1, 10))  # random number between 1 and 10
print(random.choice([1, 10]))  # select 1 or 10

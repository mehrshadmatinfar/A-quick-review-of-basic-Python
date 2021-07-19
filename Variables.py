# Integer
I = 2
print(type(I))
print("Integer example: " + str(I))

# Float
F = 2.2
print(type(F))
print("Float example: " + str(F))

# Complex
C = 2 + 7j
print(type(C))
print("Complex example: " + str(C))

# String
S = 'hello world!'
print(type(S))
print("String example: " + S)

# Evaluation
# this use for calculation app for example that get string as input and solve that string
E = eval('2 + 2')
print("Evaluation ('2 + 2') example: " + str(E))

# Python Casting
print('--- Casting ---')
print('I as integer: ' + str(I))
print('I as float: ' + str(float(I)))
print('I as complex: ' + str(complex(I)))

print('F as float: ' + str(F))
print('F as integer: ' + str(int(F)))
print('F as complex: ' + str(complex(F)))


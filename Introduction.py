from keyword import iskeyword

# variable names
print('--- variable names ---')

print('a2: ' + str('a2'.isidentifier()))      # True
print('2a: ' + str('2a'.isidentifier()))      # False
print('_myvar: ' + str('_myvar'.isidentifier()))  # True
print('my_var: ' + str('my_var'.isidentifier()))  # True
print('my$: ' + str('my$'.isidentifier()))     # False
print('if (identifier): ' + str('if'.isidentifier()))  # True but it must False
# key word check
print('if (keyword): ' + str(iskeyword('if')))         # True

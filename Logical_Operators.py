a = 2
b = 2
c = 4
d = 1

# and
print('------- and -------')
C = a == b and a == c
print("a == b and a == c --> " + str(C))
C = a == b and a <= c
print("a == b and a <= c --> " + str(C))
print(type(C))

# or
print('------- or --------')
C = a == b or a == c
print("a == b or a == c --> " + str(C))
C = a == b or a <= c
print("a == b or a <= c --> " + str(C))

# not
print('------- not -------')
C = not(a == b and a == c)
print("not(a == b and a == c) --> " + str(C))
C = not(a == b and a <= c)
print("not(a == b and a <= c) --> " + str(C))

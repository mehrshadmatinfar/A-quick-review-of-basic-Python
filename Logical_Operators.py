a = 2
b = 2
c = 4
d = 1

# and
C = a == b and a == c
print("C = a == b and a == c --> " + str(C))
C = a == b and a <= c
print("C = a == b and a <= c --> " + str(C))

# or
C = a == b or a == c
print("C = a == b or a == c --> " + str(C))
C = a == b or a <= c
print("C = a == b or a <= c --> " + str(C))

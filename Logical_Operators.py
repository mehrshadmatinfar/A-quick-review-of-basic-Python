a = 2
b = 2
c = 4
d = 1

# and
C = a == b and a == c
print("a == b and a == c --> " + str(C))
C = a == b and a <= c
print("a == b and a <= c --> " + str(C))

# or
C = a == b or a == c
print("a == b or a == c --> " + str(C))
C = a == b or a <= c
print("a == b or a <= c --> " + str(C))

# not
C = not(a == b and a == c)
print("not(a == b and a == c) --> " + str(C))
C = not(a == b and a <= c)
print("not(a == b and a <= c) --> " + str(C))

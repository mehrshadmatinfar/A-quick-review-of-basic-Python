# IF
print('--- if ---')
a = 1
b = 2
c = 7

if a == b:
    print("a == b")
elif a == c and a != c:
    print("a == c")
else:
    print("a != b")
print("I'm not in if 'HA HA HA HA...'")

# Conditional expression
print('--- conditional expression ---')
m = a if a < b else b
print(m)

# While
while a <= c:
    print(a)
    a += 1
else:
    print("stop")
    a = 1

# for
for i in range(1, 10):
    if i != 3:
        print(i)
        continue
print("-----------------")
for i in range(10):
    print(i)
    if i == 4:
        break
name = "How are you?"
for i in range(len(name)):
    print(name[i])

# Pass
if 1 == 1:
    pass  # pass does nothing :)

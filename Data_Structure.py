# Sequence
a = 'hello world!'
print(a[1])  # first array is array number "0"
print(a[1:5])
print(a[:5])

print('Length = ' + str(len(a)))

# array & List
print('--- list ---')
List = [[1, 2, 3],
        [5, 8, 3],
        [9, 6, 4],
        'This is not Matrix',
        2,
        [5, 8]]
print(type(List))  # <class 'list'>
print(len(List))  # 6
print(List.index(2))  # 4
print(List)  # [[1, 2, 3], [5, 8, 3], [9, 6, 4], 'This is not Matrix', 2, [5, 8]]
print(List[1][2])  # 3
print(List[3])  # This is not Matrix

print('--- part 01 (another list) ---')
another_list = [8, 2, 12, 36, 15, 28, 2, 3]
print(another_list.index(2))  # 1
print(another_list[1])        # 2
another_list[1] = 7           # list is mutable
print(another_list)           # [8, 7, 12, 36, 15, 28, 2, 3]

print('--- part 02 ---')
print(another_list[1:4])      # [7, 12, 36]
print(another_list[0:3])      # [8, 7, 12]
print(another_list[3:])       # [36, 15, 28, 2, 3]
print(another_list[0:5:2])    # [8, 12, 15]
print(another_list[::-2])     # [3, 28, 36, 7]

print('--- part 03 ---')
print(max(another_list))      # 36
print(min(another_list))      # 2
print(sum(another_list))      # 111
print(another_list.count(2))  # 1

print('--- part 04 ---')
another_list.insert(2, 999)
print(another_list)           # [8, 7, 999, 12, 36, 15, 28, 2, 3]
another_list.remove(999)
print(another_list)           # [8, 7, 12, 36, 15, 28, 2, 3]
another_list.append(951)
print(another_list)           # [8, 7, 12, 36, 15, 28, 2, 3, 951]
another_list.append(['a', 'b'])
print(another_list)           # [8, 7, 12, 36, 15, 28, 2, 3, 951, ['a', 'b']]
print(len(another_list))      # 10
print(another_list.pop())     # ['a', 'b']
print(another_list)           # [8, 7, 12, 36, 15, 28, 2, 3, 951]
another_list.extend(['a', 'b'])
print(another_list)           # [8, 7, 12, 36, 15, 28, 2, 3, 951, 'a', 'b']
print(len(another_list))      # 11
print(another_list.pop(-2))   # 'a'
print(another_list)           # [8, 7, 12, 36, 15, 28, 2, 3, 951, 'b']
del another_list[-1]
print(another_list)           # [8, 7, 12, 36, 15, 28, 2, 3, 951]
another_list.sort()
print(another_list)           # [2, 3, 7, 8, 12, 15, 28, 36, 951]
another_list.reverse()
print(another_list)           # [951, 36, 28, 15, 12, 8, 7, 3, 2]
another_list.clear()
print(another_list)           # []

print('--- part 05 ---')
a = [3, 5]
b = a * 2
print(b)                      # [3, 5, 3, 5]

a = [1, 2, 3]
b = ['a', 'b']
print(a + b)                  # [1, 2, 3, 'a', 'b']

print('--- part 06 (loop and list) ---')
for i in List:
    print(i)

a = [i for i in range(3)]
print(a)                      # [0, 1, 2]

grade = [5, 19, 20, 10, 7]
a = [i for i in grade if i >= 10]
print(a)                      # [19, 20, 10]


# Tuple
a = ('a', 19, 'hello')
print(type(a))
print(a)
a = 'a', 19, 'hello'
print(type(a))
print(a)

# Dictionary
a = {"math": 15, "history": 20, "Geography": 19, "chemistry": 19, "Physics": 19}
print(type(a))
print(a)
print(a["history"])

# Set
a = {4, 10, 19, 24}
print(type(a))
print(a)

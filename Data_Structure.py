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
print('--- tuple ---')
Tuple = ('a', 19, 'hello')        # tuples are immutable
print(type(Tuple))                # <class 'tuple'>
print(Tuple)                      # ('a', 19, 'hello')
another_Tuple = 'a', 'b', 'c', 'd', 'e', 'f'
print(type(another_Tuple))        # <class 'tuple'>
print(another_Tuple)              # ('a', 'b', 'c', 'd', 'e', 'f')
print(another_Tuple[0])           # a
print(another_Tuple[2:5])         # ('c', 'd', 'e')
print('f' in another_Tuple)       # True
print('z' in another_Tuple)       # False
print('--- part 01 ---')
my_Tuple = 1, 2, 4, 7, 19, 21, 24
print(type(my_Tuple))             # <class 'tuple'>
print(my_Tuple)                   # (1, 2, 4, 7, 19, 21, 24)
print(sum(my_Tuple))              # 78
print(max(my_Tuple))              # 24
print(min(my_Tuple))              # 1
print(my_Tuple.count(2))          # 1
print(tuple(reversed(my_Tuple)))  # (24, 21, 19, 7, 4, 2, 1)
my_List = list(my_Tuple)
print(my_List)                    # [1, 2, 4, 7, 19, 21, 24]
my_List.append(74)
print(my_List)                    # [1, 2, 4, 7, 19, 21, 24, 74]
print(tuple(my_List))             # (1, 2, 4, 7, 19, 21, 24, 74)
print('--- part 02 ---')
Tuple1 = (1, 2)
Tuple2 = ('x', 'y')
c = zip(Tuple1, Tuple2)
print(list(c))           # [(1, 'x'), (2, 'y')]

x = [(1, 'x'), (2, 'y')]
u = zip(*x)             # unzip
print(list(u))          # [(1, 2), ('x','y')]


# Dictionary
print('--- Dictionary ---')
Dictionary = {"math": 15, "history": 20, "Geography": 19, "chemistry": 19, "Physics": 19}
print(type(Dictionary))                # <class 'dict'>
print(Dictionary)                      # {'math': 15, 'history': 20, 'Geography': 19, 'chemistry': 19, 'Physics': 19}
print(len(Dictionary))                 # 5
print(Dictionary["history"])           # 20
print(Dictionary.get("history"))       # 20
print(list(Dictionary.keys()))         # ['math', 'history', 'Geography', 'chemistry', 'Physics']
print(list(Dictionary.values()))       # [15, 20, 19, 19, 19]
print(list(Dictionary.items()))        # [('math',15),('history',20),('Geography',19),('chemistry',19),('Physics',19)]
print('--- part 01 (Dictionary and loop) ---')
for key, value in Dictionary.items():
        print(key + ' --> ' + str(value))
print('--- part 02 ---')
dict01 = {'x': 3, 'y': 2, 'z': 1}
dict02 = {'w': 8, 't': 7}
combine_dicts = {**dict01, **dict02}
print(combine_dicts)  # {'x': 3, 'y': 2, 'z': 1, 'w': 8, 't': 7}

k = ['a', 'b']  # list
v = [4, 8]  # list
z = zip(k, v)
d = dict(z)
print(d)  # {'a': 4, 'b': 8}

Nested_dict = {
        'name': 'Ali',
        'children': ['Elena', 'Alice'],
        'phone': {'home': '021-82880000', 'mobile': '+79055856249'}
}
print(len(Nested_dict))                # 3
print(Nested_dict['phone']['mobile'])  # +79055856249
print(Nested_dict['children'][0])      # Elena

# Set
print('--- Set ---')
Set = {4, 10, 19, 24, 24, 24, 24}
print(type(Set))    # <class 'set'>
print(Set)          # {4, 10, 19, 24}
print(len(Set))     # 5
Set.add('U')
print(Set)          # {4, 10, 'U', 19, 24}
Set.remove('U')
print(Set)          # {4, 10, 19, 24}
print('--- part 01 ---')
another_Set = {4, 19, 21, 7, 24}
print(another_Set)                      # {4, 7, 19, 21, 24}

print(Set.intersection(another_Set))    # {24, 19, 4}
print(Set & another_Set)                # {24, 19, 4}

print(Set.union(another_Set))           # {4, 7, 10, 19, 21, 24}
print(Set | another_Set)                # {4, 7, 10, 19, 21, 24}

print(Set.difference(another_Set))      # {10}
print(Set - another_Set)                # {10}

print(Set.issubset(another_Set))        # False

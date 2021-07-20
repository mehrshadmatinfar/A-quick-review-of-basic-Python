s = 'python'

print(len(s))  # 6
print('th' in s)  # True

print(s.islower())  # True
print(s.isalpha())  # True
print(s.isdigit())  # False

print(s.find('o'))  # 4
print(s.count('o'))  # 1

print(s.title())  # Python
print(s.upper())  # PYTHON

print(s.ljust(8, '+'))  # python++
print(s.startswith('py'))  # True

print(s.replace('thon', 'ramid'))  # pyramid

print('--------------------------------------------------')

s = '$python$$'
print(s.strip('$'))  # python
print(s.lstrip('$'))  # python$$
print(s.rstrip('$'))  # $python

print('--------------------------------------------------')

s = 'Python created by Rossum'
a = s.split(' ')
print(a)  # ['Python', 'created', 'by', 'Rossum']

print('--------------------------------------------------')

b = ['Python', 'created', 'by', 'Rossum']
c = ' '.join(b)
print(c)

print('--------------------------------------------------')
print('# format #')

s = 'python'

print(f'name : {s}')  # name : python
print('name:{}'.format(s))  # name : python

print('--------------------------------------------------')

a = 'Mehrshad'
b = 'Matinfar'

print('name:{0}   family:{1}'.format(a, b))

# name:Mehrshad   family:Matinfar

print('--------------------------------------------------')

a = 15
b = 17.9999

print('{:d} {:.1f}'.format(a, b))  # 15  18.0

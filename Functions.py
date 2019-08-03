class program:
    name = ""
    ID = 0


a = program()
a.name = "Hello World!"
a.ID = 19

b = program()
b.name = "bye world!"
b.ID = 33
b.add_To_Class = 59

print(b.add_To_Class)


def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(even(19))

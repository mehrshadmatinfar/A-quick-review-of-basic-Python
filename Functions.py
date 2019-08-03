# part 1
class program(object):
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

# part 2


def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(even(19))

# part 3


class Time(object):
    hours = 0
    minutes = 0
    second = 0


def Time_Print(t):
    print(str(t.hours) + ":" + str(t.minutes) + ":" + str(t.second))


afternoon = Time()
afternoon.hours = 17
afternoon.minutes = 35
afternoon.second = 6

Time_Print(afternoon)


# part 4
class Time2(object):
    hours = 0
    minutes = 0
    second = 0

    def Time_Print2(u):
        print(str(u.hours) + ":" + str(u.minutes) + ":" + str(u.second))


morning = Time2()
morning.hours = 8
morning.minutes = 20
morning.second = 10
Time2.Time_Print2(morning)

# part 5


class Language(object):
    def langname(self, name):
        self.name = name

    def dispname(self):
        return self.name


L1 = Language()
L1.langname("java")
print(L1.dispname())

# part 6


class Time3(object):
    def __init__(self, hours=0, minutes=0, second=0):
        self.hours = hours
        self.minutes = minutes
        self.second = second

    def printTime3(self):
        print(str(self.hours) + ":" + str(self.minutes) + ":" + str(self.second))


time3 = Time3(10, 10, 10)
time3.printTime3()
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

# part 7


class father(object):
    k = 7

    def __init__(self, color='green'):
        self.color = color

    def Hello1(self):
        print("It is Class1!")

    def printColor(self):
        print("I like the color", self.color)

    def __localHello(self):
        print("A hardy Hello only used within the class!")


class mather(object):
    pass


class son(father, mather):
    def __init__(self):
        father.__init__(self, color='green')

    def Hello2(self):
        print("It is Class2!")
        print(self.k, "is my favorite number")


c1 = father()
c2 = son()
print("Class1 says hello:")
c1.Hello1()

print("Class2 says a Class1 hello:")
c2.Hello1()

print("Class2 says its own hello:")
c2.Hello2()

print("Class1 color via __init__():")
c1.printColor()

print("Class2 color via inherited __init__() and printColor():")
c2.printColor()

print("Class1 changes its mind about the color:")
c1 = father('yellow')
c1.printColor()

print("Wonder what Class2 has to say now:")
c2.printColor()
print('-'*20)

if hasattr(father, "Hello2"):
    print(c1.Hello2())
else:
    print("Class1 does not contain method Hello2()")
if issubclass(son, father):
    print("Class2 is a subclass of Class1, or Class2 has inherited Class1")

print("Variable k from Class1 =", c1.k)
print('-'*20)

if hasattr(father, "__localHello()"):
    print(c1.__localHello())
else:
    print("No access to Class1 private method __localHello()")

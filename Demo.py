# Constructor
"""class Computer:
    def __init__(self):
        self.name = "Vijay"
        self.age = 29

    def update(self):
        self.age = 18

    def compare(self, ohers):
        if self.age == ohers.age:
            return True
        else:
            False


c1 = Computer()
c2 = Computer()
c2.name = "Sherin"
c2.age = 26

if c1.compare(c2):
    print("there are same")
else:
    print(
          "There are diffrent")

print(c1.name, c1.age)
print(c2.name, c2.age)


class Car:
    wheel = 4

    def __init__(self):
        self.mil = 10
        self.comp = "BMW"


c1 = Car()
c2 = Car()

Car.wheel=8
print(c1.comp,c1.mil,c1.wheel)
print(c2.comp,c2.mil,c2.wheel)


class Student:
    school = "Viajydya"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def info(cls):
        return cls.school
    @staticmethod
    def dot():
        print("kjdkfd;fjdfsdjfsdh")

s1 = Student(85, 78, 95)
s2 = Student(88, 79, 96)

print(s1.avg())
print(Student.info())
print(s2.avg())
Student.dot()

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'hP'
            self.cpu ='i5'
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s2 = Student('Vijay',404)
s1 = Student('Sherin',404)
s1.show()


class A:
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")

class B:
    def feature4(self):
        print("Feature 4 Working")

    def feature3(self):
        print("Feature 3 Working")

class C(A,B):
    def feature5(self):
        print("Feature 5 Working")


class A:
    def __init__(self):
        print("in it A")

    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")


class B(A):
    def __init__(self):
        print("in it B")

    def feature4(self):
        print("Feature 4 Working")

    def feature3(self):
        print("Feature 3 Working")


class C:
    def __init__(self):
        super().__init__()
        print("init C here")


a1 = C()
class pycharm:
    def executes(self):
        print("compiling")
        print("Running")

class Myediter:
    def executes(self):
        print("spelling Check")
        print("Concection Check")
        print("compiling")

        print("Running")

class Laptop:
    def code(self,ide):
        ide.executes()

ide = Myediter()
lap1 = Laptop()
lap1.code(ide)
a = "5"
b = "6"

c,d = 5,6
print(a + b)

print(str.__add__(a, b))
print(int.__add__(c,d ))
"""


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, others):
        m1 = self.m1 + others.m1
        m2 = self.m2 + others.m2
        s3 = Student(m1,m2)

        return s3


s1 = Student(45, 85)
s2 = Student(48, 75)
s3 = s1 + s2
print(s3.m1)
print(s3.m2)

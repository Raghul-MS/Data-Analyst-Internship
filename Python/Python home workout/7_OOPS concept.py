#class and object has its types

#inheritance - a class that inherits another calss is called inheritance

'''Single Inheritance – One parent, one child.

Multiple Inheritance – Child inherits from more than one parent.

Multilevel Inheritance – Inheritance chain (A → B → C).

Hierarchical Inheritance – One parent, multiple children.

Hybrid Inheritance – Combination of the above.'''


#single inheritance - one parent class and one child class
'''
class dad:
    def phone(self):
        print("dad's phone")
class son(dad):
    def laptop(self):
        print("son's laptop")
obj=son()
obj.phone()
obj.laptop()
'''
#multiple inheritance - a class which can access multiple class is known as multiple class
'''
class dad:
    def phone(self):
        print("dad's phone")
class mom:
    def sweet(self):
        print("mom's sweet")
class son(dad,mom):
    def laptop(self):
        print("son's laptop")
obj=son()
obj.phone()
obj.sweet()
obj.laptop()
'''
#multilevel inheritance- a class is derived from a classs which is also derived from another class
'''
class grandpa:
    def phone(self):
        print("grandpa phone")
class dad(grandpa):
    def money(self):
        print("dad's money")
class son(dad):
    def laptop(self):
        print("son's laptop")
obj=son()
obj.phone()
obj.money()
obj.laptop()
'''
#hierarchical- multiple classes that inherits one parent class
'''
class dad():
    def money(self):
        print("dad's money")
class son1(dad):
    def laptop1(self):
        print("son's laptop")
class son2(dad):
    def laptop2(self):
        print("son's laptop")

class son3(dad):
    def laptop3(self):
        print("son's laptop")

obj1=son1()
obj1.laptop1()
obj2=son2()
obj2.laptop2()
obj3=son3()

obj3.laptop3()
obj4=dad()
obj4.money()
'''
#hybrid- combination of two or more types of inheritance
'''
class A:
    def show_A(self):
        print("Class A")

class B(A):
    def show_B(self):
        print("Class B")

class C:
    def show_C(self):
        print("Class C")

class D(B, C):  # D inherits from B and C
    def show_D(self):
        print("Class D")

obj = D()
obj.show_A()
obj.show_B()
obj.show_C()
obj.show_D()
'''

#POLYMORPHISM

# the word polymorphism means having many forms. in programming polymorphism means the same function name (but different signatures) being used for different types. the key difference is the data types and number of arguments used in function.

'''
def add(a,b,c=0):
    print(a+b+c)
add(1,2)
add(1,2,3)
'''

'''
class animal:
    def sound(self):
        print("animal makes a sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class bird(animal):
    def sound(self):
        print("birds sing")
obj1=dog()
obj1.sound()
'''

'''
class shape:
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)
obj=rectangle()
obj.area()
'''
'''class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def info(self):
        print(self.name,self.grade)
obj=student("raghul","A")
obj.info()
    '''

'''class vehicle:
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")
obj=car()
obj.start()
'''
'''
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
obj=manager("raghul",50000,"data analyst")
obj.display()
'''




















































































































        



























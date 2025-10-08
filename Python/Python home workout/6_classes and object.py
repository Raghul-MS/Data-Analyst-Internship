
#CLASS AND OBJECTS


'''
class goa:
    name=""
    drink=""
    def party(self):
        print("Let's Party....")
    def beach(self):
        print("enjoy beach")
ramesh=goa()
suresh=goa()
ramesh.name="Ramesh"
suresh.name="Suresh"
ramesh.drink="Yes"
suresh.drink="No"
print("Name:",ramesh.name)
print("drink:",ramesh.drink)
ramesh.party()
print("Name:",suresh.name)
print("drink:",suresh.drink)
suresh.beach()
'''


'''
class laptop:
    price=""
    processor=""
    ram=""
hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=50000
hp.processor="i6"
hp.ram="8"

dell.price=60000
dell.processor="i5"
dell.ram="16"

lenovo.price=70000
lenovo.processor="i7"
lenovo.ram="16"

print("hp:")
print("price:",hp.price)
print("processor",hp.processor)
print("ram",hp.ram)

print("dell:")
print("price:",dell.price)
print("processor",dell.processor)
print("ram",dell.ram)

print("lenovo:")
print("price:",lenovo.price)
print("processor",lenovo.processor)
print("ram",lenovo.ram)
'''
'''
class kodaikanal:
    name=""
    budget=5000
    drink=""
    def party(self):
        print("let's rock...")
raghul=kodaikanal()
prajith=kodaikanal()
raghul.name="Raghul"
raghul.budget
raghul.drink="yes"
prajith.name="Prajith"
prajith.budget
prajith.drink="yes"
print("Name:",raghul.name)
print("Budget:",raghul.budget)
print("Drink:",raghul.drink)
print("Name",prajith.name)
print("Budget:",prajith.budget)
print("Drink:",prajith.drink)
raghul.party()
'''

#constructor and self keyword
'''
class laptop:
    def __init__(self,price,ram):   #"__init__" is a constructor that is inbuilt function in python that can be called when object is created we dont have to call the function name
        self.price=price   #"__init__ " is used to assign a variable(attributes) 
        self.ram=ram       #we have to use "self" when we were using the function inside a class
    def display(self):
        print("price:",self.price)
        print("ram:",self.ram)
hp=laptop(50000,"8gb")
hp.display()
'''

#pass- it is used in a class to make it empty
'''
class laptop:
    pass
'''

#example for class and object
'''
class student:
    def __init__(self,name,register_number):
        self.name=name
        self.register_number=register_number
    def display(self):
        print("Name:",self.name)
        print("register number:",self.register_number)
obj=student("Raghul",85)
obj.display()
'''
'''
class fruit:
    def __init__(self,color):
        self.color=color
    def apple(self):
        print("Apple color:",self.color)
obj=fruit("Red")
obj.apple()
'''
'''
class teacher:
    def __init__(self,name,register_number):
        self.name=name
        self.register_number=register_number
    def display(self):
        print("Name:",self.name)
        print("register number:",self.register_number)
obj1=teacher("Raghul",85)
obj1.display()
obj2=teacher("Prajith",81)
obj2.display()
'''

'''
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("add",self.a+self.b)
    def sub(self):
        print("sub",self.a-self.b)
    def mul(self):
        print("mul",self.a*self.b)
    def div(self):
        print("div",self.a/self.b)
obj=calculator(2,2)
obj.add()
obj.sub()
obj.mul()
obj.div()
'''
#Types of class variables
#instance variable
'''
class teacher:
    def __init__(self,name,register_number):   #assigniag a variable inside a constuctor is known as instancde variable
        self.name=name
        self.register_number=register_number
    def display(self):
        print("Name:",self.name)
        print("register number:",self.register_number)
obj1=teacher("Raghul",85)
obj1.display()
obj2=teacher("Prajith",81)
obj2.display()
'''
#class variable
'''
class phone:
    chargertype="c-type"   #class variable is assigned inside a class it is known as class variable
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("charger type:",self.chargertype)
obj1=phone("samsung",10000)
obj1.display()
obj2=phone("redmi",10000)
obj2.display()
obj3=phone("realme",10000)
obj3.display()
'''











































































































































































































































































































































































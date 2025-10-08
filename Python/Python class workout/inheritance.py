#single inheritance
'''
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()
class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname() 
'''
#multilevel
'''
class family:
    def father(self):
        print("am prajith father")
class prajith(family):
    def child(self):
        print("i want to give my son prajith to swetha and subiska")
class sis(prajith):
    def prajisis(self):
        print("i support prajith")
obj=family()
obj.father()
obj.child()
obj.prajisis()'''  


#multiple
'''
class family:
    def father(self):
        print("am prajith father")
class prajith:
    def child(self):
        print("i want to give my son prajith to swetha and subiska")
class sis(family,prajith):
    def prajisis(self):
        print("i support prajith")
obj=sis()
obj.father()
obj.child()
obj.prajisis()
'''

#hierarchical
'''
class family:
    def father(self):
        print("am prajith father")
class prajith(family):
    def child(self):
        print("i want to give my son prajith to swetha and subiska")
class sis(family):
    def prajisis(self):
        print("i support prajith")
obj=sis()
obj.father()
obj.prajisis()
obj=prajith()
obj.child()
obj.father()'''

#hybrid
''''
class mother:
    def mom(self):
        print("am mother ")
class family:
    def father(self):
        print("am prajith father")
class prajith(family):
    def child(self):
        print("i want to give my son prajith to swetha and subiska")
class sis(mother,family):
    def prajisis(self):
        print("i support prajith")
a=prajith()
a.child()
a.father()

b=sis()
b.father()
b.prajisis()
b.mom()
'''

































































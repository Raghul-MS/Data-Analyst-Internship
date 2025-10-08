'''class hi:
    x=5
    y=7

    def hlo(self):
        print('hlo world')
obj=hi()
print(obj.x+obj.y)
print(obj.y)

obj.hlo()'''
'''
class wel:
    def hello(self):
       i=1
       for i in range(1,10):
           print("priya is waiting for prajith")
      
obj=wel()
obj.hello()
'''
'''
class hi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def my_name(self):
        print('my name is ',self.name )
        
    def my_age(self):
        print("my age is:",self.age)
        
obj=hi('vivek',23)
obj.my_name()
obj.my_age()
'''

'''
class hi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def my_name(self):
        print('my name is ',self.name )
        
    def my_age(self):
        print("my age is:",self.age)
        
obj=hi('vivek',23)
obj.my_name()
obj.my_age()

print('===========')

b=hi('rahul',23)
b.my_name()
b.my_age()

print('===========')

c=hi('prejith', 20)
c.my_name()
c.my_age()

'''


'''class hi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def names(self):
        print("my name is:",self.name)
    def ages(self):
        print("my age is:",self.age)
a=hi("raghul",21)
a.names()
a.ages()
print("--------")

b=hi("prajith",22)
b.names()
b.ages()
print("--------")
'''

'''class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def shape(self):
        print("area of rectangle:",self.length*self.breadth)
        print("perimeter of rectangle:",2*(self.length+self.breadth))
obj=rectangle(2,5)
obj.shape()
'''
'''
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print("make:",self.make)
        print("model:",self.model)
        print("year:",self.year)
obj=Car("india","tata",2020)
obj.display_info()
'''
'''
class student:
    def __init__(self,name,rollno,mark):
        self.name=name
        self.rollno=rollno
        self.mark=mark
    def calculate_grade(self):
            print("name:",self.name)
            print("rollno:",self.rollno)
            print("mark:",self.mark)
            if(self.mark>=90):
                print("grade:A+")
            elif(self.mark>=80):
                print("grade:A+")
            elif(self.mark>=90):
                print("grade:A")
            elif(self.mark>=70):
                print("grade:B+")
            elif(self.mark>=60):
                print("grade:B")
            elif(self.mark>=50):
                print("grade:C+")
            elif(self.mark>=40):
                print("grade:C")
            elif(self.mark>=35):
                print("grade:D")
            else:
                print("grade:NO Grade")
obj1=student("A",1,90)
obj1.calculate_grade()
print("---------")
obj2=student("B",2,80)
obj2.calculate_grade()
print("---------")
obj3=student("C",3,70)
obj3.calculate_grade()
print("---------")
obj4=student("D",4,60)
obj4.calculate_grade()
print("---------")
obj5=student("E",5,50)
obj5.calculate_grade()
print("---------")
obj6=student("F",6,40)
obj6.calculate_grade()
print("---------")
obj7=student("G",7,30)
obj7.calculate_grade()
print("---------")
obj8=student("H",8,450)
obj8.calculate_grade()
print("---------")
obj9=student("I",9,35)
obj9.calculate_grade()
print("---------")
obj10=student("J",10,83)
obj10.calculate_grade()
print("---------")
'''

'''
class bank_account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,deposit_amount):
        self.balance+=deposit_amount
        
        
    def withdraw(self,withdraw_amount):
        self.balance-=withdraw_amount
        
        
    def get_balance(self):
        print("current balance:",self.balance)
        
obj=bank_account("Raghul",500)
obj.deposit(1000)
obj.withdraw(500)
obj.get_balance()
'''       
'''class bank_account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
        print("Account holder:",self.account_holder)
    def deposit(self):
        deposit_amount=int(input("Enter deposit amount:"))
        self.balance+=deposit_amount
        print("account balance:",self.balance)
        
    def withdraw(self):
        withdraw_amount=int(input("Enter withdraw amount:"))
        self.balance-=withdraw_amount
        
        
    def get_balance(self):
        print("current balance:",self.balance)
        
obj=bank_account("Raghul",500)
obj.deposit()
obj.withdraw()
obj.get_balance()
'''

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

class family:
    def father(self):
        print("am prajith father")
class prajith(family):
    def child(self):
        print("i want to give my son prajith to swetha and subiska")
obj=prajith()
obj.father()
obj.child()
    
        






































































































































































































  






































































































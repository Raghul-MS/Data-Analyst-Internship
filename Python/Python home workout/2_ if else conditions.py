
#if-else (BOOLEAN VALUES (TRUE,FALSE))

'''
if(True):
    print("Yes")
else:
    print("No")

         #in if condition if it is true then only it print the if condition if it false it will print else condition

if(False):
    print("Yes")
else:
    print("No")
'''

#comparison operator (there are many comparison operator it is used to compare two values it will either print true or false)
'''print("win"=="winn")''' #if it same it will print true otherwise it will print false

'''
rcb="win"
if(rcb=="win"):
    print("nammda")
else:
    print("oombi")
'''

#Example (if_else)using comparison operator
'''
meghna=input("meghna died or not?")
if(meghna=="died"):
    print("suriya meets priya")
else:
    print("suriya weds meghna")
'''

'''
mark=int(input("enter mark:"))
if(mark>35):
    print("pass")
else:
    print("fail")
'''

'''
income=int(input("enter the income:"))
if(income>7000):
    print("sclrship available")
else:
    print("not eligible")
'''
'''
number=int(input("enter a number:"))
if(number%3==0 and number%5==0):     #binary operators(and,or ,not)
    print("it is divisible by 3 and 5")
else:
    print("it is not divisible by 3 and 5")
'''
#odd or even
'''
a=int(input("enter a number:"))
if(a%2==0):
    print("even")
else:
    print("odd")
'''

'''
score=int(input("enter score out of 100:"))
if(score<35):
    print("poor student")
if(score>=35 and score<=70):
        print("average student")
if(score>70):
        print("good student")
'''


'''
score=int(input("enter score out of 100:"))
if(score<35):
    print("poor student")    #elif is used to execute the progrem faster if we use elifit will stop the program after the statement is false but in if it check all the if 
elif(score>=35 and score<=70):
        print("average student")
elif(score>70 and score >100):
    print("good student")
else:
print("invalid score")
'''

#mini calculator
'''
a=int(input("A:"))
b=int(input("B:"))
operation=input("add/sub/div/mul:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a+b)
elif(operation=="mul"):
    print(a+b)
elif(operation=="div"):
    print(a+b)
else:
    print("no operation")
'''
'''
score_percentage=int(input("percentage:"))
if(score_percentage>=70):
    name=input("name:")
    department=input("department:")
    location=input("location:")
    print("you are eligible")
else:
    print("not eligible")
'''


'''
salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
    required=int(input("enter required loan amount:"))
    print("you are not eligible for loan")
if(required<=50000):
                 print("you are eligible")
elif(required>50000):
    print("maximum loan amount is 50000")
'''

'''
tamil=int(input("tamil:"))
english=int(input("english:"))
maths=int(input("maths:"))
science=int(input("science:"))
social=int(input("social:"))
total=tamil+english+maths+science+social
average=total/5
if(average<35):
    print("additional class is required")
else:
    print("you are good to go")
'''

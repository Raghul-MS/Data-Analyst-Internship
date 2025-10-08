#FOR LOOP

'''for i in "apple":
    print(i)       #here the applw is stored as sting so it will take apple as 5 letters and print it onme bye one
'''
'''
a=["apple","orange","kiwi"]
for i in a:        #here it is stored in set so it will take the word as index and print the word one by one 
    print(i)
'''

'''
for i in range(11):  #it will print values before 11 from 1 to 10
    print(i)
'''

#Example for loop
'''
for i in range(1,11):
    print(i,"x 2 =",i*2)
'''

'''
a=int(input("enter a number a:"))
b=int(input("enter a number b:"))
for i in range(a+1,b):
    print(i)
'''

'''
for i in range(1,11):
    if(i%2==0):
        print(i)
'''

'''count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)



'''
'''ecount=0
ocount=0
for i in range(1,14):
    if(i%2==0):
        ecount=ecount+1
    else:
           ocount=ocount+1
print("even:",ecount)
print("odd:",ocount)
'''
'''
count=0
for i in range(1,100):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)
'''

'''
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)
'''

#for loop with list
'''
a=[]
print("enter 5 num")
for i in range(5):
    num=int(input("enter a num"+str(i+1)))
    a.append(num)
print(a)

sum=0

for i in a:
    sum=sum+i
    
print("sum",sum)
'''
''' 
sum=0
for i  in range(1,8):
    print("the first 7 natural number is:",i)
    sum=sum+i
print(sum)
'''

#NESTED FOR LOOP

'''
for i in range(1,6):
    for j in range(1,3):
        print(j,"apple")
'''
'''
for j in range(1,3):
    print("week:",j) 
    for i in range(1,4):
           print("day:",i)
'''

'''
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*",end="")
'''



#WHILE LOOP
'''
i=0              #while loop is used when the number loop is unknown 
while(i==0):      #like if dont know how many times we dont know to run the loop
    print(i)      #we have to make the while loop fail otherwise the loop won't stop
    i=1+1          #while loop only run when the condition is true otherwise it wont run
'''


#EXAMPLE FOR WHILE LOOP
'''
i=1
while(i<6):
    print(i)
    i=i+1
'''


'''i=10
while(i<=200):
    print(i,end=",")
    i=i+10
'''



i=10
while(i>0):
    print(i)
    i=i-1

'''
i=3
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)
'''

'''
n = 20
a, b = 0, 1
for i in range(n):
    print(a,end=" ")
    a, b = b, a + b
'''
'''
n = 5
fact = 1
for i in range(1, n + 1):
    fact=fact*i
print(fact)'''
'''
num = int(input("entr a number:"))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
'''

'''
num=10
for i in range(1,10):
    if num>=10:
        
        print(i)'''

'''
initial_salary=50000
current_salary=initial_salary
for years in range(1,11):
    current_salary=current_salary+(current_salary*0.05)
    print(f"Salary after increment of 5% in year {years} : {current_salary}")
    '''
'''
total_class=25
attended=0
for i in range(1,19):
    percentage=(i/total_class)*100
    attended=percentage
    print("The percentage after attending class ",i,"is:",attended)
    
'''
'''
price=[100,250,400,560,700]
for i in price:
    discounted=i-(i*0.10)
    print("The price after discount of 10% percentage",i," is:",discounted)
'''

'''
savings=0
for i in range(1,13):
    savings=savings+1000
    print("The savings after end of each month ",i,"is:",savings)
'''
'''
electricity_cost=5
unit=[120,135,150,160,145]
month=1
for i in unit:
    i=i*5
    print("The unit cost for month" ,month ,"is:",i)
    month=month+1
'''

mark=[78,85,90,66,72]
for i in mark:
    percentage=i/100*(100)
    print("the percentage  for each subject mark",i,"is:",percentage)
    























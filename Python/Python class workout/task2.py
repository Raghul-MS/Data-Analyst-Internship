'''def filter_even_numbers(numbers):
    numb=[i for i in numbers  if i%2==0]
    return numb
numbers=[1,2,3,4,5,6,7,8,9,10]
result=filter_even_numbers(numbers)
print(result)
'''

'''
def square_of_numbers(numbers):
    numb=[i**2 for i in numbers  ]
    return numb
numbers=[1,2,3,4,5,6,7,8,9,10]
result=square_of_numbers(numbers)
print(result)
'''
'''def square_number(numbers):
    result=[]
    for i in numbers:
        result.append(i**2)
    return result
a=[1,2,3,4,5,6,7,8,9,10]
print(square_number(a))
'''   
'''a=int(input("enter a number:"))
str_a=str(a)
length_a=len(str_a)

num=0
for i in str_a:
    num=num+int(i)**length_a
    print(num)
if (a==num):
    print("Number is armstrong")
else:
    print("number is not armstrong")
'''   

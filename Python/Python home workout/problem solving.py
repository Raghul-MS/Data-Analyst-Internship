'''10 Basic Python Problems to Practice
- Sum or Product Check
Given two numbers, return their product if it's less than 1000; otherwise, return their sum.
- Current and Previous Number Sum
Loop through numbers 0 to 9 and print the sum of the current number and the previous one.
- Count Characters in a String
Write a function that counts how many times each character appears in a string.
- Check for Palindrome
Determine if a given string reads the same forward and backward.
- Find the Largest of Three Numbers
Use conditional statements to find the largest among three inputs.
- Swap Two Variables Without a Temp Variable
Swap values of two variables using Python’s multiple assignment.
- Reverse a String
Take a string and return its reverse using slicing.
- Print Even Numbers from a List
Loop through a list and print only the even numbers.
- Calculate the Area of a Circle
Given a radius, compute the area using the formula\pi r^2.
- Convert Celsius to Fahrenheit
Write a function to convert temperature from Celsius to Fahrenheit.
'''

# Sum or Product Check
#Given two numbers, return their product if it's less than 1000; otherwise, return their sum.
'''
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if(a * b<=1000):
    print(a*b)
else:
    print(a+b)
'''

#Current and Previous Number Sum
#Loop through numbers 0 to 9 and print the sum of the current number and the previous one.
'''
previous_num=0
for current_num in range(10):
    total=previous_num+current_num
    print("current Number:" ,current_num, "Previous Number:" ,previous_num, "Sum:", total)
    previous_num = current_num
'''

#Count Characters in a String
#Write a function that counts how many times each character appears in a string.
'''
def count_characters(a):
    result = {}
    for char in a:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
print(count_characters("hello world!"))
'''

#Check for Palindrome
#Determine if a given string reads the same forward and backward.
'''
def palindrome():
    a=input("Enter a word:")
    y=a.lower()
    if(y[::-1]==y):
        print(a,"is palindrome")
    else:
        print(a,"is not palindrome")
palindrome()
'''

#Find the Largest of Three Numbers
#Use conditional statements to find the largest among three inputs.
'''
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a>b and a>c):
    print(a,": A is largest among three numbers")
elif(b>a and b>c):
    print(b,": B is largest among three numbers")
elif(c>a and c>b):
    print(c,": C is largest among three numbers")
else:
    print("There is a tie among the numbers")
'''

#Swap Two Variables Without a Temp Variable
#Swap values of two variables using Python’s multiple assignment.
'''
a,b=10,20
a,b=b,a
print(a,b)
'''
#Reverse a String
#Take a string and return its reverse using slicing.
'''
a="HELLO"
print(a[-1::-1])
'''

#Print Even Numbers from a List
#Loop through a list and print only the even numbers.
'''
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in list:
    if(i%2==0):
        print(i)
'''

#Calculate the Area of a Circle
#Given a radius, compute the area using the formula\pi r^2.
'''
import math as a
radius = float(input("Enter the radius of the circle: "))
area = a.pi * radius ** 2
print("Area of the circle is:", area)
'''

#Convert Celsius to Fahrenheit
#Write a function to convert temperature from Celsius to Fahrenheit.
'''
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
temp_c = float(input("Enter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print("Temperature in Fahrenheit:", temp_f)
'''


animals=['lion','tiger', 'monkey', 'elephant','frog']
filtered_animals=[animal.title() for animal in animals]
print(filtered_animals)
























































































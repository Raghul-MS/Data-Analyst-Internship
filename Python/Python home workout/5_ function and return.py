#FUNCTIONS
#TO CREATE A FUNCTIONS WE HAVE TO USE "def" key before the functions
#to print the functions we have to call the function name

'''
def painter():
    print("painting") # we have used painter as function so we have to call the function last to print the output
painter()
'''


'''
a=int(input("enter a number:"))
b=int(input("enter a number:"))
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)   #to print the output we have to call the function otherwise it wont run
def div():
    print(a/b)
add()
sub()
mul()
div()
'''

'''
a=int(input("enter a number:"))
def oddoreven():
    if(a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
oddoreven()
'''

#PARAMETER AND ARGUMENTS

'''
def painter(msg,date):
    print("the message is:",msg)
    print("the message is:",date)
painter("we have to paint a house"," it is today")


#def painter(msg,date)- "msg,date" is parameter
#painter("we have to paint a house"," it is today")-"we have to paint a house"," it is today"-it is arguments
#when we use parameter in the function we have to give arguments whenn we call the function
'''

'''
a=int(input("enter a number:"))
def passorfail():
    if(a<=34):
        print("fail")
    else:
        print("pass")
passorfail()
'''

'''
a=int(input("enter a number:"))
b=int(input("enter a number:"))
def printrange():
    for i in range(a,b):
        print(i)
printrange()
'''

#RETURN KEYWORD

#"return" is used only inside a function ,we cant use return outside a function
#in function when we use the return the program will stop in the return and the program will not run after that

'''
def painter():
    return "am a painter"
msg=painter()
print(msg)
'''
'''
def valueofa():
    return 10
a=valueofa()
print(a)
'''

'''
s_username="EMC"
s_password="123"
uname=input("enter username:")
password=input("enter password:")
def validate():
    if uname==s_username and password==s_password:
        return True
    else:
        return False
print(validate())
'''
'''
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
def add():
    return a+b   
sum=add()
sum=(a+b)*c
print(sum)
'''
'''    
def add(n1,n2):
    return n1+n2
a=int(input("enter a number a:"))
b=int(input("enter a number b:"))
c=int(input("enter a number c:"))
added=add(a,b)
multiply=added*c
print(added)
print(multiply)
'''
































































































































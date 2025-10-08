#reverse
'''for i in range(5,0,-1):
    print()
    for j in range(1,i+1):
        print("*",end="")
'''
#left angle triangle
'''
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*",end="")
        '''
    

#pyramid

'''
for i in range(1, 5 + 1):
    print(" " * (5- i) + "* " * i)

'''

#diamond
'''n = 5
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
'''

'''n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    gap = " " * ((n - i) * 2 + 1)
    print(spaces + stars + gap + stars)'''


rows=4
for i in range(1,rows+1):
    spaces=rows-i
    stars=2*i-1
    print(" "*spaces+"*"*stars)






































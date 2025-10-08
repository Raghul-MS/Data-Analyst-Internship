'''
x=input("Enter a word:")
def palindrome():
    y=x.lower()
    if(y==y[::-1]):
        print(x,"is palindrome")
    else:
        print("not palindrome")
palindrome()
'''
'''
def count_word(text):
    text=text.lower()
    words=text.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
print(count_word("hello world! hello again"))
'''
'''
a=[1,1,1,2,2,3,4,4,5,6,7,6,8,6,7,9,0]
def duplicate():
    b=set(a)
    c=list(b)
    print(c)
duplicate()
'''        
        

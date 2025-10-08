
z=input("Enter a word:")
def palindrome():
    y=z.lower()
    if(y==y[::-1]):
        print(y,"is palindrome")
    else:
        print(y,"is not palindrome")
palindrome()

print("/-/-/-/-/-/-")

def count_letters_and_spaces():
    text = input("Enter your text: ")
    text = text.lower()
    freq = {}
    letters = 0
    spaces = 0
    for char in text:
        if char.isalpha():
            letters = letters + 1
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        elif char.isspace():
            spaces = spaces + 1
    print(freq)
    print("Number of spaces:",spaces)
count_letters_and_spaces()


print("/-/-/-/-/-/-")


a = []
while True:
    b = input("Do you want to add a number? (yes/no):")
    b.lower()
    if b == "yes":
        c = int(input("Enter a number: "))
        a.append(c)
    elif b == "no":
        print("The list you given:", a)
        break
    else:
        print("Please enter 'yes' or 'no'")
       
    

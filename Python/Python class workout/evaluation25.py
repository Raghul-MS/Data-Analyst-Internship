print("1st progarm")
def palindrome(word):
    a=word.lower()
    if a==a[::-1]:
        print(word,"is palindrome")
    else:
        print(word,"is not palindrome")
palindrome("Madam")

print("2nd progarm")
def word_frequencies(text):
    text=text.lower()
    words=text.split()
    print(words)
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq
print(word_frequencies("hello iam Raghul Hello am Prajith"))


print("3rd progarm")
a=[1,2,3,2,1,3,4,5,6,5,47,8,9,7]
b=set(a)
c=list(b)
print(c)




print("4th progarm")
def count_letters_digits(sentence):
    letter_count = 0
    digit_count = 0
    for word in sentence:
        if word.isalpha():
            letter_count += 1
        elif word.isdigit():
            digit_count += 1
    return letter_count, digit_count
a=input("Enter a sentence: ")
letters, digits = count_letters_digits(a)
print("Letters:", letters)
print("Digits:", digits)


print("5th progarm")
class BankAccount:
    def __init__(self,Account_holder,Balance):
        self.Account_holder=Account_holder
        self.balance=Balance
        print("Account holder:",self.Account_holder)
    def deposit(self):
        deposit_amount=int(input("Enter deposit amount:"))
        self.balance+=deposit_amount
        print("account balance:",self.balance)
    def withdraw(self):
        withdraw_amount=int(input("Enter withdraw amount:"))
        self.balance-=withdraw_amount
        print("account balance:",self.balance)
obj=BankAccount("Raghul",5000)
obj.deposit()
obj.withdraw()

  
        




























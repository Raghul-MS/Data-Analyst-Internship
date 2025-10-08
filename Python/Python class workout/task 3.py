
def even():
    numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    even_numbers=[]
    for num in numbers:
        if num%2==0:
            numbers=even_numbers.append(num)
    return even_numbers
print(even())    


def square():
    a=[1,2,3,4,5,6,7,8,9]
    b=[]
    for i in a:
        b.append(i**2)
    return b
print(square())


def details():
    data = {}
    while True:
        name = input("Enter name (or type 'done' to finish): ")
        if name.lower() == "done":
            break
        score = int(input("Enter score: "))
        data[name] = score
    return data

result = details()
print("Collected Data:", result)



























        

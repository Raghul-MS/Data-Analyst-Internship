#1
fruits=["kiwi","orange","apple","mango","cherry"]
print(fruits)

#2
fruits=["kiwi","orange","apple","mango","cherry"]
print(fruits[0:4])

#3
fruits=["kiwi","orange","apple","mango","cherry"]
print(fruits[-1])


#4
fruits=["kiwi","orange","apple","mango","cherry"]
print(fruits[2:5])

#5
fruits=["kiwi","orange","apple","mango","cherry"]
fruits[2]="lemon"
print(fruits)

#6
fruits=["kiwi","orange","apple","mango","cherry"]
fruits.insert(3,"lemon")
print(fruits)

#7
fruits=["kiwi","orange","apple","mango","cherry"]
fruits.append("lemon")
print(fruits)

#8
fruits=["kiwi","orange","apple","mango","cherry"]
veg=["carrot","cucumber","brinjal",]
fruits.extend(veg)
print(fruits)


#9
fruits=["kiwi","orange","apple","mango","cherry"]
fruits.remove("apple")
print(fruits)

#10
fruits=["kiwi","orange","apple","mango","cherry"]
fruits.pop(3)
print(fruits)

#11
fruits=["kiwi","orange","apple","mango","cherry"]
fruits.clear()
print(fruits)

#12
fruits=["kiwi","orange","apple","mango","cherry"]
veg=["carrot","cucumber","brinjal",]
c=fruits+veg
print(c)

#13
fruits=["kiwi","orange","apple","mango","cherry"]
fruits.reverse()
print(fruits)

#14
fruits=["kiwi","orange","apple","mango","cherry","apple","kiwi"]
x=fruits.count("kiwi")
print(x)

#15
fruits=("kiwi","orange","apple","mango","cherry")
a=list(fruits)
a.append("lemon")
a.pop(3)
fruits=tuple(a)
print(fruits)






































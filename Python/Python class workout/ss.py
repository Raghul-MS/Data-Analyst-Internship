'''fruits=["apple","banana","mango"]
vege=["tomato","onion","cucumber"]
vege.append("carrot")
vege.insert(2,"brinjal")
fruits.extend(vege)
fruits.pop(1)
print(fruits)

list1 = [1,2,3]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



fruit=["apple","banana","mango","apple"]
fruit.reverse()
print(fruit.index('banana'))
print(fruit)
print(fruit.count('apple'))
print(len(fruit))


fruits.append('khk')
print(fruits)
x=fruits.copy()
print(x)
'''


'''a={1,2,3,4,5}
b={6,7,8,9,0}
c=list(a)
d=list(b)
c.extend(d)
e=set(c)
print(e)'''


'''a={1,2,3,4,5}
b={6,7,8,3,4,9,0}
a.add(3)
b.remove(4)
a.remove(4)
c=a|b  #union(|) print all the values except duplicate values
d=a&b   #intersect(&) print all the values thet are same
e=a-b   #differce(-) print the values of 'a' that are not present 'b' 
print(c)
print(d)
print(e)'''

#dictionary{"key" : "values"}


bike_details={ "Owner name": "Raghul" , "Bike Model": "NS200" , "Year" : 2018}
bike_details["Owner name"]="Prajith"
bike_details.update({"FC": 2035})
bike_details["color"]= "Black"
bike_details.pop("Year")
print(bike_details)











































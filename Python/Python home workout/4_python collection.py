#PYTHON COLLECTION
#Four collection of array(list[],tuple(),set{},dictionary{keY:value})

#LIST[]-ORDERED,CAHNGEABLE,ALLOW DUPLICATE
#TUPL()-ORDERED,UNCHANGABLE,ALLOW DUPLICATE
#SET{}-UNORDERED,UNCHANGABLE,UNINDEXED,NOT ALLOW DUPLICATE
#DICTIONARY{}-**ORDERED,CHANGABLE,NOT ALLOW DUPLICATE

#LIST[]
'''
a=[1,2,3,4,5]
b=[11,22,33,44,55]
a.extend(b)
print(a)
print(a[0])
a.append(6)
a.append("raghul")
a[1]=11
a.pop(3)
a.insert(0,0)
print(a)
'''

#TUPLE() - to modify the tuple we have to chnage into list to modify the values
'''
a=(1,2,3,4,5)
b=(12,22,33,44)
c=list(a)
d=list(b)
c.extend(d)
a=tuple(c)
b=tuple(b)
print(a)
'''


#SET{} -same like that we have change the set to list to modify the set
        #but we can add,remove,update,pop
'''
a={1,2,3,4,5}
a.add(6)
a.remove(2)
a.pop()
print(a)
'''

#DICTIONARY -

a={"name":"raghul","age":21,"place":"tkc"}   #key:value pair
a["color"]="red"
a.update({"age":22})
print(a)

#create a list
li=[1,2,3]
print(type(li))
li=[1,2,"Parikh",3.4]
print(li)
#access and change elements in lists
print(li[3])
# print(li[4])
li[0]=5
li[3]="Rohan"
# li[4]=9
print(li)
#slicing of a list
print(li[1:3])
print(li[:])
print(li[1:10])
#insert and append elements in list
li.append("Laraib")
print(li)
li.insert(1,4)
li.insert(6,10)
li.insert(9,"Amy")
li.append([9,10,11])
li.extend([9,100,23])
#removing elements from list
li.remove(2)
li.remove(6)
print(li)
li.pop()
li.pop(5)
print(li)
li=[1,2,3,"Laraib",3, 45,"Rohan"]
for i in range(len(li)):
    print(li[i], end=" ")

for i in range(2,len(li)):
    print(li[i], end=" ")

for i in li:
    print(i)

for i in li[4:]:
    print(i)

for i in li[3:5]:
    print(i)
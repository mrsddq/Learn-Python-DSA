n=int(input())
li=[int(x) for x in input().split()]
print(li)
ele=int(input())
isFound=False
for i in range (len(li)):
    if li[i]==ele:
        print(i)
        isFound=True
        break
if isFound is False:
    print(-1)
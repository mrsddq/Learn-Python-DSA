# lists are mutable
def increment(li):
    li[0]=li[0]+2
    return

li=[1,2,3,4]
increment(li)
print(li)
a1=23
a2=3.4
a3=4-5j
print(type(a1))
print(type(a2))
print(type(a3))

a=10
print(id(a))
a=a+1
print(a)
print(id(a))

a=10
b=10
print(id(a))
print(id(b))
# -5 to 256 - this is the range of optimization

a=1000
b=1000
print(id(a))
print(id(b))


a = 10
id1 = id(a)
b = a + 2-2
id2 = id(b)
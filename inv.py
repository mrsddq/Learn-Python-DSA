# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fact(n-1)

# n=int(input())
# f=fact(n)
# print(f)

def print1ToN(n):
    if n==0:
        return
    print1ToN(n-1)
    print(n)
    return
n=int(input())
p=print1ToN(n)
print(p)

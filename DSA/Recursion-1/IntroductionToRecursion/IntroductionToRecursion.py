def fact(n):
    if n==0:
        return n*fact(n-1)

n=int(input())
f=fact(2)
print(f)
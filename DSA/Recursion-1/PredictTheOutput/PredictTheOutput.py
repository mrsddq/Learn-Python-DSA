def printNumbers(n):
    if(n<0):
        return
    print(n,end=" ")
    printNumbers(n-2)
num = 5
printNumbers(num)

def fun(n):
    if(n == 4):
        return n
    else:
        return 2*fun(n+1)
print(fun(2))
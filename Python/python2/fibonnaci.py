#fibonnaci number 0 1 1 2 3 5 8 13......
def fib(n):
    if n<0:
        print("Error")
    elif n==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(1,6):
    print(fib(i),end=" ")
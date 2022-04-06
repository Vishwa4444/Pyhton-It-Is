def prime(m,n):
    for v in range(m,n+1):
        if v > 1:
            for i in range(2,v):
                if n%i==0:
                    break
        else:
         print(v)
prime(3,7)
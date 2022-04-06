for i in range(10):
    if i%2==0:
        continue
    else:
        a = '*'*i
        print(a.center(20,'-'))
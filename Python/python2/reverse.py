#Reverse a given string
s1 = input("Enter a string to be reversed:")
def rev(s1):
    s2  =  ""
    index  =  len(s1)
    while index > 0:
        s2 += s1[index-1]
        index -= 1
    return s2
print(rev(s1))


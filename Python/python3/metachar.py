import re
mystr = "Black bug bit a black bee"
patt = re.compile(r'bugs?')  # regex symbol question mark ?
a= patt.findall(mystr)
print(a)
patt = re.compile(r'b*')     # regex symbol star *
b= patt.findall(mystr)
print(b)
patt = re.compile(r'b+')      # regex symbol plus +
c= patt.findall(mystr)
print(c)
patt = re.compile(r'.')        # regex symbol dot .
d= patt.findall(mystr)
print(d)

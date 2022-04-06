import re
str="black Bug 67 ta bit black bee"
patt = re.compile(r'\A')
patt = re.compile(r'\b')
patt = re.compile(r'\w')
x = patt.findall(str)
print(x)
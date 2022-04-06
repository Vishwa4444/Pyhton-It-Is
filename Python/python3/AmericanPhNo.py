import re
x = input("Enter the String :")
AmPhNo = re.compile(r'\d{3}-\d{3}-\d{4}')
a = AmPhNo.findall(x)
print(a)
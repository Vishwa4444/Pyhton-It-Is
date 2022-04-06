import re
#greedy selects higest possible string
greddy = re.compile(r'(ha){1,100}')
a = greddy.search("hahahahaha")
a.group()
print(a)
# non greedy selects lowest possible string
nongreddy = re.compile(r'(ha){1,100}?')   #only difference is a question mark ?
b = nongreddy.search("hahahahaha")
b.group()
print(b)
#finall() vs search()
phno = re.compile(r'\d{3}-\d{3}-\d{4}')
c1  = phno.search('cell:111-222-3333 work:444-444-4444')  #search:  only first match is searched
c2= phno.findall('cell:111-222-3333 work:444-444-4444')    #findall :searches untill last match
print(c1)    #  search()
print(c2)    #  findall()


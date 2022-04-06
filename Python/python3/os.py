import re
greedy = re.compile(r'(ha){1,100}')
x = greedy.search('hahahahaha')
y = x.group()
print(y)

nongreedy = re.compile(r'(ha){2,100}?')
z = nongreedy.search(('hahahaha'))
e = z.group()
print(e)
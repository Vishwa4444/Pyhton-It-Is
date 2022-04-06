import pprint
stud =[{'name':'vishwa','age':21},{'name':'harsh','age':20}]
print(pprint.pformat(stud))
file = open('MyStuds.py','w')
print(file.write('stud =' + pprint.pformat(stud) + '\n'))
file.close()


import shelve

# STORING DATA INTO FILE
s = shelve.open("MyShelve")
s['name'] = 'vishwa'
s['age']  = 21
for key in s:
    print(s[key])
s.close()

#RETRIVE STORED DATA
s = shelve.open("MyShelve")
print("Printing  stored data ")
print(s['name'])
print(s['age'])
s.close()




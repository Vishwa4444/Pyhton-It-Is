# l1=[1,2,3,4,5]
# l2=[1,2,3,5,4]
# print(bool(l1==l2))

d1 ={'k1':'1','k2':'2','k3':'3','k4':'4','k5':'5'}
# d2 ={'k1':1,'k2':2,'k3':3,'k5':5,'k4':4}
# print(bool(d1==d2))

for k , v in d1.items():
    print('key:'+k+ ' value:'+v,end=" ")
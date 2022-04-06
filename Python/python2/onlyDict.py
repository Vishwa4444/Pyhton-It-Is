# dict1 = {'k1':'car','k2':'bike','k3':'vi'}
# # print(dict1.values())
# # print(dict1.keys())
# # print((dict1.items()))
# # for k in dict1.keys():
# #     print(k,end=" ")
# # print()
# # for v in dict1.values():
# #     print(v,end=" ")
# # print("\nitems")
# # for k,v in dict1.items():
# #     print(k,v)
# # print(dict1.get('k5',12))
# print(dict1.setdefault('k5',0))
import copy

l= [1,[1,2,3],[4,5,6]]
x = copy.copy(l)
print(l)
print(x)
x[1][0]=20
print(l)
print(x)


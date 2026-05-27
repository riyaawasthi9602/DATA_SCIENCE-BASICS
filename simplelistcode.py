import numpy as np
# list=[1,2,3,4,5,6,7,8,9,10]
# amit=np.array(list)
# print(amit)

v1=np.array([1,2,3,4,5,6,7,8,9,10])
print(v1[v1>5])
print(v1+5)
print(v1*2)
print(v1*2)
print(v1[1:5])
print(v1[::-1])
print(v1[0:5:-1])

s=[[1,2,3],[3,4,5],[5,6,7]]
s1=np.array(s)
print(s1[1])
print(s1[2])
print(s1[-1])
print(s1[1][1])
print(s1[1][-1])
print(s[-1][-2])
print(s1[1][0])
s1[0][0]=12
s2=(s1+s1)
print(s2)
print([[s1],[s1]])
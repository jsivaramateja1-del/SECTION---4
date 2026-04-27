import numpy as np

'''
a = np.linspace(1,4,4)
print(a)
'''

'''
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
'''

'''
a = np.array([[1,2,3],[4,5,6]])
print(a[0])
'''

'''
a = np.array([12,4,4,5,5,5])
print(a[2:])
print(a[:3])

b = np.array([[12,3,4,4,5],[5,6,7,8,9],[11,12,13,14,15]])
# print(b[0][3])
# print(b[2][2])
# print(b[1,3])
print(b.ndim)
print(b.shape)
print(len(b.shape))

import math
print(b.size)
print(b.shape)
print(b.size == math.prod(b.shape))

c = np.array([1.2,2.3,5.4])
print(c.dtype)

d = np.zeros(5)
print(d)

e = np.ones(5)
print(e)

f = np.empty(7)
print(f)

'''

'''
a = np.arange(5,10,3) # start , end +1 , steps
print(a)

b = np.linspace(0,10,num = 5)
print(b)

x = np.ones(2,dtype = np.int64)
print(x)

y = np.ones(2,dtype = np.float64)
print(y)
'''

'''
a = np.array([2,1,5,3,7,4,6,8])
print(a)
print(np.sort(a))
print(a)
'''

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(np.concatenate((x,y),axis = 0))
print(np.concatenate((x,y),axis = 1))
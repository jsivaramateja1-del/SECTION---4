'''
print('Hello world!')
a = 4
b = 6.6
c = 'Section 4'
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))
'''
'''
c = a+b
print(c)
print('sum = %d'%(c))
'''
'''
d = 10
e = 3
f = d/e  #float value
g = d//e #integer value
print(f)
print(g)
print(10%3)
'''
'''
l=[1,2,3,4,5,6,7,'SOMENAME',[12,4,4,5]]
for i in range(9):  #0-8 values taken
    print(l[i])
for i in range(5,9):
    print(l[i])
'''
'''
l1 = []
l2=[0,0,0,0,0]
for i in range(20):
    l1.append(i)
for i in range(5):
    l2[i] = i + 1
print(l1)
print(l2)
'''
'''
a = int(input())
b = int(input())
print('Sum =',a+b)
print('Difference =',a-b)
print('Product =',a*b)
print('Float Division =',a/b)
print('Integer Division =',a//b)
'''
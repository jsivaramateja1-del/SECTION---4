# # Comprehension

# # List 
# l = [i for i in range(0,5)]
# print(l)
# l1 = [i*i for i in range(0,5)]
# print(l1)
# l2 = [i for i in range(0,10) if i%2 == 0]
# print(l2)

# # Dictionary
# d1 = {i:i*i for i in range(1,7)}
# print(d1)
# d2 = {i:chr(i) for i in range(65,80)}
# print(d2)

#tuple
# t1 = () # THIS IS IMMUTTABLE
# print(type(t1))
# t2 = (12,4,4,5,7)
# print(t2[1])
# try:
#     t2[1] = 45 # Type Error
# except TypeError:
#     print("Type Error")
# print(t2[::-1])
# t3 = (2,3,5,[])
# print(t3)
# t3[3].append(45)
# print(t3)

# # casting
# l = [1,2,3,4,5]
# t5 = tuple(l) # Type Casting into list from tuple.This t5 tuple is copy of list.
# print(l)
# print(t5)
# t = (3,1,4,2,42,52,14)
# t1 = list(t) # Type Casting into tuple from list.This t1 list is copy of tuple.
# # sorting manual
# for i in range(len(t1)):
#     for j in range(i+1,len(t1)):
#         if t1[i] > t1[j]:
#             temp = t1[i]
#             t1[i] = t1[j]
#             t1[j] = temp           
# t1 = tuple(t1)
# print(t1)
# l = list(t)
# print(l)
# l.sort() # sort the same list
# k = sorted(l) # returns a new list of sorted elements
# print(k)
# print(l)

# l = ["red","orange","blue"]
# l1 = l
# l1.append("brown")
# print(l)

# l = ["red","orange","blue"]
# # l1 = [x for x in l] 
# l1 = l[:]
# l1.append("brown")
# print(l)

# # with iteration
# def mult_iter(a,b):
#     result = 0
#     while b > 0:
#         result += a
#         b -= 1
#     return result

# # with recursion
# def multi_cursion(a,b):
#     result = 0
#     if b == 0:
#         return result
#     else:
#         return a + multi_cursion(a,b-1)
# a,b = map(int,input("Enter numbers : ").split(" "))
# print(mult_iter(a,b))
# print(multi_cursion(a,b))

# fibonacci series
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
n = int(input("Enter number : "))
print(fibo(n))

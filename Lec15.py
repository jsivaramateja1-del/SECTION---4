
'''
# Method 1 for Target Sum in the list with repeating for two numbers
def target_sum(l,s):
    res = []
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] + l[j] == s:
                res.append((l[i],l[j]))
    print(res)
target_sum([1,2,3,4,2,1,34,1],3)
'''

'''
# Method 2 for Target Sum in the list without repeating for two numbers
def target_sum(l,s):
    res = []
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] + l[j] == s:
                res.append((l[i],l[j]))
    print(res)
target_sum([1,2,3,4,2,1,34,1],3)
'''
'''
# Method for Target Sum in the list with repeating for three numbers
def target_sum(l,s):
    res = []
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(j+1,len(l)):
                if l[i] + l[j] + l[k] == s:
                    res.append((l[i],l[j],l[k]))
    print(res)
target_sum([1,2,3,4,2,1,34,1],3)
'''

# slicing 
'''
#l1 = [1,24,5,6,7,8,9,92,42]
l1 = "university"
l2 = l1[2:5] # [start : end - 1]
print(l2)
l3 = l1[1:6:2] #[start : end - 1 : steps]
print(l3)
l4 = l1[:7] #[0:7]
print(l4)
l4 = l1[7:1:-1] 
print(l4)
l5 = l1[::-1]
print(l5)
'''
def longest_sub_sequence(l):
    max_length = 0
    ind2 = 0
    for i in range(len(l)):
        count = 1
        ind = i
        for j in range(i, len(l)-1):
            if l[j+1] > l[j]:
                count += 1
            else:
                break
        if count > max_length:
            max_length = count
            ind2 = ind
    print(max_length)
    print(l[ind2:ind2+max_length])
l = list(map(int,input("Enter numbers : ").split()))
longest_sub_sequence(l)
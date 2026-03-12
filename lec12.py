'''
# Removing duplicates
l = list(map(int,input("Enter numbers : ").split()))
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
'''
'''
# Highest Ocuurence out of all elements
l = list(map(int,input("Enter numbers : ").split()))
max_count = 0
max_element = None
for i in l:
    count = 0
    for j in l:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        max_element = i
print(max_element, "occurs", max_count, "times")
'''
'''
# Highest Ocuurence for each element
l = list(map(int,input("Enter numbers : ").split()))
checked = []
for i in l:
    if i not in checked:
        count = 0
        for j in l:
            if i == j:
                count += 1
        print(i, "occurs", count, "times")
        checked.append(i)
'''
'''
# dictonary
# key and value
d1 = {}
d2 = {"Abc" : 4, "Bplpl" : 5 , "1" : 8, "2" : 90} # key : value
# print(d2["Abc"])
# print(d2["Bplpl"])
print(d2.keys())
print(d2.values())
print(type(d1))
'''
# Find the numbers of occurences of the elements
'''
# l = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,4]
l = "saiuniversity_chennai_tamil_nadu"
d1 = {}
for i in l:
    if i not in d1.keys():
        d1[i] = 1
    else:
        d1[i] += 1
print(d1)
'''
'''
# Highest occurence element
# l = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,4]
d1 = {}
l = list(map(int,input("Enter the numbers : ").split()))

for i in l:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1
maximum = d1[i]
k = i
for i in d1.keys():
    if d1[i] > maximum:
        maximum = d1[i]
        k = i
print(f"{k} occurenced  {maximum}")
'''
'''
# highest occurence another way
d1 = {}
l = list(map(int,input("Enter the numbers : ").split()))
# l = "saiuniversity_chennai_tamil_nadu"

for i in l:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1
maximum = 0
k = None
for i in d1:
    if d1[i] > maximum:
        maximum = d1[i]
        k = i
print(f"{k} occurred {maximum} times")
'''

# s = "aabbbcccc"
# output = abc_abbccc
s = input("Enter string : ")
unique = ""
duplicates = ''
for ch in s:
    if ch not in unique:
        unique += ch
    else:
        duplicates += ch
print(unique+'_'+duplicates)

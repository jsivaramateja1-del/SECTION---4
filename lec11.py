'''
class my_list:
    def __init__(self):
        self.l = [0,0,0,0,0,0,0,0,0,0,0]
l = my_list()
print(type(l))
'''
'''
l = []
print(type(l))
l.append(1.2)
l.append(6)
l.append(56)
l.append(100)
l.append("university")
l.insert(2,2026)
print(l)
l.insert(5,69)
print(l)
l.pop(3) # specific index
print(l)
print(l[-1]) # negative indexing
print(l[-2])
l.pop()  # default last index
print(l) 
l.append(6)
print(l)
l.remove(6) # removes first occurence
print(l)
'''

'''
l = [2,3,5,"teja",2.4,[1,2,3]]
# one of the way to print list (prefered when the length is known)
for i in range(6):
    print(l[i],end = " ")
print()

# reverse order
for i in range(5,-1,-1):
    print(l[i],end = " ")

# another way (length is unknown)
for i in l:
    print(i)
    
print(l[3][3])
print(l[5][0])
print(l[5][1])
print(l[5][2])

for i in range(4): # teja = 4 letters
    if i < 3:
        print(l[3][i],end=",")
    else:
        print(l[3][i],end="")
'''

'''
l = list(map(int,input("Enter numbers: ").split(" ")))
maximum = l[0]
minimum = l[0]
sum = 0
count = 0
for i in l:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
    sum = sum + i
    count += 1
average = sum / count
print("Average = ",average)
print(l)
print("Maximum = ",maximum)
print("Minimum = ",minimum)
'''


# second largest and second smallest
l = list(map(int,input("Enter numbers : ").split()))
f_maximum = l[0]
s_maximum = l[1]
f_minimum = l[0]
s_minimum = l[1]
for i in l:
    if i > f_maximum:
        f_maximum = i
    if i < f_minimum:
        f_minimum = i
for i in l:
    if i > s_maximum and i < f_maximum:
        s_maximum = i
    if i < s_minimum and i > f_minimum:
        s_minimum = i
print("First Smallest = ",f_minimum)
print("Second Smallest = ",s_minimum)
print("First Largest = ",f_maximum)
print("Second Largest = ",s_maximum)

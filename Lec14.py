'''
d1 = {"A":["B","D","E"] , "B":["A"] , "C":["B","E"] , "D":["C","A"] , "E":["C","A"]}
n1 = input("Enter first node : ")
n2 = input("Enter second node : ")
print(d1.keys())
print(type(d1.keys()))
if n1 in d1.keys():
    if n2 in d1[n1]:
        print("True")
    else:
        print("False")
else:
    print("Invalid")
'''
'''
def seperate(str):
    d1 ={}
    l = []
    for i in str:
        if i not in d1.keys():
            d1[i] = 1
        else:
            d1[i] += 1
    print(d1)
    for i in d1.keys():
        k = i * d1[i]
        l.append(k)
    return l
print(seperate("cartoon")) # ['c','a','r','t','oo','n']
print(seperate("cccbbaaa")) # ['ccc','bb','aaa']
'''

def movedups(str):
    d1 = {}
    unique = ""
    duplicates = ""
    for i in str:
        if i not in d1.keys():
            d1[i] = 1
            unique += (i)
        else:
            d1[i] += 1
            duplicates += (i)
    return unique+'_'+duplicates
print(movedups("aaabbbbccccc"))
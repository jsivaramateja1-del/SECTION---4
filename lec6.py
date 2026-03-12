'''
s = "sai university "
v_count = 0
sp_count = 0
c_count = 0
for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            v_count += 1
        elif i == " ":
            sp_count += 1
        else:
            c_count += 1
print("Vowels count = %d"%(v_count))
print("Consonants count = %d"%(c_count))
print("Space count = %d"%(sp_count))
'''
'''
s = "programmingINPYTHON"
s1 =''
for i in s:
    x = ord(i)
    if (x >= 97 and x <= 122):
        s1 += chr(ord(i) - 32)
    else:
        s1 += i
print("String in upper case = %s"%(s1))
'''
'''
s = 'programming'
s[0] = "P" # TypeError : 'str' object does not support item assignment 
print(s[0])
s1 = ''
'''
'''
s1 = input("Enter a string : ")
ch = input("Enter a character :")
found = 0 #flag variable
for i in s1:
    if i == ch:
        found = 1
        print("Yes")
        break
if found == 0:
    print("No")
'''
'''
s = "sai university"
sub_string = input("Enter a sub-string : ")
if sub_string in s:
    print("Present")
else:
    print("Absent")
'''
'''
s = "sai university"
c = input("Enter character : ")
if c in s:
    print("Present")
else:
    print("Absent")
'''
'''
s = "sai university"
c = input("Enter character : ")
if c not in s:
    print("Absent")
else:
    print("Present")
'''
'''
# a = 2356
#sum of square of digits
# while loop
num = int(input("Enter an integer : "))
rem = 0
sum = 0
while num != 0:
    rem = num%10
    sum = sum + rem * rem
    num = num//10
print("Sum of square of digits = %d"%(sum))
'''
'''
# a = 2356
#sum of cubes of digits
# while loop
num = int(input("Enter an integer : "))
rem = 0
sum = 0
while num != 0:
    rem = num%10
    sum = sum + rem ** 3
    num = num//10
print("Sum of cubes of digits = %d"%(sum))
'''
'''
num = 0
while True:
    num = int(input("Enter an number (1 to stop): "))
    if num == 1:
        break
    else:
        continue
'''
'''
a = int(input("Enter an integer 1 : "))
b = int(input("Enter an integer 2 : "))
try:
    print(a/b)
except ZeroDivisionError:
    print("Ok But We Can Continue")
print("Program ends")
'''
'''
s = "sai"

for i in range(0,9):
    try:
        print(s[i],end="")
    except IndexError:
        continue
'''
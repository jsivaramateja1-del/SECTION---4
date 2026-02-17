'''
# string
s = "Teja"
s1 = "Rama "
s2 = "Siva"
s3 = s2 + " " +s1 + s
print(s3)
print("Name : %s "%(s2 + " " + s1 +s))
'''
'''s = input("Enter a string : ") # input = something
#syntax of for loop
for i in range(0,9): #(start,ending)
    print(s[i])
'''
'''
s = input("Enter a string : ")
for i in range(0,9):
    print(s[i])
'''
'''
#method
s = input("Enter an string : ")
for i in s:
    print(i,end='')
'''
'''
s = input("Enter an string : ")
for i in s:
    print(i,end=',')
'''
'''
s = "SaiUniversity"
for i in range(0,13,):
    print(s[i],end="")
'''
'''
s = "SaiUniversity"
for i in range(0,13,3): #(starting , ending , number of steps)
    print(s[i],end="")
'''
'''
# Reversing a string
s = "SaiUniversity"
for i in range(12,-1,-1): #(starting , ending , number of steps)
    print(s[i],end="")
'''
'''
# Odd numbers upto 20
for i in range(1,20,2):
    print(i,end=" ")
'''
'''
# numbers divisible by 4 upto 14
for i in range(1,15):
    if i%4==0:
        print(i)
'''
'''
# numbers divisible by either 2 or 3 upto 50
for i in range(1,51):
    if i%2==0 or i%3==0:
        print(i,end=" ")
'''
'''
# numbers divisible by both 2 or 3 upto 50
for i in range(1,51):
    if i%2==0 and i%3==0:
        print(i,end=" ")
'''
'''
# while loop example : 
p = 12345
i = 0
#syntax of while loop
while i<8:
    print(i,end = " ")
    i+=1
'''
'''
# counting number of digits and sum of digits
a = int(input("Enter an integer : "))
count = 0
rem = 0
while a!=0:
    rem += a%10
    a = a//10
    count += 1
print("Number of digits = %d."%(count))
print("Sum of digits = %d"%(rem))
'''
'''
# Print all odd indexes of number
n = input("Enter an integer : ")
for i in range(len(n)):
    if i%2!=0:
        print(i,end=" ")
'''

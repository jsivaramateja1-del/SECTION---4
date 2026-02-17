'''
# write a program such ask numbers from user and add them until sum exceeds 100 using while loop.
sum = 0
while sum < 100 :
    if sum >= 100:
        break
    else:
        a = int(input("Enter an number : "))
        sum += a
print("Sum = ",sum)
'''

'''
# syntax of functions
def greet():
    print("Hello from great")
    return 1
# By default python function returns None
# greet()
print(greet())
'''
'''
def sum2(a,b):
    return a+b
x = int(input("Enter an number : "))
y = int(input("Enter an number : "))
print("The sum of two numbers are :",sum2(x,y))
'''
'''
def factorial_1(n):
    if n == 0 or n == 1:
        return 1
    #else:
    #    return n * factorial_1(n-1)
    # pass #placeholder
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
    

a = int(input("Enter an integer to find factorial : "))

b = factorial_1(a)

print(f"the factorial of a number {a} is {b}")
'''
'''
# convert uppercase letters in a word into lowercase letters with return
def to_lower(n):
    ch = ''
    for i in range(len(n)):
        if 65 <= ord(n[i]) <= 90:
            ch += chr(ord(n[i]) + 32)
        else:
            ch += n[i]
    return ch
a = input("Enter a string : ")
print("String in lower case :",to_lower(a))
'''
'''
# convert uppercase letters in a word into lowercase letters without return
def to_lower(n):
    ch = ''
    for i in n:
        if 65 <= ord(i) <= 90:
            ch += chr(ord(i) + 32)
        else:
            ch += i
    print("String in lower case :",ch)
a = input("Enter a string : ")
to_lower(a)
'''
'''
# count the number of digits using functions
def ncount(n):
    i = 0
    count = 0
    if n == 0:
        return 1
    while n != 0:
        a = n%10
        count += 1
        n = n // 10
        i += 1
    return count
a = int(input("Enter a number : "))
print("Count of Digits =",ncount(a))
'''
'''
# convert uppercase letters in a word into lowercase letters with return
def to_lower(n):
    ch = ''
    for i in range(len(n)):
        if (65 <= ord(n[i]) <= 90) or (97 <= ord(n[i]) <= 122):
            ch += chr(ord(n[i]) ^ 32) # With Bitwise operator
        # elif 97 <= ord(n[i]) <= 122:
        #    ch += chr(ord(n[i]) - 32) # Without Bitwise operator
        else:
            ch += n[i]
    return ch
a = input("Enter a string : ")
print("New String :",to_lower(a))
'''


'''
#Write a program that takes input a positive integer and prints the quotient and remainder. When the number divided by 2.
n = int(input("Enter an number : "))
quotient = n >> 1
remainder = n & 1
print("Quotient = %d"%quotient)
print("Remainder = %d"%remainder)
'''
'''
#Using bitwise operator tell number is divisble by 4 or not.
n = int(input("Enter an number : "))
if n & 3 == 0:
    print("%d is divisible by 4."%n)
else:
    print("%d is not divisble by 4."%n)
'''
'''
#Using bitwise operator tell number is divisble by 8 or not.
n = int(input("Enter an number : "))
if n & 7 == 0:
    print("%d is divisible by 8."%n)
else:
    print("%d is not divisble by 8."%n)
'''
'''
#Using bitwise operator tell number is divisble by 16 or not.
n = int(input("Enter an number : "))
if n & 15 == 0:
    print("%d is divisible by 16."%n)
else:
    print("%d is not divisble by 16."%n)
'''

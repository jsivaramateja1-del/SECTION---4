'''
s = "sai university"
if isinstance(s,str):
    print("It is string.")
else:
    print("It is not string.")
'''

'''
s1 = "sanjay"
if s1.isalpha():
    print("Only alphabets.")
else:
    print("Not only alphabets")
'''

'''
s2 = 19
if s2.isnumeric():
    print("Only numbers.")
else:
    print("Not only numbers.")
'''

'''
s3 = "sanjay@123"
if s3.isalnum():
    print("Only alphabets and numbers.")
else:
    print("Not only alphabets and numbers.")
'''

'''
try:
    a = int(input("Enter an integer : "))
    b = int(input("Enter an integer : "))
    c = a // b
except ZeroDivisionError:
    print("Zero Division Error is occured.")
else:
    print("Result : %d" % c)
finally:
    print("Successfully executed.")
'''

'''
import math
try:
    b = int(input())
    a = math.sqrt(b)
except ValueError:
    print("Negative Input is given.")
    print("Result : %f" % math.sqrt(abs(b)))
else:
    print("Result : %f" % a)
finally:
    print("Code executed successfully.")
'''

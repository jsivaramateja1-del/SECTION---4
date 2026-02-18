'''
#if else
a = 150
if a > 100:
    print("Greater than 100")
if a > 120:
    print("Greater than 120")
if a > 140:
    print("Greater than 140")
else:
    print("nothing")
'''
'''
# example for if else
user_name = "teja123"
password = "teja@123"
print("Enter login credentials :")
a = input("Enter Username : ")
b = input("Enter Password : ")
if a == user_name and b == password:
    print("Login Successful")
else:
    print("Wrong Credentials")
'''
'''
# if elif and else
a = int(input('Enter a number:'))
if a%7==0 and a%9==0:
    print('Number is divisible by 7 and 9')
elif a%9==0:
    print('Number is divisible by 9')
elif a%7==0:
    print('Number is divisible by 7')
else:
    print('Number is not divisible by 7 and 9')
'''
'''
# divisibilty
num = int(input("Enter a number:"))
if num%7==0:
    print("Number is divisible by 7")
    if num%9==0:
        print("Number is divisble by 9")
    else:
        print("Number is not divisble by 9")
else:
    if num%9==0:
        print("Number is divisible by 9")
    else:
        print("Number is not divisible by 7 and 9")
'''
'''
# even and odd
a = int(input("Enter an number:"))
if a%2==0:
    print("Even number")
else:
    print("Odd number")
'''
'''
a = int(input("Enter an number:"))
b = int(input("Enter an number:"))
op = input("Enter any operator (+,-,*,/,//,%) :")
if op =='+':
    print('Sum = %d'%(a+b))
elif op =='-':
    print('Difference = %d'%(a-b))
elif op =='*':
    print('Product = %d'%(a*b))
elif op == '/':
    print('Float division = %d'%(a/b))
elif op == '//':
    print('Integer division = %d'%(a//b))
elif op == '%':
    print('Remainder = %d'%(a%b))
else:
    print("Give correct operator")
'''
'''
length = int(input("Enter Length :"))
breadth = int(input("Enter Breadth :"))
print(f"Area {length*breadth}")
print(f"Perimeter {2*(length+breadth)}")
'''
'''
a = -5
b = 3
print(a%b)
'''
a = int(input("Enter a value :"))
b = int(input("Enter b value :"))
c = int(input("Enter c value :"))
d = b**2-4*a*c
if d >= 0:
    print("Roots are real.")
else :
    print("Roots are complex.")
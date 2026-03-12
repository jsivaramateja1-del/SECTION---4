'''
#Decimal to Binary, Octal and Hexadecimal Conversion
num = int(input("Enter a decimal number: "))
print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))
'''
'''
# Bitwise Operators in Python 
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = a & b  #AND
d = a | b  #OR
e = a ^ b  #XOR
f = ~a     #NOT
g = a << 2 #Left Shift adds 2 bits means multiply by 4
h = a >> 2 #Right Shift removes 2 bits means divide by 4
print("AND:", c)
print("OR:", d)
print("XOR:", e)
print("NOT:", f)
print("Left Shift:", g)
print("Right Shift:", h)
'''
'''
#Finding a number is even or odd using Bitwise Operator
a = int(input("Enter an integer: "))
if a & 1 == 0:
    print(f"{a} is Even.")
else:
    print(f"{a} is Odd.")
'''
'''
#Left Shift and Right Shift Operators
num = int(input("Enter a number: "))
print(num<<1)  
print(num>>1)
'''
'''
#Ascii value of a character
char = input("Enter a character: ")
print(f"Ascii value of {char} is {ord(char)}")
'''
'''
#Ascii character from a value
val = int(input("Enter an integer value: "))
print(f"Character for ascii value {val} is {chr(val)}")
'''
'''
#Swapping of two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Method 1
a, b = x, y
a = a + b
b = a - b
a = a - b
print("Method 1:", a, b)

# Method 2
a, b = x, y
a = a ^ b
b = a ^ b
a = a ^ b
print("Method 2:", a, b)

# Method 3
a, b = x, y
if b != 0:
    a = a * b
    b = a // b
    a = a // b
    print("Method 3:", a, b)
else:
    print("Method 3: Not possible (division by zero)")

# Method 4
a, b = x, y
a, b = b, a
print("Method 4:", a, b)
'''
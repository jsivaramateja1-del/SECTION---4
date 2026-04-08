'''
# counting number of digits in a number using recursion
def count(n):
    if n == 0:
        return 0
    else:
        return 1 + count(n//10)
    
n = int(input("Enter an number : "))
print(count(n))
'''
'''
# count the number of characters in a string
def str_count(string):
    if string == "":
        return 0
    else:
        return 1 + str_count(string[1:])
    
string = input("Enter string : ")
print(str_count(string))
'''

'''
# multiplication of two numbers using recursion
def mutliply(a,b):
    if b == 0:
        return 0
    else:
        return a + mutliply(a,b-1)
        
a = int(input("Enter number : "))
b = int(input("Enter number : "))
print(mutliply(a,b))
'''



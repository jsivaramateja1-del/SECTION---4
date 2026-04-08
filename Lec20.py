'''
def coin_change(amount,coin):
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    if coin == 0:
        return 0
    if coin == 5:
        return coin_change(amount-5,5) + coin_change(amount,2)
    elif coin == 2:
        return coin_change(amount-2,2) + coin_change(amount,1)
    else:
        return coin_change(amount-1,1)
    
amount = 6
print("Number of ways : %d" %(coin_change(amount,5)))
'''

'''
# Reverses elements of a tuple with the least possible time complexity using type casting
def reverse_tuple(tup):
    tup = list(tup)
    return tuple(reversed(tup))

tup = (1, 2, 3, 4, 5)
print(reverse_tuple(tup))
'''

'''
def find_common_elements(t1,t2):
    result = []
    for i in t1:
        if i in t2:
            result.append(i)
            
    return tuple(result)

t1 = (1,2,3,4,5)
t2 = (3,4,5,6,7)
print(find_common_elements(t1,t2))
'''


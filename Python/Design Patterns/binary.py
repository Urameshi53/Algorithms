# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:08:55 2023

@author: User
"""

'''Binary Search Iterative'''
high = 100 
low = 0
ans = 0
num = 73
guess = 0
while ans != num:
    ans = (high+low)//2
    if ans < num:
        low = ans 
    else:
        high = ans 
    guess += 1
    # print(ans)
    
# print(guess)

    
'''Binary Search - Recursive'''
def bsearch(num, high, low):
    ans = (high+low)//2
    print(ans)
    if ans == num:
        return True
    elif ans < num:
        return bsearch(num, high, ans)
    else:
        return bsearch(num, ans, low)
    
print(bsearch(1,100,0))

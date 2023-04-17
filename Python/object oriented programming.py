# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 21:23:06 2021

@author: User
"""

class one:
    def __init__(self, max=0):
        self.max = max
        
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
            

def my_gen():
    n = 1
    print('This is printed first')
    yield n
    n = 2
    print('This is printed second')
    yield n
    n = 3
    print('This is printed third')
    yield n
    
n_gen = my_gen()
# print(next(n_gen))

# for i in n_gen:
#     print(i)

def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1,-1,-1):
        yield my_str[i]
        
# for char in rev_str('hello'):
#     print(char)

my_list = [1,3,6,10]
list_ = [x**2 for x in my_list]
generator = (x**2 for x in my_list)

# print(list_)
# for i in generator:
#     print(i)


def PowTwoGen(max=0):
    n = 0
    while n < max:
        n+=1
        yield 2 ** n

n = PowTwoGen(5)
# for i in n:
#     print(i)

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2
        
print(sum(square(fibonacci_numbers(10))))




# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:15:23 2021

@author: User
"""

class Stack():
    def __init__(self):
        self.items = []
        
    def push(self, item):
        return self.items.insert(0,item)
        
    def pop(self):
        return self.items.pop(0)
        
    def topEl(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return 0
    
    def isEmpty(self):
        return len(self.items)<=0
    
    def clear(self):
        self.items = []
        
    def printAll(self):
        return self.items
    
e = Stack()
e.push(1)
e.push(2)
e.push(6)
# print(e.printAll())

# num1 = input('Enter the first number: ')
# num2 = input('Enter the second number: ')

n = Stack()
m = Stack()
# for i in num1:
#     n.push(int(i))
# for i in num2:
#     m.push(int(i))
# a = Stack()
# print(n.printAll())
# print(m.topEl())
# m.pop()
# print(m.printAll())

# print(m.isEmpty())
# print(a.isEmpty())

def addition(a,b):
    c = 0
    r = Stack()
    while not(a.isEmpty()) or not(b.isEmpty()):
        # print(a.topEl(), b.topEl(), end="   ")
        c = c + a.topEl() + b.topEl()
        if not(a.isEmpty()):
            a.pop()
        if not(b.isEmpty()):
            b.pop()
        n = c%10
        r.push(n)
        c = c//10
        # print(c,n)
    if c != 0:
        r.push(c)
    num = ''
    for i in r.printAll():
        num+=str(i)
    return int(num)

# print(addition(m,n))
      
def balance_1(s):
    o = Stack()
    chs = ['(', '[', '{', '/*']
    nchs = [')', ']', '}','*/']
    for i in s:
        if i in chs:
            o.push(i)
            n = i
        elif i in nchs:
            if o.isEmpty():
                return False
            else:
                if chs.index(n)==nchs.index(i):
                    o.pop()
                else:
                    return False
    return o.isEmpty()

# print(balance('while (m < (n[8) + o]) { p = 7; /* initialize p */ r = 6; }'))
# print(balance('(a()eee))'))
# print(balance('(x+y)*(z-2*(6))'))
# print(balance('s=t[5]+u/(v*(w+y))'))
# print(balance('g[10] = h[i[9]] + (j + k) * l;'))
# print(balance('g[10] = h[i[9]] + j + k) * l;'))
# print(balance('7-(3(2*9))4)(1'))
# print(balance('(4+3)*3+3(3-8)'))


def balance(s):
    o = Stack()
    for i in s:
        if i == '(':
            o.push(i)
        elif i == ')':
            if o.isEmpty():
                return False
            else:
                o.pop()
    return o.isEmpty()

print(balance('(a()eee))'))
print(balance('(x+y)*(z-2*(6))'))
print(balance('7-(3(2*9))4)(1'))
print(balance('(4+3)*3+3(3-8)'))

        
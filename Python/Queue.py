# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:40:30 2021

@author: User
"""

import string

letters = string.ascii_lowercase
dic = {}
# print(letters)

word = 'hello world'
new = ''

for i in letters:
    for j in range(len(letters)):
        dic[j] = letters[j]
# print(dic)
for i in word:
    if i in letters:
        n = letters.index(i)
        new += dic[25-n]
    else:
        new+=i
        continue
# print(new)

# file = open("new.txt", "w")
# for i in range(4):
#     line = input()
#     file.write(line+"\n")
# file.close()

file = open("new.txt","r")
# for i in range(4):
#     print(file.readline(), end='')
file.close()

class Queue():
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        self.items.pop(0)
        
    def isEmpty(self):
        return len(self.items)==0
    
    def firstEl(self):
        return self.items[0]
        
    def print_q(self):
        return self.items
        

queue = Queue()
queue.enqueue("Emma")
queue.enqueue("Joshua")
queue.enqueue("Michael")
queue.dequeue()
print(queue.print_q())
        
        
def indicator():
    n = 4
    file = open("new.txt", "r")
    q = Queue()
    acrostic=''
    while n>0:
        copy = file.readline()
        q.enqueue(copy[0])
        print(copy)
        n-=1
    acrostic=acrostic.join(q.print_q())
    return acrostic

print(indicator())
        
        
        
        
        
        
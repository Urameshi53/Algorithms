# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:54:14 2021

@author: User
"""
import numpy as np
import pandas as pd


# Data Structures
# Stack
class Stack(object):
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.insert(0, item)
        
    def pop(self):
        self.items.pop(0)
        
    def print_stack(self):
        print(self.items)
        
    def empty(self):
        return len(self.items)<=0
        
# emma = Stack()
# emma.push(1)
# emma.push(2)
# emma.push(3)
# emma.print_stack()

# for i in range(2):
#     emma.print_stack()
#     emma.pop()
    
# emma.print_stack()

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l.insert(0,10)
# print(l)

#Queues
class Queue(object):
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items)==0
        
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        self.items.pop(0)
        
    def show_item(self, i):
        return self.items[i]
        
    def print_queue(self):
        print(self.items)
        
# ama = Queue()
# ama.enqueue(1)
# ama.enqueue(2)
# ama.enqueue(3)
# ama.print_queue()

# for i in range(2):
#     print("Printed", ama.show_item(0))
#     ama.dequeue()
    
# ama.print_queue()
# ama.dequeue()
# print(ama.is_empty())


# LinkedLists
class Node:
    def __init__(self, data, nest):
        self.data = data
        self.nest = nest
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)
        
    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return 
        curr = self.head
        while curr.nest:
            curr = curr.nest
        curr.nest = Node(data, None)
        
    def get_last_node(self):
        n = self.head
        while(n.nest != None):
            n = n.nest
        return n.data
    
    def is_empty(self):
        return self.head == None
    
    def print_list(self):
        n = self.head
        while n!=None:
            print(n.data, end = "=>")
            n = n.nest
        print()
        
    def search_node(self, target):
        n = self.head
        while n != None and n.data!=target:
            n = n.nest
        return n is not None
    
    def remove_node(self, target):
        n = self.head
        p = n
        while n!=None and n.data != target:
            p = n
            n = n.nest
        if n == self.head:
            self.head = n.nest
        else:
            p.nest = n.nest
            n.nest = None
            return p.nest.data
    
    def remove_node_2(self, target):
        predNode = None 
        curNode = self.head
        while curNode is not None and curNode.data != target:
            predNode = curNode
            curNode = curNode.nest
            
        if curNode is not None:
            if curNode is self.head:
                self.head = curNode.nest
            else:
                predNode.nest = curNode.nest
                
    def traversal(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.nest      

# sam = LinkedList()
# sam.add_at_front(6)
# sam.add_at_front(7)
# sam.add_at_front(8)
# sam.add_at_front(9)
# sam.add_at_end(10)
# sam.print_list()
# print(sam.search_node(9))
# sam.remove_node(7)
# sam.print_list()
# sam.remove_node(9)
# sam.print_list()
# sam.add_node(6)
# sam.print_list()


# Graphs
class Graph():
    def __init__(self, size):
        self.adj = [[0]*size for i in range(size)]
        self.size = size
    
    def add_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid edge", (orig,dest))
        else:
            self.adj[orig-1][dest-1] = 1
            self.adj[dest-1][orig-1] = 1
            
    def remove_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid edge")
        else:
            self.adj[orig-1][dest-1]=0
            self.adj[dest-1][orig-1]=0
            
    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print('{:4}'.format(val), end='')
                
G = Graph(4)
G.add_edge(1,3)
G.add_edge(3,4)
G.add_edge(2,4)
G.remove_edge(1,3)
G.display()

def balance(s):
    o = Stack()
    for i in s:
        if i == '(':
            o.push(i)
        elif i == ')':
            if o.empty():
                return False
            else:
                o.pop()
    return o.empty()

# print(balance('(a()eee))'))
# print(balance('(x+y)*(z-2*(6))'))
# print(balance('7-(3(2*9))4)(1'))
# print(balance('(4+3)*3+3(3-8)'))

p = [180,172,178,185,190,195,192,200,210,190,100,120]
m = 0
v = 0
c = 0
for i in p:
    m+=i
for i in p:
    v+=(i-m)**2
v = v/len(p)
s = v**0.5
# print(m,s)

x = np.array(p)
q = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(q[0][2])
# print(q.ndim)
# print(q.size)
# print(q.shape)

y = np.array([3,1,5])
# print(y)
y = np.append(y,4)
# print(y)
y = np.delete(y,0)
# print(y)
y = np.sort(y)
# print(y)

z = np.arange(2,100,3)
# print(z)

h = np.arange(1,7)
# print(h)
t = x.reshape(4,3)
# print(t)

j = np.arange(1,8,3)
k = j.reshape(3,1)
# print(k[1][0])

# print(np.mean(x))
# print(np.median(x))
# print(np.var(x))
# print(np.std(x))

# data = np.array([150000,125000,320000,540000,200000,120000,160000,230000,280000,290000,300000,500000,420000,100000,150000,280000])
# s = np.std(data)
# m = np.mean(data)
# print(m,s)
# d = m-s
# e = s+m
# t = data.size
# y = data[(data>d)&(data<e)]
# print(d,e)
# print(y)
# u = y.size
# print((u*100)/t)

data = {'ages':[14,18,24,42],'heights':[165,180,176,184]}

df = pd.DataFrame(data, index=['James','Bob','Amy','Dave'])
# print(df.loc['James'])
# print(df['ages'][0])
# print(df[['ages','heights']])
# print(df.iloc[2:4])

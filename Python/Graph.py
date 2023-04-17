# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:01:37 2022

@author: User
"""

class Node(object):
    def __init__(self, key):
        self.nest = None
        self.prev = None
        self.key = key
        self.color = ''
        self.d = 0
        self.pred = None
        

class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insert(self,x):
        x.nest = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None
        
    def printList(self):
        x = self.head 
        while(x != None):
            print(x.key)
            x = x.nest
            
# a = Node('a')
# b = Node('b')
# c = Node('c')
# l = LinkedList()
# l.insert(a)
# l.insert(b)
# l.insert(c)
# l.printList()

class Queue(object):
    def __init__(self):
        self.q = []
        
    def enqueue(self, x):
        self.q.insert(0, x)
        
    def printQueue(self):
        for i in self.q:
            print(i)
            
    def is_empty(self):
        return self.q.length == 0
    
    def dequeue(self):
        x = self.q[0]
        self.q.pop(0)
        return x
        
    
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.insert(3)
# q.insert(4)
# q.insert(5)
# q.insert(6)
# q.printQueue()        
# l = [1,2,3]
# print(l.po)

class Graph(object):
    def __init__(self):
        self.vertices = []
        
    def bfs(self):
        for i in self.vertices:
            x = i.head
            while(x != None):
                x.color = "WHITE"
                x.d = 0
                x.pred = None
                
        s = self.vertices[0].head
        s.d = 0
        s.pred = None 
        q = Queue()
        while q.is_empty() == False:
            u = q.dequeue()
            for i in self.vertices:
                v = i.head
                while(x != None):
                    v.color = "GRAY"
                    v.d = u.d+1
                    v.pred = u
                    q.enqueue(v)
            u.color = "BLACK"
            
    
            
        



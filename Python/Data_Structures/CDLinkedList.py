# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:36:05 2022

@author: User
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.prev = None 
        self.nest = None

class CDLinkedList(object):    
    def __init__(self):
        self.sent = Node(0)
        
    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev 
    
    def search(self, k):
        x = self.nil.next 
        while x!=self.nil and x.key != k:
            x = x.next 
        return x
    
    def insert(self, x):
        y = self.sent
        x.nest = y.nest
        y.nest.prev = x
        y.nest = x
        x.prev = y
        
    def printlist(self):
        x = self.sent.nest
        while x != None:
            if x.key==0:
                break
            print(x.key)
            x = x.next
            
            
# Wikepedia
class CircularDoublyLinkedList(object):
    def printForwards(self, node):
        x = node.nest
        while x != node:
            print(x.value)
            x = x.nest
        print(x.value)
    
    def printBackwards(self, node):
        x = node.nest
        while x != node:
            print(x.value)
            x = x.prev
        print(x.value)
        
        
            

C = CDLinkedList()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

C.insert(a)
C.printList()
            
            
            
            
            
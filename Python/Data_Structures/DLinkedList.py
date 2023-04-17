# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:35:47 2022

@author: User
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.prev = None 
        self.nest = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None
        
    def delete(self,x):
        if x.prev != None:
            x.prev.nest = x.nest
        else:
            self.head = self.head.nest
        if x.nest != None:
            x.nest.prev = x.prev
            
    # Wikepedia
    def remove(self, node):
        if node.prev == None:
            self.head = node.nest 
        else:
            node.prev.nest = node.nest
        if node.nest == None:
            self.last = node.prev
        else:
            node.nest.prev = node.prev
            
    def insert(self,x):
        if self.head == None and self.last == None:
            self.last = x
        x.nest = self.head 
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None
        
    # Wikepedia
    def insertBefore(self, new, old):
        new.prev = old 
        if old.nest == None:
            new.nest = None 
            self.last = new 
        else:
            new.nest = old.nest 
            old.nest.prev = new  
        old.nest = new
            
    def insertBeforem(self, new, old):
        if old.nest != None:
            new.nest = old.nest 
            old.nest.prev = new 
            old.nest = new 
        else:
            old.nest = new 
            self.last = new 
        new.prev = old
        
    # Wikepedia
    def insertAfter(self, new, old):
        new.nest = old 
        if old.prev == None:
            new.prev = None 
            self.head = new 
        else:
            new.prev = old.prev 
            old.prev.nest = new 
        old.prev = new 
        
    def insertAfterm(self, new, old):
        new.nest = old 
        if old.prev == None:
            old.prev = new 
            self.head = new
        else:
            old.prev.nest = new 
            new.prev = old.prev 
        old.prev = new
        
    def search(self,k):
        x = self.head 
        while x != None and x.value != k:
            x = x.nest 
        return x.value
    
    def printList(self):
        x = self.head 
        while x != None:
            print(x.value)
            x = x.nest 
            
    def printList2(self):
        x = self.last 
        while x != None:
            print(x.value)
            x = x.prev
            
    def insertBeginning(self, new):
        if self.head == None:
            self.head = new 
            self.last = new 
            new.prev = None 
            new.nest = None 
        else:
            self.insertBefore(self.head,new)
    
    def insertEnd(self, new):
        if self.last == None:
            self.insertBeginning(new)
        else:
            self.insertAfter(self.last, new)
    
# D = DoublyLinkedList()
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')

# D.insert(a)
# D.insert(b)
# D.insert(c)
# # D.printList()
# # print(D.head.value)
# # print('Middle')
# # D.delete(b)
# # D.printList()
# # print(D.last.value)
# D.printList()
# print('Emmanuel')
# D.insertAfterm(d, a)
# D.printList()
        
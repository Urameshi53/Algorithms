# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:27:01 2022

@author: User
"""
import string
letters = string.ascii_lowercase
alphabets = [i for i in letters]


class Node(object):
    def __init__(self):
        self.children = [None]*26
        self.is_terminal = False 
        
class Trie(object):
    def __init__(self):
        self.root = Node()
        
    def search(self, key):
        x = self.root
        for i in range(len(key)):
            character = key[i]
            if x.children[alphabets.index(character)] == None:
                return False 
            x = x.children[alphabets.index(character)]
        return x.is_terminal
    
    def insert(self, key):
        x = self.root
        for i in range(len(key)):
            character = key[i]
            characterIndex = alphabets.index(character)
            if x.children[characterIndex] == None:
                x.children[characterIndex] = Node()
            x = x.children[characterIndex]
        x.is_terminal = True
            
    def delete(self,key):
        x = self.root 
        if key == None:
            if x.is_terminal == True:
                x.is_terminal = False 
            return None 
        x.children[alphabets.index(key[0])] = self.delete(x.children[alphabets.index(key[0])])
        return x
    

keys = ["the","a","there","anaswe","any","by","their"]
output = ["Not present in trie",
              "Present in trie"]



# Trie object
t = Trie()
 
# Construct trie
for key in keys:
        t.insert(key)
        
t.delete('the')
 
# Search for different keys
print("{} ---- {}".format("the",output[t.search("the")]))
print("{} ---- {}".format("these",output[t.search("these")]))
print("{} ---- {}".format("their",output[t.search("their")]))
print("{} ---- {}".format("thaw",output[t.search("thaw")]))
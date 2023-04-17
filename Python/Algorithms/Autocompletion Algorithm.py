# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:54:50 2022

@author: User
"""

# Python3 program to demonstrate auto-complete
# feature using Trie data structure.
# Note: This is a basic implementation of Trie
# and not the most optimized one.

class Node(object):
    def __init__(self):
        self.children = {}
        self.last = False 
        
class Trie(object):
    def __init__(self):
        self.root = Node()
        
    def formTrie(self, keys):
        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)
            
    def insert(self, key):
        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        x = self.root 
        for i in key:
            if not x.children.get(i):
                x.children[i] = Node()
            x = x.children[i]
        x.last = True
        
    def suggestions(self, x, word):
        # Method to recursively traverse the trie
        # and return a whole word.
        if x.last:
            print(word)
        for i,j in x.children.items():
            self.suggestions(j, word+i)
            
    def printAutoSuggestions(self, key):
        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        x = self.root 
        for i in key:
            # no string in the Trie has the prefix
            if not x.children.get(i):
                return 0 
            x = x.children[i]
            
        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        if not x.children:
            return False
        
        self.suggestions(x, key)
        return True 

# Driver Code
keys = ["hello", "dog", "hell", "cat", "a",
        "hel", "help", "helps", "helping"]  # keys to form the trie structure.
key = "h"  # key for autocomplete suggestions.
 
# creating trie object
t = Trie()
 
# creating the trie structure with the
# given set of strings.
t.formTrie(keys)
 
# autocompleting the given key using
# our trie structure.
comp = t.printAutoSuggestions(key)
 
if comp == False:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")
 
# This code is contributed by amurdia and muhammedrijnas
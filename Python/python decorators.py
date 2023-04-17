# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:16:59 2022

@author: User
"""

def authenticator(func):
    def processor():
        u = input("What is your username? ")
        p = input("What is your password? ")
        if u == "Lancelot" and p == "password":
            func()
        else:
            print("Access Denied")
    return processor

@authenticator
def main():
    print("Welcome to the new world.")
    
    
# main()

def authenticator(func):
    def processor(*args, **kwargs):
        u = input("What is your username? ")
        p = input("What is your password? ")
        if u == "Lancelot" and p == "password":
            func(*args, **kwargs)
        else:
            print("Access Denied")
    return processor

@authenticator
def main(name):
    print(f"Welcome to the new world {name}")
    
# main("Percival")

from functools import wraps

def decorator(func):
    @wraps(func)
    def decorate():
        return func().upper()
    return decorate

@decorator
def up():
    return "Hello Percival"

print(up())
print(up.__name__)
    
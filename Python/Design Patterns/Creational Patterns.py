# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:43:43 2022

@author: User
"""

class Dialog(object):
    def createButton(self):
        button = "This is a button"
        return button
        
    def render(self):
        B = self.createButton()
        B.onClick()
        B.render()
            
class WindowsDialog(Dialog):
    def createButton(self):
        windows = WindowsButton()
        return windows
    
class WebDialog(Dialog):
    def createButton(self):
        web = HTMLButton()
        return web 
    
class LinusDialog(Dialog):
    def createButton(self):
        linus = LinusButton()
        return linus

class Button(object):
    def render(self):
        print("I am a button")
    
    def onClick(self):
        print("You clickec me")
        
class WindowsButton(Button):
    def render(self):
        print("I am a windows Button")
        
    def onClick(self):
        print("You clicked a windows button")
        
class HTMLButton(Button):
    def render(self):
        print("I am a web Button")
        
    def onClick(self):
        print("You clicked a web Button")
        
class LinusButton(Button):
    def render(self):
        print("I am a linus Button")
        
    def onClick(self):
        print("You clicked on a linus Button")
        
class Application(object):
    def __init__(self, dialogType):
        super().__init__()
        self.dialogType = dialogType
        
    def initialize(self):        
        if self.dialogType == 'windows':
            self.dialog = WindowsDialog()
        elif self.dialogType == 'web':
            self.dialog = WebDialog()
        else:
            self.dialog = LinusDialog()
    
    def main(self):
        self.initialize()
        self.dialog.render()
        
a = Application("windows")
# a.main()

b = Application("web")
# b.main()

c = Application('linus')
c.main()
        
            
            
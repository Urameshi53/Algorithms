# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:10:19 2022

@author: User
"""

class GUIFactory(object):
    def createButton(self):
        b = 0
        
    def createCheckbox(self):
        c = 0

class WinFactory(GUIFactory):
    def createButton(self):
        w = WinButton() 
        return w 
    
    def createCheckbox(self):
        c = WinCheckbox() 
        return c
        
class MacFactory(GUIFactory):
    def createButton(self):
        b = MacButton() 
        return b
        
    def createCheckbox(self):
        a = MacCheckbox()
        return a 
    
class Button(object):
    def paint(self):
        print("Button")
        
class WinButton(Button):
    def paint(self):
        print("Windows button")
        
class MacButton(Button):
    def paint(self):
        print("Mac Button")
        
class Checkbox(object):
    def paint(self):
        print("Check box")
        
class WinCheckbox(Checkbox):
    def paint(self):
        print('Windows checkbox')
        
class MacCheckbox(Checkbox):
    def paint(self):
        print('Mac checkbox')
        
class Application(object):
    def __init__(self,factory):
        self.factory = factory 
        self.button = None
        self.check = None
    
    def createUI(self):
        self.button = self.factory.createButton()
        self.check = self.factory.createCheckbox()
    
    def paintB(self):
        self.button.paint()
    
    def paintC(self):
        self.check.paint()
        
class ApplicationConfigurator(object):
    def __init__(self,platform):
        self.platform = platform
  
    def main(self):
        if self.platform == 'windows':
            factory = WinFactory()
        else:
            factory = MacFactory()
            
        app = Application(factory)
        return app
        
win = ApplicationConfigurator('windows')
app = win.main()
app.createUI()
app.paintC()
app.paintB()
    
        

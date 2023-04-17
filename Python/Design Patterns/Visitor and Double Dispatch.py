# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:00:49 2023

@author: User
"""


# class Graphic(object):
#     def draw(self):
#         pass 
    

# class Shape(Graphic):
#     _id : None
    
#     def draw(self):
#         pass 
    

# class Dot(Shape):
#     x = None 
#     y = None
    
#     def draw(self):
#         pass 
    

# class Circle(Dot):
#     radius: None 
    
#     def draw(self):
#         pass 
    

# class Rectangle(Shape):
#     height = None
#     width = None 
    
#     def draw(self):
#         pass 
    

# class CompoundGraphic(Graphic):
#     children = []
    
#     def draw(self):
#         pass 
    
    
# class Exporter(object):
#     def export(self, s: Shape):
#         print('Exporting shape.')
        
#     def export(self, d: Dot):
#         print('Exporting dot')
        
#     def export(self, c: Circle):
#         print("Exporting circle")
        
#     def export(self, r: Rectangle):
#         print("Exporting rectangle")
        
#     def export(self, cs: CompoundGraphic):
#         print('Exporting compound')
        
    
# class App:
#     def export(shape: Shape):
#         exporter = Exporter()
#         exporter.export(shape)

# app = App()
# circle = Circle()
# app.export(circle)
# Unfortunately, this will output 'Exporting shape'


class Visitor:
    def visit(self,s: Shape):
        print("Visited shape")
        
    def visit(self,d: Dot):
        print('Visited dot')
        
    
class Graphic:
    def accept(self,v: Visitor):
        pass 
    

class Shape(Graphic):
    def accept(self,v: Visitor):
        '''
        Compiler knows for sure that 'this' is a shape.
        Which means that the 'visit(s: Shape)' can be safely called.
        '''
        v.visit(self)
        

class Dot(Shape):
    def accept(self,v: Visitor):
        '''
        Compiler know that 'this' is a 'Dot'. Which means that
        the 'visit(s: Dot)' can be safely called.
        '''
        v.visit(self)
        

v = Visitor()
g = Dot() 

'''
The 'accept' method is overridden, not overloaded. Compiler binds it
dynamically. Therefore the 'accept' will be executed on a class that 
corresponds to an object calling it a metho (in our case, the 'Dot' class)
'''
g.accept(v)

# Output: 'Visited dot'


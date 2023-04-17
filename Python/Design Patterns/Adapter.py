# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:34:17 2023

@author: User
"""


# import math

# '''
# Say you have two classes with compatible interfaces: Roundhole and RoundPeg.
# '''
# class RoundHole:
#     def __init__(self, radius):
#         self.radius = radius 
        
#     def getRadius(self):
#         #pass # Return the radius of the hole.
#         return self.radius
        
#     def fits(self, peg):
#         return self.getRadius() >= peg.getRadius()
    

# class RoundPeg:
#     def __init__(self, radius):
#         self.radius = radius 
        
#     def getRadius(self):
#         # pass # Return the radius of the peg.
#         return self.radius
        
    
# # But there's an incompatible class: SquarePeg
# class SquarePeg:
#     def __init__(self, width):
#         self.width = width 
    
#     def getWidth(self):
#         # pass # Return the square peg width 
#         return self.width
        

# '''
# An adapter class lets you fit square pegs into round holes. It extends the 
# RoundPeg class to let the adapter objects act as round pegs.
# '''
# class SquarePegAdapter(RoundPeg):
#     '''
#     In reality, the adapter contains an instance of the SquarePeg class.
#     '''
#     peg: SquarePeg 
    
#     def __init__(self, peg: SquarePeg):
#         self.peg = peg 
        
#     def getRadius(self):
#         '''
#         The adapter pretends that it's a round peg with a radius that could
#         fit the square peg that the adapter actually wraps
#         '''
#         return self.peg.getWidth() + math.sqrt(2)/2
    

# # Somewhere in client code.
# hole = RoundHole(5)
# rpeg = RoundPeg(5)
# hole.fits(rpeg) # true 

# small_sqpeg = SquarePeg(5)
# large_sqpeg = SquarePeg(10)
# hole.fits(small_sqpeg) # this won't compile (incompatible types)

# small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
# large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
# hole.fits(small_sqpeg_adapter) # True
# hole.fits(large_sqpeg_adapter) # False


'''
Conceptual Example (via inheritance)
'''
# class Target:
#     '''
#     The Target defines the domain-specific interface used by the client code.
#     '''
    
#     def request(self) -> str:
#         return "Target: The default target's behavior"
    
    
# class Adaptee:
#     '''
#     The Adaptee contains some useful behavior, but its interface is 
#     incompatible with the existing client code. The Adaptee needs some
#     adaptation before the client code can use it.
#     '''
    
#     def specific_request(self) -> str:
#         return '.eetpadA eht fo roivaheb laicepS'
    

# class Adapter(Target, Adaptee):
#     '''
#     The Adapter makes the Adaptee's interface compatible with the target's
#     interface via multiple inheritance.
#     '''
    
#     def request(self) -> str:
#         return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"
    

# def client_code(target: 'Target') -> None:
#     '''
#     The client code supports all classes that follow the Target interface.
#     '''
    
#     print(target.request(), end='')
    

# if __name__=="__main__":
#     print('Client: I can work just fine with the Target objects:')
#     target = Target()
#     client_code(target)
#     print('\n')
    
#     adaptee = Adaptee()
#     print('Client: The Adapter class has a weird interface. See, I don\'t understand it:')
#     print(f'Adapter: {adaptee.specific_request()}', end='\n\n')
    
#     print('Client: But I can work with it via the Adapter:')
#     adapter = Adapter()
#     client_code(adapter)
    
    

'''
Conceptual Example (via object composition)
'''
class Target:
    '''
    The Target defines the domain-specific interface used by the client code.
    '''
    
    def request(self) -> str:
        return 'Target: The default target\'s behavior.'
    
    
class Adaptee:
    '''
    The Adaptee contains some useful behavior, but its interface is 
    incompatible with the existing client code. The Adapter needs some 
    adaptation before the client code can use it.
    '''
    
    def specific_request(self) -> str:
        return '.eetpadA eht fo roivaheb laicepS'
    

class Adapter(Target):
    '''
    The Adapter makes the Adapter's interface compatible with the Target's 
    interface via composition.
    '''
    
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee 
        
    def request(self) -> str:
        return f'Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}'
    

def client_code(target: Target) -> None:
    '''
    The client code supports all classes that follow the Target interface.
    '''
    
    print(target.request(), end='')
    

if __name__=='__main__':
    print('CLient: I can work just fine with the Target objects:')
    target = Target() 
    client_code(target)
    print('\n')
    
    adaptee = Adaptee() 
    print('Client: The Adaptee class has a weird interface. See I don\'t understand it:')
    print(f'Adaptee: {adaptee.specific_request()}', end='\n\n')
    
    print('Client: But I can work with it via the Adapter:')
    adapter = Adapter(adaptee)
    client_code(adapter)






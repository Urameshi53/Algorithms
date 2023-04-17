# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:20:20 2023

@author: User
"""

from __future__ import annotations 

# '''
# The 'implementation' interface declares methods common to all concrete
# implementation classes. It doesn't have to mathc the abstraction's interface.
# In fact, the two interfaces can be entirely different. Typically, the 
# implementation interface provides only primitive operations, while the 
# abstraction defines higher-level operations based on those primitives.
# '''
# class Device:
#     def isEnabled(self):
#         pass 
    
#     def enable(self):
#         pass 
    
#     def disable(self):
#         pass
    
#     def getVolume(self):
#         pass 
    
#     def setVolume(self, percent):
#         pass
    
#     def getChannel(self):
#         pass 
    
#     def setChannel(self):
#         pass 


# '''
# The 'abstraction' defines the interface for the 'control' part of 
# the two class hierarchies. It maintains a reference to an object 
# of the 'implementation' hierarchy and delegates all of the real 
# work to this object.
# '''
# class RemoteControl:
#     device: Device
    
#     def __init__(self, device: Device):
#         self.device = device
        
#     def togglePower(self):
#         if self.device.isEnabled():
#             self.device.disable()
#         else:
#             self.device.enable()
            
#     def volumeDown(self):
#         self.device.setVolume(self.device.getVolume() - 10)
        
#     def volumeUp(self):
#         self.device.setVolume(self.device.getVolume() + 10)
        
#     def channelDown(self):
#         self.device.setChannel(self.device.getChannel() - 1)
        
#     def channelUp(self):
#         self.device.setChannel(self.device.getChannel() + 1)
        
    
# '''
# You can extend classes from the abstraction hierarchy independently 
# from device classes.
# '''
# class AdvancedRemoteControl(RemoteControl):
#     def mute(self):
#         self.device.setVolume(0)
            

# # All devices follow the same interface.
# class Tv(Device):
#     pass


# class Radio(Device):
#     pass 


# # Somewhere in client code 
# tv = Tv()
# remote = RemoteControl(tv)
# remote.togglePower()

# radio = Radio()
# remote = AdvancedRemoteControl(radio)
    

'''
Conceptual Example
'''
from abc import ABC, abstractmethod 


class Abstraction:
    '''
    The Abstraction defines the interface for the 'control' part of the two
    class hierarchies. It maintains a reference to an object of the 
    implementation hierarchy and delegates all of the real work to this object.
    ''' 
    
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation 
        
    def operation(self) -> str:
        return (f'Abstraction: Base operations with: \n'
                f'{self.implementation.operation_implementation()}')
    

class ExtendedAbstraction(Abstraction):
    '''
    You can extend the Abstraction without changing the implementation classes.
    '''
    
    def operation(self) -> str:
        return (f'ExtendedAbstraction: Extended operation with:\n'
                f'{self.implementation.operation_implementation()}')
    

class Implementation(ABC):
    '''
    The implementation defines the interface for all implementation classes.
    It doesn't have to match the Abstraction's interface. In fact, the two 
    interfaces can be entirely different. Typically, the implementation 
    interface provides only primitive operations, while the Abstraction 
    defines higher-level operations based on those primitives.
    '''
    
    @abstractmethod 
    def operation_implementation(self) -> str:
        pass 
    

'''
Each Concrete Implementation corresponds to a specific platform and implements
the Implementation interface using that platform's API.
'''
class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return 'ConcreteImplementationA: Here\'s the result of the platform A.'
    
    
class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return 'ConcreteImplementationB: Here\'s the result on the platform B.'
    
    
def client_code(abstraction: Abstraction) -> None:
    '''
    Except for the initialization phase, where an Abstraction object gets 
    linked with a specific Implementation object, the client code should only
    depend on the Abstraction class. This way the client code can support 
    any abstraction-implementation combination.
    '''
    
    # ...
    print(abstraction.operation(), end='')
    # ...
    
    
if __name__ == '__main__':
    '''
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    '''
    
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)
    
    print('\n')
    
    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
    
    
    




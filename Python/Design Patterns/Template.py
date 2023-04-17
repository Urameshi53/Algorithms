# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:46:26 2023

@author: User
"""

# from abc import ABC, abstractmethod

# '''
# The abstract class defines a template method that contains a skeleton of some 
# algorithm composed of calls, usually to abstract primitive operations. 
# Concrete subclasses implement these operations, but leave the template method
# itself intact.
# '''

# class GameAI:
#     '''
#     The template method defines the skeleton of an algorithm
#     '''
    
#     def turn(self):
#         self.collectResources()
#         self.buildStructures()
#         self.buildUnits()
#         self.attack()
        
#     ''' 
#     Some of the steps may be implemented right in a base class.
#     '''
    
#     def collectResources(self):
#         # for s in self.builtStructures:
#         #     s.append()
#         pass 
    
#     ''' 
#     And some of them may be defined as abstract.
#     '''
#     @abstractmethod 
#     def buildStructures(self):
#         pass 
    
#     @abstractmethod 
#     def buildUnits(self):
#         pass
    
#     '''
#     A class can have several template methods.
#     '''
#     def attack(self):
#         enemy = closestEnemy()
#         if enemy == None:
#             self.sendScouts(map.center())
#         else:
#             self.sendWarriors(enemy.position)
            
#     @abstractmethod 
#     def sendScouts(self, position):
#         pass 
    
#     @abstractmethod 
#     def sendWarriors(self, position):
#         pass
    

# '''
# Concrete classes have to implement all abstract operations of the base class
# but they must not override the template method itself.
# '''

# class OrcsAI(GameAI):
#     def buildStructures(self):
#         if (there are some resources):
#             pass ''' Build farms, then barracks, then stronghold.'''
            
    
#     def buildUnits(self):
#         if (there are plenty of resources):
#             if(there are no scouts):
#                 pass # Build peon, add it to scouts group.
#             else:
#                 pass # Build grunt, add it to warriors group.
                
#     # ....
    
#     def sendScouts(self, position):
#         if scout.length > 0:
#             pass # Send scouts to position.
            
#     def sendWarriors(self, position):
#         if warriors.length > 5:
#             pass # Send warriors to position
            

# '''
# Subclasses can also override some operations with a default implementation.
# '''

# class MonsterAI(GameAI):
#     def collectResources(self):
#         pass # Monsters don't collect resources.
        
#     def buildStructures(self):
#         pass # Monsters don't build structures.
        
#     def buildUnits(self):
#         pass # Monsters don't build units.
        

'''
Conceptual Example
'''

from abc import ABC, abstractmethod 

class AbstractClass(ABC):
    '''
    The Abstract Class defines a template method that contains a skeleton of 
    some algorithm, composed of calls to (usually) abstract primitive 
    operations.
    '''
    
    def template_method(self) -> None:
        '''
        The template method defines the skeleton of an algorithm

        Returns
        -------
        None
            DESCRIPTION.

        '''
        
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()
        
    # These operations already have implementations.
    
    def base_operation1(self) -> None:
        print('AbstractClass says: I am doing the bulk of the work.')
        
    def base_operation2(self) -> None:
        print('AbstractClass says: But I let subclasses override some operations.')
        
    def base_operation3(self) -> None:
        print('AbstractClass says: But I am doing the bulk of the work anyway')
        
    # These operations have to be implemented in subclasses
    
    @abstractmethod 
    def required_operations1(self) -> None:
        pass 
    
    @abstractmethod 
    def required_operations2(self) -> None:
        pass 
    
    '''
    These are 'hooks'. Subclasses may override them, but it's not mandatory 
    since the hooks already have default (but empty) implementation. Hooks
    provide additional extensions points in some crucial places of the 
    algorithm.
    '''
    
    def hook1(self) -> None:
        pass
    
    def hook2(self) -> None:
        pass
    

class ConcreteClass1(AbstractClass):
    '''
    Concrete classes have to implement all abstract operations of the base 
    class. They can also override some operations with a default 
    implementation.
    '''
    
    def required_operations1(self) -> None:
        print('ConcreteClass1 says: implemented operation1')
        
    def required_operations2(self) -> None:
        print('ConcreteClass1 says: Implemented Operation2')
        
    
class ConcreteClass2(AbstractClass):
    '''
    Usually, concrete classes override only a fraction of base class 
    operations.
    '''
    
    def required_operations1(self) -> None:
        print('ConcreteClass2 says: Implemented Operation1')
        
    def required_operations2(self) -> None:
        print('ConcreteClass2 says: Implemented Operation2')

    def hook1(self) -> None:
        print('ConcreteClass2 says: Overridden Hook1')


def client_code(abstract_class: AbstractClass) -> None:
    '''
    The client code calls the template method to execute the algorithm. 
    Client code does not have to know the concrete class of an object 
    it works with, as long as it works with objects through the 
    interface of their base class.
    

    Parameters
    ----------
    abstract_class : AbstractClass
        DESCRIPTION.

    Returns
    -------
    None
        DESCRIPTION.

    '''    
    
    # ....
    abstract_class.template_method() 
    # ....
    

if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print('')
    
    print('Same client code can work with different subclasses:')
    client_code(ConcreteClass2())
    
    
    
    
    
    
        


# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:35:39 2023

@author: User
"""


# '''
# The Strategy interface declares operations common to all supported 
# versions of some algorithm. The context uses this interface to call 
# the algorithm defined by the concrete strategies.
# '''

# class Strategy(object):
#     def execute(self,a,b):
#         pass 
    
# '''
# Concrete strategies implement the algorithm while following the 
# base strategy interface. The interface makes them interchangeable 
# in the context.
# '''

# class ConcreteStrategyAdd(Strategy):
#     def execute(self,a,b):
#         return a + b


# class ConcreteStrategySubtract(Strategy):
#     def execute(self,a,b):
#         return a-b 
    

# class ConcreteStrategyMultiply(Strategy):
#     def execute(self, a, b):
#         return a*b
    
    
# class Context:
#     strategy: Strategy 
    
#     def setStrategy(self, strategy: Strategy) -> None:
#         self.strategy = strategy 
        
#     def executeStrategy(self, a: int, b: int):
#         return self.strategy.execute(a,b)
    

# if __name__ == "__main__":
#     context = Context() 
#     a = 5
#     b = 6
#     action = input("Enter operation: ")
    
#     if action == 'add':
#         context.setStrategy(ConcreteStrategyAdd())
        
#     if action == 'sub':
#         context.setStrategy(ConcreteStrategySubtract())
        
#     if action == 'mult':
#         context.setStrategy(ConcreteStrategyMultiply())
    
#     result = context.executeStrategy(a, b)
#     print(result)


from __future__ import annotations 
from abc import ABC, abstractmethod 
from typing import List 

class Context():
    '''
    The context defines the interface of interest to clients.
    '''
    
    def __init__(self, strategy: Strategy) -> None:
        '''
        Usually, the context accepts a strategy through the constructor,
        but also provides a setter to change it at runtime.
        '''
        
        self._strategy = strategy 
        
    @property 
    def strategy(self) -> Strategy:
        '''
        The context maintains a reference to one of the strategy objects.
        The context does not know the concrete class of a strategy. It 
        should work with all strategies via the strategy interface.
        '''
        
        return self._strategy 
    
        '''

        Parameters
        ----------
        strategy : Strategy
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        '''

    @strategy.setter 
    def strategy(self, strategy: Strategy) -> None:
        '''
        Usually, the context allows replacing a Strategy object at runtime.
        '''
        
        self._strategy = strategy
        
    def do_some_business_logic(self) -> None:
        '''
        The Context delegates some work to the Strategy object instead of 
        implementing multiple versions of the algorithm on its own.
        '''
        
        '''

        Parameters
        ----------
        strategy : Strategy
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        '''
        # ....
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(['a','b','c','d','e'])
        print(','.join(result))
        # ....
        

class Strategy(ABC):
    ''' 
    The Strategy interface declares operations common to all supported versions of 
    some algorithm.
    
    The Context uses this interface to call the algorithm defined by Concrete 
    Strategies.
    '''
    
    @abstractmethod
    def do_algorithm(self, data: List):
        pass
    

''' 
Concrete Strategies implement the algorithm while following the base Strategy 
interface. The interface makes them interchangeable in the Context.
'''


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)
    

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))
    

if __name__ == "__main__":
    '''
    The client code picks a concrete strategy and passes it to the context. The 
    client should be aware of the differences between strategies in order to 
    make the right choice.
    '''
    
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print() 
    
    print("CLient: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB() 
    context.do_some_business_logic()
        




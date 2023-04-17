# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:56:57 2023

@author: User
"""

from __future__ import annotations
from abc import ABC, abstractmethod 


class Context:
    '''
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    '''
    _state = None
    '''
    A reference to the current state of the Context.
    '''
    def __init__(self, state: State) -> None:
        self.transition_to(state)
        
    def transition_to(self, state: State):
        '''
        The Context allows changing the State object at runtime.
        '''
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state 
        self._state.context = self 
        
    '''
    The Context delegates part of its behavior to the current State object.
    '''
    
    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()
    

class State(ABC):
    '''
    The base State class declares methods that all Concrete State should 
    implement and also provides a backreference to the Context object, 
    associated with the State. This backreference can be used by States 
    to transition the Context to another State.
    '''
    @property 
    def context(self) -> Context:
        return self._context 
    
    @context.setter 
    def context(self, context: Context) -> None:
        self._context = context 
        
    @abstractmethod 
    def handle1(self) -> None:
        pass 
    
    @abstractmethod 
    def handle2(self) -> None:
        pass 
    

''' 
Concrete States implement various behaviors, associated with a state 
of the context.
'''

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())
        
    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")
        

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")
        
    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())
        

if __name__ == "__main__":
    # The client code 
    
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()




'''
Real World Example Code
'''

'''
The AudioPlayer class acts as a context. It also maintains a reference to an 
instance of one of the state classes that represents the current state of the
audio player.
'''

# class AudioPlayer:
#     state: State = None 
#     UI, volume, playlist, currentSong = None 
    
#     def __init__(self) -> None:
#         self.state = ReadyState()
        
#         '''
#         Contest deligate handling user input to a state object. Naturally, the
#         outcome depends on what state is currently active, since each state 
#         can handle the input differently.
#         '''
        
#         UI = UserInterface()
#         UI.lockButton.onClick(self.clickLock)
#         UI.playButton.onClick(self.clickPlay)
#         UI.nextButton.onClick(self.clickNext)
#         UI.prevButton.onClick(self.clickPrevious)
        
#         '''
#         Other objects must be able to switch the audio player's active state 
#         ''' 
#         def changeState(state: State):
#             self.state = state 
            
#         # UI methods delegate execution to the active state
#         def clickLock(self):
#             self.state.clickLock()
            
#         def clickPlay(self):
#             self.state.clickPlay()
            
#         def clickNext(self):
#             self.state.clickNext()
            
#         def clickPrev(self):
#             self.state.clickPrev()
            
#         # A state may call some service methods on the context.
#         def startPlayback(self):
#             pass
        
#         def stopPlayback(self):
#             pass 
        
#         def nextSong(self):
#             pass 
        
#         def prevSong(self):
#             pass
        
#         def fastForward(self, time):
#             pass 
        
#         def rewind(self, time):
#             pass
        
        
# '''
# The base state class declares methods that all concrete states  should implement
# and also provides a backreference to the context object associated with the 
# state. States can use the backreference to transition the context to another state.
# '''

# class State:
#     player: AudioPlayer = None 
    
#     '''
#     Context passes itself through the state constructor. This may help a state 
#     fetch some useful context data if it's needed.
#     '''
    
#     def __init__(self, player):
#         self.player = player 
        
#     def clickLock(self):
#         pass 
    
#     def clickPlay(self):
#         pass 
    
#     def clickNext(self):
#         pass 
    
#     def clickPrevious(self):
#         pass
    

# '''
# Concrete states implement various behaviours associated with a state of the context. 
# '''

# class LockedState(State):
#     '''
#     When you unlock a locked player, it may assume one of two states.
#     '''
    
#     def clickLock(self):
#         if player.playing():
#             player.chageState(PlayingState(player))
#         else:
#             player.changeState(ReadyState(player))
            
#     def clickPlay(self):
#         pass 
    
#     def clickNext(self):
#         pass 
    
#     def clickPrevious(self):
#         pass 
    
    
# # They can also trigger state transitions in the context.
# class ReadyState(State):
#     def clickLock(self):
#         player.changeState(LockedState(player))
        
#     def clickPlay(self):
#         player.nextSong()
        
#     def clickPrevious(self):
#         player.previousSong()
        

# class PlayingState(State):
#     def clickLock(self):
#         player.changeState(LockedState(player))
        
#     def clickPlay(self):
#         player.stopPlayback()
#         player.changeState(ReadyState(player))
        
#     def clickNext(self):
#         if event.doubleclick():
#             player.nextSong() 
#         else:
#             player.fastForward(5)
            
#     def clickPrevious(self):
#         if event.doubleclick():
#             player.previous()
#         else:
#             player.rewind(5)
            
            

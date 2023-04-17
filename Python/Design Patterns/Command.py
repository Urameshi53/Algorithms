# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:08:24 2023

@author: User
"""

from __future__ import annotations 
from abc import ABC, abstractmethod 



class Command(ABC):
    '''
    The command interface declares a method for executing a command.
    '''
    
    @abstractmethod 
    def execute(self) -> None:
        pass 
    
class SimpleCommand(Command):
    '''
    Some commands can implement simple operations on their own.
    '''
    
    def __init__(self, payload: str) -> None:
        self._payload = payload 
        
    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing {self._payload}")
        

class ComplexCommand(Command):
    ''' 
    However, some commands can delegate more complex operations to other objects, called 'receivers'.
    '''
    
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        '''
        Complex commands can accept one or several receiver objects along with any
        context data via the constructor.
        '''
        
        self._receiver = receiver 
        self._a = a
        self._b = b
        
    def execute(self) -> None:
        '''
        Commands can delegate to any method of a receiver.
        '''
        
        print('ComplexCommand: Complex stuff should be done by a receiver object', end='')
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    '''
    The Receiver classes contain some important business logic. They know how to perform all kinds
    of operations, ,associated with carrying out a request. In fact, any class may serve as a Receiver.
    '''
    
    def do_something(self, a: str) -> None:
        print(f'\nReceiver: Working on ({a}.)', end='')
        
    def do_something_else(self, b: str) -> None:
        print(f'\nReceiver: Also working on ({b}.)', end='')
        

class Invoker:
    '''
    The Invoker is associated with one or several commands. It sends a request to the command.
    '''
    
    _on_start = None 
    _on_finish = None
    
    '''
    Initialize commands.
    '''
    
    def set_on_start(self, command: Command):
        self._on_start = command 
        
    def set_on_finish(self, command: Command):
        self._on_finish = command 
        
    def do_something_important(self) -> None:
        '''
        The Invoker does not depend on concrete command or receiver classes. The Invoker passes a 
        request to a receiver indirectly, by executing a command.
        '''
        
        print('Invoker: Does anybody want something done before I begin?')
        if isinstance(self._on_start, Command):
            self._on_start.execute()
            
        print('Invoker: ...doing something really important...')
        print('Invoker: Does anybody want something done after I finish?')
        
        if isinstance(self._on_finish, Command):
            self._on_finish.execute() 
            

if __name__ == "__main__":
    '''
    The client code can parameterize an invoker with any commands.
    '''
    
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand('Say Hi!'))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, 'Send email', 'Save report'))
    
    invoker.do_something_important()
    
    
# '''
# # The base command class defines the common interface for all concrete commands.
# class Command:
#     app: Application 
#     editor: Editor 
#     backup: text 
    
#     def __init__(self, app: Application, editor: Editor):
#         self.app = app 
#         self.editor = editor 
        
#     # Make a backup of the editor's state.
#     def saveBackup(self):
#         backup = editor.text 
        
#     # Restore the editor's state.
#     def undo(self):
#         editor.text = backup 
        
#     '''
#     # The execution method is declared abstract to force all concrete commands 
#     # to provide their own implementations. The method must return true or false
#     # depending on whether the command changes the editor's state.
#     '''
#     def execute(self):
#         pass
    
    
# # The concrete commands go here
# class CopyCommand(Command):
#     # The copy command isn't saved to the history since it doesn't changet the
#     # editor's state.
#     def execute(self):
#         app.clipboard = editor.getSelection()
#         return False
    

# class CutCommand(Command):
#     '''
#     # The cut command does change the editor's state, therefore it must be 
#     # saved to the history. And it'll be saved as long as the method returns 
#     # true.
#     '''
#     def execute(self):
#         saveBackup()
#         app.clipboard = editor.getSelection()
#         editor.deleteSelection()
#         return true 
    

# class PasteCommand(Command):
#     def execute(self):
#         saveBackup()
#         editor.replaceSelection(app.clipboard)
#         return true 
    

# # The undo operation is also a command.
# class UndoCommand(Command):
#     def execute(self):
#         app.undo()
#         return False 
    

# # The global command history is just a stack.
# class CommandHistory:
#     history: []
    
#     # Last in ....
#     def push(self, c: Command):
#         # Push the command to the end of the history array.
#         pass 
    
#     # ....first out 
#     def pop(self) -> Command:
#         # Get the most recent command 
#         pass 
    
    
# '''
# # The editor class has actual text editing operations. It plays the role of a 
# # receiver: all commands end up delegating execution to the editor's methods.
# '''
# class Editor:
#     text: str 
    
#     def getSelection(self):
#         # Return selected text
#         pass
    
#     def deleteSelection(self):
#         # Delete selected text.
#         pass
    
#     def replaceSelection(self, text):
#         # Insert the clipboard's contents at the current position.
#         pass
    

# '''
# # The application class sets up object relations. It acts as a sender: when 
# # something needs to be done, it creates a command object and executes it.
# '''
# class Application:
#     clipboard: str
#     editors: []
#     activeEditor: Editor
#     history: CommandHistory
    
#     # The code which assigns commands to UI objects may look like this.
#     def createUI(self):
#         # ....
#         # copy = function() { executeCommand(
#         #     new CopyCommand(this, activeEditor)) }
#         # copyButton.setCommand(copy)
#         # shortcuts.onKeyPress("Ctrl+C", copy)

#         # cut = function() { executeCommand(
#         #     new CutCommand(this, activeEditor)) }
#         # cutButton.setCommand(cut)
#         # shortcuts.onKeyPress("Ctrl+X", cut)

#         # paste = function() { executeCommand(
#         #     new PasteCommand(this, activeEditor)) }
#         # pasteButton.setCommand(paste)
#         # shortcuts.onKeyPress("Ctrl+V", paste)

#         # undo = function() { executeCommand(
#         #     new UndoCommand(this, activeEditor)) }
#         # undoButton.setCommand(undo)
#         # shortcuts.onKeyPress("Ctrl+Z", undo)
#         pass
        
#     # Execute a command and check whether it has to be added to the history.
#     def executeCommand(self, command):
#         if command.execute():
#             history.push(command)
            
#     '''
#     # Take the most recent command from the history and run its undo method.
#     # Note that we don't know the class of that command. But we don't have to,
#     # since the command knows how to undo its own action.
#     '''
#     def undo(self):
#         command = history.pop()
#         if command != None:
#             command.undo()
# '''
            
            
    
    
    
    
    
    
    
    
    
    
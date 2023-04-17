# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:00:23 2021

@author: User
"""
#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

''' 
Chapter Two - Hello
'''
from PyQt5.QtWidgets import *
import sys

# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setWindowTitle("Hello")
#         layout = QGridLayout()
#         self.setLayout(layout)
#         label = QLabel("Hello, World!")
#         layout.addWidget(label, 0, 0)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()

# sys.exit(app.exec_())
# Download: PushButton

'''
Chapter 3 - Window
'''
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import sys

# class Window(QWindow):
#     def __init__(self):
#         QWindow.__init__(self)
#         self.setTitle("Window")
#         self.resize(400,300)
        
# app = QApplication(sys.argv)

# screen = Window()
# screen.show()

# sys.exit(app.exec_())

# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import sys

# class Window(QWindow):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setTitle("Hello")
#         self.setMinimumWidth(600)
#         self.setMinimumHeight(500)
        
# app = QApplication(sys.argv)

# screen = Window()
# screen.show()

# sys.exit(app.exec_())

# Download: PushButton


'''
Chapter 4 - BoxLayout
'''
# from PyQt5.QtWidgets import *
# import sys

# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
        
#         layout = QBoxLayout(QBoxLayout.LeftToRight)
#         self.setLayout(layout)
        
#         label = QLabel("Label 1")
#         layout.addWidget(label, 0)
#         label = QLabel("Label 2")
#         layout.addWidget(label, 0)
        
#         layout2 = QBoxLayout(QBoxLayout.TopToBottom)
#         layout.addLayout(layout2)
        
#         label = QLabel("Label 3")
#         layout2.addWidget(label, 0)
#         label = QLabel("Label 4")
#         layout2.addWidget(label, 0)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()

# sys.exit(app.exec_())


'''
Chapter 5 - GridLayout 
'''
# from PyQt5.QtWidgets import *
# import sys

# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
        
#         layout = QGridLayout()
#         self.setLayout(layout)
        
#         label = QLabel("Label (0, 0)")
#         layout.addWidget(label, 0, 0)
#         label = QLabel("Label (0,1)")
#         layout.addWidget(label, 0, 1)
#         label = QLabel("Label (1, 0) spanning 2 columns")
#         layout.addWidget(label, 1, 0, 1, 2)
#         label = QLabel("Label (1, 0) spanning 2 rows")
#         layout.addWidget(label, 0, 2, 2, 1)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()

# sys.exit(app.exec_())

'''
Chapter 6 - Label
'''
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         label = QLabel("The Story of Dale")
#         layout.addWidget(label, 0, 0)
#         label = QLabel("Few people could understand Dale's motivation. It wasn't something that was easy") 
#         label.setWordWrap(True)
#         layout.addWidget(label, 0, 1)
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())



'''
Chapter 7 - PushButton
'''
# from PyQt5.QtWidgets import *
# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         button = QPushButton("Click Me")
#         button.clicked.connect(self.on_button_clicked)
#         layout.addWidget(button, 0, 0)
        
#     def on_button_clicked(self):
#         print("The button was pressed!")
        
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


'''
Chapter 8 - RadioButton
'''
# from PyQt5.QtWidgets import *
# import sys

# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         radiobutton = QRadioButton("Brazil")
#         radiobutton.setChecked(True)
#         radiobutton.country = "Brazil"
#         radiobutton.toggled.connect(self.on_radio_button_toggled)
#         layout.addWidget(radiobutton, 0, 0)
#         radiobutton = QRadioButton("Argentina")
#         radiobutton.country = "Argentina"
#         # radiobutton.toggled.connect(self.on_radio_button_toggled)
#         layout.addWidget(radiobutton, 0, 1)
#         radiobutton = QRadioButton("Ecuador")
#         radiobutton.country = "Ecuador"
#         # radiobutton.toggled.connect(self.on_radio_button_toggled)
#         layout.addWidget(radiobutton, 0, 2)
        
#     def on_radio_button_toggled(self):
#         radiobutton = self.sender()
            
#         if radiobutton.isChecked():
#             print("Selected country is %s" % (radiobutton.country))

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 9 - CheckButton
'''
# from PyQt5.QtWidgets import *
# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.checkbox1 = QCheckBox("Kestrel")
#         self.checkbox1.setChecked(True)
#         self.checkbox1.toggled.connect(self.checkbox_toggled)
#         layout.addWidget(self.checkbox1, 0, 0)
#         self.checkbox2 = QCheckBox("Sparrowhawk")
#         self.checkbox2.toggled.connect(self.checkbox_toggled)
#         layout.addWidget(self.checkbox2, 1, 0)
#         self.checkbox3 = QCheckBox("Hobby")
#         self.checkbox3.toggled.connect(self.checkbox_toggled)
#         layout.addWidget(self.checkbox3, 2, 0)
        
#     def checkbox_toggled(self):
#         selected = []
        
#         if self.checkbox1.isChecked():
#             selected.append("Kestrel")
       
#         if self.checkbox2.isChecked():
#             selected.append("Sparrowhawk")
        
#         if self.checkbox3.isChecked():
#             selected.append("Hobby")
#             print("Selected: %s" % (" ".join(selected)))

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 10 - ToolTip
'''
# from PyQt5.QtWidgets import *
# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         button = QPushButton("Simple ToolTip")
#         button.setToolTip("This ToolTip simply displays text.")
#         layout.addWidget(button, 0, 0)
#         button = QPushButton("Formatted ToolTip")
#         button.setToolTip("<b>Formatted text</b> can also be displayed.")
#         layout.addWidget(button, 1, 0)

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 11 - WhatsThis
'''
# from PyQt5.QtWidgets import *
# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         label = QLabel("Focus ComboBox and press SHIFT+F1")
#         layout.addWidget(label)
#         self.combobox = QComboBox()
#         self.combobox.setWhatsThis("This is a 'WhatsThis' object description.")
#         layout.addWidget(self.combobox)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 12 - LineEdit
'''
# from PyQt5.QtWidgets import *
# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.lineedit = QLineEdit()
#         self.lineedit.returnPressed.connect(self.return_pressed)
#         layout.addWidget(self.lineedit, 0, 0)
        
#     def return_pressed(self):
#         print(self.lineedit.text())
            
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 13 - ButtonGroup
'''
# class Window(QWidget):
#     def __init__(self):
#         self.QandA = {
#             'What is the name of the male part of a flower':'Stamen', 'A group of Petals is called':'Corolla',
#             'A group of Sepals is called':'Calyx'
#                       }
#         QWidget.__init__(self)
#         self.create_widgets()
#         self.setMaximumWidth(500)
#         self.setMaximumHeight(500)
#         # self.resize(500,500)
        
#     def create_widgets(self):
        
#         layout = QGridLayout()
#         self.setLayout(layout)
#         label = QLabel('1. What is self pollination?')
#         layout.addWidget(label, 0, 0)
               
#         radiobutton = QRadioButton('Answer 1')
#         layout.addWidget(radiobutton, 1, 0)
        
#         radiobutton = QRadioButton('Answer 1')
#         layout.addWidget(radiobutton, 2, 0)
        
#         radiobutton = QRadioButton('Answer 1')
#         layout.addWidget(radiobutton, 1, 1)
        
#         radiobutton = QRadioButton('Answer 1')
#         layout.addWidget(radiobutton, 2, 1)
        
#         self.buttongroup = QButtonGroup()
#         self.buttongroup.setExclusive(False)
#         self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
#         button = QPushButton("Previous")
#         self.buttongroup.addButton(button, 1)
#         layout.addWidget(button, 3, 0)
#         button = QPushButton("Next")
#         self.buttongroup.addButton(button, 2)
#         layout.addWidget(button, 3, 1)
        
    
#     def on_button_clicked(self, id):
#         for button in self.buttongroup.buttons():
#             if button is self.buttongroup.button(id):
#                 print("%s was clicked!" % (button.text()))
#     def check_answer(self, question):
        

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 14 - GroupBox
'''
# from PyQt5.QtWidgets import *
# import sys
# class GroupBox(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setWindowTitle("GroupBox")
#         layout = QGridLayout()
#         self.setLayout(layout)
#         groupbox = QGroupBox("GroupBox Example")
    
#         layout.addWidget(groupbox)
#         vbox = QVBoxLayout()
#         groupbox.setLayout(vbox)
#         radiobutton = QRadioButton("RadioButton 1")
#         radiobutton.setChecked(True)
#         vbox.addWidget(radiobutton)
#         radiobutton = QRadioButton("RadioButton 2")
#         vbox.addWidget(radiobutton)
#         print(groupbox.isChecked())
# app = QApplication(sys.argv)
# screen = GroupBox()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 15 - Completer
'''
# from PyQt5.QtWidgets import *
# import sys

# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         names = ["George", "Marcus", "Samantha", "Steven", "Maria"]
#         completer = QCompleter(names)
#         self.lineedit = QLineEdit()
#         self.lineedit.setCompleter(completer)
#         layout.addWidget(self.lineedit, 0, 0)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 16 - Calendar
'''

# from PyQt5.QtWidgets import *
# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         calendar = QCalendarWidget()
#         layout.addWidget(calendar)
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

'''
Chapter 17 - Dialogue Box
'''

# from PyQt5.QtWidgets import *
# import sys
# class Dialog(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         label = QLabel("This is a dialog.")
#         layout.addWidget(label, 0, 0)
#         buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
#         layout.addWidget(buttonbox)
# app = QApplication(sys.argv)
# screen = Dialog()
# screen.show()
# sys.exit(app.exec_())

from PyQt5.QtWidgets import *
import sys
class Dialog(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        
        time = QTime()
        time.setHMS(0, 0, 10)
        start = time.start()
        
        label = QLabel(str(time.second()))
        layout.addWidget(label, 0, 0)
        
        
app = QApplication(sys.argv)
screen = Dialog()
screen.show()
sys.exit(app.exec_())



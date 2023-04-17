# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:17:53 2023

@author: User
"""


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import sys


# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setWindowTitle('Hello')
        
#         layout = QGridLayout()
#         self.setLayout(layout)
        
#         label = QLabel('Hello World')
#         layout.addWidget(label, 0, 0)


# class Window(QWindow):
#     def __init__(self):
#         QWindow.__init__(self)
#         self.setTitle('Window')
#         self.resize(400,500)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)
        
        label = QLabel('Label 1')
        layout.addWidget(label, 0)
        label = QLabel('Label 2')
        layout.addWidget(label, 0)
        
        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)
        
        label = QLabel('Label 3')
        layout2.addWidget(label, 0)
        label = QLabel('Label 4')
        layout2.addWidget(label, 0)
        


if __name__=='__main__':       
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:17:26 2023

@author: User
"""

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        button = QPushButton('Click Me')
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button, 0, 0)
        
    def on_button_clicked(self):
        print('The button was pressed.')
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    
    screen = Window()
    screen.show()
    
    sys.exit(app.exec_())
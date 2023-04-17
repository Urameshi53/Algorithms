# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:53:08 2021

@author: User
"""

from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("School Management System")
        
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(400,300)
        self.setCentralWidget(QLabel("Hi there!"))
        # layout.addWidget(label, 0, 0)
        
app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
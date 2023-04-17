# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:44:58 2021

@author: User
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle('NSMQ')
#         self.setGeometry(250,250,600,500)
#         self.label = QLabel('Arial font', self)
#         self.label.move(100,100)
#         self.label.setFont(QFont('Arial', 14))
#         self.label1 = QLabel('Times New Roman', self)
#         self.label1.move(100,120)
#         self.label1.setFont(QFont('Times', 14))
#         self.show()
        
# app = QApplication(sys.argv)
# window = Window()
# sys.exit(app.exec_())
        
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QVBoxLayout()
        
        btn = QPushButton("Greet")
        btn.clicked.connect(self.greeting)
        
        layout.addWidget(btn)
        self.msg = QLabel('')
        layout.addWidget(self.msg)
        self.setLayout(layout)
        
    def greeting(self):
        if self.msg.text():
            self.msg.setText('')
        else:
            self.msg.setText('Hello world')
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
        
        
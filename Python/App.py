# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 08:25:23 2021

@author: User
"""

#!/usr/bin/env python3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         label1 = QLabel("Example content contained in a tab.")
#         label2 = QLabel("More example text in the second tab.")
#         tabwidget = QTabWidget()
#         tabwidget.addTab(label1, "Tab 1")
#         tabwidget.addTab(label2, "Tab 2")
#         layout.addWidget(tabwidget, 0, 0)
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

# # 

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         menubar = QMenuBar()
#         layout.addWidget(menubar, 0, 0)
#         actionFile = menubar.addMenu("File")
#         actionFile.addAction("New")
#         actionFile.addSeparator()
#         actionFile.addAction("Quit")
#         menubar.addMenu("Edit")
#         menubar.addMenu("View")
#         menubar.addMenu("Help")

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        time = QTime()
        time.setHMS(13, 15, 40)
        timeedit = QTimeEdit()
        timeedit.setTime(time)
        layout.addWidget(timeedit, 0, 0)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
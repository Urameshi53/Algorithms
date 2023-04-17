# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:13:19 2023

@author: User
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys 


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        # label1 = QLabel('Example content')
        # label2 = QLabel('More example text')
        
        # tabwidget = QTabWidget()
        # tabwidget.addTab(label1, 'Tab 1')
        # tabwidget.addTab(label2, 'Tab 2')
        # layout.addWidget(tabwidget, 0, 0)
        
        tabbar = QTabBar()
        tabbar.addTab('Tab 1')
        tabbar.addTab('Tab 2')
        tabbar.addTab('Tab 3')
        layout.addWidget(tabbar, 0, 0)
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    
    screen = Window()
    screen.show()
    
    sys.exit(app.exec_())
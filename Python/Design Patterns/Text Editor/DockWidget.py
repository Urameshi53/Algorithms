# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:15:58 2023

@author: User
"""

from PyQt5.QtWidgets import *
import sys 


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        dockwidget = QDockWidget()
        dockwidget.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetVerticalTitleBar)
        layout.addWidget(dockwidget)
        
        treewidget = QTreeWidget()
        dockwidget.setWidget(treewidget)
        
        label = QLabel('DockWidget is docked')
        layout.addWidget(label)
        


if __name__=='__main__':
    app = QApplication(sys.argv)
    
    screen = Window()
    screen.show()
    
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:44:20 2021

@author: User
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

class Window(QMainWindow):
    """Mian Window"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle("QMiainWindow")
        self.setCentralWidget(QPlainTextEdit("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        self.resize(400,300)
        
    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)
        
        self.file = self.menuBar().addMenu("&File")
        
    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)
        
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
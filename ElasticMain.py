# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:14:53 2019

@author: Vector30
"""

import sys

from PyQt5 import QtWidgets,QtCore

import ElasticStart
import ElasticLocalFun
import ElasticWebFun


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = ElasticStart.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.webElastic)
        self.ui.pushButton_2.clicked.connect(self.localElastic)
        
    def webElastic(self):
        self.web=ElasticWebFun.MyWindow()
        self.web.show()
    
    def localElastic(self):
        
        self.local=ElasticLocalFun.MyWindow()
        self.local.show()
        
        
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    app.lastWindowClosed.connect(app.quit)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
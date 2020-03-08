# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:28:08 2019

@author: nammabfc
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:27:46 2019

@author: Vector30
"""

from PyQt5 import QtWidgets,QtCore
import ElasticError
class MyWindow(QtWidgets.QMainWindow):
     def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = ElasticError.Ui_MainWindow()
        self.ui.setupUi(self)
        
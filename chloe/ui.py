#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:06:33 2023

@author: chloe
"""
import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
import simplebox

class mgui(QMainWindow): 
    def __init__(self):
        super(mgui,self).__init__()
        self.setWindowTitle("SVGen")
        uic.loadUi("svgenSimple.ui", self)
        self.show()
        self.genButton.clicked.connect(self.genButton_clicked)
        
    def genButton_clicked(self):
        dlg = QMessageBox(self)
        x = self.xSpinBox.value()
        y = self.ySpinBox.value()
        text = self.txtEdit.text()
        obj = simplebox.box(x,y,text)
        obj.draw()
        dlg.setWindowTitle("Success")
        dlg.setText("Generated SVG to local directory")
        genButton = dlg.exec()

def main():
    app = QApplication([])
    
    window = mgui()
    app.exec_()
    
if __name__ == '__main__':
    main()

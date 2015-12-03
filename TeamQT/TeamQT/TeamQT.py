# coding: utf-8
 
import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QDialog):
    
    #def resizeEvent(self ,resizeEvent):
    #    QtWidgets.QMessageBox.information(self,"Information!","Window has been resized...")    
    

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        
        self.ui = uic.loadUi("qt3.ui")        
        
        width = 1000
        height = 600
        
        self.ui.treeWidget.setColumnWidth(0,int(width*2/11))
        self.ui.treeWidget.setColumnWidth(1,int(width*5/11))
        self.ui.treeWidget.setColumnWidth(2,int(width*2/11))
        self.ui.treeWidget.setColumnWidth(3,int(width*2/11))
               
        self.ui.actionAdd_Files.setShortcut('Ctrl+O')
        self.ui.actionAdd_Files.setStatusTip('Open new File')
        self.ui.actionAdd_Files.triggered.connect(self.addButton)
        
        self.ui.convertButton.pressed.connect(self.convertButton)
        self.ui.addButton.pressed.connect(self.addButton)
        self.ui.formatButton.pressed.connect(self.formatButton)
        self.ui.pathButton.pressed.connect(self.pathButton)
        self.ui.show()

    
    def convertButton(self):
        print("I'm convert Button")
    def formatButton(self):
        print("I'm format Button")
    def pathButton(self):
        print("I'm path Button")
    
    def addButton(self):
        fnames = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open file', '/home')
        if len(fnames[0]) == 0:
            return
        else:
            for k in range(len(fnames)):
                a = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
                a.setText(0, "unchanged")
                a.setText(1, fnames[0][k])
                a.setText(2, os.path.basename(fnames[0][k]))
    
 
    @pyqtSlot()
    def convertSlot(self):
        print('click')
 

    
        
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myForm = Form()
    sys.exit(app.exec())
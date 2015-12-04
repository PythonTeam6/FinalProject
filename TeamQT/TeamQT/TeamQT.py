# coding: utf-8
 
import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QMainWindow):
    
    def resizeEvent(self ,resizeEvent):
        geo = self.frameGeometry()   
        print(geo.width(), geo.height())
        
        width = geo.width()
        height = geo.height()

        self.treeWidget.resize(width, int(height*521/631))
        self.treeWidget.setColumnWidth(0,int(width*2/11))
        self.treeWidget.setColumnWidth(1,int(width*5/11))
        self.treeWidget.setColumnWidth(2,int(width*2/11))
        self.treeWidget.setColumnWidth(3,int(width*2/11))
        #QtWidgets.QMessageBox.information(self,"Information!","Window has been resized...")    
    

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        
        #self.ui = uic.loadUi("qt3.ui")        
        uic.loadUi("qt3.ui", self)
        
        geo = self.frameGeometry()        
        print(geo.width(), geo.height())
        width = geo.width()
        height = geo.height()
        

        self.treeWidget.setColumnWidth(0,int(width*2/11))
        self.treeWidget.setColumnWidth(1,int(width*5/11))
        self.treeWidget.setColumnWidth(2,int(width*2/11))
        self.treeWidget.setColumnWidth(3,int(width*2/11))
               
        self.actionAdd_Files.setShortcut('Ctrl+O')
        self.actionAdd_Files.setStatusTip('Open new File')
        self.actionAdd_Files.triggered.connect(self.OnClickAdd)
        
        self.convertButton.pressed.connect(self.OnClickConvert)
        self.addButton.pressed.connect(self.OnClickAdd)
        self.formatButton.pressed.connect(self.OnClickFormat)
        self.pathButton.pressed.connect(self.OnClickPath)
        #self.show()

    
    def OnClickConvert(self):
        print("I'm convert Button")
    def OnClickFormat(self):
        print("I'm format Button")
    def OnClickPath(self):
        print("I'm path Button")
    
    def OnClickAdd(self):
        fnames = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open file', '/home')
        if len(fnames[0]) == 0:
            return
        else:
            for k in range(len(fnames)):
                a = QtWidgets.QTreeWidgetItem(self.treeWidget)
                a.setText(0, "unchanged")
                a.setText(1, fnames[0][k])
                a.setText(2, os.path.basename(fnames[0][k]))
    
 
    @pyqtSlot()
    def convertSlot(self):
        print('click')
 

    
        
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myForm = Form()
    myForm.show()
    sys.exit(app.exec())
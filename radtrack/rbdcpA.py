"""
Copyright (c) 2015 RadiaBeam Technologies. All rights reserved
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from os.path import expanduser, dirname
import sdds
import sys

import sip
sip.setapi('QString', 2)
from PyQt4 import QtGui, QtCore

from radtrack.dcp.Servicelib import *
from radtrack.dcp.SRWlib import SRWFileRead1, SRW
from radtrack.dcp.Flatfilelib import FF, FFColRead
from radtrack.dcp.Plotlib2axis import *
from radtrack.dcp.moverage import *
from radtrack.dcp.FourieT import *
from radtrack.dcp.math_analyses import *
from radtrack.ui.datavizwidget import Ui_Form

ColumnPicked = [0]
NumPage = 0
ColumnXAxis =-1
MaxNumParam=999
MaxNumColum=999

class RbDcp(QtGui.QWidget):
    acceptsFileTypes = ['save', 'twi','out','sig','cen','dat','txt','sdds','bun','fin']
    defaultTitle = 'Data Visualization'
    task = 'Analyze simulation results'
    category = 'tools'
    
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        if self.parent is None:
            self.parent = self
            self.parent.lastUsedDirectory = expanduser('~').replace('\\', '\\\\')
        self.container = self
        
        self.currentFiletype = ''
        self.ui.files.itemClicked.connect(self.importFromFileList)
        self.ui.selectplot.activated.connect(self.graphset)
        self.ui.pushButton.clicked.connect(lambda : self.importFile())
        self.ui.xaxis.activated.connect(self.customgraph)
        self.ui.yaxis.activated.connect(self.customgraph)
        
    def exportToFile(self, fileName):
        with open(fileName, 'w'):
            pass
        
    def importFromFileList(self, listItem):
        self.importFile(listItem.text())

    def importFile(self, openFile = None):
        if not openFile:
            openFile = QtGui.QFileDialog.getOpenFileName(self, 'Open file', self.parent.lastUsedDirectory)
            if not openFile:
                return
            else:
                self.parent.lastUsedDirectory = dirname(openFile)

        ext = os.path.splitext(openFile)[-1].lower().lstrip(".")
        if ext in ['sdds', 'out', 'twi', 'sig', 'cen', 'bun', 'fin']:
            self.showDCP_ele(openFile)
        elif ext == 'save':
            return
        else:
            raise ValueError(openFile + " unrecognized file type.")

        for index in range(self.ui.files.count()):
            if self.ui.files.item(index).text() == openFile:
                self.ui.files.setCurrentRow(index)
                break
        else:
            self.ui.files.addItem(openFile)
            self.ui.files.setCurrentRow(self.ui.files.count() - 1)

        try:
            self.parent.addToRecentMenu(openFile, True)
        except AttributeError:
            pass

        self.currentFiletype = ext
        if ext == 'twi':
            self.twiselect()
        elif ext == 'out':
            self.outselect()
        elif ext == 'sig':
            self.sigselect()
            
        self.dataopt()
        
    def showDCP_ele(self, openFile):
        #reset data selection
        ColumnPicked = [0]
        ColumnXAxis = -1

        #SDDS specific code
        self.x=sdds.SDDS(0)
        self.x.load(openFile)

        #get # of pages and columns
        (_,_,_,_,self.Ncol,_,_,Npage)=SDDSreshape(self.x,ColumnXAxis,ColumnPicked,NumPage)
        stringOut="Columns: "+str(self.Ncol)+" Pages: "+str(Npage)+" ColumnElements: "+\
        str(np.shape(self.x.columnData)[2])
        paramsOut ='\nPARAMTER INFO \n'
        for i,a in enumerate(self.x.parameterName):
            paramsOut+=str(a)+'='+str(self.x.parameterData[i])+'\n'
        self.ui.legend.setText(QtGui.QApplication.translate("dcpwidget",\
            'FILE INFO \n'+self.x.description[0]+stringOut+paramsOut, None, QtGui.QApplication.UnicodeUTF8))

        #preview of parameters
        self.preview()

        #preview of sdds data
        self.sddsprev()
        
    def sddsprev(self):
        ColumnPicked = []
        for i in range(self.Ncol):
            ColumnPicked.append(i)
        (Xrvec,Yrvec,YLab,Npar,Ncol,NcolPicked,NElemCol,Npage)=SDDSreshape(self.x,ColumnXAxis,ColumnPicked,NumPage) #reshapes file into vectors and a matrix

        for i, a in enumerate(Yrvec):
            #if i>0:# skip first column i+1=>i to adjust, because of extra 0 column!!!?
            if size(a)<1000:
                self.ui.data.setRowCount(shape(Yrvec)[1]+4)
                for j, b in enumerate(a):
                    self.ui.data.setItem(j+3,i,QtGui.QTableWidgetItem(str(b)))
            else:
                for j in range(1000):
                    self.ui.data.setItem(j+3,i,QtGui.QTableWidgetItem(str(a[j])))
                    
    def preview(self):
        self.reset()

        #set table sizes
        self.ui.data.setRowCount(1000)
        self.ui.data.setColumnCount(self.Ncol+1)

        for i,a in enumerate(self.x.columnDefinition):
            self.ui.data.setItem(0,i, QtGui.QTableWidgetItem(a[2]))
            self.ui.data.setItem(2,i, QtGui.QTableWidgetItem(a[1]))

        for i,a in enumerate(self.x.columnName):
            self.ui.data.setItem(1,i,QtGui.QTableWidgetItem(a))

    def reset(self):
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax2.clear()
        self.ui.widget.canvas.ax2.set_visible(False)
        self.ui.data.clearContents()
        self.ui.widget.canvas.draw()
        
    #displaying and setting data options method
    def dataopt(self):
        self.ui.xaxis.clear()
        self.ui.yaxis.clear()
        for i in self.x.columnName:
            self.ui.xaxis.addItem(i)
            self.ui.yaxis.addItem(i)

    def twiselect(self):
        self.ui.selectplot.clear()
        self.ui.selectplot.addItem('s v. beta x')
        self.ui.selectplot.addItem('s v. beta y')
        
    def outselect(self):
        self.ui.selectplot.clear()
        self.ui.selectplot.addItem('t v. p')
        self.ui.selectplot.addItem('x v. y')
        
    def sigselect(self):
        self.ui.selectplot.clear()
        self.ui.selectplot.addItem('s v. sigma x')
        self.ui.selectplot.addItem('s v. sigma y')
        
    def graphset(self):
        if self.currentFiletype == 'twi':
            self.ui.xaxis.setCurrentIndex(0)
            if self.ui.selectplot.currentIndex() == 0:
                self.ui.yaxis.setCurrentIndex(1)
            elif self.ui.selectplot.currentIndex() == 1:
                self.ui.yaxis.setCurrentIndex(7)
                
        elif self.currentFiletype == 'out':
            if self.ui.selectplot.currentIndex() == 0:
                self.ui.xaxis.setCurrentIndex(4)
                self.ui.yaxis.setCurrentIndex(5)
            elif self.ui.selectplot.currentIndex() == 1:
                self.ui.xaxis.setCurrentIndex(0)
                self.ui.yaxis.setCurrentIndex(2)
                
        elif self.currentFiletype == 'sig':
            self.ui.xaxis.setCurrentIndex(0)
            if self.ui.selectplot.currentIndex() == 0:
                self.ui.yaxis.setCurrentIndex(53)
            elif self.ui.selectplot.currentIndex() == 1:
                self.ui.yaxis.setCurrentIndex(55)
                
        self.customgraph()
    
    def customgraph(self):
        ColumnXAxis=0
        xname = self.ui.xaxis.currentText()
        yname = self.ui.yaxis.currentText()
        linetype = ''
        marktype = 'o'
        if (self.currentFiletype == 'twi') or (self.currentFiletype =='sig'):
            linetype = '-'
            marktype = ''
            
        ColumnPicked = []

        #resets display
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax2.clear()
        self.ui.widget.canvas.draw()
        for i,a in enumerate(self.x.columnName):
            if xname == a:
                ColumnXAxis=i
            
            if yname == a:
                ColumnPicked.append(i)
                
        (Xrvec,Yrvec,Ylab,Npar,Ncol,NcolPicked,NElemCol,Npage)=SDDSreshape(self.x,ColumnXAxis,ColumnPicked,NumPage)
        Xlab=[self.x.columnDefinition[ColumnXAxis][2]+", "+self.x.columnDefinition[ColumnXAxis][1]]
        PlotColnS1(Xrvec,Yrvec,linetype,marktype,self.x.description[0],Xlab,Ylab, self.ui.widget.canvas)
       
        
def main():
    app = QtGui.QApplication(sys.argv)
    myapp = RbDcp()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
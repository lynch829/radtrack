# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genesis.ui'
#
# Created: Fri Feb 06 11:30:31 2015
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_genesis(object):
    def setupUi(self, genesis):
        genesis.setObjectName("genesis")
        genesis.resize(843, 544)
        self.gridLayoutWidget = QtGui.QWidget(genesis)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 60, 701, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.simulation = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulation.sizePolicy().hasHeightForWidth())
        self.simulation.setSizePolicy(sizePolicy)
        self.simulation.setObjectName("simulation")
        self.gridLayout.addWidget(self.simulation, 1, 2, 1, 1)
        self.time = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy)
        self.time.setObjectName("time")
        self.gridLayout.addWidget(self.time, 1, 1, 1, 1)
        self.undulator = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undulator.sizePolicy().hasHeightForWidth())
        self.undulator.setSizePolicy(sizePolicy)
        self.undulator.setObjectName("undulator")
        self.gridLayout.addWidget(self.undulator, 0, 0, 1, 1)
        self.radiation = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radiation.sizePolicy().hasHeightForWidth())
        self.radiation.setSizePolicy(sizePolicy)
        self.radiation.setObjectName("radiation")
        self.gridLayout.addWidget(self.radiation, 0, 2, 1, 1)
        self.beam = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beam.sizePolicy().hasHeightForWidth())
        self.beam.setSizePolicy(sizePolicy)
        self.beam.setObjectName("beam")
        self.gridLayout.addWidget(self.beam, 0, 1, 1, 1)
        self.particle = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.particle.sizePolicy().hasHeightForWidth())
        self.particle.setSizePolicy(sizePolicy)
        self.particle.setObjectName("particle")
        self.gridLayout.addWidget(self.particle, 0, 3, 1, 1)
        self.focus = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.focus.sizePolicy().hasHeightForWidth())
        self.focus.setSizePolicy(sizePolicy)
        self.focus.setObjectName("focus")
        self.gridLayout.addWidget(self.focus, 1, 0, 1, 1)
        self.scan = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan.sizePolicy().hasHeightForWidth())
        self.scan.setSizePolicy(sizePolicy)
        self.scan.setObjectName("scan")
        self.gridLayout.addWidget(self.scan, 1, 3, 1, 1)
        self.io = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.io.sizePolicy().hasHeightForWidth())
        self.io.setSizePolicy(sizePolicy)
        self.io.setObjectName("io")
        self.gridLayout.addWidget(self.io, 1, 4, 1, 1)
        self.mesh = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mesh.sizePolicy().hasHeightForWidth())
        self.mesh.setSizePolicy(sizePolicy)
        self.mesh.setObjectName("mesh")
        self.gridLayout.addWidget(self.mesh, 0, 4, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(genesis)
        self.graphicsView.setGeometry(QtCore.QRect(70, 310, 561, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.cute = QtGui.QPushButton(genesis)
        self.cute.setGeometry(QtCore.QRect(640, 310, 131, 91))
        self.cute.setObjectName("cute")

        self.retranslateUi(genesis)
        QtCore.QMetaObject.connectSlotsByName(genesis)

    def retranslateUi(self, genesis):
        genesis.setWindowTitle(QtGui.QApplication.translate("genesis", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.simulation.setText(QtGui.QApplication.translate("genesis", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.time.setText(QtGui.QApplication.translate("genesis", "Time Dependence", None, QtGui.QApplication.UnicodeUTF8))
        self.undulator.setText(QtGui.QApplication.translate("genesis", "Undulator", None, QtGui.QApplication.UnicodeUTF8))
        self.radiation.setText(QtGui.QApplication.translate("genesis", "Radiation", None, QtGui.QApplication.UnicodeUTF8))
        self.beam.setText(QtGui.QApplication.translate("genesis", "Beam", None, QtGui.QApplication.UnicodeUTF8))
        self.particle.setText(QtGui.QApplication.translate("genesis", "Particle Loading", None, QtGui.QApplication.UnicodeUTF8))
        self.focus.setText(QtGui.QApplication.translate("genesis", "Focusing", None, QtGui.QApplication.UnicodeUTF8))
        self.scan.setText(QtGui.QApplication.translate("genesis", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.io.setText(QtGui.QApplication.translate("genesis", "I/O", None, QtGui.QApplication.UnicodeUTF8))
        self.mesh.setText(QtGui.QApplication.translate("genesis", "Mesh", None, QtGui.QApplication.UnicodeUTF8))
        self.cute.setText(QtGui.QApplication.translate("genesis", "Execute", None, QtGui.QApplication.UnicodeUTF8))

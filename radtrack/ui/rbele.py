# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbele.ui'
#
# Created: Mon Apr 13 08:39:50 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ELE(object):
    def setupUi(self, ELE):
        ELE.setObjectName(_fromUtf8("ELE"))
        ELE.resize(1061, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ELE.sizePolicy().hasHeightForWidth())
        ELE.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(ELE)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.parametersLabel = QtGui.QLabel(ELE)
        self.parametersLabel.setStyleSheet(_fromUtf8("QLabel {font-weight:bold}"))
        self.parametersLabel.setObjectName(_fromUtf8("parametersLabel"))
        self.verticalLayout.addWidget(self.parametersLabel)
        self.line_2 = QtGui.QFrame(ELE)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.bunchSourceLabel = QtGui.QLabel(ELE)
        self.bunchSourceLabel.setObjectName(_fromUtf8("bunchSourceLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.bunchSourceLabel)
        self.bunchSourceComboBox = QtGui.QComboBox(ELE)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bunchSourceComboBox.sizePolicy().hasHeightForWidth())
        self.bunchSourceComboBox.setSizePolicy(sizePolicy)
        self.bunchSourceComboBox.setObjectName(_fromUtf8("bunchSourceComboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.bunchSourceComboBox)
        self.beamLineSourceLabel = QtGui.QLabel(ELE)
        self.beamLineSourceLabel.setObjectName(_fromUtf8("beamLineSourceLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.beamLineSourceLabel)
        self.beamLineSourceComboBox = QtGui.QComboBox(ELE)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beamLineSourceComboBox.sizePolicy().hasHeightForWidth())
        self.beamLineSourceComboBox.setSizePolicy(sizePolicy)
        self.beamLineSourceComboBox.setObjectName(_fromUtf8("beamLineSourceComboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.beamLineSourceComboBox)
        self.beamLineLabel = QtGui.QLabel(ELE)
        self.beamLineLabel.setEnabled(True)
        self.beamLineLabel.setObjectName(_fromUtf8("beamLineLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.beamLineLabel)
        self.beamLineComboBox = QtGui.QComboBox(ELE)
        self.beamLineComboBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beamLineComboBox.sizePolicy().hasHeightForWidth())
        self.beamLineComboBox.setSizePolicy(sizePolicy)
        self.beamLineComboBox.setObjectName(_fromUtf8("beamLineComboBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.beamLineComboBox)
        self.momentumLabel = QtGui.QLabel(ELE)
        self.momentumLabel.setObjectName(_fromUtf8("momentumLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.momentumLabel)
        self.momentumLineEdit = QtGui.QLineEdit(ELE)
        self.momentumLineEdit.setObjectName(_fromUtf8("momentumLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.momentumLineEdit)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.FieldRole, spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.simulateButton = QtGui.QPushButton(ELE)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulateButton.sizePolicy().hasHeightForWidth())
        self.simulateButton.setSizePolicy(sizePolicy)
        self.simulateButton.setObjectName(_fromUtf8("simulateButton"))
        self.horizontalLayout_4.addWidget(self.simulateButton)
        self.abortButton = QtGui.QPushButton(ELE)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abortButton.sizePolicy().hasHeightForWidth())
        self.abortButton.setSizePolicy(sizePolicy)
        self.abortButton.setObjectName(_fromUtf8("abortButton"))
        self.horizontalLayout_4.addWidget(self.abortButton)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.progressBar = QtGui.QProgressBar(ELE)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.progressBar)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.splitter = QtGui.QSplitter(ELE)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.simulationStatusLabel = QtGui.QLabel(self.layoutWidget)
        self.simulationStatusLabel.setEnabled(False)
        self.simulationStatusLabel.setStyleSheet(_fromUtf8("QLabel {font-weight: bold}"))
        self.simulationStatusLabel.setObjectName(_fromUtf8("simulationStatusLabel"))
        self.verticalLayout_3.addWidget(self.simulationStatusLabel)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_3.addWidget(self.line_3)
        self.simulationStatusTextEdit = QtGui.QTextEdit(self.layoutWidget)
        self.simulationStatusTextEdit.setEnabled(False)
        self.simulationStatusTextEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.simulationStatusTextEdit.setReadOnly(True)
        self.simulationStatusTextEdit.setObjectName(_fromUtf8("simulationStatusTextEdit"))
        self.verticalLayout_3.addWidget(self.simulationStatusTextEdit)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.simulationResultsLabel = QtGui.QLabel(self.layoutWidget1)
        self.simulationResultsLabel.setEnabled(False)
        self.simulationResultsLabel.setStyleSheet(_fromUtf8("QLabel {font-weight: bold}"))
        self.simulationResultsLabel.setObjectName(_fromUtf8("simulationResultsLabel"))
        self.verticalLayout_2.addWidget(self.simulationResultsLabel)
        self.line_4 = QtGui.QFrame(self.layoutWidget1)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.simulationResultsListWidget = QtGui.QListWidget(self.layoutWidget1)
        self.simulationResultsListWidget.setEnabled(False)
        self.simulationResultsListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.simulationResultsListWidget.setObjectName(_fromUtf8("simulationResultsListWidget"))
        self.verticalLayout_2.addWidget(self.simulationResultsListWidget)
        self.horizontalLayout.addWidget(self.splitter)
        self.bunchSourceLabel.setBuddy(self.bunchSourceComboBox)
        self.beamLineSourceLabel.setBuddy(self.beamLineSourceComboBox)
        self.beamLineLabel.setBuddy(self.beamLineComboBox)
        self.momentumLabel.setBuddy(self.momentumLineEdit)

        self.retranslateUi(ELE)
        QtCore.QMetaObject.connectSlotsByName(ELE)

    def retranslateUi(self, ELE):
        ELE.setWindowTitle(_translate("ELE", "Form", None))
        self.parametersLabel.setText(_translate("ELE", "Parameters", None))
        self.bunchSourceLabel.setText(_translate("ELE", "Bunch Source:", None))
        self.beamLineSourceLabel.setText(_translate("ELE", "Beam Line Source:", None))
        self.beamLineLabel.setText(_translate("ELE", "Beam Line:", None))
        self.momentumLabel.setText(_translate("ELE", "Momentum:", None))
        self.simulateButton.setText(_translate("ELE", "Simulate", None))
        self.abortButton.setText(_translate("ELE", "Abort", None))
        self.simulationStatusLabel.setText(_translate("ELE", "Simulation Status", None))
        self.simulationResultsLabel.setText(_translate("ELE", "Simulation Results", None))
        self.simulationResultsListWidget.setToolTip(_translate("ELE", "Right-click to open the selected files.", None))


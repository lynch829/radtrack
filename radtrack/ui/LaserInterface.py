# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaserInterface.ui'
#
# Created: Thu Mar 26 10:44:26 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_LaserInterface(object):
    def setupUi(self, LaserInterface):
        LaserInterface.setObjectName(_fromUtf8("LaserInterface"))
        LaserInterface.resize(1703, 823)
        self.formLayoutWidget = QtGui.QWidget(LaserInterface)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 120, 221, 80))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.topLevelParams = QtGui.QFormLayout(self.formLayoutWidget)
        self.topLevelParams.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.topLevelParams.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.topLevelParams.setMargin(0)
        self.topLevelParams.setHorizontalSpacing(12)
        self.topLevelParams.setObjectName(_fromUtf8("topLevelParams"))
        self.wavelengthLabel = QtGui.QLabel(self.formLayoutWidget)
        self.wavelengthLabel.setObjectName(_fromUtf8("wavelengthLabel"))
        self.topLevelParams.setWidget(0, QtGui.QFormLayout.LabelRole, self.wavelengthLabel)
        self.waistSize = QtGui.QLineEdit(self.formLayoutWidget)
        self.waistSize.setObjectName(_fromUtf8("waistSize"))
        self.topLevelParams.setWidget(1, QtGui.QFormLayout.FieldRole, self.waistSize)
        self.waistPositionLabel = QtGui.QLabel(self.formLayoutWidget)
        self.waistPositionLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.waistPositionLabel.setObjectName(_fromUtf8("waistPositionLabel"))
        self.topLevelParams.setWidget(2, QtGui.QFormLayout.LabelRole, self.waistPositionLabel)
        self.waistSizeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.waistSizeLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.waistSizeLabel.setObjectName(_fromUtf8("waistSizeLabel"))
        self.topLevelParams.setWidget(1, QtGui.QFormLayout.LabelRole, self.waistSizeLabel)
        self.wavelength = QtGui.QLineEdit(self.formLayoutWidget)
        self.wavelength.setObjectName(_fromUtf8("wavelength"))
        self.topLevelParams.setWidget(0, QtGui.QFormLayout.FieldRole, self.wavelength)
        self.waistPosition = QtGui.QLineEdit(self.formLayoutWidget)
        self.waistPosition.setObjectName(_fromUtf8("waistPosition"))
        self.topLevelParams.setWidget(2, QtGui.QFormLayout.FieldRole, self.waistPosition)
        self.highLevelInputsLabel = QtGui.QLabel(LaserInterface)
        self.highLevelInputsLabel.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.highLevelInputsLabel.setObjectName(_fromUtf8("highLevelInputsLabel"))
        self.offsetLabel = QtGui.QLabel(LaserInterface)
        self.offsetLabel.setGeometry(QtCore.QRect(10, 230, 151, 20))
        self.offsetLabel.setObjectName(_fromUtf8("offsetLabel"))
        self.ghTable = QtGui.QTableWidget(LaserInterface)
        self.ghTable.setGeometry(QtCore.QRect(10, 250, 371, 311))
        self.ghTable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ghTable.setToolTip(_fromUtf8(""))
        self.ghTable.setObjectName(_fromUtf8("ghTable"))
        self.ghTable.setColumnCount(2)
        self.ghTable.setRowCount(100)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(20, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(21, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(22, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(23, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(24, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(25, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(26, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(27, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(28, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(29, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(30, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(31, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(32, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(33, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(34, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(35, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(36, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(37, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(38, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(39, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(40, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(41, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(42, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(43, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(44, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(45, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(46, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(47, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(48, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(49, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(50, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(51, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(52, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(53, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(54, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(55, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(56, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(57, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(58, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(59, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(60, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(61, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(62, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(63, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(64, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(65, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(66, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(67, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(68, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(69, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(70, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(71, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(72, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(73, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(74, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(75, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(76, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(77, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(78, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(79, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(80, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(81, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(82, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(83, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(84, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(85, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(86, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(87, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(88, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(89, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(90, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(91, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(92, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(93, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(94, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(95, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(96, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(97, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(98, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setVerticalHeaderItem(99, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ghTable.setHorizontalHeaderItem(1, item)
        self.generatePulse = QtGui.QToolButton(LaserInterface)
        self.generatePulse.setGeometry(QtCore.QRect(10, 10, 101, 23))
        self.generatePulse.setObjectName(_fromUtf8("generatePulse"))
        self.saveToFile = QtGui.QToolButton(LaserInterface)
        self.saveToFile.setGeometry(QtCore.QRect(130, 10, 81, 23))
        self.saveToFile.setObjectName(_fromUtf8("saveToFile"))
        self.xyPlot = matplotlibWidget(LaserInterface)
        self.xyPlot.setGeometry(QtCore.QRect(390, 380, 421, 361))
        self.xyPlot.setToolTip(_fromUtf8(""))
        self.xyPlot.setObjectName(_fromUtf8("xyPlot"))
        self.zyPlot = matplotlibWidget(LaserInterface)
        self.zyPlot.setGeometry(QtCore.QRect(830, 380, 411, 361))
        self.zyPlot.setToolTip(_fromUtf8(""))
        self.zyPlot.setObjectName(_fromUtf8("zyPlot"))
        self.zxPlot = matplotlibWidget(LaserInterface)
        self.zxPlot.setGeometry(QtCore.QRect(390, 10, 851, 361))
        self.zxPlot.setToolTip(_fromUtf8(""))
        self.zxPlot.setObjectName(_fromUtf8("zxPlot"))
        self.unitsLabel = QtGui.QLabel(LaserInterface)
        self.unitsLabel.setGeometry(QtCore.QRect(280, 100, 81, 16))
        self.unitsLabel.setObjectName(_fromUtf8("unitsLabel"))
        self.formLayoutWidget_2 = QtGui.QWidget(LaserInterface)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(280, 120, 101, 74))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.units = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.units.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.units.setMargin(0)
        self.units.setObjectName(_fromUtf8("units"))
        self.unitsXYLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.unitsXYLabel.setObjectName(_fromUtf8("unitsXYLabel"))
        self.units.setWidget(0, QtGui.QFormLayout.LabelRole, self.unitsXYLabel)
        self.unitsXY = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.unitsXY.setObjectName(_fromUtf8("unitsXY"))
        self.units.setWidget(0, QtGui.QFormLayout.FieldRole, self.unitsXY)
        self.unitsZLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.unitsZLabel.setObjectName(_fromUtf8("unitsZLabel"))
        self.units.setWidget(1, QtGui.QFormLayout.LabelRole, self.unitsZLabel)
        self.unitsZ = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.unitsZ.setDragEnabled(True)
        self.unitsZ.setObjectName(_fromUtf8("unitsZ"))
        self.units.setWidget(1, QtGui.QFormLayout.FieldRole, self.unitsZ)
        self.ticksLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.ticksLabel.setObjectName(_fromUtf8("ticksLabel"))
        self.units.setWidget(2, QtGui.QFormLayout.LabelRole, self.ticksLabel)
        self.numTicks = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.numTicks.setObjectName(_fromUtf8("numTicks"))
        self.units.setWidget(2, QtGui.QFormLayout.FieldRole, self.numTicks)
        self.importFile = QtGui.QToolButton(LaserInterface)
        self.importFile.setGeometry(QtCore.QRect(130, 40, 81, 23))
        self.importFile.setObjectName(_fromUtf8("importFile"))
        self.xyPlotExtFields = matplotlibWidget(LaserInterface)
        self.xyPlotExtFields.setGeometry(QtCore.QRect(1270, 70, 411, 361))
        self.xyPlotExtFields.setToolTip(_fromUtf8(""))
        self.xyPlotExtFields.setObjectName(_fromUtf8("xyPlotExtFields"))
        self.xyPlotFitDiff = matplotlibWidget(LaserInterface)
        self.xyPlotFitDiff.setGeometry(QtCore.QRect(1270, 450, 411, 361))
        self.xyPlotFitDiff.setToolTip(_fromUtf8(""))
        self.xyPlotFitDiff.setObjectName(_fromUtf8("xyPlotFitDiff"))
        self.externalFields = QtGui.QToolButton(LaserInterface)
        self.externalFields.setGeometry(QtCore.QRect(1270, 10, 101, 23))
        self.externalFields.setObjectName(_fromUtf8("externalFields"))
        self.noTitles = QtGui.QToolButton(LaserInterface)
        self.noTitles.setGeometry(QtCore.QRect(280, 70, 31, 21))
        self.noTitles.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.noTitles.setObjectName(_fromUtf8("noTitles"))
        self.generateCoeffs = QtGui.QToolButton(LaserInterface)
        self.generateCoeffs.setGeometry(QtCore.QRect(1390, 10, 141, 23))
        self.generateCoeffs.setObjectName(_fromUtf8("generateCoeffs"))

        self.retranslateUi(LaserInterface)
        QtCore.QMetaObject.connectSlotsByName(LaserInterface)
        LaserInterface.setTabOrder(self.waistSize, self.generatePulse)
        LaserInterface.setTabOrder(self.generatePulse, self.saveToFile)
        LaserInterface.setTabOrder(self.saveToFile, self.importFile)
        LaserInterface.setTabOrder(self.importFile, self.unitsXY)
        LaserInterface.setTabOrder(self.unitsXY, self.unitsZ)
        LaserInterface.setTabOrder(self.unitsZ, self.ghTable)

    def retranslateUi(self, LaserInterface):
        LaserInterface.setWindowTitle(_translate("LaserInterface", "Form", None))
        self.wavelengthLabel.setText(_translate("LaserInterface", " lambda [um]", None))
        self.waistSize.setToolTip(_translate("LaserInterface", "<html><head/><body><p>Design momentum is the average momentum for zero offset.</p><p>Defaul units can be overridden.</p></body></html>", None))
        self.waistPositionLabel.setText(_translate("LaserInterface", " z0 [m]", None))
        self.waistSizeLabel.setText(_translate("LaserInterface", "<html><head/><body><p align=\"center\">w0 [um]</p></body></html>", None))
        self.wavelength.setToolTip(_translate("LaserInterface", "<html><head/><body><p>Design momentum is the average momentum for zero offset.</p><p>Defaul units can be overridden.</p></body></html>", None))
        self.waistPosition.setToolTip(_translate("LaserInterface", "<html><head/><body><p>Design momentum is the average momentum for zero offset.</p><p>Defaul units can be overridden.</p></body></html>", None))
        self.highLevelInputsLabel.setText(_translate("LaserInterface", "Top level params", None))
        self.offsetLabel.setText(_translate("LaserInterface", "Gauss-Hermite coefficients:", None))
        item = self.ghTable.verticalHeaderItem(0)
        item.setText(_translate("LaserInterface", "0", None))
        item = self.ghTable.verticalHeaderItem(1)
        item.setText(_translate("LaserInterface", "1", None))
        item = self.ghTable.verticalHeaderItem(2)
        item.setText(_translate("LaserInterface", "2", None))
        item = self.ghTable.verticalHeaderItem(3)
        item.setText(_translate("LaserInterface", "3", None))
        item = self.ghTable.verticalHeaderItem(4)
        item.setText(_translate("LaserInterface", "4", None))
        item = self.ghTable.verticalHeaderItem(5)
        item.setText(_translate("LaserInterface", "5", None))
        item = self.ghTable.verticalHeaderItem(6)
        item.setText(_translate("LaserInterface", "6", None))
        item = self.ghTable.verticalHeaderItem(7)
        item.setText(_translate("LaserInterface", "7", None))
        item = self.ghTable.verticalHeaderItem(8)
        item.setText(_translate("LaserInterface", "8", None))
        item = self.ghTable.verticalHeaderItem(9)
        item.setText(_translate("LaserInterface", "9", None))
        item = self.ghTable.verticalHeaderItem(10)
        item.setText(_translate("LaserInterface", "10", None))
        item = self.ghTable.verticalHeaderItem(11)
        item.setText(_translate("LaserInterface", "11", None))
        item = self.ghTable.verticalHeaderItem(12)
        item.setText(_translate("LaserInterface", "12", None))
        item = self.ghTable.verticalHeaderItem(13)
        item.setText(_translate("LaserInterface", "13", None))
        item = self.ghTable.verticalHeaderItem(14)
        item.setText(_translate("LaserInterface", "14", None))
        item = self.ghTable.verticalHeaderItem(15)
        item.setText(_translate("LaserInterface", "15", None))
        item = self.ghTable.verticalHeaderItem(16)
        item.setText(_translate("LaserInterface", "16", None))
        item = self.ghTable.verticalHeaderItem(17)
        item.setText(_translate("LaserInterface", "17", None))
        item = self.ghTable.verticalHeaderItem(18)
        item.setText(_translate("LaserInterface", "18", None))
        item = self.ghTable.verticalHeaderItem(19)
        item.setText(_translate("LaserInterface", "19", None))
        item = self.ghTable.verticalHeaderItem(20)
        item.setText(_translate("LaserInterface", "20", None))
        item = self.ghTable.verticalHeaderItem(21)
        item.setText(_translate("LaserInterface", "21", None))
        item = self.ghTable.verticalHeaderItem(22)
        item.setText(_translate("LaserInterface", "22", None))
        item = self.ghTable.verticalHeaderItem(23)
        item.setText(_translate("LaserInterface", "23", None))
        item = self.ghTable.verticalHeaderItem(24)
        item.setText(_translate("LaserInterface", "24", None))
        item = self.ghTable.verticalHeaderItem(25)
        item.setText(_translate("LaserInterface", "25", None))
        item = self.ghTable.verticalHeaderItem(26)
        item.setText(_translate("LaserInterface", "26", None))
        item = self.ghTable.verticalHeaderItem(27)
        item.setText(_translate("LaserInterface", "27", None))
        item = self.ghTable.verticalHeaderItem(28)
        item.setText(_translate("LaserInterface", "28", None))
        item = self.ghTable.verticalHeaderItem(29)
        item.setText(_translate("LaserInterface", "29", None))
        item = self.ghTable.verticalHeaderItem(30)
        item.setText(_translate("LaserInterface", "30", None))
        item = self.ghTable.verticalHeaderItem(31)
        item.setText(_translate("LaserInterface", "31", None))
        item = self.ghTable.verticalHeaderItem(32)
        item.setText(_translate("LaserInterface", "32", None))
        item = self.ghTable.verticalHeaderItem(33)
        item.setText(_translate("LaserInterface", "33", None))
        item = self.ghTable.verticalHeaderItem(34)
        item.setText(_translate("LaserInterface", "34", None))
        item = self.ghTable.verticalHeaderItem(35)
        item.setText(_translate("LaserInterface", "35", None))
        item = self.ghTable.verticalHeaderItem(36)
        item.setText(_translate("LaserInterface", "36", None))
        item = self.ghTable.verticalHeaderItem(37)
        item.setText(_translate("LaserInterface", "37", None))
        item = self.ghTable.verticalHeaderItem(38)
        item.setText(_translate("LaserInterface", "38", None))
        item = self.ghTable.verticalHeaderItem(39)
        item.setText(_translate("LaserInterface", "39", None))
        item = self.ghTable.verticalHeaderItem(40)
        item.setText(_translate("LaserInterface", "40", None))
        item = self.ghTable.verticalHeaderItem(41)
        item.setText(_translate("LaserInterface", "41", None))
        item = self.ghTable.verticalHeaderItem(42)
        item.setText(_translate("LaserInterface", "42", None))
        item = self.ghTable.verticalHeaderItem(43)
        item.setText(_translate("LaserInterface", "43", None))
        item = self.ghTable.verticalHeaderItem(44)
        item.setText(_translate("LaserInterface", "44", None))
        item = self.ghTable.verticalHeaderItem(45)
        item.setText(_translate("LaserInterface", "45", None))
        item = self.ghTable.verticalHeaderItem(46)
        item.setText(_translate("LaserInterface", "46", None))
        item = self.ghTable.verticalHeaderItem(47)
        item.setText(_translate("LaserInterface", "47", None))
        item = self.ghTable.verticalHeaderItem(48)
        item.setText(_translate("LaserInterface", "48", None))
        item = self.ghTable.verticalHeaderItem(49)
        item.setText(_translate("LaserInterface", "49", None))
        item = self.ghTable.verticalHeaderItem(50)
        item.setText(_translate("LaserInterface", "50", None))
        item = self.ghTable.verticalHeaderItem(51)
        item.setText(_translate("LaserInterface", "51", None))
        item = self.ghTable.verticalHeaderItem(52)
        item.setText(_translate("LaserInterface", "52", None))
        item = self.ghTable.verticalHeaderItem(53)
        item.setText(_translate("LaserInterface", "53", None))
        item = self.ghTable.verticalHeaderItem(54)
        item.setText(_translate("LaserInterface", "54", None))
        item = self.ghTable.verticalHeaderItem(55)
        item.setText(_translate("LaserInterface", "55", None))
        item = self.ghTable.verticalHeaderItem(56)
        item.setText(_translate("LaserInterface", "56", None))
        item = self.ghTable.verticalHeaderItem(57)
        item.setText(_translate("LaserInterface", "57", None))
        item = self.ghTable.verticalHeaderItem(58)
        item.setText(_translate("LaserInterface", "58", None))
        item = self.ghTable.verticalHeaderItem(59)
        item.setText(_translate("LaserInterface", "59", None))
        item = self.ghTable.verticalHeaderItem(60)
        item.setText(_translate("LaserInterface", "60", None))
        item = self.ghTable.verticalHeaderItem(61)
        item.setText(_translate("LaserInterface", "61", None))
        item = self.ghTable.verticalHeaderItem(62)
        item.setText(_translate("LaserInterface", "62", None))
        item = self.ghTable.verticalHeaderItem(63)
        item.setText(_translate("LaserInterface", "63", None))
        item = self.ghTable.verticalHeaderItem(64)
        item.setText(_translate("LaserInterface", "64", None))
        item = self.ghTable.verticalHeaderItem(65)
        item.setText(_translate("LaserInterface", "65", None))
        item = self.ghTable.verticalHeaderItem(66)
        item.setText(_translate("LaserInterface", "66", None))
        item = self.ghTable.verticalHeaderItem(67)
        item.setText(_translate("LaserInterface", "67", None))
        item = self.ghTable.verticalHeaderItem(68)
        item.setText(_translate("LaserInterface", "68", None))
        item = self.ghTable.verticalHeaderItem(69)
        item.setText(_translate("LaserInterface", "69", None))
        item = self.ghTable.verticalHeaderItem(70)
        item.setText(_translate("LaserInterface", "71", None))
        item = self.ghTable.verticalHeaderItem(71)
        item.setText(_translate("LaserInterface", "72", None))
        item = self.ghTable.verticalHeaderItem(72)
        item.setText(_translate("LaserInterface", "722", None))
        item = self.ghTable.verticalHeaderItem(73)
        item.setText(_translate("LaserInterface", "73", None))
        item = self.ghTable.verticalHeaderItem(74)
        item.setText(_translate("LaserInterface", "74", None))
        item = self.ghTable.verticalHeaderItem(75)
        item.setText(_translate("LaserInterface", "75", None))
        item = self.ghTable.verticalHeaderItem(76)
        item.setText(_translate("LaserInterface", "76", None))
        item = self.ghTable.verticalHeaderItem(77)
        item.setText(_translate("LaserInterface", "77", None))
        item = self.ghTable.verticalHeaderItem(78)
        item.setText(_translate("LaserInterface", "78", None))
        item = self.ghTable.verticalHeaderItem(79)
        item.setText(_translate("LaserInterface", "79", None))
        item = self.ghTable.verticalHeaderItem(80)
        item.setText(_translate("LaserInterface", "80", None))
        item = self.ghTable.verticalHeaderItem(81)
        item.setText(_translate("LaserInterface", "81", None))
        item = self.ghTable.verticalHeaderItem(82)
        item.setText(_translate("LaserInterface", "82", None))
        item = self.ghTable.verticalHeaderItem(83)
        item.setText(_translate("LaserInterface", "83", None))
        item = self.ghTable.verticalHeaderItem(84)
        item.setText(_translate("LaserInterface", "84", None))
        item = self.ghTable.verticalHeaderItem(85)
        item.setText(_translate("LaserInterface", "85", None))
        item = self.ghTable.verticalHeaderItem(86)
        item.setText(_translate("LaserInterface", "86", None))
        item = self.ghTable.verticalHeaderItem(87)
        item.setText(_translate("LaserInterface", "87", None))
        item = self.ghTable.verticalHeaderItem(88)
        item.setText(_translate("LaserInterface", "88", None))
        item = self.ghTable.verticalHeaderItem(89)
        item.setText(_translate("LaserInterface", "89", None))
        item = self.ghTable.verticalHeaderItem(90)
        item.setText(_translate("LaserInterface", "90", None))
        item = self.ghTable.verticalHeaderItem(91)
        item.setText(_translate("LaserInterface", "91", None))
        item = self.ghTable.verticalHeaderItem(92)
        item.setText(_translate("LaserInterface", "92", None))
        item = self.ghTable.verticalHeaderItem(93)
        item.setText(_translate("LaserInterface", "93", None))
        item = self.ghTable.verticalHeaderItem(94)
        item.setText(_translate("LaserInterface", "95", None))
        item = self.ghTable.verticalHeaderItem(95)
        item.setText(_translate("LaserInterface", "9", None))
        item = self.ghTable.verticalHeaderItem(96)
        item.setText(_translate("LaserInterface", "96", None))
        item = self.ghTable.verticalHeaderItem(97)
        item.setText(_translate("LaserInterface", "97", None))
        item = self.ghTable.verticalHeaderItem(98)
        item.setText(_translate("LaserInterface", "98", None))
        item = self.ghTable.verticalHeaderItem(99)
        item.setText(_translate("LaserInterface", "100", None))
        item = self.ghTable.horizontalHeaderItem(0)
        item.setText(_translate("LaserInterface", "M (horizontal coeff\'s)", None))
        item = self.ghTable.horizontalHeaderItem(1)
        item.setText(_translate("LaserInterface", "N (   vertical coeff\'s  )", None))
        self.generatePulse.setToolTip(_translate("LaserInterface", "Generate a particle beam with the specified parameters.", None))
        self.generatePulse.setText(_translate("LaserInterface", "Generate Pulse", None))
        self.saveToFile.setToolTip(_translate("LaserInterface", "Save particle data to a file.", None))
        self.saveToFile.setText(_translate("LaserInterface", "Save to File", None))
        self.unitsLabel.setText(_translate("LaserInterface", "Plotting units", None))
        self.unitsXYLabel.setText(_translate("LaserInterface", "   x, y", None))
        self.unitsXY.setToolTip(_translate("LaserInterface", "Units to be used for axis labels of position-like variables.\n"
"For example: m, mm, um (or microns), nm ...", None))
        self.unitsZLabel.setText(_translate("LaserInterface", "<html><head/><body><p>&nbsp; &nbsp; z</p></body></html>", None))
        self.unitsZ.setToolTip(_translate("LaserInterface", "Units to be used for axis labels of angle-like variables.\n"
"For example: rad, mrad, urad (or microrad) ...", None))
        self.ticksLabel.setText(_translate("LaserInterface", "# ticks", None))
        self.numTicks.setToolTip(_translate("LaserInterface", "Suggest a maximum # of tick marks for the axes.\n"
"Logic for actual # is due to matplotlib library.", None))
        self.importFile.setToolTip(_translate("LaserInterface", "Import particle data from a file.", None))
        self.importFile.setText(_translate("LaserInterface", "Import File", None))
        self.externalFields.setToolTip(_translate("LaserInterface", "Generate a particle beam with the specified parameters.", None))
        self.externalFields.setText(_translate("LaserInterface", "External fields", None))
        self.noTitles.setToolTip(_translate("LaserInterface", "Toggle plot titles on/off.", None))
        self.noTitles.setStatusTip(_translate("LaserInterface", "Toggle plot titles on/off.", None))
        self.noTitles.setText(_translate("LaserInterface", "NT", None))
        self.generateCoeffs.setToolTip(_translate("LaserInterface", "Generate a particle beam with the specified parameters.", None))
        self.generateCoeffs.setText(_translate("LaserInterface", "Gauss-Hermite coefficients", None))

from radtrack.gui.matplotlibwidget import matplotlibWidget

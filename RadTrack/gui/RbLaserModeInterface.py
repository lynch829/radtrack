# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RbLaserModeInterface.ui'
#
# Created: Thu Jun 05 14:02:06 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_laserModeInterface(object):
    def setupUi(self, laserModeInterface):
        laserModeInterface.setObjectName("laserModeInterface")
        laserModeInterface.resize(1703, 823)
        self.formLayoutWidget = QtGui.QWidget(laserModeInterface)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 120, 221, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.topLevelParams = QtGui.QFormLayout(self.formLayoutWidget)
        self.topLevelParams.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.topLevelParams.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.topLevelParams.setContentsMargins(0, 0, 0, 0)
        self.topLevelParams.setHorizontalSpacing(12)
        self.topLevelParams.setObjectName("topLevelParams")
        self.wavelengthLabel = QtGui.QLabel(self.formLayoutWidget)
        self.wavelengthLabel.setObjectName("wavelengthLabel")
        self.topLevelParams.setWidget(0, QtGui.QFormLayout.LabelRole, self.wavelengthLabel)
        self.waistSize = QtGui.QLineEdit(self.formLayoutWidget)
        self.waistSize.setObjectName("waistSize")
        self.topLevelParams.setWidget(1, QtGui.QFormLayout.FieldRole, self.waistSize)
        self.waistPositionLabel = QtGui.QLabel(self.formLayoutWidget)
        self.waistPositionLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.waistPositionLabel.setObjectName("waistPositionLabel")
        self.topLevelParams.setWidget(2, QtGui.QFormLayout.LabelRole, self.waistPositionLabel)
        self.waistSizeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.waistSizeLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.waistSizeLabel.setObjectName("waistSizeLabel")
        self.topLevelParams.setWidget(1, QtGui.QFormLayout.LabelRole, self.waistSizeLabel)
        self.wavelength = QtGui.QLineEdit(self.formLayoutWidget)
        self.wavelength.setObjectName("wavelength")
        self.topLevelParams.setWidget(0, QtGui.QFormLayout.FieldRole, self.wavelength)
        self.waistPosition = QtGui.QLineEdit(self.formLayoutWidget)
        self.waistPosition.setObjectName("waistPosition")
        self.topLevelParams.setWidget(2, QtGui.QFormLayout.FieldRole, self.waistPosition)
        self.highLevelInputsLabel = QtGui.QLabel(laserModeInterface)
        self.highLevelInputsLabel.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.highLevelInputsLabel.setObjectName("highLevelInputsLabel")
        self.offsetLabel = QtGui.QLabel(laserModeInterface)
        self.offsetLabel.setGeometry(QtCore.QRect(10, 230, 151, 20))
        self.offsetLabel.setObjectName("offsetLabel")
        self.ghTable = QtGui.QTableWidget(laserModeInterface)
        self.ghTable.setGeometry(QtCore.QRect(10, 250, 371, 181))
        self.ghTable.setToolTip("")
        self.ghTable.setObjectName("ghTable")
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
        self.generatePulse = QtGui.QToolButton(laserModeInterface)
        self.generatePulse.setGeometry(QtCore.QRect(10, 10, 101, 23))
        self.generatePulse.setObjectName("generatePulse")
        self.saveToFile = QtGui.QToolButton(laserModeInterface)
        self.saveToFile.setGeometry(QtCore.QRect(130, 10, 81, 23))
        self.saveToFile.setObjectName("saveToFile")
        self.xyPlot = matplotlibWidget(laserModeInterface)
        self.xyPlot.setGeometry(QtCore.QRect(390, 380, 421, 361))
        self.xyPlot.setToolTip("")
        self.xyPlot.setObjectName("xyPlot")
        self.zyPlot = matplotlibWidget(laserModeInterface)
        self.zyPlot.setGeometry(QtCore.QRect(830, 380, 411, 361))
        self.zyPlot.setToolTip("")
        self.zyPlot.setObjectName("zyPlot")
        self.zxPlot = matplotlibWidget(laserModeInterface)
        self.zxPlot.setGeometry(QtCore.QRect(390, 10, 851, 361))
        self.zxPlot.setToolTip("")
        self.zxPlot.setObjectName("zxPlot")
        self.unitsLabel = QtGui.QLabel(laserModeInterface)
        self.unitsLabel.setGeometry(QtCore.QRect(280, 100, 81, 16))
        self.unitsLabel.setObjectName("unitsLabel")
        self.formLayoutWidget_2 = QtGui.QWidget(laserModeInterface)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(280, 120, 101, 74))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.units = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.units.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.units.setContentsMargins(0, 0, 0, 0)
        self.units.setObjectName("units")
        self.unitsXYLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.unitsXYLabel.setObjectName("unitsXYLabel")
        self.units.setWidget(0, QtGui.QFormLayout.LabelRole, self.unitsXYLabel)
        self.unitsXY = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.unitsXY.setObjectName("unitsXY")
        self.units.setWidget(0, QtGui.QFormLayout.FieldRole, self.unitsXY)
        self.unitsZLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.unitsZLabel.setObjectName("unitsZLabel")
        self.units.setWidget(1, QtGui.QFormLayout.LabelRole, self.unitsZLabel)
        self.unitsZ = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.unitsZ.setDragEnabled(True)
        self.unitsZ.setObjectName("unitsZ")
        self.units.setWidget(1, QtGui.QFormLayout.FieldRole, self.unitsZ)
        self.ticksLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.ticksLabel.setObjectName("ticksLabel")
        self.units.setWidget(2, QtGui.QFormLayout.LabelRole, self.ticksLabel)
        self.numTicks = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.numTicks.setObjectName("numTicks")
        self.units.setWidget(2, QtGui.QFormLayout.FieldRole, self.numTicks)
        self.importFile = QtGui.QToolButton(laserModeInterface)
        self.importFile.setGeometry(QtCore.QRect(130, 40, 81, 23))
        self.importFile.setObjectName("importFile")
        self.xyPlotExtFields = matplotlibWidget(laserModeInterface)
        self.xyPlotExtFields.setGeometry(QtCore.QRect(1270, 70, 411, 361))
        self.xyPlotExtFields.setToolTip("")
        self.xyPlotExtFields.setObjectName("xyPlotExtFields")
        self.xyPlotFitDiff = matplotlibWidget(laserModeInterface)
        self.xyPlotFitDiff.setGeometry(QtCore.QRect(1270, 450, 411, 361))
        self.xyPlotFitDiff.setToolTip("")
        self.xyPlotFitDiff.setObjectName("xyPlotFitDiff")
        self.externalFields = QtGui.QToolButton(laserModeInterface)
        self.externalFields.setGeometry(QtCore.QRect(1270, 10, 101, 23))
        self.externalFields.setObjectName("externalFields")
        self.noTitles = QtGui.QToolButton(laserModeInterface)
        self.noTitles.setGeometry(QtCore.QRect(280, 70, 31, 21))
        self.noTitles.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.noTitles.setObjectName("noTitles")
        self.generateCoeffs = QtGui.QToolButton(laserModeInterface)
        self.generateCoeffs.setGeometry(QtCore.QRect(1390, 10, 141, 23))
        self.generateCoeffs.setObjectName("generateCoeffs")

        self.retranslateUi(laserModeInterface)
        QtCore.QMetaObject.connectSlotsByName(laserModeInterface)
        laserModeInterface.setTabOrder(self.waistSize, self.generatePulse)
        laserModeInterface.setTabOrder(self.generatePulse, self.saveToFile)
        laserModeInterface.setTabOrder(self.saveToFile, self.importFile)
        laserModeInterface.setTabOrder(self.importFile, self.unitsXY)
        laserModeInterface.setTabOrder(self.unitsXY, self.unitsZ)
        laserModeInterface.setTabOrder(self.unitsZ, self.ghTable)

    def retranslateUi(self, laserModeInterface):
        laserModeInterface.setWindowTitle(QtGui.QApplication.translate("laserModeInterface", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.wavelengthLabel.setText(QtGui.QApplication.translate("laserModeInterface", " lambda [um]", None, QtGui.QApplication.UnicodeUTF8))
        self.waistSize.setToolTip(QtGui.QApplication.translate("laserModeInterface", "<html><head/><body><p>Design momentum is the average momentum for zero offset.</p><p>Defaul units can be overridden.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.waistPositionLabel.setText(QtGui.QApplication.translate("laserModeInterface", " z0 [m]", None, QtGui.QApplication.UnicodeUTF8))
        self.waistSizeLabel.setText(QtGui.QApplication.translate("laserModeInterface", "<html><head/><body><p align=\"center\">w0 [um]</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.wavelength.setToolTip(QtGui.QApplication.translate("laserModeInterface", "<html><head/><body><p>Design momentum is the average momentum for zero offset.</p><p>Defaul units can be overridden.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.waistPosition.setToolTip(QtGui.QApplication.translate("laserModeInterface", "<html><head/><body><p>Design momentum is the average momentum for zero offset.</p><p>Defaul units can be overridden.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.highLevelInputsLabel.setText(QtGui.QApplication.translate("laserModeInterface", "Top level params", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetLabel.setText(QtGui.QApplication.translate("laserModeInterface", "Gauss-Hermite coefficients:", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(0).setText(QtGui.QApplication.translate("laserModeInterface", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(1).setText(QtGui.QApplication.translate("laserModeInterface", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(2).setText(QtGui.QApplication.translate("laserModeInterface", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(3).setText(QtGui.QApplication.translate("laserModeInterface", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(4).setText(QtGui.QApplication.translate("laserModeInterface", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(5).setText(QtGui.QApplication.translate("laserModeInterface", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(6).setText(QtGui.QApplication.translate("laserModeInterface", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(7).setText(QtGui.QApplication.translate("laserModeInterface", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(8).setText(QtGui.QApplication.translate("laserModeInterface", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(9).setText(QtGui.QApplication.translate("laserModeInterface", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(10).setText(QtGui.QApplication.translate("laserModeInterface", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(11).setText(QtGui.QApplication.translate("laserModeInterface", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(12).setText(QtGui.QApplication.translate("laserModeInterface", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(13).setText(QtGui.QApplication.translate("laserModeInterface", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(14).setText(QtGui.QApplication.translate("laserModeInterface", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(15).setText(QtGui.QApplication.translate("laserModeInterface", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(16).setText(QtGui.QApplication.translate("laserModeInterface", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(17).setText(QtGui.QApplication.translate("laserModeInterface", "17", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(18).setText(QtGui.QApplication.translate("laserModeInterface", "18", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(19).setText(QtGui.QApplication.translate("laserModeInterface", "19", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(20).setText(QtGui.QApplication.translate("laserModeInterface", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(21).setText(QtGui.QApplication.translate("laserModeInterface", "21", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(22).setText(QtGui.QApplication.translate("laserModeInterface", "22", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(23).setText(QtGui.QApplication.translate("laserModeInterface", "23", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(24).setText(QtGui.QApplication.translate("laserModeInterface", "24", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(25).setText(QtGui.QApplication.translate("laserModeInterface", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(26).setText(QtGui.QApplication.translate("laserModeInterface", "26", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(27).setText(QtGui.QApplication.translate("laserModeInterface", "27", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(28).setText(QtGui.QApplication.translate("laserModeInterface", "28", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(29).setText(QtGui.QApplication.translate("laserModeInterface", "29", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(30).setText(QtGui.QApplication.translate("laserModeInterface", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(31).setText(QtGui.QApplication.translate("laserModeInterface", "31", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(32).setText(QtGui.QApplication.translate("laserModeInterface", "32", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(33).setText(QtGui.QApplication.translate("laserModeInterface", "33", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(34).setText(QtGui.QApplication.translate("laserModeInterface", "34", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(35).setText(QtGui.QApplication.translate("laserModeInterface", "35", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(36).setText(QtGui.QApplication.translate("laserModeInterface", "36", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(37).setText(QtGui.QApplication.translate("laserModeInterface", "37", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(38).setText(QtGui.QApplication.translate("laserModeInterface", "38", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(39).setText(QtGui.QApplication.translate("laserModeInterface", "39", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(40).setText(QtGui.QApplication.translate("laserModeInterface", "40", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(41).setText(QtGui.QApplication.translate("laserModeInterface", "41", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(42).setText(QtGui.QApplication.translate("laserModeInterface", "42", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(43).setText(QtGui.QApplication.translate("laserModeInterface", "43", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(44).setText(QtGui.QApplication.translate("laserModeInterface", "44", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(45).setText(QtGui.QApplication.translate("laserModeInterface", "45", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(46).setText(QtGui.QApplication.translate("laserModeInterface", "46", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(47).setText(QtGui.QApplication.translate("laserModeInterface", "47", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(48).setText(QtGui.QApplication.translate("laserModeInterface", "48", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(49).setText(QtGui.QApplication.translate("laserModeInterface", "49", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(50).setText(QtGui.QApplication.translate("laserModeInterface", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(51).setText(QtGui.QApplication.translate("laserModeInterface", "51", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(52).setText(QtGui.QApplication.translate("laserModeInterface", "52", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(53).setText(QtGui.QApplication.translate("laserModeInterface", "53", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(54).setText(QtGui.QApplication.translate("laserModeInterface", "54", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(55).setText(QtGui.QApplication.translate("laserModeInterface", "55", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(56).setText(QtGui.QApplication.translate("laserModeInterface", "56", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(57).setText(QtGui.QApplication.translate("laserModeInterface", "57", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(58).setText(QtGui.QApplication.translate("laserModeInterface", "58", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(59).setText(QtGui.QApplication.translate("laserModeInterface", "59", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(60).setText(QtGui.QApplication.translate("laserModeInterface", "60", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(61).setText(QtGui.QApplication.translate("laserModeInterface", "61", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(62).setText(QtGui.QApplication.translate("laserModeInterface", "62", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(63).setText(QtGui.QApplication.translate("laserModeInterface", "63", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(64).setText(QtGui.QApplication.translate("laserModeInterface", "64", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(65).setText(QtGui.QApplication.translate("laserModeInterface", "65", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(66).setText(QtGui.QApplication.translate("laserModeInterface", "66", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(67).setText(QtGui.QApplication.translate("laserModeInterface", "67", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(68).setText(QtGui.QApplication.translate("laserModeInterface", "68", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(69).setText(QtGui.QApplication.translate("laserModeInterface", "69", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(70).setText(QtGui.QApplication.translate("laserModeInterface", "71", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(71).setText(QtGui.QApplication.translate("laserModeInterface", "72", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(72).setText(QtGui.QApplication.translate("laserModeInterface", "722", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(73).setText(QtGui.QApplication.translate("laserModeInterface", "73", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(74).setText(QtGui.QApplication.translate("laserModeInterface", "74", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(75).setText(QtGui.QApplication.translate("laserModeInterface", "75", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(76).setText(QtGui.QApplication.translate("laserModeInterface", "76", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(77).setText(QtGui.QApplication.translate("laserModeInterface", "77", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(78).setText(QtGui.QApplication.translate("laserModeInterface", "78", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(79).setText(QtGui.QApplication.translate("laserModeInterface", "79", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(80).setText(QtGui.QApplication.translate("laserModeInterface", "80", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(81).setText(QtGui.QApplication.translate("laserModeInterface", "81", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(82).setText(QtGui.QApplication.translate("laserModeInterface", "82", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(83).setText(QtGui.QApplication.translate("laserModeInterface", "83", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(84).setText(QtGui.QApplication.translate("laserModeInterface", "84", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(85).setText(QtGui.QApplication.translate("laserModeInterface", "85", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(86).setText(QtGui.QApplication.translate("laserModeInterface", "86", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(87).setText(QtGui.QApplication.translate("laserModeInterface", "87", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(88).setText(QtGui.QApplication.translate("laserModeInterface", "88", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(89).setText(QtGui.QApplication.translate("laserModeInterface", "89", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(90).setText(QtGui.QApplication.translate("laserModeInterface", "90", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(91).setText(QtGui.QApplication.translate("laserModeInterface", "91", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(92).setText(QtGui.QApplication.translate("laserModeInterface", "92", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(93).setText(QtGui.QApplication.translate("laserModeInterface", "93", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(94).setText(QtGui.QApplication.translate("laserModeInterface", "95", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(95).setText(QtGui.QApplication.translate("laserModeInterface", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(96).setText(QtGui.QApplication.translate("laserModeInterface", "96", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(97).setText(QtGui.QApplication.translate("laserModeInterface", "97", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(98).setText(QtGui.QApplication.translate("laserModeInterface", "98", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.verticalHeaderItem(99).setText(QtGui.QApplication.translate("laserModeInterface", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("laserModeInterface", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.ghTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("laserModeInterface", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.generatePulse.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Generate a particle beam with the specified parameters.", None, QtGui.QApplication.UnicodeUTF8))
        self.generatePulse.setText(QtGui.QApplication.translate("laserModeInterface", "Generate Pulse", None, QtGui.QApplication.UnicodeUTF8))
        self.saveToFile.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Save particle data to a file.", None, QtGui.QApplication.UnicodeUTF8))
        self.saveToFile.setText(QtGui.QApplication.translate("laserModeInterface", "Save to File", None, QtGui.QApplication.UnicodeUTF8))
        self.unitsLabel.setText(QtGui.QApplication.translate("laserModeInterface", "Plotting units", None, QtGui.QApplication.UnicodeUTF8))
        self.unitsXYLabel.setText(QtGui.QApplication.translate("laserModeInterface", "   x, y", None, QtGui.QApplication.UnicodeUTF8))
        self.unitsXY.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Units to be used for axis labels of position-like variables.\n"
"For example: m, mm, um (or microns), nm ...", None, QtGui.QApplication.UnicodeUTF8))
        self.unitsZLabel.setText(QtGui.QApplication.translate("laserModeInterface", "<html><head/><body><p>&nbsp; &nbsp; z</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.unitsZ.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Units to be used for axis labels of angle-like variables.\n"
"For example: rad, mrad, urad (or microrad) ...", None, QtGui.QApplication.UnicodeUTF8))
        self.ticksLabel.setText(QtGui.QApplication.translate("laserModeInterface", "# ticks", None, QtGui.QApplication.UnicodeUTF8))
        self.numTicks.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Suggest a maximum # of tick marks for the axes.\n"
"Logic for actual # is due to matplotlib library.", None, QtGui.QApplication.UnicodeUTF8))
        self.importFile.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Import particle data from a file.", None, QtGui.QApplication.UnicodeUTF8))
        self.importFile.setText(QtGui.QApplication.translate("laserModeInterface", "Import File", None, QtGui.QApplication.UnicodeUTF8))
        self.externalFields.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Generate a particle beam with the specified parameters.", None, QtGui.QApplication.UnicodeUTF8))
        self.externalFields.setText(QtGui.QApplication.translate("laserModeInterface", "External fields", None, QtGui.QApplication.UnicodeUTF8))
        self.noTitles.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Toggle plot titles on/off.", None, QtGui.QApplication.UnicodeUTF8))
        self.noTitles.setStatusTip(QtGui.QApplication.translate("laserModeInterface", "Toggle plot titles on/off.", None, QtGui.QApplication.UnicodeUTF8))
        self.noTitles.setText(QtGui.QApplication.translate("laserModeInterface", "NT", None, QtGui.QApplication.UnicodeUTF8))
        self.generateCoeffs.setToolTip(QtGui.QApplication.translate("laserModeInterface", "Generate a particle beam with the specified parameters.", None, QtGui.QApplication.UnicodeUTF8))
        self.generateCoeffs.setText(QtGui.QApplication.translate("laserModeInterface", "Gauss-Hermite coefficients", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidget import matplotlibWidget

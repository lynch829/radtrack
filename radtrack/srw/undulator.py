# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'undulator.ui'
#
# Created: Wed Nov 05 18:33:47 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

import sip
#sip.setapi('QString', 2)
from PyQt4 import QtCore, QtGui

class ui_form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(926, 677)
        self.formLayoutWidget = QtGui.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 301, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.numper = QtGui.QLineEdit(self.formLayoutWidget)
        self.numper.setObjectName("numper")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.numper)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_11)
        self.undper = QtGui.QLineEdit(self.formLayoutWidget)
        self.undper.setObjectName("undper")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.undper)
        self.by = QtGui.QLineEdit(self.formLayoutWidget)
        self.by.setObjectName("by")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.by)
        self.bx = QtGui.QLineEdit(self.formLayoutWidget)
        self.bx.setObjectName("bx")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.bx)
        self.phbx = QtGui.QLineEdit(self.formLayoutWidget)
        self.phbx.setObjectName("phbx")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.phbx)
        self.phby = QtGui.QLineEdit(self.formLayoutWidget)
        self.phby.setObjectName("phby")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.phby)
        self.sbx = QtGui.QLineEdit(self.formLayoutWidget)
        self.sbx.setObjectName("sbx")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.sbx)
        self.sby = QtGui.QLineEdit(self.formLayoutWidget)
        self.sby.setObjectName("sby")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.sby)
        self.xcid = QtGui.QLineEdit(self.formLayoutWidget)
        self.xcid.setObjectName("xcid")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.xcid)
        self.ycid = QtGui.QLineEdit(self.formLayoutWidget)
        self.ycid.setObjectName("ycid")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.ycid)
        self.zcid = QtGui.QLineEdit(self.formLayoutWidget)
        self.zcid.setObjectName("zcid")
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.zcid)
        self.formLayoutWidget_2 = QtGui.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(350, 30, 261, 181))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_12 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_18)
        self.iavg = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.iavg.setObjectName("iavg")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.iavg)
        self.partstatmom1x = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.partstatmom1x.setObjectName("partstatmom1x")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.partstatmom1x)
        self.partstatmom1y = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.partstatmom1y.setObjectName("partstatmom1y")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.partstatmom1y)
        self.partstatmom1z = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.partstatmom1z.setObjectName("partstatmom1z")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.partstatmom1z)
        self.partstatmom1xp = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.partstatmom1xp.setObjectName("partstatmom1xp")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.partstatmom1xp)
        self.partstatmom1yp = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.partstatmom1yp.setObjectName("partstatmom1yp")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.partstatmom1yp)
        self.partstatmom1gamma = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.partstatmom1gamma.setObjectName("partstatmom1gamma")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.partstatmom1gamma)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 270, 81, 71))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget_3 = QtGui.QWidget(Form)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(650, 30, 261, 178))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_19 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_19)
        self.meth = QtGui.QComboBox(self.formLayoutWidget_3)
        self.meth.setObjectName("meth")
        self.meth.addItem("")
        self.meth.addItem("")
        self.meth.addItem("")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.meth)
        self.label_20 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_20)
        self.relprec = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.relprec.setObjectName("relprec")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.relprec)
        self.label_21 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_21)
        self.label_22 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_24)
        self.usetermin = QtGui.QComboBox(self.formLayoutWidget_3)
        self.usetermin.setObjectName("usetermin")
        self.usetermin.addItem("")
        self.usetermin.addItem("")
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.usetermin)
        self.label_25 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_25)
        self.sampfactnxnyprop = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.sampfactnxnyprop.setObjectName("sampfactnxnyprop")
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.sampfactnxnyprop)
        self.zstartint = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.zstartint.setObjectName("zstartint")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.zstartint)
        self.zendint = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.zendint.setObjectName("zendint")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.zendint)
        self.nptraj = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.nptraj.setObjectName("nptraj")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.nptraj)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(350, 250, 291, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.formLayoutWidget_4 = QtGui.QWidget(Form)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(30, 370, 301, 80))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtGui.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_31 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_31.setObjectName("label_31")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_31)
        self.label_32 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_32.setObjectName("label_32")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_32)
        self.intensity = QtGui.QComboBox(self.formLayoutWidget_4)
        self.intensity.setObjectName("intensity")
        self.intensity.addItem("")
        self.intensity.addItem("")
        self.intensity.addItem("")
        self.intensity.addItem("")
        self.intensity.addItem("")
        self.intensity.addItem("")
        self.intensity.addItem("")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.intensity)
        self.label_33 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_33.setObjectName("label_33")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_33)
        self.deparg = QtGui.QComboBox(self.formLayoutWidget_4)
        self.deparg.setObjectName("deparg")
        self.deparg.addItem("")
        self.deparg.addItem("")
        self.deparg.addItem("")
        self.deparg.addItem("")
        self.deparg.addItem("")
        self.deparg.addItem("")
        self.deparg.addItem("")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.deparg)
        self.polar = QtGui.QComboBox(self.formLayoutWidget_4)
        self.polar.setObjectName("polar")
        self.polar.addItem("")
        self.polar.addItem("")
        self.polar.addItem("")
        self.polar.addItem("")
        self.polar.addItem("")
        self.polar.addItem("")
        self.polar.addItem("")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.polar)
        self.label_26 = QtGui.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(150, 10, 46, 13))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtGui.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(450, 10, 46, 13))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtGui.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(760, 10, 46, 13))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtGui.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(150, 350, 46, 13))
        self.label_29.setObjectName("label_29")
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 340, 311, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(330, 30, 20, 421))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_30 = QtGui.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(470, 230, 71, 16))
        self.label_30.setObjectName("label_30")
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(340, 220, 571, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(620, 30, 20, 195))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.status = QtGui.QTextEdit(Form)
        self.status.setGeometry(QtCore.QRect(740, 270, 181, 161))
        self.status.setObjectName("status")
        self.analytic = QtGui.QTextEdit(Form)
        self.analytic.setGeometry(QtCore.QRect(30, 490, 311, 171))
        self.analytic.setObjectName("analytic")
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(390, 471, 521, 191))
        self.graphicsView.setObjectName("graphicsView")
        self.label_34 = QtGui.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(740, 250, 46, 13))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtGui.QLabel(Form)
        self.label_35.setGeometry(QtCore.QRect(30, 470, 131, 16))
        self.label_35.setObjectName("label_35")
        self.plotButton = QtGui.QPushButton(Form)
        self.plotButton.setGeometry(QtCore.QRect(650, 370, 81, 61))
        self.plotButton.setObjectName("plotButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Number of Periods", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Period Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Peak Vertical Field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Peak Horizontal Field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Inital Phase of Horizontal Field Component", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Inital Phase of Vertical Field Componenent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Symmetry of Horizontal Field Component", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Symmetry of Vertical Field Component", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Horizontal Coordinate of Undulator Center ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Vertical Coordinate of Undulator Center", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Longitufinal Coordinate of Undulator Center", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "Avergae Current", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Form", "Initial Horizontal Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "Inital Vertical Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "Inital Longitudinal Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Form", "Initial Relative Horizontal Velocity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Form", "Initial Relative Vertical Velocity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Form", "Relativistic Gamma", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "SRW", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Form", "SR calculation method", None, QtGui.QApplication.UnicodeUTF8))
        self.meth.setItemText(0, QtGui.QApplication.translate("Form", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.meth.setItemText(1, QtGui.QApplication.translate("Form", "Auto-Undulator", None, QtGui.QApplication.UnicodeUTF8))
        self.meth.setItemText(2, QtGui.QApplication.translate("Form", "Auto-Wiggler", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Form", "Relative precision", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Form", "Start integration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Form", "End integration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Form", "Number of trajectory points", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Form", "Use terminating terms", None, QtGui.QApplication.UnicodeUTF8))
        self.usetermin.setItemText(0, QtGui.QApplication.translate("Form", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.usetermin.setItemText(1, QtGui.QApplication.translate("Form", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Form", "Sampling factor (nx,ny)", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Number of points along Energy", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Number of Points along X", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Number of points along Y", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(3).setText(QtGui.QApplication.translate("Form", "Position to calculate SR", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(4).setText(QtGui.QApplication.translate("Form", "Inital Photon Energy", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(5).setText(QtGui.QApplication.translate("Form", "Final Photon Energy", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(6).setText(QtGui.QApplication.translate("Form", "Inital X position", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(7).setText(QtGui.QApplication.translate("Form", "Inital Y position", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(8).setText(QtGui.QApplication.translate("Form", "Final X position", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(9).setText(QtGui.QApplication.translate("Form", "Final Y position", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Mesh", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("Form", "polarization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("Form", "intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.intensity.setItemText(0, QtGui.QApplication.translate("Form", "Single Electron Intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.intensity.setItemText(1, QtGui.QApplication.translate("Form", "Multi Electron Intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.intensity.setItemText(2, QtGui.QApplication.translate("Form", "Single Electron FLux", None, QtGui.QApplication.UnicodeUTF8))
        self.intensity.setItemText(3, QtGui.QApplication.translate("Form", "Multi Electron FLux", None, QtGui.QApplication.UnicodeUTF8))
        self.intensity.setItemText(4, QtGui.QApplication.translate("Form", "Single Electron Radiation Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.intensity.setItemText(5, QtGui.QApplication.translate("Form", "Real Part of Electron E-Field", None, QtGui.QApplication.UnicodeUTF8))
        self.intensity.setItemText(6, QtGui.QApplication.translate("Form", "Imaginary Part of Electron E-Field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("Form", "Dependent Argument", None, QtGui.QApplication.UnicodeUTF8))
        self.deparg.setItemText(0, QtGui.QApplication.translate("Form", "e (energy)", None, QtGui.QApplication.UnicodeUTF8))
        self.deparg.setItemText(1, QtGui.QApplication.translate("Form", "x (horizontal)", None, QtGui.QApplication.UnicodeUTF8))
        self.deparg.setItemText(2, QtGui.QApplication.translate("Form", "y (vertical)", None, QtGui.QApplication.UnicodeUTF8))
        self.deparg.setItemText(3, QtGui.QApplication.translate("Form", "x & y", None, QtGui.QApplication.UnicodeUTF8))
        self.deparg.setItemText(4, QtGui.QApplication.translate("Form", "e & x", None, QtGui.QApplication.UnicodeUTF8))
        self.deparg.setItemText(5, QtGui.QApplication.translate("Form", "e & y", None, QtGui.QApplication.UnicodeUTF8))
        self.deparg.setItemText(6, QtGui.QApplication.translate("Form", "e & x & y", None, QtGui.QApplication.UnicodeUTF8))
        self.polar.setItemText(0, QtGui.QApplication.translate("Form", "Linear Horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.polar.setItemText(1, QtGui.QApplication.translate("Form", "Linear Vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.polar.setItemText(2, QtGui.QApplication.translate("Form", "Linear 45 Degrees", None, QtGui.QApplication.UnicodeUTF8))
        self.polar.setItemText(3, QtGui.QApplication.translate("Form", "Linear 135 Degrees", None, QtGui.QApplication.UnicodeUTF8))
        self.polar.setItemText(4, QtGui.QApplication.translate("Form", "Circular Right", None, QtGui.QApplication.UnicodeUTF8))
        self.polar.setItemText(5, QtGui.QApplication.translate("Form", "Circular", None, QtGui.QApplication.UnicodeUTF8))
        self.polar.setItemText(6, QtGui.QApplication.translate("Form", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("Form", "Undulator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("Form", "Beam", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Form", "Precision", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Form", "Plots", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("Form", "Wavefront", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("Form", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("Form", "Analytic Calculations", None, QtGui.QApplication.UnicodeUTF8))
        self.plotButton.setText(QtGui.QApplication.translate("Form", "Plot", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genund.ui'
#
# Created: Tue Feb 03 18:52:33 2015
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_genund(object):
    def setupUi(self, genund):
        genund.setObjectName("genund")
        genund.resize(300, 350)
        self.formLayoutWidget = QtGui.QWidget(genund)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 241, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.iwityp = QtGui.QPushButton(self.formLayoutWidget)
        self.iwityp.setObjectName("iwityp")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.iwityp)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.aw0 = QtGui.QLineEdit(self.formLayoutWidget)
        self.aw0.setObjectName("aw0")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.aw0)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.xlamd = QtGui.QLineEdit(self.formLayoutWidget)
        self.xlamd.setObjectName("xlamd")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.xlamd)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.nwig = QtGui.QLineEdit(self.formLayoutWidget)
        self.nwig.setObjectName("nwig")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.nwig)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_8)
        self.nsec = QtGui.QLineEdit(self.formLayoutWidget)
        self.nsec.setObjectName("nsec")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.nsec)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.awx = QtGui.QLineEdit(self.formLayoutWidget)
        self.awx.setObjectName("awx")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.awx)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.awy = QtGui.QLineEdit(self.formLayoutWidget)
        self.awy.setObjectName("awy")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.awy)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delaw = QtGui.QLineEdit(self.formLayoutWidget)
        self.delaw.setObjectName("delaw")
        self.horizontalLayout.addWidget(self.delaw)
        self.iertyp = QtGui.QSpinBox(self.formLayoutWidget)
        self.iertyp.setObjectName("iertyp")
        self.horizontalLayout.addWidget(self.iertyp)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)

        self.retranslateUi(genund)
        QtCore.QMetaObject.connectSlotsByName(genund)

    def retranslateUi(self, genund):
        genund.setWindowTitle(QtGui.QApplication.translate("genund", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("genund", "Undulator Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.iwityp.setText(QtGui.QApplication.translate("genund", "Planar/Helical", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("genund", "Undulator Parameter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("genund", "Period Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("genund", "Number of Periods:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("genund", "Sections:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("genund", "Field Errors:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("genund", "Offset - x:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("genund", "Offset - y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("genund", "seed:", None, QtGui.QApplication.UnicodeUTF8))


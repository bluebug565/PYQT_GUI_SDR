# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sdr_login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 264)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/CU-Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:qlineargradient(spread:pad, x1:0.931818, y1:0.159, x2:0.960227, y2:0, stop:0.181818 rgba(129, 30, 106, 248), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.groupBox_login = QtWidgets.QGroupBox(Dialog)
        self.groupBox_login.setGeometry(QtCore.QRect(30, 40, 331, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.groupBox_login.setFont(font)
        self.groupBox_login.setAutoFillBackground(True)
        self.groupBox_login.setStyleSheet("QgroupBox:{\n"
"qlineargradient(spread:pad, x1:0.926136, y1:0.04, x2:0.960227, y2:0, stop:1 rgba(122, 115, 114, 239));\n"
"}")
        self.groupBox_login.setObjectName("groupBox_login")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_login)
        self.layoutWidget_2.setGeometry(QtCore.QRect(217, 150, 101, 39))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.login_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_btn.setFont(font)
        self.login_btn.setAutoFillBackground(False)
        self.login_btn.setCheckable(True)
        self.login_btn.setAutoDefault(True)
        self.login_btn.setDefault(True)
        self.login_btn.setFlat(False)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_4.addWidget(self.login_btn)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_login)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 296, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.username = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        self.username_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.username_lineEdit.setFrame(True)
        self.username_lineEdit.setDragEnabled(False)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout_2.addWidget(self.username_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.password_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_3.addWidget(self.password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Security"))
        self.groupBox_login.setTitle(_translate("Dialog", "Signin"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.username.setText(_translate("Dialog", "USERNAME"))
        self.password.setText(_translate("Dialog", "PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


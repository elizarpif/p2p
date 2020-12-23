# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/messenger.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 682)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 243, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 243, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 243, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 440, 421, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.addrLn = QtWidgets.QLineEdit(self.centralwidget)
        self.addrLn.setGeometry(QtCore.QRect(90, 30, 131, 21))
        self.addrLn.setObjectName("addrLn")
        self.addrLb = QtWidgets.QLabel(self.centralwidget)
        self.addrLb.setGeometry(QtCore.QRect(90, 10, 81, 16))
        self.addrLb.setStyleSheet("QWidget#centralwidget {\n"
"    background: QColor(176, 224, 230)\n"
"}")
        self.addrLb.setObjectName("addrLb")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(520, 440, 131, 41))
        self.sendButton.setObjectName("sendButton")
        self.chat = QtWidgets.QTextEdit(self.centralwidget)
        self.chat.setEnabled(True)
        self.chat.setGeometry(QtCore.QRect(90, 70, 421, 361))
        self.chat.setStyleSheet("QTextEdit: {\n"
" border-style: outset;\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"}")
        self.chat.setReadOnly(True)
        self.chat.setObjectName("chat")
        self.logLabel = QtWidgets.QLabel(self.centralwidget)
        self.logLabel.setGeometry(QtCore.QRect(377, 30, 141, 20))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        font.setItalic(True)
        self.logLabel.setFont(font)
        self.logLabel.setObjectName("logLabel")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(520, 20, 112, 41))
        self.connectButton.setObjectName("connectButton")
        self.portLn = QtWidgets.QLineEdit(self.centralwidget)
        self.portLn.setGeometry(QtCore.QRect(230, 30, 131, 21))
        self.portLn.setObjectName("portLn")
        self.portLb = QtWidgets.QLabel(self.centralwidget)
        self.portLb.setGeometry(QtCore.QRect(230, 10, 81, 16))
        self.portLb.setStyleSheet("QWidget#centralwidget {\n"
"    background: QColor(176, 224, 230)\n"
"}")
        self.portLb.setObjectName("portLb")
        self.currentAddr = QtWidgets.QLabel(self.centralwidget)
        self.currentAddr.setEnabled(True)
        self.currentAddr.setGeometry(QtCore.QRect(540, 140, 211, 16))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        font.setItalic(True)
        self.currentAddr.setFont(font)
        self.currentAddr.setObjectName("currentAddr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 100, 141, 20))
        self.label.setObjectName("label")
        self.logEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logEdit.setEnabled(False)
        self.logEdit.setGeometry(QtCore.QRect(90, 500, 421, 61))
        self.logEdit.setObjectName("logEdit")
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setGeometry(QtCore.QRect(660, 440, 121, 41))
        self.fileButton.setObjectName("fileButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мессенджер"))
        self.addrLn.setText(_translate("MainWindow", "127.0.0.1"))
        self.addrLb.setText(_translate("MainWindow", "Address"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.chat.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.logLabel.setText(_translate("MainWindow", "Disconnected"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.portLn.setText(_translate("MainWindow", "9000"))
        self.portLb.setText(_translate("MainWindow", "Port"))
        self.currentAddr.setText(_translate("MainWindow", "9000"))
        self.label.setText(_translate("MainWindow", "Current address"))
        self.fileButton.setText(_translate("MainWindow", "File"))


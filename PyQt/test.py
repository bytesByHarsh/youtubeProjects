# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(40, 180, 71, 28))
        self.okButton.setObjectName("okButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(130, 180, 93, 28))
        self.closeButton.setObjectName("closeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 50, 191, 121))
        self.textEdit.setObjectName("textEdit")
        self.testSlider = QtWidgets.QSlider(self.centralwidget)
        self.testSlider.setGeometry(QtCore.QRect(450, 160, 160, 16))
        self.testSlider.setOrientation(QtCore.Qt.Horizontal)
        self.testSlider.setObjectName("testSlider")
        self.option1CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.option1CheckBox.setGeometry(QtCore.QRect(260, 60, 71, 20))
        self.option1CheckBox.setObjectName("option1CheckBox")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 230, 611, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.option2CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.option2CheckBox.setGeometry(QtCore.QRect(260, 90, 75, 20))
        self.option2CheckBox.setObjectName("option2CheckBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.okButton.setText(_translate("MainWindow", "OK"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "Test Window"))
        self.option1CheckBox.setText(_translate("MainWindow", "Option 1"))
        self.option2CheckBox.setText(_translate("MainWindow", "Option 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


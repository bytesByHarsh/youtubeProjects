from PyQt5 import QtWidgets, uic
import sys


class NetworkUi(QtWidgets.QMainWindow):
	def __init__(self):
		super(NetworkUi,self).__init__() #Call the inherited classes __init__ method
		uic.loadUi('test.ui', self)
		self.show()

app = QtWidgets.QApplication(sys.argv)
window = NetworkUi()
app.exec_()
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import sys

import cv2,imutils

class PaintUI(QtWidgets.QMainWindow):
	def __init__(self):
		super(PaintUI,self).__init__() #Call the inherited classes __init__ method
		uic.loadUi('main.ui', self)
		
		## Add Code here
		self.fileName = None
		self.tmp = None
		self.cannyThreshold1 = 0
		self.cannyThreshold2 = 100

		# Signal and Slots
		self.loadButton.clicked.connect(self.loadImage)
		self.saveButton.clicked.connect(self.label.clear)
		self.thresh1Slider.valueChanged['int'].connect(self.thresholdValue1)
		self.thresh2Slider.valueChanged['int'].connect(self.thresholdValue2)

		self.show()

	def loadImage(self):
		"""
		Load user selected photo and set to label
		"""
		self.fileName = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
		if not self.fileName:
			return
		self.img = cv2.imread(self.fileName)
		self.setPhoto(self.img)

	def setPhoto(self,image):
		"""
		Set photo over label

		TODO: Resize according to the label and image size
		"""
		self.tmp = image
		image = imutils.resize(image,height=590)
		frame = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
		image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
		self.label.setPixmap(QtGui.QPixmap.fromImage(image))

	def thresholdValue1(self,value):
		self.cannyThreshold1 = value
		print(f"Thresh 1: {value}")

	def thresholdValue2(self,value):
		self.cannyThreshold2 = value
		print(f"Thresh 2: {value}")



app = QtWidgets.QApplication(sys.argv)
window = PaintUI()
app.exec_()
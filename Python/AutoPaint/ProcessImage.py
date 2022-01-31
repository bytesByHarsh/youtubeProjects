import pyautogui
import time
import cv2

pyautogui.PAUSE = 0.01

class ProcessImage():
	def __init__(self):
		self.canvas_start_ratio_x = 10.0/1920
		self.canvas_start_ratio_y = 180.0/1080

		self.canvas_size_ratio_x = 1070.0/1920
		self.canvas_size_ratio_y = 670.0/1080

		self.screenWidth, self.screenHeight = pyautogui.size()

		self.canvas_start_x = self.screenWidth*self.canvas_start_ratio_x
		self.canvas_start_y = self.screenHeight*self.canvas_start_ratio_y

		self.canvas_end_x = self.canvas_start_x + self.canvas_size_ratio_x*self.screenWidth
		self.canvas_end_y = self.canvas_start_y + self.canvas_size_ratio_y*self.screenHeight

		self.img = None

	def loadImage(self,img):
		self.img = img.copy()
		(self.h,self.w) = self.img.shape[:2]

		if self.h>self.w:
			self.img = self.image_resize(self.img,height=int(self.canvas_size_ratio_y*self.screenHeight))
		else:
			self.img = self.image_resize(self.img,width=int(self.canvas_size_ratio_x*self.screenWidth))

		self.image_pre_process()
		self.edge_detection()

	def refreshImage(self,thesh1,thresh2):
		self.edges = cv2.Canny(image=self.img_blur, threshold1=thesh1, threshold2=thresh2)
		return self.edges

	def image_resize(self,image, width = None, height = None, inter = cv2.INTER_AREA):
		dim = None
		(h, w) = image.shape[:2]
		if width is None and height is None:
			return None

		if width is None:
			r = height / float(h)
			dim = (int(w * r), height)
		else:
			r = width / float(w)
			dim = (width, int(h * r))
		resized = cv2.resize(image, dim, interpolation = inter)
		return resized

	def image_pre_process(self):
		self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
		self.img_blur = cv2.GaussianBlur(self.img_gray, (3,3), 0)

	def edge_detection(self):
		# self.sobelx = cv2.Sobel(src=self.img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge
		# self.sobely = cv2.Sobel(src=self.img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge
		# self.sobelxy = cv2.Sobel(src=self.img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X

		self.edges = cv2.Canny(image=self.img_blur, threshold1=30, threshold2=50)

	def startPainting(self):
		print("Starting Painting")
		
		pyautogui.moveTo(self.canvas_start_x, self.canvas_start_y)

		rows,cols = self.edges.shape
		for i in range(rows):
			for j in range(cols):
				if(self.edges[i,j]):
					pyautogui.click(self.canvas_start_x+j, self.canvas_start_y+i)

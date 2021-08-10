import cv2
import numpy as np

class ChangeSize():
	def __init__(self, oldImg):
		self.oldImg = oldImg
		self.oldX, self.oldY, self.oldZ = np.shape(oldImg)


	def zoom(self, x1, y1, x2, y2, windowSizeX, windowSizeY = None):

		ImgYsubbed = self.oldImg[y1:y2]
		newImg = np.zeros((y2-y1,x2-x1,self.oldZ),dtype="uint8")

		for i in range(y2-y1):
			newImg[i] = ImgYsubbed[i][x1:x2]

		ratio = (y2-y1)/(x2-x1)
		windowSizeY = int(windowSizeX*ratio)

		newImg = cv2.resize(newImg, (windowSizeX,windowSizeY), interpolation = cv2.INTER_NEAREST)

		return newImg, (windowSizeX,windowSizeY)
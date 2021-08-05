import cv2
import numpy as np
import time

img = cv2.imread("testImage.jpg")
imgLowRes = cv2.resize(img, (1000,1000))

class ChangeSize():
	def __init__(self, oldImg):
		self.oldImg = oldImg
		self.oldX, self.oldY, self.oldZ = np.shape(oldImg)


	def zoom(self, x1, y1, x2, y2, windowSize):

		ImgYsubbed = self.oldImg[y1:y2]
		newImg = np.zeros((y2-y1,x2-x1,self.oldZ),dtype="uint8")

		for i in range(y2-y1):
			newImg[i] = ImgYsubbed[i][x1:x2]

		ratio = (y2-y1)/(x2-x1)

		newImg = cv2.resize(newImg, (windowSize,int(windowSize*ratio)), interpolation = cv2.INTER_NEAREST)

		return newImg

resizer=ChangeSize(imgLowRes)

newImg = resizer.zoom(10,10,900,200,800)

cv2.imshow("hello",newImg)
cv2.waitKey(0)

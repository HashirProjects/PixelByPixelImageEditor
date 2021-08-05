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


def getMousePostion(img):

	def onClick(event,x,y,flags,param):
		if event == cv2.EVENT_LBUTTONDBLCLK:
			param.append((x,y))
			if len(param) > 2:
				param.pop(0)

	coorList=[]

	cv2.namedWindow('image')
	cv2.setMouseCallback('image',onClick,coorList)

	while True:
		
		cv2.imshow('image',img)
		k = cv2.waitKey(0) & 0xFF
		if k == ord('a'):
			resizer = ChangeSize(img)
			newImg = resizer.zoom(coorList[0][0],coorList[0][1],coorList[1][0],coorList[1][1],800)

			cv2.namedWindow('image')
			cv2.setMouseCallback('image',onClick,coorList)
			cv2.imshow("image", newImg)

			img = newImg
		elif k == 27:
			break


getMousePostion(img)

import cv2
import numpy as np
import time

img = cv2.imread("testImage.jpg")
imgLowRes = cv2.resize(img, (1000,1000))

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


def getMousePostion(img):

	def onClick(event,x,y,flags,param):
		if event == cv2.EVENT_LBUTTONDBLCLK:
			param.append((x,y))
			if len(param) > 2:
				param.pop(0)

	def onClickZoomed(event,x,y,flags,param):
		if event == cv2.EVENT_LBUTTONDBLCLK:
			param.append((x,y))
			if len(param) > 2:
				param.pop(0)

	coorList=[]
	coorListZoomed=[]
	currentZoom = [(0,0),(1000,1000)]

	cv2.namedWindow('image')
	cv2.setMouseCallback('image',onClick,coorList)
	resizer = ChangeSize(img)

	while True:

		cv2.imshow('image',img)# this will always show the same img

		k = cv2.waitKey(0) & 0xFF

		if k == ord('a'):
			currentZoom = coorList

			newimg, windowSize = resizer.zoom(coorList[0][0],coorList[0][1],coorList[1][0],coorList[1][1],800)

			cv2.namedWindow("new image")
			cv2.setMouseCallback('new image',onClick,coorListZoomed)
			cv2.imshow("new image", newimg)

		elif k == ord('s'):


			xDiff = currentZoom[0][0] - currentZoom[1][0]
			yDiff = currentZoom[0][1] - currentZoom[1][1]


			coorList[0] = (currentZoom[0][0] + int((coorListZoomed[0][0]* xDiff)/windowSize[0]), currentZoom[0][1] + int((coorListZoomed[0][1]* xDiff)/windowSize[0]))
			coorList[1] = (currentZoom[1][0] + int((coorListZoomed[1][0]* yDiff)/windowSize[1]), currentZoom[1][1] + int((coorListZoomed[1][1]* yDiff)/windowSize[1]))
			
			newimg, windowSize = resizer.zoom(coorList[0][0],coorList[0][1],coorList[1][0],coorList[1][1],800)

			cv2.namedWindow("new image")
			cv2.setMouseCallback('new image',onClick,coorListZoomed)
			cv2.imshow("new image", newimg)

			currentZoom = coorList


		elif k == 27:
			break


getMousePostion(img)

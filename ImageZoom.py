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


def main(img):

	def onClick(event,x,y,flags,param):
		if event == cv2.EVENT_LBUTTONDBLCLK:
			param.append((x,y))
			if len(param) > 2:
				param.pop(0)

	def findOriginalCoor(windowSize, origin, segmentSize, point):
		X = origin[0] + (point[0] * segmentSize[0]) /windowSize[0]
		Y = origin[1] + (point[1] * segmentSize[1]) /windowSize[1] 

		return int(X),int(Y)

	coorList=[]
	coorListZoomed=[]
	currentZoom = [(0,0),(1000,1000)]

	cv2.namedWindow('image')
	cv2.setMouseCallback('image',onClick,coorList)

	cv2.namedWindow("new image")
	cv2.setMouseCallback('new image',onClick,coorListZoomed)

	resizer = ChangeSize(img)

	cv2.imshow('image',img)# this window will always show the same img

	while True:

		k = cv2.waitKey(0) & 0xFF

		if k == ord('a'):
			currentZoom = coorList

			newimg, windowSize = resizer.zoom(coorList[0][0],coorList[0][1],coorList[1][0],coorList[1][1],800)

			cv2.imshow("new image", newimg)

		elif k == ord('s'):

			xDiff = currentZoom[1][0] - currentZoom[0][0]
			yDiff = currentZoom[1][1] - currentZoom[0][1]

			segmentSize = (xDiff,yDiff)
			points = [(),()]

			points[0]=findOriginalCoor(windowSize,currentZoom[0],segmentSize,coorListZoomed[0])
			points[1]=findOriginalCoor(windowSize, currentZoom[0],segmentSize,coorListZoomed[1])

			newimg, windowSize = resizer.zoom(points[0][0],points[0][1],points[1][0],points[1][1],800)

			cv2.imshow("new image", newimg)

			currentZoom = points

		elif k == ord('d'):
			print(f"coor list {coorList}")
			print(f"coor list zoomed {coorListZoomed}")

		elif k == ord('f'):

			xDiff = currentZoom[1][0] - currentZoom[0][0]
			yDiff = currentZoom[1][1] - currentZoom[0][1]

			segmentSize = (xDiff,yDiff)

			pixl = findOriginalCoor(windowSize, currentZoom[0],segmentSize,coorListZoomed[1])
			print(pixl)

			img[pixl[1]][pixl[0]]= [0,0,0]


			cv2.imshow("image",img)
			resizer = ChangeSize(img)

			currentZoom = coorList

			newimg, windowSize = resizer.zoom(coorList[0][0],coorList[0][1],coorList[1][0],coorList[1][1],800)

			cv2.imshow("new image", newimg)

		elif k == 27:
			break

main(img)

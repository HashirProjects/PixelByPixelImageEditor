import cv2
import numpy as np
import time

img = cv2.imread("testImage.jpg")
imgLowRes = cv2.resize(img, (50,50))

print(type(imgLowRes))

class ChangeSize():
	def __init__(self, oldImg):
		self.oldImg = oldImg
		self.oldX, self.oldY, self.oldZ = np.shape(oldImg)


	def imgZoom(self, multiplier):

		newImg = np.zeros((self.oldX*multiplier, self.oldY * multiplier, self.oldZ), dtype="uint8")
		currentColumnPosition = 0

		for column in self.oldImg:
			
			newColumn= np.zeros((self.oldY*multiplier, self.oldZ), dtype="uint8")
			currentPixelPosition = 0

			for pixel in column:
				for i in range(multiplier):

					for i in range(self.oldZ):
						newColumn[currentPixelPosition][i]=pixel[i]

					currentPixelPosition += 1

			for i in range(multiplier):

				for i in range(self.oldY * multiplier):
					newImg[currentColumnPosition][i] = newColumn[i]

				currentColumnPosition += 1

		return newImg

	def defSize(self, X, Y):

		newImg = np.zeros((X,Y,self.oldZ),dtype="uint8")
		currentColumnPosition = 0

		multiplierX = int(X/self.oldX)
		multiplierY = int(Y/self.oldY)

		for column in self.oldImg:
			
			newColumn = np.zeros((Y,self.oldZ),dtype="uint8")
			currentPixelPosition = 0

			for pixel in column:
				for i in range(multiplierY):

					for i in range(self.oldZ):
						newColumn[currentPixelPosition][i]=pixel[i]

					currentPixelPosition += 1

			for i in range(multiplierX):

				for i in range(Y):
					newImg[currentColumnPosition][i] = newColumn[i]

				currentColumnPosition += 1

		return newImg		




resizer=ChangeSize(imgLowRes)

newImg = resizer.defSize(1000,1000)

print(newImg, np.shape(newImg))

cv2.imshow("hello",newImg)
cv2.waitKey(0)

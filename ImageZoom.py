import cv2
import numpy as np
import time

img = cv2.imread("testImage.jpg")
imgLowRes = cv2.resize(img, (50,50))

print(imgLowRes)

def imgZoom(oldImg, multiplier):

	newImg = []
	newColumn=[]
	for column in oldImg:
		
		newColumn =[]

		for pixel in column:
			for i in range(multiplier):
				newColumn.append(pixel)

		for i in range(multiplier):
			newImg.append(newColumn)

	return np.array(newImg)

newImg = imgZoom(imgLowRes,9)

print(newImg)

cv2.imshow("hello",newImg)
cv2.waitKey(0)

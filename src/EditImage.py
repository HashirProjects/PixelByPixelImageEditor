import cv2
from src.ChangeSize import ChangeSize

class EditImage():
    def __init__(self, imgPath):

        def onClick(event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                param.append((x,y))
                if len(param) > 2:
                    param.pop(0)

        self.imgPath = imgPath
        self.img = cv2.imread(imgPath)

        self.colour = [0,0,0]

        self.coorList=[]
        self.coorListZoomed=[]
        self.currentZoom = [(),()]

        cv2.namedWindow('image')
        cv2.setMouseCallback('image',onClick,self.coorList)

        cv2.namedWindow("new image")
        cv2.setMouseCallback('new image',onClick,self.coorListZoomed)

        self.resizer = ChangeSize(self.img)


    def run(self):

        def findOriginalCoor(windowSize, origin, segmentSize, point):
            X = origin[0] + (point[0] * segmentSize[0]) /windowSize[0]
            Y = origin[1] + (point[1] * segmentSize[1]) /windowSize[1] 

            return int(X),int(Y)

        def orderCoorlist(coorList):
            XValues = [coorList[0][0],coorList[1][0]]
            YValues = [coorList[0][1],coorList[1][1]]

            orderedCoorList = [(),()]

            orderedCoorList[0] = (min(XValues),min(YValues))

            orderedCoorList[1] = (max(XValues),max(YValues))
             
            return orderedCoorList

        cv2.imshow('image',self.img)# this window will always show the same img

        while True:

            k = cv2.waitKey(0) & 0xFF

            if k == ord('a'):

                if self.coorList == []:
                    raise Exception("Insufficient parameters entered for this action")

                entryList = orderCoorlist(self.coorList)
                
                self.currentZoom = entryList

                newimg, windowSize = self.resizer.zoom(entryList[0][0],entryList[0][1],entryList[1][0],entryList[1][1],800)

                cv2.imshow("new image", newimg)

            elif k == ord('s'):

                if len(self.coorListZoomed) < 2:
                    raise Exception("Insufficient parameters entered for this action")

                entryList = orderCoorlist(self.coorListZoomed)

                xDiff = self.currentZoom[1][0] - self.currentZoom[0][0]
                yDiff = self.currentZoom[1][1] - self.currentZoom[0][1]

                segmentSize = (xDiff,yDiff)
                originalPoints = [(),()]


                originalPoints[0]=findOriginalCoor(windowSize,self.currentZoom[0],segmentSize,entryList[0])
                originalPoints[1]=findOriginalCoor(windowSize,self.currentZoom[0],segmentSize,entryList[1])

                self.currentZoom = originalPoints

                newimg, windowSize = self.resizer.zoom(originalPoints[0][0],originalPoints[0][1],originalPoints[1][0],originalPoints[1][1],800)

                cv2.imshow("new image", newimg)

            elif k == ord('d'):
                print(f"coor list {self.coorList}")
                print(f"coor list zoomed {self.coorListZoomed}")

            elif k == ord('f'):

                xDiff = self.currentZoom[1][0] - self.currentZoom[0][0]
                yDiff = self.currentZoom[1][1] - self.currentZoom[0][1]

                segmentSize = (xDiff,yDiff)

                pixl = findOriginalCoor(windowSize, self.currentZoom[0],segmentSize,self.coorListZoomed[-1])
                print(pixl)

                self.img[pixl[1]][pixl[0]]= self.colour


                cv2.imshow("image",self.img)
                self.resizer = ChangeSize(self.img)


                newimg, windowSize = self.resizer.zoom(self.currentZoom[0][0],self.currentZoom[0][1],self.currentZoom[1][0],self.currentZoom[1][1],800)

                cv2.imshow("new image", newimg)

            elif k == ord("g"):

                pixl = self.coorList[-1]

                self.img[pixl[1]][pixl[0]]= self.colour


                cv2.imshow("image",self.img)
                self.resizer = ChangeSize(self.img)


                newimg, windowSize = self.resizer.zoom(self.currentZoom[0][0],self.currentZoom[0][1],self.currentZoom[1][0],self.currentZoom[1][1],800)

                cv2.imshow("new image", newimg)


            elif k == ord("h"):
                self.colour = input(
                    """
Enter the RGB values of the colour 
> """).split(",")

            elif k == 27:
                break

        cv2.destroyAllWindows()

    def save(self):
        cv2.imwrite(self.imgPath, self.img)

if __name__ == "__main__":
    imageEditor = EditImage("C:/Users/hashi/OneDrive/Desktop/Programming/ImageEditor/testImage.jpg")
    imageEditor.run()
import cv2
from ChangeSize import ChangeSize

class EditImage():
    def __init__(self, imgPath, colour):

        def onClick(event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                param.append((x,y))
                if len(param) > 2:
                    param.pop(0)

        self.img = cv2.imread(imgPath)

        self.colour = colour

        self.coorList=[]
        self.coorListZoomed=[]
        self.currentZoom = []

        cv2.namedWindow('image')
        cv2.setMouseCallback('image',onClick,self.coorList)

        cv2.namedWindow("new image")
        cv2.setMouseCallback('new image',onClick,self.coorListZoomed)

        self.resizer = ChangeSize(self.img)

        cv2.imshow('image',self.img)# this window will always show the same img


    def orderCoorlist(self):
        XValues = [self.coorList[0][0],self.coorList[1][0]]
        YValues = [self.coorList[0][1],self.coorList[1][1]]

        self.coorList = [(),()]

        self.coorList[0] = (min(XValues),min(YValues))

        self.coorList[1] = (max(XValues),max(YValues))

    def orderCoorlistZoomed(self):
        XValues = [self.coorListZoomed[0][0],self.coorListZoomed[1][0]]
        YValues = [self.coorListZoomed[0][1],self.coorListZoomed[1][1]]

        self.coorListZoomed = [(),()]

        self.coorListZoomed[0] = (min(XValues),min(YValues))

        self.coorListZoomed[1] = (max(XValues),max(YValues))

    def run(self):
        def findOriginalCoor(windowSize, origin, segmentSize, point):
            X = origin[0] + (point[0] * segmentSize[0]) /windowSize[0]
            Y = origin[1] + (point[1] * segmentSize[1]) /windowSize[1] 

            return int(X),int(Y)

        while True:

            k = cv2.waitKey(0) & 0xFF

            if k == ord('a'):

                if self.coorList == []:
                    raise Exception("Insufficient parameters entered for this action")

                self.orderCoorlist()
                
                self.currentZoom = self.coorList

                newimg, windowSize = self.resizer.zoom(self.coorList[0][0],self.coorList[0][1],self.coorList[1][0],self.coorList[1][1],800)

                cv2.imshow("new image", newimg)

            elif k == ord('s'):

                if len(self.coorListZoomed) < 2:
                    raise Exception("Insufficient parameters entered for this action")

                self.orderCoorlist()

                xDiff = self.currentZoom[1][0] - self.currentZoom[0][0]
                yDiff = self.currentZoom[1][1] - self.currentZoom[0][1]

                segmentSize = (xDiff,yDiff)
                points = [(),()]

                points[0]=findOriginalCoor(windowSize,self.currentZoom[0],segmentSize,self.coorListZoomed[0])
                points[1]=findOriginalCoor(windowSize,self.currentZoom[0],segmentSize,self.coorListZoomed[1])

                newimg, windowSize = self.resizer.zoom(points[0][0],points[0][1],points[1][0],points[1][1],800)

                cv2.imshow("new image", newimg)

                self.currentZoom = points

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

            elif k == 27:
                break

imageEditor = EditImage("C:/Users/hashi/OneDrive/Desktop/Programming/ImageEditor/testImage.jpg", [0,0,0])
imageEditor.run()
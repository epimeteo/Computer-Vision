import cv2 as cv
import numpy as np

x1=0
y1=0
x2=0
y2=0
bandRoi=False

#<------------------------------------------------------------------->

def roiImg(img):
    global x1,y1,x2,y2,bandRoi
    if(bandRoi == True):
        roiImage = img[y1:y2,x1:x2]
        showImage("roiImage",roiImage,1)
    
#<------------------------------------------------------------------->
def mouseClick(event,x,y,flags,param):
    global x1,y1,x2,y2,bandRoi
    print(x1,y1,x2,y2,bandRoi)
    if(event == cv.EVENT_LBUTTONDOWN):
        x1 = abs(x)
        y1 = abs(y)
        
    if(event == cv.EVENT_LBUTTONUP):
        x2 = abs(x)
        y2 = abs(y)
        bandRoi = True
cv.namedWindow("imgColor")
cv.setMouseCallback("imgColor", mouseClick)
#<------------------------------------------------------------------->

def binaryThreshold(imgGray, umbral): # el objeto debe ser blanco, de no ser asi se intercalan los umbrales
    
    h,w = imgGray.shape[:2]
    
    for i in range(h):
        
        for j in range(w):
            
            if (imgGray[i][j] >= umbral):
                
                imgGray[i][j] = 0 #pongo el pixel imgGray[i][j] en 0 = negro
            else:
                imgGray[i][j] = 255 #pongo el pixel imgGray[i][j] en 0 = blanco
    return imgGray

#<------------------------------------------------------------------->                   

def loadImage (path,a) : 
    return cv.imread(path,a)

#<------------------------------------------------------------------->

def showImage(nameWindow, img, t):
    cv.imshow(nameWindow, img)
    cv.waitKey(t)
    return 0
#<-------------------------------------------------------------------> 
def main(path):
    
    while(True):
        img= loadImage(path, 1)# a 1 = full color, 0 = Escala de grises
        
        imgGray = loadImage(path, 0)# a 1 = full color, 0 = Escala de grises

        roiImg(img)   
        
        showImage("imgColor", img, 1)
        
        #destroyWindow()

   
    
   
    
#<------------------------------------------------------------------->
path = input() # Leer entrada
main(path)

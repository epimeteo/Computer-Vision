import cv2 as cv
import numpy as np

#<------------------------------------------------------------------->

            
#<------------------------------------------------------------------->


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

def loadImage (path,a) : # a 1 = full color, 0 = Escala de grises
    return cv.imread(path,a)

#<------------------------------------------------------------------->

def showImage(nameWindow, img, t): #las funciones se declaran con "def"
    cv.imshow(nameWindow, img)
    cv.waitKey(t)
    return 0

#<------------------------------------------------------------------->
def destroyWindow():
    cv.destroyAllWindows()
#<------------------------------------------------------------------->
def nothing(x):
    pass
#<------------------------------------------------------------------->
cv.namedWindow("imgColor") #Crea una ventana que contenga el trackbar

cv.createTrackbar("umbral1", "imgColor", 0, 255, nothing) #trackbar
    
def main(path):

    while(True):
        img = loadImage(path, 1)# a 1 = full color, 0 = Escala de grises
        
        imgGray = loadImage(path, 0)# a 1 = full color, 0 = Escala de grises
        
        umbral1 = cv.getTrackbarPos("umbral1", "imgColor")
        print(umbral1)
        imgBinary = binaryThreshold( imgGray.copy() , umbral1) #la funcion .copy retorna una copia porque utiliaz los mismos espacios de memoria que la otra imgen
       
        
        showImage("imgBinary", imgBinary, 1)
        
        showImage("imgColor", img, 1)

        #destroyWindow()
#<------------------------------------------------------------------->
path="delfin.jpg"

main(path)

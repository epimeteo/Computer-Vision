import cv2 as cv
import numpy as np

x1=0
y1=0
contador = 0

#<------------------------------------------------------------------->

def valPixel(img):
    global x1,y1
    print(img[y1,x1])
    
#<------------------------------------------------------------------->
def mouseClick(event,x,y,flags,param):
    global x1,y1  
    if(event == cv.EVENT_LBUTTONDOWN):
       x1 = x
       y1 = y
       
       contador = contador + 1
       
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
    
def main(path):
    
    while(contador < 4):
        img= loadImage(path, 1)# a 1 = full color, 0 = Escala de grises
        
        imgGray = loadImage(path, 0)# a 1 = full color, 0 = Escala de grises
        
        #imgBinary = binaryThreshold( imgGray.copy() , 128) #la funcion .copy retorna una copia porque utiliaz los mismos espacios de memoria que la otra imgen
        
        valPixel(img)   
        
        #showImage("imgBinary", imgBinary, 1)
        
        showImage("imgColor", img, 1)
        
        #destroyWindow()

   
    
   
    
#<------------------------------------------------------------------->

path="delfin.jpg"

main(path)

import numpy as np
import cv2 as cv

path = "22.jpg"

def showHistogram(imgGray):
    wbins = 256
    hbins = 256
    #cv.calcHist(images, channels, mask, histSize, ranges)###
    
    histr = cv.calcHist([imgGray],[0],None,[hbins],[0,wbins])
    
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(histr)

    imgHist = np.zeros([hbins, wbins], np.uint8)
    
    for w in range(wbins):
        binVal = histr[w]
        intensity = binVal*(hbins-1)/max_val
        cv.line(imgHist, (w,hbins), (w,hbins-intensity),255)
    
    return imgHist
 
def showImage(namedWindow,img,t):
    cv.imshow(namedWindow, img)
    cv.waitKey(t)

def loadImage(path,a):
    return cv.imread(path,a)

def destroyWindow():
    cv.destroyAllWindows
    
if __name__ == "__main__":
    #iniciar programa
    
    img = loadImage(path,1)
    imgGray = loadImage(path,0)
    showImage("imgColor",img,0)
    

    imgHist = showHistogram(imgGray)
    showImage("imgHist",imgHist,0)
    
    
    


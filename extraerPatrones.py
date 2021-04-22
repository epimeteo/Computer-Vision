import cv2
import numpy as np
import xlsxwriter as xlsx
from glob import glob

row = 0
col = 0
#para ir saltando de fila en fila/comlumna
i = 1
#crear el archivo de excel
libroTrabajo = xlsx.Workbook('DataNumsPairs.xlsx')
hojaTrabajo =libroTrabajo.add_worksheet('CaractNums')

vectorNums = ['0','2','4','6','8']

for j in range(0,len(vectorNums)):
    for imgPath in glob('num/'+vectorNums[j]+'/*.png'):
        imgColor = cv2.imread(imgPath,1)
        img      = cv2.imread(imgPath,0)
        img      = cv2.resize(img,(25,50))
        imgColor = cv2.resize(imgColor,(25,50))
        
        ret, imgBin = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        #encontrar y almacenar contornos
        contours,hierarchy = cv2.findContours(imgBin.copy(),\
                                                    cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            x,y,w,h =cv2.boundingRect(cnt)
            a=cv2.contourArea(cnt)
            if(a>10):
                cv2.rectangle(imgColor,(x,y),(x+w, y+h),(255,0,0),2)
                #cv2.imshow('imgColor',imgColor)
                #cv2.waitKey(0)
                perimetro = cv2.arcLength(cnt,True)
                ra = float(w/h)
                c = a/(pow(perimetro,2))
                rg = a/(w*h)
                M = cv2.moments(cnt)
                Hu = cv2.HuMoments(M)
                print(Hu[0][0],Hu[1][0])
                cv2.imshow('imgColor',imgColor)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                vectorCaract = np.array([a,perimetro,ra,c,rg,Hu[0][0],Hu[1][0],Hu[2][0]],dtype = np.float32)
                for carac in vectorCaract:
                    hojaTrabajo.write(row,0,vectorNums[j])
                    hojaTrabajo.write(row,i,carac)
                    i=i+1
                i=1
                row=row+1
libroTrabajo.close()
print('fin..')

##cv2.imshow('imgBin',imgBin)
##cv2.waitKey(0)


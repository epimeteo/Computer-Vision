
import cv2
import numpy as np
import time

path="billar.mp4"

capture = cv2.VideoCapture(path)

time.sleep(2)#tiempo antes de que comienze el video en segundos, con el fin de que alcance a cargar el id de la camara y procesar

#Como un video es una secuencia de imagenes debo emplear un for o un while infinito
while(capture.isOpened()): #isOpened() retorna un bool cuando se abre el video
    ret, frame = capture.read() # del video vaya leyendo de a 1 frame por vez, si es capaz de leer ese frame haga el ret=true
    if(ret==False):
        break#salgase del while
    #Aqui va el procesamiento:
    
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #El frame lo vaoms a pasara a gris

    h,w = frame_gray.shape
    
    ret2, frame_binary = cv2.threshold(frame_gray, 230 ,255, cv2.THRESH_BINARY) # lo pasamos a binario

    contours, hierarchy = cv2.findContours(frame_binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    img_contours= np.zeros((h,w,3), np.uint8)

    for cnt in contours:
        x,y, wc, hc = cv2.boundingRect(cnt)
        area=wc*hc
        if(area>50):
            cv2.drawContours(img_contours,cnt,-1,(255,0,0),2)
            cv2.imshow("img_contours", img_contours)
            cv2.waitKey(1)

    cv2.imshow("frame_binary",frame_binary)
    cv2.waitKey(30)
    
capture.release()
cv2.destroyAllWindows()

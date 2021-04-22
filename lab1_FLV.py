import cv2 as cv
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import ImageFont

class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if o is self.widget and e.type() == QtCore.QEvent.MouseMove:
            self.positionChanged.emit(e.pos())
        return super().eventFilter(o, e)


class Ui_MainWindow(object):
    
    def __init__(self):
            super(Ui_MainWindow,self).__init__()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#<---------------------------imagen-------------------------------------->        
##      QPixmap supports all the major image formats:
##      BMP,GIF,JPG,JPEG,PNG,PBM,PGM,PPM,XBM and XPM.
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(20, 10, 721, 491))
        self.imagen.setMouseTracking(True)
        self.imagen.setText("")
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.imagen.mousePressEvent = self.selectFields
#<---------------------------layout-------------------------------------->       
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(800, 100, 251, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(800, 300, 251, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(840, 340, 160, 163))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
#<---------------------------campos-------------------------------------->         
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setObjectName("create")
        self.gridLayout_2.addWidget(self.create, 4, 1, 1, 1)
        self.create.clicked.connect(self.createAnot)
        
        self.campo1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.campo1.setObjectName("campo1")
        self.gridLayout_2.addWidget(self.campo1, 0, 1, 1, 1)

        self.campo2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.campo2.setObjectName("campo2")
        self.gridLayout_2.addWidget(self.campo2, 1, 1, 1, 1)
        
        self.campo3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.campo3.setObjectName("campo3")
        self.gridLayout_2.addWidget(self.campo3, 2, 1, 1, 1)
        
        self.campo4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.campo4.setObjectName("campo4")
        self.gridLayout_2.addWidget(self.campo4, 3, 1, 1, 1)
#<---------------------------cargar imagen-------------------------------->         
        self.botonCargar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.botonCargar.setObjectName("botonCargar")
        self.horizontalLayout.addWidget(self.botonCargar)
        self.botonCargar.clicked.connect(self.cargarImagen)
        
        self.rutaDeImagen = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.rutaDeImagen.setObjectName("rutaDeImagen")
        self.horizontalLayout.addWidget(self.rutaDeImagen)
#<---------------------------botones de color------------------------------>         
        self.botonAzul = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonAzul.setObjectName("botonAzul")
        self.verticalLayout.addWidget(self.botonAzul)
        self.botonAzul.clicked.connect(self.colorAzul)
        
        self.botonVerde = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonVerde.setObjectName("botonVerde")
        self.verticalLayout.addWidget(self.botonVerde)
        self.botonVerde.clicked.connect(self.colorVerde)
        
        self.botonRojo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonRojo.setObjectName("botonRojo")
        self.verticalLayout.addWidget(self.botonRojo)
        self.botonRojo.clicked.connect(self.colorRojo)

        self.botonAmarillo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.botonAmarillo.setObjectName("botonAmarillo")
        self.verticalLayout.addWidget(self.botonAmarillo)
        self.botonAmarillo.clicked.connect(self.colorAmarillo)
#<---------------------------QSliders-------------------------------------->         
        self.elTrackbarVertical = QtWidgets.QSlider(self.centralwidget)
        self.elTrackbarVertical.setGeometry(QtCore.QRect(1080, 100, 22, 441))
        self.elTrackbarVertical.setOrientation(QtCore.Qt.Vertical)
        self.elTrackbarVertical.setObjectName("elTrackbarVertical")
        self.elTrackbarVertical.setRange(0, 255)#Selecciona el valor minimo y maximo que saca el trackbar
        #No se concentra en el teclado cuando esta sobre la region
        self.elTrackbarVertical.setPageStep(5)#Máximo desplazamiento cuando se selecciona fuera de la region para moverlo
        self.elTrackbarVertical.valueChanged.connect(self.updateTrackbarVertical)
        

        
        self.elTrackbarHorizontal = QtWidgets.QSlider(self.centralwidget)
        self.elTrackbarHorizontal.setGeometry(QtCore.QRect(30, 520, 711, 22))
        self.elTrackbarHorizontal.setOrientation(QtCore.Qt.Horizontal)
        self.elTrackbarHorizontal.setObjectName("elTrackbarHorizontal")
        self.elTrackbarHorizontal.setRange(0, 255)
        self.elTrackbarHorizontal.setPageStep(5)
        self.elTrackbarHorizontal.valueChanged.connect(self.updateTrackbarHorizontal)
#<--------------------------barra de menu-------------------------------------->         
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 27))
        self.menubar.setObjectName("menubar")       
        self.menuimagen_original = QtWidgets.QMenu(self.menubar)
        self.menuimagen_original.setObjectName("menuimagen_original")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
#<------------------------acciones de imagen-------------------------------->         
        
        
        self.actionImagen_original = QtWidgets.QAction(MainWindow)
        self.actionImagen_original.setObjectName("actionImagen_original")
        
        self.actionImagen_Numerada = QtWidgets.QAction(MainWindow)
        self.actionImagen_Numerada.setObjectName("actionImagen_Numerada")
        
        
        self.actionImagen_con_anotaciones = QtWidgets.QAction(MainWindow)
        self.actionImagen_con_anotaciones.setObjectName("actionImagen_con_anotaciones")
        
        
        self.menuimagen_original.addAction(self.actionImagen_original)
        self.menuimagen_original.addAction(self.actionImagen_Numerada)
        self.menuimagen_original.addAction(self.actionImagen_con_anotaciones)
        self.menubar.addAction(self.menuimagen_original.menuAction())

        self.actionImagen_original.triggered.connect(self.mostrarImgOrigi)
        self.actionImagen_Numerada.triggered.connect(self.mostrarImgNumer)
        self.actionImagen_con_anotaciones.triggered.connect(self.mostrarImgAnot)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create.setText(_translate("MainWindow","Crear anotacion"))
        self.label_4.setText(_translate("MainWindow", "3"))
        self.label_2.setText(_translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "4"))
        self.label_3.setText(_translate("MainWindow", "2"))
        self.botonCargar.setText(_translate("MainWindow", "Cargar imagen"))
        self.botonAzul.setText(_translate("MainWindow", "AZUL"))
        self.botonVerde.setText(_translate("MainWindow", "VERDE"))
        self.botonRojo.setText(_translate("MainWindow", "ROJO"))
        self.botonAmarillo.setText(_translate("MainWindow", "AMARILLO"))
        self.menuimagen_original.setTitle(_translate("MainWindow", "Tipos de imagenes"))
        self.actionImagen_original.setText(_translate("MainWindow", "Imagen original"))
        self.actionImagen_Numerada.setText(_translate("MainWindow", "Imagen Numerada"))
        self.actionImagen_con_anotaciones.setText(_translate("MainWindow", "Imagen con anotaciones"))

    def cargarImagen(self):
##      QPixmap supports all the major image formats:
##      BMP,GIF,JPG,JPEG,PNG,PBM,PGM,PPM,XBM and XPM.
        self.pathValue = self.rutaDeImagen.text()
        imagenOriginal = cv.imread(self.pathValue,1)
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_original.jpg",imagenOriginal)
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_punteada_0.jpg",imagenOriginal)
        self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_original.jpg"))

    def selectFields(self,event):
        global contador1
        global contador2
        global positionX
        global positionY
        
        if contador1 < 4: 
            texto = ['1','2','3','4']
            
            x = event.pos().x()
            y = event.pos().y()
            positionX.append(x)
            positionY.append(y)
            
            img = cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_punteada_"+str(contador1)+".jpg",1)
            
            resized = cv.resize(img, (721, 491), cv.INTER_AREA)
            
            h,w= resized.shape[:2]
            
            contador2=contador2+(h//5)

            if positionX[contador1] < w//2:
                cv.circle(resized,(x,y),2,(255,255,255),-1)
                cv.line(resized,(x,y),((15),contador2),(255,255,255),1)
                cv.putText(resized,texto[contador1],(10,contador2),cv.FONT_HERSHEY_SIMPLEX,0.4, (255,255,255))
            else:
                cv.circle(resized,(x,y),2,(255,255,255),-1)
                cv.line(resized,(x,y),((688),contador2),(255,255,255),1)
                cv.putText(resized,texto[contador1],((690),contador2),cv.FONT_HERSHEY_SIMPLEX,0.4, (255,255,255))
            
            contador1=contador1+1
            cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_punteada_"+str(contador1)+".jpg",resized)
            self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_punteada_"+str(contador1)+".jpg"))
        else:
            contador1=0
            contador2=0
            positionX.clear()
            positionY.clear()
            self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_punteada_0.jpg"))
            
            

    def createAnot(self):
        global positionX
        global positionY
        
        contador2=0
        
        texto = [self.campo1.text(), self.campo2.text(), self.campo3.text() , self.campo4.text()]
        img_load= cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_punteada_0.jpg")
        img = cv.resize(img_load, (721, 491), cv.INTER_AREA)
        h,w= img.shape[:2]
        
        for i in range(len(texto)):
            
            contador2=contador2+(h//5)
            
            suma_pixels = 4+(7*len(texto[i]))
            
            resta_pixels = 721-(7*len(texto[i]))
            
            if positionX[i] < w//2:
                cv.circle(img,(positionX[i],positionY[i]),2,(255,255,255),-1)
                cv.line(img,(positionX[i],positionY[i]),((suma_pixels+7),contador2),(255,255,255),1)
                cv.putText(img,texto[i],((3),contador2),cv.FONT_HERSHEY_SIMPLEX,0.4, (255,255,255))
            else:
                cv.circle(img,(positionX[i],positionY[i]),2,(255,255,255),-1)
                cv.line(img,(positionX[i],positionY[i]),((resta_pixels-7),contador2),(255,255,255),1)
                cv.putText(img,texto[i],((resta_pixels),contador2),cv.FONT_HERSHEY_SIMPLEX,0.4, (255,255,255))
                
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_anotaciones.jpg",img)
        self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_anotaciones.jpg"))
        


    def updateTrackbarHorizontal(self, value):
        global valMax
        valMin=value
        valMax=valMax
        img_instancia_0 = cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_original.jpg",1)
        ret, img_instancia_1 = cv.threshold(img_instancia_0,valMin, valMax, cv.THRESH_BINARY)
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_elTrackbar.jpg",img_instancia_1)
        self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_elTrackbar.jpg"))
        
    def updateTrackbarVertical(self, value):

        global valMin
        global valMax
        valMin=valMin
        valMax=value
        img_instancia_0 = cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_original.jpg",1)
        ret, img_instancia_1 = cv.threshold(img_instancia_0,valMin, valMax, cv.THRESH_BINARY)
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_elTrackbar.jpg",img_instancia_1)
        self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_elTrackbar.jpg"))
        
        

    def colorAzul(self):
        imgBlue = cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_elTrackbar.jpg",1)
        h,w = imgBlue.shape[:2]
        for i in range(0,h):
            for j in range(0,w):
                if(imgBlue[i][j][0] > 0 ):
                    imgBlue[i][j][1] = 0   
                    imgBlue[i][j][2] = 0
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_azul.jpg",imgBlue)
        pathBlue =  "C:/VArt/Laboratorio 1 VArt/img/imagen_azul.jpg"
        self.imagen.setPixmap(QtGui.QPixmap(pathBlue))

        
    def colorVerde(self):
        imgGreen = cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_elTrackbar.jpg",1)
        h,w = imgGreen.shape[:2]
        for i in range(0,h):
            for j in range(0,w):
                if(imgGreen[i][j][0] > 0 ):
                    imgGreen[i][j][0] = 0   
                    imgGreen[i][j][2] = 0
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_verde.jpg",imgGreen)
        pathGreen =  "C:/VArt/Laboratorio 1 VArt/img/imagen_verde.jpg"
        self.imagen.setPixmap(QtGui.QPixmap(pathGreen))

        
    def colorRojo(self):
        imgRed = cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_elTrackbar.jpg",1)
        h,w = imgRed.shape[:2]
        for i in range(0,h):
            for j in range(0,w):
                if(imgRed[i][j][0] > 0 ):
                    imgRed[i][j][0] = 0   
                    imgRed[i][j][1] = 0
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_rojo.jpg",imgRed)
        pathRed=  "C:/VArt/Laboratorio 1 VArt/img/imagen_rojo.jpg"
        self.imagen.setPixmap(QtGui.QPixmap(pathRed))

        
    def colorAmarillo(self):
        imgGreen = cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_verde.jpg",1)
        imgRed = cv.imread("C:/VArt/Laboratorio 1 VArt/img/imagen_rojo.jpg",1)
        imgYellow = cv.add(imgGreen,imgRed)
        cv.imwrite("C:/VArt/Laboratorio 1 VArt/img/imagen_amarillo.jpg",imgYellow)
        pathYellow =  "C:/VArt/Laboratorio 1 VArt/img/imagen_amarillo.jpg"
        self.imagen.setPixmap(QtGui.QPixmap(pathYellow))
    def mostrarImgAnot(self):
        self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_anotaciones.jpg"))
        
    def mostrarImgNumer(self):
        self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_punteada_4.jpg"))
        
    def mostrarImgOrigi(self):
        self.imagen.setPixmap(QtGui.QPixmap("C:/VArt/Laboratorio 1 VArt/img/imagen_original.jpg"))
            
        
if __name__ == "__main__":
    import sys
    valMin=0
    valMax=0
    positionX=[]
    positionY=[]
    contador1=0
    contador2=0
    count1=0
    count2=0
    count3=0
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

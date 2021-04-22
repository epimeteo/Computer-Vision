import numpy as np
import xlrd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib

book_excel = xlrd.open_workbook("DataNumsPairs.xlsx")

def load_xlsx(book):
    
    sh = book.sheet_by_index(0)
    print(sh.nrows,sh.ncols)
    x = np.zeros( (sh.nrows , sh.ncols-1) )
    y = []
    
    for i in range( 0 , sh.nrows ):
        
        for j in range( 0 , (sh.ncols - 1) ):
            
            x[ i , j ] = sh.cell_value( rowx = i , colx = (j+1) )
        if (sh.cell_value(rowx = i, colx = 0) == '0' ):
            y.append(0)
        if (sh.cell_value(rowx = i, colx = 0) == '2' ):
            y.append(1)
        if (sh.cell_value(rowx = i, colx = 0) == '4' ):
            y.append(2)
        if (sh.cell_value(rowx = i, colx = 0) == '6' ):
            y.append(3)
        if (sh.cell_value(rowx = i, colx = 0) == '8' ):
            y.append(4)
            
    #Las máquinas de IA todo los trabajan en .float (flotante)
    y = np.array( y , np.float32 )
    
    return x,y,sh.nrows,sh.ncols

if __name__=='__main__':
    
    X,Y,filas,columnas = load_xlsx(book_excel)
    print(Y)
    #Normalizar los datos con la funcion StandarScaler
    #voy a transformar los datos de X de tal manera que el
    #va a encontrar una distribucion gausiana donde la
    #media se igual a 1 y la desviacion sea igual a 0 y esos
    #valores transformados me los va a llevar a X_SS
    model_ss = StandardScaler()#TOdos los modelos se deben almacenar en una variable
    X_SS = model_ss.fit_transform(X)
    
    for i in range(0,10):
        #entrenese y aprenda, y verifique que fue lo que aprendió

        #Separacion de datos en entrenamiento y en testeo
        sample_train,sample_test,response_train,response_test = train_test_split( X_SS ,Y,test_size=0.3)
        #configuracion del modelo en los parametros normales
        model_mlp = MLPClassifier(activation = 'relu', hidden_layer_sizes=(50,),max_iter=1000, tol=0.0001)
        #entrenamiento del modelo con los datos del train
        model_mlp.fit(sample_train,response_train)
        #verificacion de que fue lo que predijo el modelo con el resultado de las muestras que deje
        #muestras que deje para el test
        #Lo que el va a predecir, utilizando el modelo model_mlp()
        #utilizando sample test
        response_predict = model_mlp.predict(sample_test)
        #Le estamos diciendo que compare el response_test
        #vs lo que el predijo(que tanto se parecen)
        accuracy = accuracy_score(response_test,response_predict)
        #eso se imprime
        
        print(accuracy)

    #todos los modelos.fit se deben guardar
    joblib.dump(model_ss, 'model_ss.pkl')
    joblib.dump(model_mlp, 'model_mlp.pkl')
    

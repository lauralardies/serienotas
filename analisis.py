import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

class EstadisticaNotas(): 
    # Creamos un DataFrame con Pandas a partir del archivo .csv
    df = pd.read_csv("grades.csv", ",")

    # Nuestro dataset tiene 6 "assignments" distintos, por lo que habrá que hacer el mismo cálculo 6 veces, uno de cada assignment. 

    # ---- ESTUDIO DE LA TENDENCIA CENTRAL ----

    def media(self): # Primero calculamos la media de cada uno de los exámenes.
        media1 = self.df["assignment1_grade"].mean()
        media2 = self.df["assignment2_grade"].mean()
        media3 = self.df["assignment3_grade"].mean()
        media4 = self.df["assignment4_grade"].mean()
        media5 = self.df["assignment5_grade"].mean()
        media6 = self.df["assignment6_grade"].mean()
        print("\nMedia Examen 1: " + str(media1) + "\nMedia Examen 2: " + str(media2) + "\nMedia Examen 3: " + str(media3) + "\nMedia Examen 4: " + str(media4) + "\nMedia Examen 5: " + str(media5) + "\nMedia Examen 6: " + str(media6))

    def mediana(self): # Ahora calculamos la mediana.
        mediana1 = self.df["assignment1_grade"].median()
        mediana2 = self.df["assignment2_grade"].median()
        mediana3 = self.df["assignment3_grade"].median()
        mediana4 = self.df["assignment4_grade"].median()
        mediana5 = self.df["assignment5_grade"].median()
        mediana6 = self.df["assignment6_grade"].median()
        print("\nMediana Examen 1: " + str(mediana1) + "\nMediana Examen 2: " + str(mediana2) + "\nMediana Examen 3: " + str(mediana3) + "\nMediana Examen 4: " + str(mediana4) + "\nMediana Examen 5: " + str(mediana5) + "\nMediana Examen 6: " + str(mediana6))

    def moda(self): # Por último, la(s) moda(s).
        moda1 = self.df["assignment1_grade"].mode()
        moda2 = self.df["assignment2_grade"].mode()
        moda3 = self.df["assignment3_grade"].mode()
        moda4 = self.df["assignment4_grade"].mode()
        moda5 = self.df["assignment5_grade"].mode()
        moda6 = self.df["assignment6_grade"].mode()
        print("\nModa Examen 1:\n" + str(moda1) + "\nModa Examen 2:\n" + str(moda2) + "\nModa Examen 3:\n" + str(moda3) + "\nModa Examen 4:\n" + str(moda4) + "\nModa Examen 5:\n" + str(moda5) + "\nModa Examen 6:\n" + str(moda6))

    # ---- ESTUDIO DE LA DISPERSIÓN ----

    def var(self): # Primero calculamos la varianza de cada examen realizado por los alumnos.
        varianza1 = self.df["assignment1_grade"].var()
        varianza2 = self.df["assignment2_grade"].var()
        varianza3 = self.df["assignment3_grade"].var()
        varianza4 = self.df["assignment4_grade"].var()
        varianza5 = self.df["assignment5_grade"].var()
        varianza6 = self.df["assignment6_grade"].var()
        print("\nvarianza Examen 1: " + str(varianza1) + "\nVarianza Examen 2: " + str(varianza2) + "\nVarianza Examen 3: " + str(varianza3) + "\nVarianza Examen 4: " + str(varianza4) + "\nVarianza Examen 5: " + str(varianza5) + "\nVarianza Examen 6: " + str(varianza6))

    def desviacion_tipica(self): # Ahora determinamos el valor de la desviación típica para cada examen
        dt1 = self.df["assignment1_grade"].std()
        dt2 = self.df["assignment2_grade"].std()
        dt3 = self.df["assignment3_grade"].std()
        dt4 = self.df["assignment4_grade"].std()
        dt5 = self.df["assignment5_grade"].std()
        dt6 = self.df["assignment6_grade"].std()
        print("\nDesviación Típica Examen 1: " + str(dt1) + "\nDesviación Típica Examen 2: " + str(dt2) + "\nDesviación Típica Examen 3: " + str(dt3) + "\nDesviación Típica Examen 4: " + str(dt4) + "\nDesviación Típica Examen 5: " + str(dt5) + "\nDesviación Típica Examen 6: " + str(dt6))

    def cuartil(self): # Por último, los cuartiles (.25, .5, .75)
        cuartiles1 = self.df["assignment1_grade"].quantile([.25, .5, .75])
        cuartiles2 = self.df["assignment2_grade"].quantile([.25, .5, .75])
        cuartiles3 = self.df["assignment3_grade"].quantile([.25, .5, .75])
        cuartiles4 = self.df["assignment4_grade"].quantile([.25, .5, .75])
        cuartiles5 = self.df["assignment5_grade"].quantile([.25, .5, .75])
        cuartiles6 = self.df["assignment6_grade"].quantile([.25, .5, .75])
        print("\nCuartiles del Examen 1:\n" + str(cuartiles1) + "\nCuartiles del Examen 2:\n" + str(cuartiles2) + "\nCuartiles del Examen 3:\n" + str(cuartiles3) + "\nCuartiles del Examen 4:\n" + str(cuartiles4) + "\nCuartiles del Examen 5:\n" + str(cuartiles5) + "\nCuartiles del Examen 6:\n" + str(cuartiles6))

    # ---- DATOS ABERRANTES ----

    def datos_aberrantes(self): # Calculamos las notas tipificadas : 
        z1 = np.abs(stats.zscore(self.df["assignment1_grade"]))
        z2 = np.abs(stats.zscore(self.df["assignment2_grade"]))
        z3 = np.abs(stats.zscore(self.df["assignment3_grade"]))
        z4 = np.abs(stats.zscore(self.df["assignment4_grade"]))
        z5 = np.abs(stats.zscore(self.df["assignment5_grade"]))
        z6 = np.abs(stats.zscore(self.df["assignment6_grade"]))

        # Identificamos los datos aberrantes, considerando como datos aberrantes aquellos cuyo valor tipificado es mayor que 3. 
        # El siguiente print los indica en qué posición del DataFrame se encuentra cada dato aberrante. 
        print("\nDatos aberrantes del Examen 1:\n" + str(np.where(z1 > 3)))
        print("\nDatos aberrantes del Examen 2:\n" + str(np.where(z2 > 3)))
        print("\nDatos aberrantes del Examen 3:\n" + str(np.where(z3 > 3)))
        print("\nDatos aberrantes del Examen 4:\n" + str(np.where(z4 > 3)))
        print("\nDatos aberrantes del Examen 5:\n" + str(np.where(z5 > 3)))
        print("\nDatos aberrantes del Examen 6:\n" + str(np.where(z6 > 3)))

    def visualizar(self, media, mediana, cuartil_1, cuartil_2, cuartil_3): #Creamos una función que me ayude a visualizar los datos del dataset.
        plt.subplot(2, 2, 1)
        plt.hist(self.df)
        plt.title("Histograma y media")
        plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 2)
        plt.hist(self.df)
        plt.title("Histograma y mediana")
        plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1,label = str(mediana))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 3)
        plt.hist(self.df)
        plt.title("Histograma y cuartiles")
        plt.axvline(cuartil_1, color='orange', linestyle='dashed', linewidth=1,label = "Q1: "+str(cuartil_1))
        plt.axvline(cuartil_2, color='orange', linestyle='dashed', linewidth=1,label = "Q2: "+str(cuartil_2))
        plt.axvline(cuartil_3, color='orange', linestyle='dashed', linewidth=1,label = "Q3: "+str(cuartil_3))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 4)
        plt.boxplot(self.df)
        plt.title("Diagrama de caja y bigotes")
        plt.show()
    
    def imprimir(self): # Por último, tenemos esta función que nos muestra lo que aparecerá en consola.
        n = len(self.df.index) # El número de notas que hay de cada examen
        minimos = self.df.min() # El valor mínimo de cada examen
        maximos = self.df.max() # El valor máximo de cada examen

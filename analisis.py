import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EstadisticaNotas(): 
    # Creamos un DataFrame con Pandas a partir del archivo .csv
    df = pd.read_csv("grades.csv", ",")

    # Nuestro dataset tiene 6 "assignments" distintos, por lo que habrá que hacer el mismo cálculo 6 veces, uno de cada assignment. 

    # ---- ESTUDIO DE LA TENDENCIA CENTRAL ----

    def valor_min(self): # Determinamos la nota más baja de ese examen
        min1 = self.df["assignment1_grade"].min()
        min2 = self.df["assignment2_grade"].min()
        min3 = self.df["assignment3_grade"].min()
        min4 = self.df["assignment4_grade"].min()
        min5 = self.df["assignment5_grade"].min()
        min6 = self.df["assignment6_grade"].min()

        return (min1, min2, min3, min4, min5, min6)

    def valor_max(self): # Determinamos la nota más alta de ese examen
        max1 = self.df["assignment1_grade"].max()
        max2 = self.df["assignment2_grade"].max()
        max3 = self.df["assignment3_grade"].max()
        max4 = self.df["assignment4_grade"].max()
        max5 = self.df["assignment5_grade"].max()
        max6 = self.df["assignment6_grade"].max()

        return (max1, max2, max3, max4, max5, max6)
        
    def media(self): # Calculamos la media de cada uno de los exámenes.
        media1 = self.df["assignment1_grade"].mean()
        media2 = self.df["assignment2_grade"].mean()
        media3 = self.df["assignment3_grade"].mean()
        media4 = self.df["assignment4_grade"].mean()
        media5 = self.df["assignment5_grade"].mean()
        media6 = self.df["assignment6_grade"].mean()

        return (media1, media2, media3, media4, media5, media6)

    def mediana(self): # Ahora calculamos la mediana.
        mediana1 = self.df["assignment1_grade"].median()
        mediana2 = self.df["assignment2_grade"].median()
        mediana3 = self.df["assignment3_grade"].median()
        mediana4 = self.df["assignment4_grade"].median()
        mediana5 = self.df["assignment5_grade"].median()
        mediana6 = self.df["assignment6_grade"].median()

        return (mediana1, mediana2, mediana3, mediana4, mediana5, mediana6)

    def moda(self): # Por último, la(s) moda(s).
        moda1 = self.df["assignment1_grade"].mode()
        moda2 = self.df["assignment2_grade"].mode()
        moda3 = self.df["assignment3_grade"].mode()
        moda4 = self.df["assignment4_grade"].mode()
        moda5 = self.df["assignment5_grade"].mode()
        moda6 = self.df["assignment6_grade"].mode()

        return (moda1, moda2, moda3, moda4, moda5, moda6)

    # ---- ESTUDIO DE LA DISPERSIÓN ----

    def var(self): # Primero calculamos la varianza de cada examen realizado por los alumnos.
        varianza1 = self.df["assignment1_grade"].var()
        varianza2 = self.df["assignment2_grade"].var()
        varianza3 = self.df["assignment3_grade"].var()
        varianza4 = self.df["assignment4_grade"].var()
        varianza5 = self.df["assignment5_grade"].var()
        varianza6 = self.df["assignment6_grade"].var()

        return (varianza1, varianza2, varianza3, varianza4, varianza5, varianza6)

    def desviacion_tipica(self): # Ahora determinamos el valor de la desviación típica para cada examen
        dt1 = self.df["assignment1_grade"].std()
        dt2 = self.df["assignment2_grade"].std()
        dt3 = self.df["assignment3_grade"].std()
        dt4 = self.df["assignment4_grade"].std()
        dt5 = self.df["assignment5_grade"].std()
        dt6 = self.df["assignment6_grade"].std()

        return (dt1, dt2, dt3, dt4, dt5, dt6)

    def cuartil(self): # Por último, los cuartiles (.25, .5, .75)
        cuartiles1 = self.df["assignment1_grade"].quantile([.25, .5, .75])
        cuartiles2 = self.df["assignment2_grade"].quantile([.25, .5, .75])
        cuartiles3 = self.df["assignment3_grade"].quantile([.25, .5, .75])
        cuartiles4 = self.df["assignment4_grade"].quantile([.25, .5, .75])
        cuartiles5 = self.df["assignment5_grade"].quantile([.25, .5, .75])
        cuartiles6 = self.df["assignment6_grade"].quantile([.25, .5, .75])

        return (cuartiles1, cuartiles2, cuartiles3, cuartiles4, cuartiles5, cuartiles6)

    # ---- DATOS ABERRANTES ----

    def datos_aberrantes(self, cuartil1, cuartil3, examen): # Calculamos las notas tipificadas : 
        intercuartil = cuartil3 - cuartil1

        lim_min = cuartil1 - 1.5 * intercuartil
        lim_max = cuartil1 + 1.5 * intercuartil

        # Estos dos tipos de datos aberrantes nos crea un DataFrame de True o False
        datos_aberrantes_min = (self.df[examen] < lim_min)
        datos_aberrantes_max = (self.df[examen] > lim_max)

        outliers_min = []
        outliers_max = []

        for i in range (len(datos_aberrantes_min)):
            if datos_aberrantes_min[i] == True:
                outliers_min.append(self.df.iloc[i][examen])

        for i in range (len(datos_aberrantes_max)):
            if datos_aberrantes_max[i] == True:
                outliers_max.append(self.df.iloc[i][examen])

        return (outliers_min, outliers_max)

    # ---- VISUALIZACIÓN ----

    def diagramas(self, examen):
        sns.boxplot(x = self.df[examen])
        plt.show()

        sns.displot(self.df[examen], bins = 15, kde = False)
        plt.show()

    def imprimir(self, index): # Por último, tenemos esta función que nos muestra lo que aparecerá en consola.

        # Primero definimos las variables y luego creamos los print
        index = index
        examen = "assignment" + str(index + 1) + "_grade"
        n = len(self.df.index) # El número de notas que hay de cada examen
        minimos = self.valor_min() # El valor mínimo de cada examen
        maximos = self.valor_max() # El valor máximo de cada examen
        media = self.media() # Las medias que hemos definido en la función media()
        mediana = self.mediana() # Las medianas que hemos definido en la función mediana()
        moda = self.moda() # La(s) moda(s) que se han generado en la función moda()
        varianza = self.var() # La varianza que hemos calculado en la función var()
        desviacion_tipica = self.desviacion_tipica() # La desviación típica definida en la función desviacion_tipica()
        cuartil = self.cuartil() # Los cuartiles que hemos definido en la función cuartil()
        datos_aberrantes = self.datos_aberrantes(cuartil[index].iat[0], cuartil[index].iat[2], examen) # Los datos que están fuera de lo normal
    

        print("\nE S T U D I O   D E   L A   T E N D E N C I A   C E N T R A L\n")

        print("En total, tenemos una cantidad de " + str(n) + " alumnos que han realizado estos exámenes.\n")
        print("La nota más baja de este examen ha sido un " + str(minimos[index]) + ".\n")
        print("La nota más alta de este examen ha sido un " + str(maximos[index]) + ".\n")
        print("La media de este examen ha sido de " + str(media[index]) + ".\n")
        print("La mediana de este examen ha sido de " + str(mediana[index]) + ".\n")
        print("La(s) moda(s) de este examen ha(n) sido\n" + str(moda[index]))

        print("\nE S T U D I O   D E   L A   D I S P E R S I Ó N\n")

        print("La varianza de este examen es de " + str(varianza[index]) + ".\n")
        print("La desviación típica de el examen es de " + str(desviacion_tipica[index]) + ".\n")
        print("25 % de las notas tienen un valor inferior a " + str(cuartil[index].iat[0]))
        print("50 % de las notas tienen un valor inferior a " + str(cuartil[index].iat[1]))
        print("75 % de las notas tienen un valor inferior a " + str(cuartil[index].iat[2]))

        print("\nD A T O S   A B E R R A N T E S\n")
        print("Los datos aberrantes del examen son\n- Por debajo : " + str(datos_aberrantes[0]) + "\n- Por encima : " + str(datos_aberrantes[1]))
        
        print("\nV I S U A L I Z A C I Ó N\n")
        print("Cargando diagramas ...")
        self.diagramas(examen)
import pandas as pd
import numpy as np
from scipy import stats

# Creamos un DataFrame con Pandas a partir del archivo .csv
df = pd.read_csv("grades.csv", ",")

# Nuestro dataset tiene 6 "assignments" distintos, por lo que habrá que hacer el mismo cálculo 6 veces, uno de cada assignment. 

# ---- ESTUDIO DE LA TENDENCIA CENTRAL ----

# Primero calculamos la media de cada uno de los exámenes.

media1 = df["assignment1_grade"].mean()
media2 = df["assignment2_grade"].mean()
media3 = df["assignment3_grade"].mean()
media4 = df["assignment4_grade"].mean()
media5 = df["assignment5_grade"].mean()
media6 = df["assignment6_grade"].mean()
print("\nMedia Examen 1: " + str(media1) + "\nMedia Examen 2: " + str(media2) + "\nMedia Examen 3: " + str(media3) + "\nMedia Examen 4: " + str(media5) + "\nMedia Examen 5: " + str(media5) + "\nMedia Examen 6: " + str(media6))

# Ahora calculamos la mediana.

mediana1 = df["assignment1_grade"].median()
mediana2 = df["assignment2_grade"].median()
mediana3 = df["assignment3_grade"].median()
mediana4 = df["assignment4_grade"].median()
mediana5 = df["assignment5_grade"].median()
mediana6 = df["assignment6_grade"].median()
print("\nMediana Examen 1: " + str(mediana1) + "\nMediana Examen 2: " + str(mediana2) + "\nMediana Examen 3: " + str(mediana3) + "\nMediana Examen 4: " + str(mediana5) + "\nMediana Examen 5: " + str(mediana5) + "\nMediana Examen 6: " + str(mediana6))

# Por último, la(s) moda(s).

moda1 = df["assignment1_grade"].mode()
moda2 = df["assignment2_grade"].mode()
moda3 = df["assignment3_grade"].mode()
moda4 = df["assignment4_grade"].mode()
moda5 = df["assignment5_grade"].mode()
moda6 = df["assignment6_grade"].mode()
print("\nModa Examen 1:\n" + str(moda1) + "\nModa Examen 2:\n" + str(moda2) + "\nModa Examen 3:\n" + str(moda3) + "\nModa Examen 4:\n" + str(moda5) + "\nModa Examen 5:\n" + str(moda5) + "\nModa Examen 6:\n" + str(moda6))

# ---- ESTUDIO DE LA DISPERSIÓN ----

# Primero calculamos la varianza de cada examen realizado por los alumnos.

varianza1 = df["assignment1_grade"].var()
varianza2 = df["assignment2_grade"].var()
varianza3 = df["assignment3_grade"].var()
varianza4 = df["assignment4_grade"].var()
varianza5 = df["assignment5_grade"].var()
varianza6 = df["assignment6_grade"].var()
print("\nvarianza Examen 1: " + str(varianza1) + "\nVarianza Examen 2: " + str(varianza2) + "\nVarianza Examen 3: " + str(varianza3) + "\nVarianza Examen 4: " + str(varianza5) + "\nVarianza Examen 5: " + str(varianza5) + "\nVarianza Examen 6: " + str(varianza6))

# Ahora determinamos el valor de la desviación típica para cada examen

dt1 = df["assignment1_grade"].std()
dt2 = df["assignment2_grade"].std()
dt3 = df["assignment3_grade"].std()
dt4 = df["assignment4_grade"].std()
dt5 = df["assignment5_grade"].std()
dt6 = df["assignment6_grade"].std()
print("\nDesviación Típica Examen 1: " + str(dt1) + "\nDesviación Típica Examen 2: " + str(dt2) + "\nDesviación Típica Examen 3: " + str(dt3) + "\nDesviación Típica Examen 4: " + str(dt5) + "\nDesviación Típica Examen 5: " + str(dt5) + "\nDesviación Típica Examen 6: " + str(dt6))

# Por último, los cuartiles (.25, .5, .75)

cuartiles1 = df["assignment1_grade"].quantile([.25, .5, .75])
cuartiles2 = df["assignment2_grade"].quantile([.25, .5, .75])
cuartiles3 = df["assignment3_grade"].quantile([.25, .5, .75])
cuartiles4 = df["assignment4_grade"].quantile([.25, .5, .75])
cuartiles5 = df["assignment5_grade"].quantile([.25, .5, .75])
cuartiles6 = df["assignment6_grade"].quantile([.25, .5, .75])
print("\nCuartiles del Examen 1:\n" + str(cuartiles1) + "\nCuartiles del Examen 2:\n" + str(cuartiles2) + "\nCuartiles del Examen 3:\n" + str(cuartiles3) + "\nCuartiles del Examen 4:\n" + str(cuartiles5) + "\nCuartiles del Examen 5:\n" + str(cuartiles5) + "\nCuartiles del Examen 6:\n" + str(cuartiles6))

# ---- DATOS ABERRANTES ----

# Calculamos las notas tipificadas : 
z = np.abs(stats.zscore(df["Nota"]))

# Identificamos los datos aberrantes, considerando como datos aberrantes aquellos cuyo valor tipificado es mayor que 1. 
# El siguiente print los indica en qué posición del DataFrame se encuentra cada dato aberrante. 
print(np.where(z > 1))
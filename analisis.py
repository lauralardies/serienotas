import pandas as pd

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

# Ahora calculamos la mediana.

mediana1 = df["assignment1_grade"].median()
mediana2 = df["assignment2_grade"].median()
mediana3 = df["assignment3_grade"].median()
mediana4 = df["assignment4_grade"].median()
mediana5 = df["assignment5_grade"].median()
mediana6 = df["assignment6_grade"].median()

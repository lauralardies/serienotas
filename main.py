from analisis import EstadisticaNotas

analisis = EstadisticaNotas()

while True:
    examen = input("Tenemos 6 exámenes evaluados, ¿de qué examen quieres ver las estadísticas? (1, 2, 3, 4, 5, o 6)\nExamen : ")
    if examen == "1": 
        index = 0
        break
    if examen == "2":
        index = 1
        break
    if examen == "3":
        index = 2
        break
    if examen == "4":
        index = 3
        break
    if examen == "5":
        index = 4
        break
    if examen == "6":
        index = 5
        break
    else:
        print("Inténtalo de nuevo, recuerda que sólo necesitamos que introduzcas el número del examen que quieres ver y que sólo tenemos 6 exámenes calificados.")

#analisis.datos_aberrantes()

analisis.imprimir(index)
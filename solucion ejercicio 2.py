#Ejercicio desarollado y comentado por mi persona, no se utilizo ninguna fuente externa, es un ejercicio de clasificación de clientes basado en su duración de sesión y eventos de clics en base a los ejercicios de Fase 5 momento final.

#Matriz para almacenar datos de sesiones de clientes [ID CLIENTE, Duracion (segundos), Eventos clics]
#Clasificación
#Alto = Duración > 180s y clics > 8
#Bajo = Duración < 60s y clicks < 3
#Medio = Clasificar como "Medio" en todos los demás casos.

# 'ID_CLIENTE', 'duración_segundos', 'eventos_clics'
session_matriz = [
    '123_Cliente#1', 120, 5,
    '124_Cliente#2', 300, 10,
    '125_Cliente#3', 180, 7,
    '126_Cliente#4', 45, 2,
    '127_Cliente#5', 240, 9,
    '128_Cliente#6', 30, 1,
    '129_Cliente#7', 200, 6
]

# funcion para clasificar cada cliente en la matriz

def clasificar_matriz(matriz):
    clasificaciones = []
    #bucle para recorrer la matriz de 3 en 3 (ID, duración, clics)
    for i in range(0, len(matriz), 3):
        #seleccionar los datos del cliente
        id_cliente = matriz[i]
        duracion = matriz[i + 1]
        clics = matriz[i + 2]

        #clasificar según las condiciones dadas
        # if = Condicional Si 
        if duracion > 180 and clics > 8:
            clasificacion = "Alto"
        #elif = Condicional Si no
        elif duracion < 60 and clics < 3:
            clasificacion = "Bajo"
        #else = condicional Entonces 
        else:
            clasificacion = "Medio"

        #agregar la clasificación a la lista de resultados
        clasificaciones.append((id_cliente, clasificacion))
    
    return clasificaciones

#imprimimos los resultados de la clasificación
resultados = clasificar_matriz(session_matriz)
#bucle para imprimir cada cliente y su clasificación
for cliente, clasificacion in resultados:
    #imprimir el ID del cliente y su clasificación
    print(f"{cliente}: Clasificación:{clasificacion}")
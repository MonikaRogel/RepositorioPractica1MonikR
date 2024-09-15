#SEMANA N°13 Monica Rogel

# Defino la función para calcular el promedio de temperatura por ciudad
def calcular_promedio_temperatura_por_ciudad(temperaturas):
    # Obtengo el número de semanas de la lista de temperaturas
    num_semanas = len(temperaturas)
    # Inicializo las variables para sumar las temperaturas y contar el total de temperaturas
    suma_total = 0
    count_total = 0

    # Recorro cada semana para sumar las temperaturas
    for j in range(num_semanas):
        # Obtengo la lista de temperaturas para la semana actual
        temperatura_semana = temperaturas[j]
        # Sumo las temperaturas de la semana a la suma total
        suma_total += sum(temperatura_semana)
        # Aumento el conteo total por el número de temperaturas en esa semana
        count_total += len(temperatura_semana)

    # Calculo el promedio dividiendo la suma total entre el conteo total
    promedio_ciudad = suma_total / count_total
    # Devuelvo el promedio calculado
    return promedio_ciudad


# Defino la función para imprimir los promedios de temperatura
def imprimir_promedios(ciudad_temperaturas, ciudad_nombre):
    # Calculo el promedio de temperatura para la ciudad dada
    promedio_ciudad = calcular_promedio_temperatura_por_ciudad(ciudad_temperaturas)
    # Imprimo el promedio de temperatura para la ciudad
    print(f'El total de la temperatura promedio en la {ciudad_nombre} durante las 4 semanas es de {promedio_ciudad:.2f}°C')


# Inicializo los datos de ejemplo utilizando diccionarios con nombres de ciudades actualizados
temperaturas = {
    'Ciudad de Loja': [[20, 22, 25, 28], [18, 20, 22, 24], [15, 18, 20, 22], [12, 15, 18, 20], [10, 12, 15, 18],
                    [8, 10, 12, 15], [5, 8, 10, 12]],
    'Ciudad de Cuenca': [[25, 28, 30, 32], [22, 25, 28, 30], [20, 22, 25, 28], [18, 20, 22, 25], [15, 18, 20, 22],
                      [12, 15, 18, 20], [10, 12, 15, 18]],
    'Ciudad de Quito': [[30, 32, 35, 38], [28, 30, 32, 35], [25, 28, 30, 32], [22, 25, 28, 30], [20, 22, 25, 28],
                     [18, 20, 22, 25], [15, 18, 20, 22]]
}

# Extraigo las claves del diccionario como una lista de ciudades
ciudades = list(temperaturas.keys())

while True:
    # Muestra el menú de selección de ciudad y la opción para salir
    print("Seleccione una opción:")
    for i, ciudad in enumerate(ciudades, 1):
        print(f"{i}: {ciudad}")
    print("4: Salir")

    # Solicito al usuario que ingrese su opción
    seleccion = input("Ingrese su opción (1-4): ")

    # Si el usuario elige salir, finalizo el programa
    if seleccion == '4':
        print("Saliendo del programa.")
        break

    # Si el usuario elige una opción válida, proceso la selección
    if seleccion in ['1', '2', '3']:
        ciudad_index = int(seleccion) - 1
        ciudad_nombre = ciudades[ciudad_index]
        ciudad_temperaturas = temperaturas[ciudad_nombre]
        # Imprimo los promedios de temperatura para la ciudad seleccionada
        imprimir_promedios(ciudad_temperaturas, ciudad_nombre)
        print()  # Añadido una línea en blanco para separar las salidas
    else:
        # Si la selección es inválida, muestro un mensaje de error
        print("Selección inválida. Por favor, ingrese un número entre 1 y 4.")


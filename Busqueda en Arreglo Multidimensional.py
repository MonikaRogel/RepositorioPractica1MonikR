def buscar_valor(matriz, valor_buscado):
    # Iterar sobre las filas de la matriz
    for i in range(len(matriz)):
        # Iterar sobre las columnas de la matriz
        for j in range(len(matriz[i])):
            # Comparar el valor actual con el valor buscado
            if matriz[i][j] == valor_buscado:
                # Si se encuentra el valor, devolver la posición
                return (i, j)
    # Si el valor no se encuentra en la matriz, devolver None
    return None

# Definir una matriz 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Valor que queremos buscar
valor_buscado = 50

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")

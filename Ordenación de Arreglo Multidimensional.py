def bubble_sort(fila):
    # Implementación del algoritmo Bubble Sort para ordenar una lista
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


def ordenar_fila(matriz, fila_index):
    # Hacer una copia de la matriz para no modificar la original
    matriz_ordenada = [row[:] for row in matriz]

    # Verificar que el índice de la fila esté dentro del rango
    if 0 <= fila_index < len(matriz_ordenada):
        # Ordenar la fila especificada
        matriz_ordenada[fila_index] = bubble_sort(matriz_ordenada[fila_index])
    else:
        print(f"Índice de fila {fila_index} fuera de rango.")

    return matriz_ordenada
# Definir una matriz 3x3
matriz = [
    [5, 3, 9],
    [8, 2, 7],
    [4, 6, 1]
]

# Fila que queremos ordenar (por ejemplo, la segunda fila, índice 1)
fila_index = 1

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila especificada
matriz_ordenada = ordenar_fila(matriz, fila_index)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
#actualizar

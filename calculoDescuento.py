# SEMANA N°14 Monica Rogel

# Crea una función llamada calcular_descuento que tome dos parámetros:  monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
# La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
# La función debe devolver el monto del descuento calculado.

# Función que calcula el descuento según el monto total y el porcentaje que elijas.
# Si no dices nada, aplicará un descuento del 15%.
def calcular_descuento(monto_total, descuento=15):
    return monto_total * (descuento / 100)

# Función que muestra los resultados: cuánto es el total, el descuento y lo que queda por pagar.
def imprimir_resultados(monto_total, descuento_aplicado):
    print(f"\nMonto total: ${monto_total:.2f}")  # Imprime el monto total con dos decimales
    print(f"Descuento: ${descuento_aplicado:.2f}")  # Imprime el monto del descuento con dos decimales
    print(f"Monto final después del descuento: ${monto_total - descuento_aplicado:.2f}")  # Imprime el monto final con dos decimales

# Aquí le pedimos al usuario que ingrese el monto de la compra
# Calculamos el descuento usando el 15% (que es el valor por defecto)
monto_total1 = float(input("Ingresa el monto: "))
descuento1 = calcular_descuento(monto_total1)
imprimir_resultados(monto_total1, descuento1)  # Imprimimos los resultados

# Luego pedimos otro monto al usuario
# Esta vez, calculamos el descuento usando un 50%
monto_total2 = float(input("\nIngresa el monto: "))
descuento2 = calcular_descuento(monto_total2, descuento=50)
imprimir_resultados(monto_total2, descuento2)  # Imprimir los resultados

# SEMNA N°16 Monica Rogel Q
# Trabajo con Archivos de Texto en Python

# Función para escribir notas en un archivo usando write()
def escribir_notas(nombre_archivo, notas):
    with open(nombre_archivo, 'w') as archivo:  # Usar 'with' para manejar el archivo automáticamente
        for nota in notas:
            archivo.write(nota + '\n')  # Escribir cada nota en el archivo, añadiendo un salto de línea

# Función para leer notas de un archivo usando readline()
def leer_notas(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:  # Usar 'with' para manejar el archivo automáticamente
        for linea in archivo:
            print(linea.strip())  # Imprimir la línea leída

# Notas que queremos escribir
notas = [
    "Hola, soy Monica.",
    "Mi apellido es Rogel.",
    "Vivo en la hermosa provincia de Zamora Chimchipe.",
    "Soy de la ciudad de Loja, donde disfruto de la naturaleza.",
    "Uno de mis hobbies favoritos es el senderismo; me encanta explorar nuevos senderos.",
    "Mis gustos musicales son variados: disfruto de la música electrónica y también de la clásica."
]

# Escribir las notas en el archivo
escribir_notas('nts_personales_Monica.txt', notas)
print("He guardado mis notas personales.")

# Leer las notas del archivo línea por línea
print("Aquí encontrarás mis notas:")
leer_notas('nts_personales_Monica.txt')


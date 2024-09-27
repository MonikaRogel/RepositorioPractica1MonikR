# Creamos un diccionario con información de una persona
informacion_personal = {
    "nombre": "Betzy",
    "edad": 23,
    "ciudad": "Loja",
    "profesion": "Tegnologa"
}

# Mostramos la ciudad actual
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Cambiamos la ciudad a Barcelona
informacion_personal["ciudad"] = "Yantzaza"
print(f"Nueva ciudad: {informacion_personal['ciudad']}")

# Agregamos una nueva profesión
informacion_personal["nueva_profesion"] = "Tecnologías de la Información"

# Verificamos si tiene un número de teléfono
if "telefono" not in informacion_personal:
    # Si no tiene, agregamos un número ficticio
    informacion_personal["telefono"] = "0994671001"
    print("Se ha agregado el número de teléfono.")
else:
    print("Ya tiene un número de teléfono.")

# Eliminamos la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("Se ha eliminado la clave 'edad'.")

# Mostramos la información actualizada
print(informacion_personal)

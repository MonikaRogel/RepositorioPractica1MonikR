# SEMNA N°12 Monica Rogel Q
# Definición de la matriz 3D de temperaturas para cada ciudad y semana

temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"dia": "Lunes", "temp": 78},
            {"dia": "Martes", "temp": 80},
            {"dia": "Miércoles", "temp": 82},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 85},
            {"dia": "Sábado", "temp": 88},
            {"dia": "Domingo", "temp": 92}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 76},
            {"dia": "Martes", "temp": 79},
            {"dia": "Miércoles", "temp": 83},
            {"dia": "Jueves", "temp": 81},
            {"dia": "Viernes", "temp": 87},
            {"dia": "Sábado", "temp": 89},
            {"dia": "Domingo", "temp": 93}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 77},
            {"dia": "Martes", "temp": 81},
            {"dia": "Miércoles", "temp": 85},
            {"dia": "Jueves", "temp": 82},
            {"dia": "Viernes", "temp": 88},
            {"dia": "Sábado", "temp": 91},
            {"dia": "Domingo", "temp": 95}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 75},
            {"dia": "Martes", "temp": 78},
            {"dia": "Miércoles", "temp": 80},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 84},
            {"dia": "Sábado", "temp": 87},
            {"dia": "Domingo", "temp": 91}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"dia": "Lunes", "temp": 62},
            {"dia": "Martes", "temp": 64},
            {"dia": "Miércoles", "temp": 68},
            {"dia": "Jueves", "temp": 70},
            {"dia": "Viernes", "temp": 73},
            {"dia": "Sábado", "temp": 75},
            {"dia": "Domingo", "temp": 79}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 63},
            {"dia": "Martes", "temp": 66},
            {"dia": "Miércoles", "temp": 70},
            {"dia": "Jueves", "temp": 72},
            {"dia": "Viernes", "temp": 75},
            {"dia": "Sábado", "temp": 77},
            {"dia": "Domingo", "temp": 81}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 61},
            {"dia": "Martes", "temp": 65},
            {"dia": "Miércoles", "temp": 68},
            {"dia": "Jueves", "temp": 70},
            {"dia": "Viernes", "temp": 72},
            {"dia": "Sábado", "temp": 76},
            {"dia": "Domingo", "temp": 80}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 64},
            {"dia": "Martes", "temp": 67},
            {"dia": "Miércoles", "temp": 69},
            {"dia": "Jueves", "temp": 71},
            {"dia": "Viernes", "temp": 74},
            {"dia": "Sábado", "temp": 77},
            {"dia": "Domingo", "temp": 80}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"dia": "Lunes", "temp": 90},
            {"dia": "Martes", "temp": 92},
            {"dia": "Miércoles", "temp": 94},
            {"dia": "Jueves", "temp": 91},
            {"dia": "Viernes", "temp": 88},
            {"dia": "Sábado", "temp": 85},
            {"dia": "Domingo", "temp": 82}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 89},
            {"dia": "Martes", "temp": 91},
            {"dia": "Miércoles", "temp": 93},
            {"dia": "Jueves", "temp": 90},
            {"dia": "Viernes", "temp": 87},
            {"dia": "Sábado", "temp": 84},
            {"dia": "Domingo", "temp": 81}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 91},
            {"dia": "Martes", "temp": 93},
            {"dia": "Miércoles", "temp": 95},
            {"dia": "Jueves", "temp": 92},
            {"dia": "Viernes", "temp": 89},
            {"dia": "Sábado", "temp": 86},
            {"dia": "Domingo", "temp": 83}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 88},
            {"dia": "Martes", "temp": 90},
            {"dia": "Miércoles", "temp": 92},
            {"dia": "Jueves", "temp": 89},
            {"dia": "Viernes", "temp": 86},
            {"dia": "Sábado", "temp": 83},
            {"dia": "Domingo", "temp": 80}
        ]
    ]
]
#   SEMANA 12

def imprimir_promedios(ciudad, ciudad_num):
    """Calcula y muestra el promedio de temperaturas para cada semana en la ciudad seleccionada."""
    print(f"Promedio de resultados de la ciudad {ciudad_num}:")
    for semana_index, semana in enumerate(ciudad):
        suma = 0  # Inicializamos la suma de temperaturas
        conteo = 0  # Inicializamos el conteo de días

        # Sumamos las temperaturas de cada día de la semana
        for dia in semana:
            suma += dia['temp']  # Sumamos la temperatura del día
            conteo += 1  # Aumentamos el conteo de días

        # Calculamos el promedio de temperatura para la semana
        promedio = suma / conteo

        # Mostramos el promedio de temperatura para la semana actual
        print(f"  Semana {semana_index + 1}: Promedio de temperatura = {promedio:.2f}")


while True:
    # Mostramos el menú de selección de ciudad y la opción para salir
    print("Seleccione una opción:")
    print("1: Ciudad 1")
    print("2: Ciudad 2")
    print("3: Ciudad 3")
    print("4: Salir")

    seleccion = input("Ingrese su opción (1-4): ")

    if seleccion == '4':
        print("Saliendo del programa.")
        break

    if seleccion in ['1', '2', '3']:
        ciudad_index = int(seleccion) - 1
        ciudad = temperaturas[ciudad_index]
        imprimir_promedios(ciudad, seleccion)
        print()  # Añadimos una línea en blanco para separar las salidas
    else:
        print("Selección inválida. Por favor, ingrese un número entre 1 y 4.")

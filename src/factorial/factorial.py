#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula factorial de un número o rangos                                 *
#* soporta: n, desde-hasta, -hasta, desde-                                 *
#*-------------------------------------------------------------------------*

import sys

# Función para calcular factorial
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Obtener entrada (argumento o input)
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango (ej: 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Procesamiento de la entrada
if "-" in entrada:
    
    # Caso: "-hasta" (ej: -10 → 1 a 10)
    if entrada.startswith("-"):
        hasta = int(entrada[1:])  # desde el caracter 1 en adelante
        desde = 1

    # Caso: "desde-" (ej: 5- → 5 a 60)
    elif entrada.endswith("-"):
        desde = int(entrada[:-1])  # todo menos el último caracter
        hasta = 60

    # Caso: "desde-hasta" (ej: 4-8)
    else:
        partes = entrada.split("-")
        desde = int(partes[0])
        hasta = int(partes[1])

    # Calcular factoriales en el rango
    for i in range(desde, hasta + 1):
        print("Factorial", i, "es", factorial(i))

# Caso: número único
else:
    num = int(entrada)
    print("Factorial", num, "es", factorial(num))
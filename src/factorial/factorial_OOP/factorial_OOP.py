#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* cálculo de factorial usando POO                                         *
#*-------------------------------------------------------------------------*

import sys

# Clase Factorial
class Factorial:

    # Constructor
    def __init__(self):
        pass

    # Método para calcular factorial de un número
    def calcular(self, num):
        if num < 0:
            print("No existe factorial de número negativo")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    # Método principal que calcula entre min y max
    def run(self, minimo, maximo):
        for i in range(minimo, maximo + 1):
            print("Factorial", i, "es", self.calcular(i))


# ---------------- MAIN ---------------- #

# Obtener entrada
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango (ej: 4-8): ")
else:
    entrada = sys.argv[1]

# Procesar entrada
if "-" in entrada:
    partes = entrada.split("-")
    minimo = int(partes[0])
    maximo = int(partes[1])
else:
    minimo = int(entrada)
    maximo = minimo

# Crear objeto y ejecutar
f = Factorial()
f.run(minimo, maximo)
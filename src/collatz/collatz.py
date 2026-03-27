import matplotlib.pyplot as plt

# Función que calcula pasos de Collatz
def collatz_iteraciones(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

# Listas para graficar
numeros = []
iteraciones = []

# Calcular para 1 a 10000
for i in range(1, 10001):
    numeros.append(i)
    iteraciones.append(collatz_iteraciones(i))

# Graficar
plt.scatter(iteraciones, numeros, s=1)

plt.xlabel("Cantidad de iteraciones")
plt.ylabel("Número inicial")
plt.title("Conjetura de Collatz (1 a 10000)")

plt.show()
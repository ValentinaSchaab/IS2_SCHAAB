#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# Límite inferior del intervalo
lower = 1

# Límite superior del intervalo
upper = 500

print("Prime numbers between", lower, "and", upper, "are:")

# Recorre todos los números dentro del intervalo
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
        # Se verifica si el número tiene divisores
       for i in range(2, num):
            # Si es divisible por otro número, no es primo
           if (num % i) == 0:
               break
        # Si no se encontró divisor, es primo
       else:
           print(num)

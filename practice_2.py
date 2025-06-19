#Objetivo: Crear una lista de números del 1 al 100, filtrar los números primos utilizando comprensión de listas, y luego usar un generador para recorrerlos 
# de manera perezosa (lazy), sumando los que sean mayores a un cierto valor dado por el usuario.

list = [i for i in range(1, 101)]
print(list)

primeNumbers = [ n for n in list if n%2]
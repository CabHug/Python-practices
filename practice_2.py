#Objetivo: Crear una lista de números del 1 al 100, filtrar los números primos utilizando comprensión de listas, y luego usar un generador para recorrerlos 
# de manera perezosa (lazy), sumando los que sean mayores a un cierto valor dado por el usuario.

limit = 100

#fucntion to fetch prime numbers
def isPrime(n):
    if(n <= 1):
        return False
    elif(n == 2):
        return True
    elif(n%2 == 0):
        return False
    else:
        for i in  range(3, n-1, 1):
            if(n%i == 0):
                return False
    return True


list = [i for i in range(1, limit+1)]
print(list)

primeNumbers = [ n for n in list if(isPrime(n) == True)]
#print(primeNumbers)

primeNum = iter(primeNumbers)
#Use of keyword next to iterate over the iterator
print(next(primeNum))
for n in primeNum:
    print(n)


#Generator to show even and odd numbers
def evenNum(n):
    for i in range(1,n+1):
        if(i%2 == 0):
            yield i

for num in kindOfNum(limit):
    print(num)
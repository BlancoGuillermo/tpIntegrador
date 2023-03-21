#Escribir una función que calcule el mínimo común múltiplo entre dos números

def menorDivisor(x, y):
    z = max(x, y) #tomamos el numero mayor ingresado

    while True:

        if (z % x == 0) and (z % y == 0):
            return z
        z += 1

print(menorDivisor(2, 4))
print(menorDivisor(13, 32))
print(menorDivisor(17, 15))

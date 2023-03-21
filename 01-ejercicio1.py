#Escribir una función que calcule el máximo común divisor entre dos números

def mayorDivisor(x,y):
    mD = 1 # 1 es generalmente el mayor comun divisor entre dos numeros

    ''' y es divisible por y,
        si x es divisible por y
        retornamos y
    '''

    if x % y == 0:
        return y
    
    # iteramos entre y y 0 (queda excluido), y vamos restando uno cada iteracion
    for z in range(int(y), 0, -1):
        # cuando desde 'y' encontremos resto 0
        if x % z == 0 and y % z == 0:
            mD = z # se retorna ese valor
            break

    return mD 



print(mayorDivisor(8,4))
print(mayorDivisor(15,5))

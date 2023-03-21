# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def stringToDict(txt):

    txt = txt.split() # sapara las palabras a traves de los espacios en blanco
    newDict = {}

    for i in txt:
        if i in newDict:
            newDict[i] +=1
        else:
            newDict[i] = 1
    
    return newDict


text = 'Son las 5 menos 5 faltan 5 para las 5 ¿ Cuantas veces dije 5 ?'
print(stringToDict(text))

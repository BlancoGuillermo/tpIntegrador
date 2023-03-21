'''
Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.

'''

def stringToDict(txt):
    
    txt = txt.split() # sapara las palabras a traves de los espacios en blanco
    newDict = {}

    for i in txt:
        if i in newDict:
            newDict[i] +=1
        else:
            newDict[i] = 1
    
    return newDict

def mostRepeated(words):

    maxWord = ''
    maxFreq = 0

    # for key, value in dict.items
    for i, freq in words.items():
        if freq > maxFreq:
            maxWord = i
            maxFreq = freq
    
    return maxWord, maxFreq

text = 'Son las 5 menos 5 faltan 5 para las 5 ¿ Cuantas veces dije 5 ?'
print(stringToDict(text))
print(mostRepeated(stringToDict(text)))
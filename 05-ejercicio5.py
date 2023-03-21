'''
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.

'''

def get_int():

    while True:
        try:  
            numero = int(input("Ingrese un número: "))
        # capturamos el error para que el bucle continue    
        except ValueError:  
            continue # salteamos esta iteración
        else:  
            print(numero)
            break

get_int()
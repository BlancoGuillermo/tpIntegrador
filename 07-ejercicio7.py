'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:

-   Un constructor, donde los datos pueden estar vacíos.
-   Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
    directamente, sólo ingresando o retirando dinero.
-   mostrar(): Muestra los datos de la cuenta.
-   ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
    negativa, no se hará nada.
-   retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
    rojos

'''

class Persona:
    
    def __init__(self, nombre='', edad=0, DNI=0):
        
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    #getter
    @property
    def nombre(self):
        return self.__nombre

    #setter
    @nombre.setter
    def Nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def Nombre(self, edad):
        self.__edad = edad

    @property
    def DNI(self):
        return self.__DNI

    @DNI.setter
    def Nombre(self, dni):
        self.__DNI = dni

    def Mostrar(self):
        print (f"{self.__nombre}, {self.__edad}, {self.__DNI}")

    def Es_mayor_de_edad(self):

        if self.__edad >= 18:
            print('Es mayor de edad')
        else:
            print('Es menor de edad')


class Cuenta(Persona):

    def __init__(self, titular = Persona(), cantidad = 0.0):
        
        self.__titular = titular
        self.__cantidad = cantidad

    #Getters
    @property
    def Titular(self):
        return self.__titular

    @property
    def Cantidad(self):
        return self.__cantidad
    
    #Setters
    @Titular.setter
    def Titular(self, titular):
        self.__titular = titular
    
    '''
    @Cantidad.setter
    def Cantidad(self, cantidad):
        self.__cantidad = cantidad
    '''
    def ingresar(self, dinero):
        if dinero > 0:
            self.__cantidad += dinero

    def retirar(self, dinero):
        self.__cantidad -= dinero
            
    def mostrar(self):
        print(f'La cuenta pertenece a: {self.__titular.nombre} \ny el saldo de su cuenta cuenta asciende a: ${self.__cantidad}')
    
    

persona1= Persona('Juan', 32, 12345678)

cuenta1 = Cuenta(persona1, 100000)

cuenta1.mostrar()

cuenta1.retirar(50000)

cuenta1.mostrar()

cuenta1.ingresar(20000)

cuenta1.mostrar()
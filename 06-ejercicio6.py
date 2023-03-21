'''
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:

- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
- mostrar(): Muestra los datos de la persona.
- Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

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

persona1 = Persona("Juan", 32, 12345678)

persona1.Mostrar()
persona1.Es_mayor_de_edad()

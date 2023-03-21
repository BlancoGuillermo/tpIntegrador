'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
-   Un constructor.
-   Los setters y getters para el nuevo atributo.
-   En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
    tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
    mayor de edad pero menor de 25 años y falso en caso contrario.
-   Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
-   El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
    cuenta.
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

class CuentaJoven(Cuenta):

    def __init__(self, titular=Persona(), cantidad=0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def Bonificacion(self):
        return self.__bonificacion

    @Bonificacion.setter
    def Bonificacion(self, bono):
        if bono >0 and bono < 100:
            self.__bonificacion = bono
    
    def es_titular_valido(self):
        
        return self.__titular.Es_mayor_de_edad() and self.__titular.edad < 25
    
    def retirar(self, dinero):

        if self.es_titular_valido():
            super().retirar(dinero)

    def mostrar(self):
        print(f'Cuenta Joven tiene una bonificacion del: {self.__bonificacion}%')



persona1= Persona('Juan', 23, 12345678)

cuenta1 = Cuenta(persona1, 25000)

cuentaJoven1 = CuentaJoven(Cuenta, 25)

cuentaJoven1.mostrar()
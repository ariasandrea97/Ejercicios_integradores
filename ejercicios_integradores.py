# ------------------------------------------------------------
# Ejercicios integradores
# ------------------------------------------------------------

import math


# 1. Escribir una función que calcule el máximo común divisor entre dos números. (mcd)

def mcd(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def mcm(a, b):
    return (a * b) / mcd(a, b)

#print('------------------------ Ejercicio 5 ---------------------------------')
def get_int(valor):
    while not valor.isdigit():
        valor = input('Debe ingresar un entero: ')
    valor = int(valor)
    return valor


print('------------------------ Ejercicio 1 ---------------------------------')
print('Máximo Común Divisor entre dos números: ')
a=0
b=1
while a<b:
    print("El primer numero debe ser mayor o igual al segundo ")
    a = get_int(input('Ingrese primer numero: '))
    b = get_int(input('Ingrese segundo numero: '))

resultado=mcd(a, b)
print(f"El máximo común divisor entre {a} y {b} es {resultado}.")
print ("Con funcion math.gdc: ", math.gcd(a, b))



# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números (mcm)

print('------------------------ Ejercicio 2 ---------------------------------')
print('Mínimo Común Multiplo entre dos números: ')

a = get_int(input('Ingrese primer numero: '))
b = get_int(input('Ingrese segundo numero: '))

resultado= int(mcm(a, b))
print(f"El mínimo común múltiplo entre {a} y {b} es {resultado}.")



# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario 
# con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

print('------------------------ Ejercicio 3 ---------------------------------')
#texto= input('Ingrese una cadena de caracteres:  ')
texto = 'Hola mundo! Esto es una prueba para contar cada palabra: peras manzanas tomates peras tomates tomates'
print('Texto: ', texto)

# Elimino los caracteres que no cuento como palabra
quitar = ",;:.\n!\"'"
for caracter in quitar:
    texto = texto.replace(caracter,"")  # Remplazo por "nada"

texto = texto.lower() # Paso texto a minuscula para que las palabras cuenten como una sola. Separo por espacios
palabras = texto.split(" ") # Las palabras están separadas por un espacio así que convertimos la cadena a arreglo


# Ahora cuento las palabras creando el diccionario. la clave del diccionario será la palabra, y el valor será el conteo
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")


# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra 
# que contiene y la cantidad de veces que aparece (frecuencia). 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla 
# con la palabra más repetida y su frecuencia.

def frecuencia(texto):
    quitar = "?!,;:.\n!\"'"
    for caracter in quitar:
        texto = texto.replace(caracter,"") 
    
    texto = texto.lower()
    palabras = texto.split(" ")

    diccionario_frecuencias = {}
    for palabra in palabras:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra] += 1
        else:
            diccionario_frecuencias[palabra] = 1
    return diccionario_frecuencias

def palabra_mas_repetida(diccionario):
    palabra_max = max(diccionario, key=diccionario.get)
    print("palabra maxima: ", palabra_max)
    return (palabra_max, diccionario[palabra_max])

   


print('------------------------ Ejercicio 4 ---------------------------------')
#texto= input('Ingrese una cadena de caracteres:  ')
texto = 'Peras manzanas tomates peras tomates Tomates'
print('Texto: ', texto)

diccionario= frecuencia(texto)
mi_tupla=palabra_mas_repetida(diccionario)
print('La palabra ' + mi_tupla[0] + ' es la que mas se repite con una frecuencia de ' + str(mi_tupla[1]) + ' veces.')


# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto 
# en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, 
# iterando mientras el valor no sea correcto. 
# Intente resolver el ejercicio tanto de manera iterativa como recursiva.

# *** Funcion get_int() definida mas arriba para el ejercicio 1 ***
print('------------------------ Ejercicio 5 ---------------------------------')
print("**** Funcion get_int() ****")
print('def get_int(valor):')
print('    while not valor.isdigit():')
print("        valor = input('Debe ingresar un entero: ')")
print('    valor = int(valor)')
print('    return valor')


# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# - mostrar(): Muestra los datos de la persona.
# - Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.


print('------------------------ Ejercicio 6 ---------------------------------')

class Persona:

    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property 
    def nombre(self):
        #print(" # Getter de nombre ")
        return self.__nombre

    @nombre.setter 
    def nombre(self, nombre):
        #print(" # Setter de nombre ")
        while(True):
            if(nombre.isalpha()):  
                #print("validacion completa")
                self.__nombre = nombre
                break
            else:
                print("Caracteres invalidos")
                nombre= input("Ingrese nombre: ")


    @property 
    def edad(self):
        #print("Getter de edad")
        return self.__edad

    @edad.setter 
    def edad(self, edad):
        #print("Setter de edad")
        while(True):
            if(edad.isdigit()):
                self.__edad = int(edad)
                break
            else:
                print("La edad debe ser un numero ")
                edad= input("Ingrese edad: ")

        

    @property 
    def dni(self):
        #print("Getter de dni")
        return self.__dni

    @dni.setter 
    def dni(self, dni):
        while(True):
            if(dni.isdigit() and (len(dni)>=7 and len(dni)<=8)):
                self.__dni = dni
                break
            else:
                print("DNI incorrecto")
                dni= input("Ingrese dni: ")


    def mostrar(self):
        print("-----------------------------------")
        print("Nombre: ",self.__nombre)
        print("Edad: ",self.__edad)
        print("DNI: ",self.__dni)

    
    def mayor_edad(self):
        if self.__edad>=18:
            return True
        else:
            return False

# bloque principal

persona1 = Persona()
persona1.nombre=input("Ingrese nombre: ")
persona1.edad=input("Ingrese edad: ")
persona1.dni=input("Ingrese dni: ")

persona1.mostrar()


if persona1.mayor_edad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. 
# Crear los siguientes métodos para la clase: 
# - Un constructor, donde los datos pueden estar vacíos. 
# - Los setters y getters para cada uno de los atributos. 
#   El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
# - mostrar(): Muestra los datos de la cuenta. 
# - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
#   no se hará nada. 
# - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

print('------------------------ Ejercicio 7 ---------------------------------')

class Cuenta():

    def __init__(self,titular,cantidad=0.0):
        self.__cantidad= cantidad
        self.__titular = Persona (titular.nombre, titular.edad, titular.dni)


    @property 
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter 
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    @property 
    def titular(self):
        return self.__titular

    @titular.setter 
    def titular(self, titular):
        self.__titular = titular


    def mostrar_titular(self):
        print("-----------------------------------------------")
        print("Nombre: ",self.titular.nombre)
        print("Edad: ",self.titular.edad )
        print("DNI: ",self.titular.dni)
        print("Saldo actual de la cuenta: ",self.__cantidad)
        print("-----------------------------------------------")


    def ingresar(self,cantidad):
        if(cantidad>0):
            self.__cantidad=self.__cantidad+cantidad
            print("Suma ingresada: ", cantidad )
        else:
            print("La cantidad introducida es negativa")


    def retirar(self,cantidad):
        self.__cantidad=self.__cantidad-cantidad
        print("Suma retirada: ", cantidad )




titular1=Persona()
titular1.nombre=input("Ingrese nombre: ")
titular1.edad=input("Ingrese edad: ")
titular1.dni=input("Ingrese dni: ")
#cuenta1=Cuenta(titular1.nombre, titular1.edad, titular1.dni)
cuenta1=Cuenta(titular1,0)

print("--------------------------------------------")

cuenta1.ingresar(1000)
cuenta1.ingresar(2000)
cuenta1.ingresar(-200) # no debe hacer nada
cuenta1.retirar(500)
cuenta1.mostrar_titular()
cuenta1.retirar(5000)
cuenta1.mostrar_titular()


# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuentaJoven que deriva de la clase creada 
# en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará 
# expresada en tanto por ciento. Crear los siguientes métodos para la clase: 
# - Un constructor. 
# - Los setters y getters para el nuevo atributo. 
# - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un 
#   método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
# - Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
# - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.


class CuentaJoven(Cuenta):
    def __init__(self,titular,cantidad,bonificacion=0.0):
        super().__init__(titular,cantidad)
        self.__bonificacion=bonificacion


    @property 
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter 
    def bonificacion(self, bonificacion):
        while(True):
            if(bonificacion.isdigit() ):
                if( int(bonificacion)>=0 and int(bonificacion)<=100):
                    self.__bonificacion = int(bonificacion)
                    break
                else:
                    print("La bonificacion debe ser un numero menor o igual a 100 ")
                    bonificacion= input("Ingrese bonificacion: ")
            else:
                print("La bonificacion debe ser un numero menor o igual a 100 ")
                bonificacion= input("Ingrese bonificacion: ")


    def mostrar_cuentaJoven(self):
        print("Cuenta Joven")
        #super().mostrar_titular()
        print("Bonificacion: ",self.__bonificacion)


    def es_titular_valido(self,edad):
        if (edad>=18 and edad<25):
            return True
        else:
            return False

print('------------------------ Ejercicio 8 ---------------------------------')

titular2=Persona()
titular2.nombre=input("Ingrese nombre: ")
titular2.edad=input("Ingrese edad: ")
titular2.dni=input("Ingrese dni: ")


cuentajoven=CuentaJoven(titular2, 0,0)
cuentajoven.bonificacion=input("Ingrese bonificacion: ")

print("----------------------------------------------------")

cuentajoven.mostrar_cuentaJoven()

cuentajoven.ingresar(5000)
cuentajoven.ingresar(2000)

if cuentajoven.es_titular_valido(titular2.edad):
    print("Es titular valido")
    cuentajoven.retirar(1000)
else:
    print("No es titular valido. No cumple con la edad requerida.")
    print("No es posible retirar dinero")








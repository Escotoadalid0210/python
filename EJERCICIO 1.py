
"""nombre = input(f"Ingrese su nombre: ")
cuenta = int(input(f"Ingrese su cuenta: "))

print(nombre)
print(cuenta)"""

#variable char
letra = "A"
print(letra)

#variable booleano
boleano = True
print(boleano)

boleano = False
print(boleano)

#Operadores relacionales
"""
se utilizan para establecer la relacion entre 2 variables
> mayor que 
< menor que
>=mayor igual
<=menor que 
==igual que
!= distinto

"""
#mayor que

resultado = 10> 20
print(resultado)

#menor que

resultado = 10 < 20
print(resultado)

#mayor igual que
resultado = 5 >= 5
print(resultado)
#menor igual que
resultado = 5 <= 4
print(resultado)

#igua igual
resultado = 5 ==10
print(resultado)

#distinto que

resultado = 10!=20
print(resultado)

#variables int

A = 3
B = 10
C = 5

"""resultado= A+B == C
print(resultado)"""


#ejercicio 1
resultado = (A**3 * (B**2 - 2*A*C))/(2*B)

print(resultado)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Operadores logicos

"""
AND "and"
OR  "or"
NOT  "not"
"""

#Operador logico and // multiplicacion
"""
True and True = True
True and False = False
False and True = False
False and False = False
"""
#Operador logico or // suma
"""
True and True = True
True and False = True
False and True = True
False and False = False
"""

#Operador logico not // Inverso
"""
True not = False
False not = True
"""
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ejercicio 2
a = 10
b = 12
c = 13
d = 10

resultado=((a>b)or(a<c))and((a==c)or(a>=b))

print(resultado)

#a = 3
#b = 5

a = int(input("Ingrese el numero a-> "))
b = int(input("Ingrese el numero b-> "))
resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)
print(resultado)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#entrada de datos por teclado
#entero
#string
#flotante

#entrada de datos de tipo string
nombre = input("iNGRESE SU NOMBRE")
print(nombre)

#entrada de datos de tipo entero
numero = (int(input("iNGRESE SU NUMERO")))
print ("EL NUMERO ES",numero)

#entrada de datos de tipo FLOTANTE
numero = (float(input("iNGRESE SU NUMERO")))
print (type(numero))


#salida de datos impresion
nombre = "FRANCISCO"
edad = 27
#1
#print(f"hola {nombre} tu edad es {edad}")
#2
#print("hola", nombre, "tu edad es",edad)
#3
print("hola {} tu edad es {}".format(nombre,edad))

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ejercicio 1 tarea

nombre = input("Ingrese su nombre")
identidad = input("Ingrese su identidad")
edad = int(input("Ingrese su edad"))
campus = input("Ingrese su campus")

print(f"su nombre es: {nombre} su edentidad es: {identidad} su edad es : {edad} su campus es:{campus}")
#print("su nombre es: {}, su identidad es: {} su edad es: {}  su campues es:{}".format(nombre,identidad,edad,campus))

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#formula matematica
a = int(input("a -> "))
b = int(input("b -> "))
c = int(input("c -> "))

formula = (a**3 * (b**2 - 2*a*c))/(2*b)

print(formula)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#FUNICONES INTEGRADAS
#convertir entero a binario
numero = bin(5)
print(f"el numero binario es:{numero}")

#convertir entero a hexadecimal
numero = hex(5)
print(f"el numero binario es:{numero}")

#convertir binario a decimal
numero = int("0b1010",2)
print(f"el numero binario es:{numero}")

#convertir hexadecimal a decimal
numero = int("0xa",16)
print(f"el numero binario es:{numero}")


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
SUMA
RESTA
MULTIPLICAION
DIVISION
POTENCIA
"""

#OPERACIONES SUMA
NUM1 = 10.5
NUM2 = 35

SUMA = NUM1+NUM2

print(SUMA)

#OPERACION RESTA


RESTA=NUM1 - NUM2

print(RESTA)


#OPERACION MUTIPICACION


MULTI=NUM1 * NUM2

print(MULTI)

#OPERACION DIVISION


DIVISION=NUM1 / NUM2

print(DIVISION)

#OPERACION POTENCIA
#potencia=NUM1 ** NUM2
potencia = pow(10.5,35)
print(potencia)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
1 parentesis ()
2 exponenciacion **
3 multi, division, modulo *,/,%
4 suma y resta +, -

"""

resultado = 3**3 * (13/5 - (2*4))
print(resultado)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""
Ingrese su numero de boleto : 25
ingrese su edad : 15
"""
boleto = int(input("Ingrese su numero de boleto"))
edad = int(input("Ingrese su edad"))

if boleto==45 and edad>=21:
    print(f"FELICIDADES EL NUMERO GANADOR es : 45, Eres mayor de :21")

elif boleto==45 and edad<21:
    print(f"FELICIDADES EL NUMERO GANADOR es : 45, pero no eres mayor de : 21")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#programa que solicite un caracter e indice si es vocal o no
letra = input("Digite un caracter:").lower()#lower es para cambiar de minuscula a mayuscula
print(letra)
if letra == 'a' or letra == 'e' or letra == 'i' or letra== 'o' or letra=='u':
    print("es una vocal")
else :
    print("No es una vocal")

#///////////////////////////////////////////////////////////////////////////////////
letra = input("Digite un caracter:").upper()#upper es para cambiar de mayuscula a minuscula
print(letra)
if letra == 'a' or letra == 'e' or letra == 'i' or letra== 'o' or letra=='u':
    print("es una vocal")
else :
    print("No es una vocal")

#///////////////////////////////////////////////////////////////////////////////////

num1=int(input("Ingrese primer numero"))
num2=int(input("Ingrese segundo numero"))

print("Ingrese S o s para suma")
print("Ingrese R o r para Resta")
print("Ingrese P o p, M o m para Multiplicacion")
print("Ingrese D o d para division")

letra = input("Ingrese su operacion que desea:").lower()

if letra=='S' or letra == 's':
    resultado = num1 + num2
elif letra=='R' or letra == 'r':
    resultado = num1 - num2
elif letra=='P' or letra == 'p' or letra=='M' or letra=='m':
    resultado = num1 * num2
elif letra=='D' or letra == 'd':
    resultado = num1 / num2

print(resultado)


#///////////////////////////////////////////////////////////////////////////////////
#listas son arreglos de todo tipo de datos

lista = ["lunes","Martes","Miercoles","jueves","viernes"]

print(lista[2]) #especificar un campo
#print(lista[0:5]) para recorer toda la lista


#//////////////////////////////////////////////////////////////////////
#Insertas datos en la lista

lista=[1,2,4,5]
lista.insert(2,3)#se le pone el punto y salen las opciones de ingreso parentesis
                #tambien poner la posicion donde queremos agregar
                #y el dato a ingresar
print(lista)
#//////////////////////////////////////////////////////////////////////
#metodo count para contar cuantos datos hay
lista = [1,5,2,"adalid",102.5,"unicah",1,1,1]

print(lista.count(1))#contar cuantos 1 hay

#//////////////////////////////////////////////////////////////////////
#eliminar datos de una lista "remove"
lista = [1,5,2,"adalid",102.5,"unicah",1,1,1]
lista.remove(1)
print(lista)



lista=[1,2,4,5]
lista.remove(1)
lista.insert(1,6)
print(list)


#LISTAR LA LISTA Y ORDENAR POR ORDEN ALFABETICO
lista = ['Tegucigalpa','Comayagua','El paraiso','Choluteca','La paz','Intibuca','Gracias','Copan','Santa barbara','Yoro','Islas de la bahia','Colon','Olancho']
print(lista)
lista.sort(reverse=False)
print(lista)



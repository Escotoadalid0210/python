#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''nombre = input("Ingrese su nombre")
identidad = input("Ingrese su identidad")
edad = int(input("Ingrese su edad"))
campus = input("Ingrese su campus")



print(f"su nombre es: {nombre} su edentidad es: {identidad} su edad es : {edad} su campus es:{campus}")'''
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
precio = float(input("ingrese el precio del articulo"))

descuento = precio * 0.15
if precio<=2500: #precio es menor que 2500 no se da descuento
    totalprecio=precio
    descuento =0 #ya que no aplica descuento se iguala a 0 el descuento

else: #si precio es mayor a 2500 si aplica descuento
    totalprecio=precio-descuento

totalprecio = precio - descuento

print(f"el precio total es : {totalprecio:.2f}")

#////////////////////////////////////////////////////////////////////////////////
#listas
letras = ["A","B","C","D","E","F","G","H"]
del letras[4]
print(letras)


#//////////////////////////////////////
#ingrese 3 numeros y verifique cual es el mayor y en dado caso que sean iguales todos
num1 = int(input("Digite numero 1 >>"))
num2 = int(input("Digite numero 2 >>"))
num3 = int(input("Digite numero 3 >>"))

if num1>=num2 and num1>=num3:
    print(f"numero 1 es el mayor{num1}")
elif num2>=num1 and num2>=num3:
    print(f"el numero 2 es el mayor{num2}")
elif num3>=num1 and num3>=num2:
    print(f"el numero 3 es el mayor:{num3}")
if num1==num2 and num1==num3 or num2==num1 and num2==num3 or num3==num1 and num3==num2:
    print(f"los numeros son iguales")





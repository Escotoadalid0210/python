num1= int(input("INGRESE NUMERO 1: "))
num2= float(input("INGRESE NUMERO 2: "))

print("menu de opciones:")
print("realizar la suma: presion -> +")
print("realizar la resta: presion -> -")
print("realizar la multipicacion: presion -> *")
print("realizar la division: presion -> /")
opciones = input("Ingrese la Opcion a escoger: ".lower())

if opciones=='+':
    print("\nOpcion escogida es: Suma")
    resultado = num1 + num2

elif opciones=='-':
    print("\nOpcion escogida es: Resta")
    resultado = num1- num2

elif opciones=='*':
    print("\nOpcion escogida es: Multiplicacion")
    resultado= num1 * num2

elif opciones=='/':
    print("\nOpcion escogida es: Divicion")
    resultado=num1/num2
else:
    print("Opcion no aceptada")

print("**************************")
print(num1,opciones,num2)
print(f"Resultado: {resultado}")
print("**************************")

Saldo_Inicial = 15600.00


print("*******MENU*******")
print("1.Ingresar dinero en la cuenta")
print("2.Retirar dinero de la cuenta")
print("3.Mostrar dinero disponible")
print("4.Salir")
opcion= int(input("Ingrese la operacion a deciar: "))

if opcion == 1:
        ingreso = float(input("Ingrese la cantidad de dinero: "))
        Saldo_Actual = ingreso + Saldo_Inicial
elif opcion == 2:
        retiro = float(input("Digite la cantidad a retirar: "))
        Saldo_Actual = Saldo_Inicial - retiro
elif opcion == 3:
        print(f"{Saldo_Inicial}")
        exit();
elif opcion == 4:
        exit();

print(Saldo_Actual)

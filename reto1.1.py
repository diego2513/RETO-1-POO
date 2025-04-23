numero1=int(input("Ingrese el numero 1: "))
numero2=int(input("Ingrese el numero 2: "))

opcion=int
while opcion != 0:
    print("\n+------------------------------------+")
    print("+               MENU                 +")
    print("+ 1. SUMAR LOS DOS NUMEROS  (+)      +")
    print("+ 2. RESTAR LOS DOS NUMEROS (-)      +")
    print("+ 3. DIVIDIR LOS DOS NUMEROS (/)     +")
    print("+ 4. SUMAR LOS DOS NUMEROS (*)       +")
    print("+ 5. SALIR (!)                       +")
    print("+------------------------------------+")
    opcion=input("\nIngrese la opcion de su preferencia: ")
    while opcion not in ["+" , "-" , "/" , "*" , "!"]:
        opcion=input("\nOpcion no valida ingresa de nuevo una opcion: ")
    if opcion == "+":
        print(f"\nLa suma de los numeros es {numero1 + numero2}")
    elif opcion == "-":
        print(f"\nEl numero 1 - el numero 2 es {numero1 - numero2}")
        print(f"\nEl numero 2 - el numero 1 es {numero2 - numero1}")
    elif opcion == "*":
        print(f"\nLa multiplicacion de los numeros es {numero1 * numero2}")
    elif opcion == "/":
        if numero1 == 0:
            print("\nNumero 1/numero 2 es 0 y no se puede dividir el numero 2 entre 0")
        elif numero2==0:
            print("\nNumero 2/numero 1 es 0 y no se puede dividir el numero 1 entre 0")
        else:
            print(f"\nEl numero 1/numero 2 es {numero1/numero2}")
            print(f"\nEl numero 2/numero 1 es {numero2/numero1}")
    else:
        print("\nHas salido") 
        break
  

palabra=input("Ingresa una palabra: ")

palabra = palabra.lower()

for i in range(len(palabra)):
    if palabra[i] != palabra[-(i + 1)]:
        print(f"la palabra {palabra} no es un palindromo")
        break
else:
    print(f"La palabra {palabra} es un palindromo")

    


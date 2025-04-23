primos = input("Ingresa una lista de números separados por espacios: ")

lista = primos.split() 
listap = [int(x) for x in lista] 

print(listap)
cont=int
print("Los numeros primos de tu lista de numeros son")
for i in range (len(listap)):
    cont=0
    for j in range (1,listap[i]+1):
        if listap[i]%j == 0:
            cont+=1
    if cont==2:
        print(listap[i])
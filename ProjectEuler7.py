primos = [2]
suma = 0
nmax = int(input("Ingrese un valor: "))
print("Los numeros primos hasta", nmax, "son: ")
for x in range(2, nmax):
    for i in range(2, x):
        if x%i != 0:
            continue
        else:
           break
    else:
        suma += 1
        print(suma,"°", x)
        if suma == 10001:
            break
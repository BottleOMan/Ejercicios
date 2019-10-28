primos = [2]
suma = 2
nmax = int(input("Ingrese un valor: "))
print("Los numeros primos hasta", nmax, "son: ")
for x in range(3, nmax):
    for i in range(2, x):
        if x%i != 0:
            continue
        else:
            break
    else:
        suma += x
print("La suma de los numeros primos hasta", nmax, "es: ", suma)
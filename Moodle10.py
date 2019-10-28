n = int(input("Ingrese un valor: "))
suma = 0
for x in range(1, n):
    if n%x == 0:
        suma += x
if suma == n:
    print("El valor", n, "es perfecto.")
else:
    print("El valor", n, "no es perfecto.")
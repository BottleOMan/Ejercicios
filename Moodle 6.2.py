a = int(input("Ingrese el valor A: "))
b = int(input("Ingrese el valor B: "))
par = 0
impar = 0
perfecto = 0
perfectosum = 0
if a > b:
    for x in range(b + 1, a):
        if x%2 == 0 and x != 0:
            par += 1
        elif x == 0:
            par += 0
        else:
            impar += 1
    for perf in range(b, a + 1):
        for z in range(1, perf):
            if perf%z == 0:
                perfectosum += z
                if perfectosum == perf:
                    perfecto += 1
                    
    print("La cantidad de numeros pares entre B y A es: ", par)
    print("La cantidad de numeros impares entre B y A es: ", impar)
    print("La cantidad de numeros perfectos entre B y A es: ", perfecto)
    print("")
    print("")
    print("")
else:
    print("A es menor a B.")
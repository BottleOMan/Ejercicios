n = int(input("ingrese un numero:" ))
p = 0
j = 0
for i in range(1,n + 1):
    w = i ** 2
    j += w
    p += i
s2 = p ** 2
x = s2 - j
print("la suma de los cuadrados es: ",j)
print("el cuadrado de las sumas es: ",s2)
print("y su diferencia es: ",x)
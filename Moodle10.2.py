text = str(input("Ingrese un texto: "))
n = 0
num = []
for c in text:
    if (c == "1") or (c == "2") or (c == "3") or (c == "4") or (c == "5") or (c == "6") or (c == "7") or (c == "8") or (c == "9") or (c == "0"):
        
        n += 1
        num.append(c)
        
print("Los digitos que aparecen en el texto son: ", num)
print("La cantidad de digitos en el texto es: ", n)

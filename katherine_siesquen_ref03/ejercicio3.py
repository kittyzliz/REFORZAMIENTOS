num1 = 88.584
num2 = 11.24
print("NUMEROS DECIMALES")
print("-------------------")
print(num1)
print(num2)

entero1 = int(num1)
entero2 = int(num2)
print("NUMEROS ENTEROS")
print("-------------------")
print(entero1)
print(entero2)

print("-------------------")
if entero1 % entero2 == 0:
    print("El numero", entero1, "es multiplo de", entero2)
else:
    print("El numero", entero1, "NO es multiplo de", entero2)
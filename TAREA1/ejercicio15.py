#Solicitar al usuario dos valores:
#numero1 (int)
#numero2 (int)
#Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que
#sigue):
#Proporciona el numero1:
#Proporciona el numero2:
#El numero mayor es: numeroMayor

numero1=int(input("Proporciona el numero1 = "))
numero2=int(input("Proporciona el numero2 = "))

print(numero1)
print(numero2)

if numero1 > numero2:
    print("el numero mayor es", numero1)
#elif numero2 <numero1:
#   print("el numero2 es menor que el numero1", numero2)

else:
     print("el numero2 es mayor que numero1")

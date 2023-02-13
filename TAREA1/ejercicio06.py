#Crear un script que permita calcular si un número es par o impar
#import math

a= int(input("Escribe un numero: "))

if a % 2 == 0:
    print('El número', a, 'es par.')
else:
    print('El número', a, 'es impar.')
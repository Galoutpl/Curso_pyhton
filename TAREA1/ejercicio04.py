#Crear un script que imprima el volumen de una esfera por su radio 4/3 * pi * r ** 3


import math
radio= int(input("Escribe el radio de una esfera: "))

volumen= (4/3 * math.pi) * (radio * radio * radio)

print("El volúmen de tu esfera es",volumen)

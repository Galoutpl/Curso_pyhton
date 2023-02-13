#Crear un script que reciba una cantidad infinita de números hasta decir basta, luego
#que imprima la suma de los números ingresados

cantidad = 10
print(f"Voy a solicitarte {cantidad} números:")
numeros = []
for i in range(cantidad):
    # Recuerda que range comenzará desde 0, así que imprimimos el número solicitado pero + 1
    numero = input(f"Ingresa el número {i + 1}: ")
    # Convertir a entero, pues input regresa una cadena
    numero = int(numero)
    # Lo agregamos al arreglo con append
    numeros.append(numero)

    # Finalmente, los mostramos, aunque podrías hacer cualquier otra cosa
print("Te mostraré los números que ingresaste: ")
for numero in numeros:
    print(numero)
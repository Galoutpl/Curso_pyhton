#Crear un script que indique cuantas vocales tiene una palabra

def contar_vocales(palabra):
	contador = 0
	for letra in palabra:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

palabra = str(input("Escribe una palabra: "))
cantidad = contar_vocales(palabra)
print(f"En la palabra '{palabra}'' hay {cantidad} vocales")

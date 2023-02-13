#Ingresar nombre y apellido e imprimirlo al revés

Nombre=input("Por favor ingrese su nombre: ")
Apellido = input ("Por favor ingrese su apellido: ")
def saludar(Nombre=Nombre, Apellido=Apellido):
    
    return f"Hola {Nombre} {Apellido}"

saludo = saludar ()
print(saludo)

def reverse(phrase):
    return ' '.join(list(map(lambda x: x[::-1], phrase.split())))

print(reverse(saludo))  

#Multiplicar 2 números sin usar el símbolo de la multiplicación
"""
x = int(input('Introduce un dato: '));
print("El dato es", x)
"""

a = int(input("por favor ingrese el primer numero: "));

b = int(input("por favor ingrese el segundo numero: "));

print("el dato a es: ",a)
print("el dato b es: ",b)

producto = int(0);
#mientras b es distinto de 0
while b !=0:
    producto = producto+a;
    b = b-1;
 
print("el producto entre los numeros es: ",producto)

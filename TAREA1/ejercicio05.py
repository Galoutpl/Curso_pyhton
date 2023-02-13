#Crear una script que indique si el usuario es mayor de edad

edad=int(input("Escriba su edad en numeros = "))
print(type(edad))
print(edad)

if edad <=18:
    print("usted es menor de edad", edad)
elif edad >18 and edad<100:
    print("usted es mayor de edad", edad)

else:
     print("el rango de edad no es contemplado")

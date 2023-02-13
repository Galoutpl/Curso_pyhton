#El objetivo del ejercicio es crear un sistema de calificaciones, tomando en cuenta la
#siguiente información:
#1. El usuario proporcionará un valor entre 0 y 10.
#2. Si está entre 9 y 10: imprimir una A
#3. Si está entre 8 y menor a 9: imprimir una B
#4. Si está entre 7 y menor a 8: imprimir una C
#5. Si está entre 6 y menor a 7: imprimir una D
#6. Si está entre 0 y menor a 6: imprimir una F
#7. Cualquier otro valor debe imprimir: Valor desconocido
#Por ejemplo:
#Proporciona un valor entre 0 y 10:


notas=int(input("por favor su calificacion en numeros = "))
print(type(notas))
print(notas)

if notas>=9 and notas <= 10:
    print("su calificacion es A=", notas)
elif notas <= 9 and notas>=8:
    print("su calificación es B=", notas)
elif notas>=7 and notas <=8:
        print("su calificacion es C=",notas)
elif notas>=6 and notas <=7:
        print("su calificacion es D=",notas)
elif notas>=0 and notas <=5:
        print("su calificacion es F=",notas)

else:
     print("Valor desconocido")

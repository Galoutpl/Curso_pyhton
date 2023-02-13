#Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3

x = 12
while x > 0:
    x -=3
    print(x)
   
if x % 3 == 0:
    print('El número', x, 'no es divisible para 3.')
else:
    print('El número', x, 'si es divisible para 3.')
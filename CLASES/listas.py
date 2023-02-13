"""
lista = []

print(type(lista))

lista=[
    "Diego",
    "Saavedra",
    34,
    1.65,
    True
]

print(lista)

lista.append("gaguamanj@gmail.com")
print(lista)

lista2 = lista.copy()
print(lista, lista2)
lista.clear()

print(lista, lista2)
print(lista2.count(34)) #1
print(len(lista2))
"""
lista=["a","e","i","o","u"]
print(lista[2])

print(lista.index("o"))

lista.pop()

print(lista)

lista.remove("a")
print (lista)

lista=["e","i","a","o","u"]
lista.sort()
print(lista)


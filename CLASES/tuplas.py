tupla=("esto","es","un",ejemplo","de","tupla")
print(tupla)
print(type(tupla))

tupla.pop()

tupla.count("un")
print(tupla.count("un"))
print(tupla.index("de"))

print(tupla[2])

lista=list(tupla)
lista.append("ejemplo2")

print(lista)
print(type(lista))

tupla2=tupla(lista)
print(tupla2)
"""
dic={
    "nombre":"Diego",
     "apellido":"Saavedra",
     "cel":"9999999",
     "edad":34
     }

print(type(dic))
print(dic)

print(dic["cel"])
print(dic["apellido"])

print(dic.get("apellido"))
dic["edad"]=35

print(len(dic))

dic["ciudad"]="Loja"
print(dic)

dic.pop("ciudad")
print(dic)

dic.popitem()
print(dic)

del dic["nombre"]
print(dic)

dic2=dic.copy()
print(dic2)
"""

perros={
    "Tobby":{
    "nombre":"Tobby",
    "edad": 6,
    "raza":"mestizo"
    },
    "Leo":{
    "nombre":"Leo",
    "edad":1,
    }
    }
print(type(perros))
print(perros)

rocky=dict{
    nombre="rocky",
    edad:2,
    raza:"mestizo",
}
print(type(rocky))
print(rocky)


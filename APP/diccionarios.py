#definicion
d1: dict[str, int] = {"A": 100, "x": 200}
d2: dict[str, int] = dict([("A", 100),("X", 200)]) # es lo mismo, pero en forma de funcion, dentro de una lista debe ir una tupla
print(d1)
print(d2)

#modificar
d2["A"] = 500
print(d2)
d2["Y"] = 1000 # si no existe la clave la agreda
print(d2.pop("Y")) # me retorna el valor de esa clave, y me elimina la clave
print(d2)
print(d2.popitem()) # me devolvio el ultimo elemento de la tupla y lo elimina
print(d2)
d2.setdefault("M", 1) #otra manera de agregar dato
print(d2)
d2.update(A=5, B=2, C=-1) #actualizar datos en el diccionario
print(d2)

#Acceder a una clave
print(d2["B"])
print(d2.get("X")) #en forma de funcion
if "P" in d2:
    print(d2["P"])
else:
    print("Clave no existe")

if -1 in d2:
    print("Si esta")

print(list(d2.values())) #me devuelve los valores
print(list(d2.keys()))  #me devuelve las claves

#Iterar
for e in d2:
    print(e) #m devulve las claves

for e in d2:
    print(d2[e])  #me devuelve los valores

#Iterar con tuplas

for k, v in d2.items():
    print(f"{k} => {v}")

d2["T"] = {"Nombre": "juanita", "Edad": 18}
print(d2)

d3: dict[int, str] = {}
d3[0] = "Hola"
d3[1] = "Juanita"
print(d3)


#Inicializar
a: list[int] = [1,2,3,4]
b: list[int] = list([123]) #crear una lista por medio de una funcion

print(a)
print(b)


#Acceder a los elementos
print(f"Longitud: {len(a)}")
print(f"Posición 1: {a[1]}")
print(a[-1]) #para recorrer de atras hacia adelante es con posicion negativa

# Modificar (mutabilida)
a[0] = 10
print(a)

a.append(50)
print(a)

a.remove(10)
print(a)

del a[0] #elimina posiciones
print(a)

a += [40, 50] #otra manera de hacer append
print(a)

print(a.pop()) #me saca y retorna el ultimo elemento de la lista
print(a)

print(a.pop(-1)) #me saca y retorna el que yo le diga en el parametro de la lista
print(a)

a.reverse() #me pone la lista al reves
print(a)

print(f"Index={a.index(4)}") #imprime la posicion del numero que le de
print(a)


# Recorrer lista
for i in range(len(a)): # recorre y se usa cuando tenga que hacer alguna operacion
    print(a[i])


for i, v in enumerate(a):
    print(f"{i} -> {v}")


print("\n\n")

print(a[1:2])
# solo incluye la posicion 1, la posicion 2 no por eso se pone una posicion mas grande. Esto crea una nueva lista
print(a)

print("\n")
print(a[-2:-1])

print(a[:-1]) # Todos los elementos excepto el ultimo

print("\n\n")

print(a)
print(a[0:2:1]) #que se ponga en la posicion 2, y me devuelva el numero que este antes. El tercer parametro suma. Los :: representa desde el principio hasta el final

print(a[::-1]) #pone la lista al reves, creando una nueva lista
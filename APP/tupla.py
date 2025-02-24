t: tuple[int, int, int, int] = (1,2,3,4)  #la tupla no se puede modificar

print(t[0])  #para acceder a la tupla debe de usar []
print(t[::-1])

m: tuple[int] = (10,) #para definir la tupla debo poner una , cuando es un solo elemento
print(m)
print(type(m))

#empaqueta o desempaquetado de tuplas

x,y,z,m = t
print(f"x={x}")
print(f"y={y}")
print(f"z={z}")
print(f"m={m}")



#intercambiar valores
x, y = y, x
print(f"x={x}")
print(f"y={y}")
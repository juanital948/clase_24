#hacer una funcion que tenga numeros enteros y que retorne verdadero si todos los elemntos de la lista son mayores que cero

def verificar_lista(lista):
    for i in lista:
        if i < 0:
            return False
    return True

#elemento maximo
n = [4,5,6,7,8]
print(max(n))


#elemento minimo
n = [4,5,6,7,8]
print(min(n))


# escribir una funcion qu e reciba dos listas lista1 lista2 y retorna otra lista que contiene tuplas que contiene en cada tupla los elemntos de la lista1 y de la lsita2

lista1 = [1,2,3,4,5]
lista2 = ["A", "B", "C", "D", "E"]

def combinar_listas(lista1, lista2):
    return list(zip(lista1, lista2))

print(combinar_listas(lista1, lista2))
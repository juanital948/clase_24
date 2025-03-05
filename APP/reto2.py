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


# hacer una funcion que reciba una lista de numeros enteros y la funcion debe retonar otra lista solo con los numeros de la lista original que sean pares
l2=[]
l1 = [1,2,3,4,5,6,7,8,9,10]
def numeros_pares(lista):
    for i in lista:
        if i % 2 == 0: l2.append(i)
        return l2
    print(numeros_pares(l1))


#crear una lista que reciba numeros enteros y debe retonar otra lista la lista que retorna debe contener los cuadrados de los numeros que son solo negativos de la lista original

lista = [1,-2,3,-4,5,-6,7,-8,9,10]
return_list = []
def cuadrados_negativos(lista):
    for i in lista:
        if i < 0:
            return_list.append(i**2)
    return return_list
print(cuadrados_negativos(lista))


##

lista: list[int] = [4, -4, 0, -5, 12, -8, 3]
filter(lambda n: n < 0, lista)
print(list(map(lambda n: n * n, filter(lambda n: n < 0, lista))))
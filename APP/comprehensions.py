def cuadrados_de_negativos(numeros: list[int]) -> list[int]:
    return [numero ** 2 for numero in numeros if numero < 0]

lista: list[int] = [4, -4, 0, -5, 12, -8, 3]
print(cuadrados_de_negativos(lista))


def unir_listas(lista_1: list, lista_2: list) -> list:
    n = min(len(lista_1), len(lista_2))
    return [(lista_1[i], lista_2[i]) for i in range(n)]

l1 = ["A", "B"]
l2 = [10,20,30,40]
print(unir_listas(l1, l2))

#funcion que recibe lista de nombres, y retorna otra lista de nombre si el nombre en la lista original contiene la letra M debe retornar en  mayuscula sino en minuscula

def recibir_nombres(nombres: list[str]) -> list[str]:
    return [nombre.upper() if "m" in nombre.lower() else nombre.lower() for nombre in nombres]

lista_nombres: list[str] = ["Juanita", "Samuel", "Monica", "Jose", "Luisa", "Maria"]
print(recibir_nombres(lista_nombres))

#funcion que reciba dos listas de numeros enteros y retorne una tercera lista de tuplas. esa tercera debe tener todas las posibles combinaciones de dos elementos de la primera lista con la segunda, solo dbe agregar si la suma de los dos es mayor que 10

def recibir_listas(lista_1: list[int], lista_2: list[int]) -> list[tuple]:
    return [(n1,n2) for n1 in lista_1 for n2 in lista_2 if n1 + n2 > 10]


lista_1 = [9,5,3,11]
lista_2 = [1,2,3,4]
print(recibir_listas(lista_1, lista_2))

# definir una funcion que reciba una lista de numeros enteros positivos y debe retornar un diccionario, el diccionario que retorne debe contener como clave el cuadrado del numero de la lista y como valor otra lista que contenga los primeros 10 multiplos del numero original

def recibir_numeros_enteros(lista: list[int]) -> dict[int, list[int]]:
    return {num ** 2: [num * i for i in range(1, 11)] for num in lista}
lista_1 = [9,5,3,11]
print(recibir_numeros_enteros(lista_1))
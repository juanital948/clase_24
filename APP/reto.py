# imrpimir cada elemento de la lista ennumerado desde 5
# funcion enumerate


def enumerar_lista(lista: list):
    for x in enumerate(lista, start=5):
        print(x)

l = ["A", "B", "C", "D"]
enumerar_lista(l)


#hacer una funcion que tenga numeros enteros y que retorne verdadero si todos los elemntos de la lista son mayores que cero
def verificar_mayores_que_cero(numeros: list[int]) -> bool:
    for num in numeros:
        if num == 0:
            return False
    return True

n = [4,5,6,7,8]
print(verificar_mayores_que_cero(n))

#otra manera
def verificar_mayores_que_cero_2(numeros: list[int]) -> bool:
    return all (numeros) #all recibe un objeto iterable

#sumar
n = [4,5,6,7,8]
print(sum(n))


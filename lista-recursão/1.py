
def soma(lista):
    if len(lista) == 0:
        return 0
    return lista.pop(-1) + soma(lista)

print(soma([1,2,3,4]))
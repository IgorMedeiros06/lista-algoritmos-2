import random

def matriz3x3():
    matriz = []
    for _ in range(3):
        lista = []
        for _ in range(3):
            # lista.append(random.randint(1,10))
            lista.append(int(input("Digite um valor: ")))
        matriz.append(lista)
        lista = []
    return matriz

matriz = matriz3x3()
print(matriz)

for linha in matriz:
    print(linha)

for coluna, lista in enumerate(matriz):
    for linha, item in enumerate(lista):
        if coluna == linha:
            print(item)


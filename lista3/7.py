matriz = [[1, 2],
            [3, 4],
            [5, 6]]

def atualizar_matriz_99(matriz):
    linha = matriz[1]
    linha[0] = 99
    return matriz

matriz = atualizar_matriz_99(matriz)

def matriz_transposta(matriz):
    transposta = []
    linha_transposta1 = []
    linha_transposta2 = []
    for indice, linha in enumerate(matriz):
        for indice_linha, item in enumerate(linha):
            if indice_linha==0:
                linha_transposta1.append(item)
            if indice_linha==1:
                linha_transposta2.append(item)
    transposta.append(linha_transposta1)
    transposta.append(linha_transposta2)
    return transposta

print(matriz_transposta(matriz))


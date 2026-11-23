import random

def gerador_sinais(x):
    sinais = random.choices([0,1], k=x)
    return sinais

# print(gerador_sinais(int(input(": "))))

def decofica_sinal(sinais):
    pacotes_validos = 0
    indice_pacotes_validos = []
    for i in range(len(sinais)):
        if i != (len(sinais)-2):
            if sinais[i] == 1 and sinais[i+1] == 0 and sinais[i+2] == 0:
                pacotes_validos += 1
                indice_pacotes_validos.append(i)
    return (f"Numero de pacotes válidos: {pacotes_validos}\nLista de índice: {indice_pacotes_validos}")

print(decofica_sinal(gerador_sinais(int(input(": ")))))


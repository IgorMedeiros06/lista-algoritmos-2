import random

sensores = [(1, 30, 23), (2, 35, 17), (3, 41, 21), (4, 33, 18)]

def gera_dados_sensores(x):
    dados_sensores = []
    for i in range(x):
        sensor = []
        sensor.append(i)
        sensor.append(random.randint(25,45))
        sensor.append(random.randint(15,32))
        tupla = tuple(sensor)
        dados_sensores.append(tupla)
        sensor=[]
    return dados_sensores

def verifica_sensores(dados_sensores):
    acionados = []
    maior_temp = 0
    menor_temp = 100
    for tuplas in dados_sensores:
            if tuplas[1] > maior_temp:
                maior_temp=tuplas[1]
            if tuplas[1] < menor_temp:
                menor_temp=tuplas[1]
            if tuplas[1] > 35:
                acionados.append(tuplas[0])
            if tuplas[2] < 20:
                acionados.append(tuplas[0])
    return (f"Sensores ativados: {acionados} \nMaior e menor temperatura: {(maior_temp, menor_temp)}")

print(verifica_sensores(gera_dados_sensores(int(input(": ")))))
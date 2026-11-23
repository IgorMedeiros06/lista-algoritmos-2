import random

def gerador_votos():
    contador = 0
    votos = []
    quantidade = int(input("Digite a quantidade votos que quer: "))
    while contador < quantidade:
        voto = random.choice([0,1,2,3,4])
        votos.append(voto)
        contador+=1
    return votos

votos = gerador_votos()
print(votos)

def apuracao_urna(lista):
    resumo = []
    candidato1, votos1 = [1], 0
    candidato2, votos2 = [2], 0
    candidato3, votos3 = [3], 0
    candidato4, votos4 = [4], 0
    branco = 0
    for id in lista:
        if id == 1:
            votos1 += 1
        elif id == 2:
            votos2 += 1
        elif id == 3:
            votos3 += 1
        elif id == 4:
            votos4 += 1
        else:
            branco += 1
    candidato1.append(votos1)
    candidato2.append(votos2)
    candidato3.append(votos3)
    candidato4.append(votos4)
    resumo.append(candidato1)
    resumo.append(candidato2)
    resumo.append(candidato3)
    resumo.append(candidato4)
    votos = [votos1, votos2, votos3, votos4]
    Maior_voto = 0
    for i in votos:
        if i > Maior_voto:
            Maior_voto = i
    vencendor = votos.index(Maior_voto) + 1
    return (f"Resumo: {resumo}\nVencedor: {vencendor}\nPorcetagem em branco: {(branco/len(lista))*100}%")

print(apuracao_urna(votos))
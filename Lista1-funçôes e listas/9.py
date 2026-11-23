import random

def gerador_plantao(qntd_medicos,qntd_dias_trabalhados_por_medico):
    plantoes = []
    data = []
    for i in range (qntd_medicos):
        for n in range (qntd_dias_trabalhados_por_medico):
            data.append(random.choice(list(range(1,30))))
            data.sort()
        plantoes.append(data)
        data = []
    return plantoes

def dias_plantoes(lista):
    dias = []
    for i in lista:
        for a in i:
            if i not in dias:
                dias.append(a)
    return dias

def plantao_critico(dias_plantao, escala_medica):
    menor = len(escala_medica)
    soma = 0
    for i in dias_plantao:
        for n in escala_medica:
            for a in n:
                if i == a:
                    soma += 1
        if soma<menor:
            menor = i
        soma = 0
    return menor

def medicos_platao_critico(dia, escala_medeica):
    medicos = []
    medico = 0
    for i in escala_medeica:
        for a in i:
            if medico not in medicos:
                if a == dia:
                    medicos.append(medico)
        medico += 1
    return medicos

plantoes = gerador_plantao(int(input(": ")), int(input(": ")))
dias_com_plantoes = dias_plantoes(plantoes)
plantao_critico =  (plantao_critico(dias_plantoes(plantoes), plantoes))
print(f"Dia com menos profissionais: {plantao_critico} \nMedicos do dia: {medicos_platao_critico(plantao_critico, plantoes)}")

kms = [5000,1000,5000,3800,7000,2510,3200,4210]
limite = 10000

def alerta_manutencao(lista):
    limite = int(input("Qual o limite: "))
    soma = 0
    guardar = 0
    recolher = False
    for i in range(len(lista)):
        soma += lista[i]
        if guardar!=0:
            continue
        if soma>limite or soma==limite:
            guardar = i
            recolher = True
    return (f"Quilometragem total: {soma}\nDia de ultrapassagem do limite: {guardar}\nPrecisa ser recolhido? {recolher}")

def recebe_km():
    kms = []
    while True:
        valor = int(input("(Digite 0 para finalizar a lista) Qual a distância de hoje?: "))
        if valor == 0:
            break
        else:
            kms.append(valor)
    return kms

kms = recebe_km()

print(alerta_manutencao(kms))
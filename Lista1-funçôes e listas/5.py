macas = [500,800,650,730,675,300,920,456,678,865,591,892,678,756,789]

def gerador_lista_macas():
    macas = []
    while True:
        valor = int(input("(Digite 0 para finalizar a lista) Qual o peso da maçã?: "))
        if valor == 0:
            break
        else:
            macas.append(valor)
    return macas

def controle_macas(lista):
    min = int(input("Isira o peso mínimo: "))
    max = int(input("Isira o peso maximo: "))
    exportadas = []
    descartadas = []
    for peso in lista:
        if peso>min and peso<max:
            exportadas.append(peso)
        else:
            descartadas.append(peso)
    perca = (len(descartadas)/len(lista))*100
    return (f"Exportadas: {exportadas} \nDescartadas: {descartadas} \nPorcetagem de perca: {perca}%")

macas = gerador_lista_macas()

print(controle_macas(macas))
voo = [8000,7700,7800,7900,8100,7500,7750,8000,8200,8500,8000,8450,8800,9000,8000,7200]

def turbulencia_voo(lista):
    turbulencia = False
    maior = 0
    for i in range(len(lista)-1):
        deslocamento = lista[i] - lista[i+1]
        if deslocamento>500:
            turbulencia = True
            if deslocamento>maior:
                maior = deslocamento
    return (f"Houve turbulência: {turbulencia}\nMaior queda de altitude: {maior}")

def recebe_altiude():
    altitude = []
    while True:
        valor = int(input("(Digite -1 para finalizar a lista) Qual a altitude atual?: "))
        if valor == -1:
            break
        else:
            altitude.append(valor)
    return altitude

print(turbulencia_voo(recebe_altiude()))

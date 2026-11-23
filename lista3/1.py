def percorre_lista():
    lista = []
    n = int(input("Quantos valores deseja digitar: "))
    for i in range(n):
        lista.append(int(input(f"Digite o valor {i+1}: ")))
    maior = 0
    menor = max(lista)
    soma = 0
    pares = 0
    for numero in lista:
        soma += numero
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        if numero%2 == 0:
            pares+=1
    return (f"Maior: {maior} | Menor: {menor} \nMédia: {soma/len(lista)} \nQuantidade de pares: {pares}")

print(percorre_lista())
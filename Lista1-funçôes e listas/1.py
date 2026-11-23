
def media_movel(lista,k):
    medias=[]
    while True:
        soma=0
        if len(lista)>=k:
            for i in range(k):
                soma += lista[i]
            medias.append(soma/k)
            lista.remove(lista[0])
        else:
            break
    return medias

lista=[]
while True:
    Numero=int(input("Adicione um valor ou digite 0 para parar: "))
    if Numero==0:
        break
    else:
        lista.append(Numero)


k=int(input("Digite o tamanho da janela: "))

r=media_movel(lista,k)
print(r)
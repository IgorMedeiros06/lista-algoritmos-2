
def shift_direita(lista,posicoes_deslocamento):
    for _ in range(posicoes_deslocamento):
        deslocar=lista.pop()
        lista.insert(0,(deslocar))
    return lista

lista=[]
while True:
    Numero=input("Adicione um valor ou digite 0 para parar: ")
    if Numero=="0":
        break
    else:
        lista.append(Numero)
print(f"Sua lista: {lista}")

deslocamento=int(input("Digite quanto quer deslocar os elementos: "))

resultado=shift_direita(lista,deslocamento)

print(resultado)

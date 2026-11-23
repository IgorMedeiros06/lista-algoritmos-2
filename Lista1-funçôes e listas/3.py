def contanando_lista(lista1, lista2):
    lista_contatenada = []
    while lista1!=[] or lista2!=[]:
        if len(lista1)!=0:
            lista_contatenada.append(lista1.pop(0))
        if len(lista2)!=0:
            lista_contatenada.append(lista2.pop(0))
    return lista_contatenada

def gerador_lista():
    lista=[]
    while True:
        valor=input("Adicione um valor ou digite 0 para parar: ")
        if valor=="0":
            break
        else:
            lista.append(valor)
    return lista

lista1 = gerador_lista()
print(f"lista 1 = {lista1}")
lista2 = gerador_lista()
print(f"lista 1 = {lista2}")

print(contanando_lista(lista1, lista2))
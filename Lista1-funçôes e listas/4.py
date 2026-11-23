def gerador_lista_ordenada():
    lista = []
    while True:
        valor=int(input("Adicione um valor ou digite 0 para parar: "))
        if valor==0:
            break
        else:
            lista.append(valor)
    lista.sort()
    return lista

def merge_ordenado(lista1, lista2):
    lista_final = []
    for valor1 in lista1:
        remover_lista2 = []
        for valor2 in lista2:
            if valor1<valor2:
                lista_final.append(valor1)
                break
            elif valor2==valor1:
                lista_final.append(valor1)
                lista_final.append(valor2)
                remover_lista2.append(valor2)
                break
            else:
                lista_final.append(valor2)
                remover_lista2.append(valor2)
        if lista2 == []:
            lista_final.append(valor1)
        for remove in remover_lista2:
            lista2.remove(remove)
        remover_lista2 = []
    if lista2!=[]:
        for i in lista2:
            lista_final.append(i)
    return lista_final

lista1 = gerador_lista_ordenada()
print(f"Lista1 = {lista1}")
lista2 = gerador_lista_ordenada()
print(f"Lista2 = {lista2}")

print(merge_ordenado(lista1,lista2))

# Tentativas falhas:

# lista1 = gerador_lista_ordenada()
# print(f"lista 1 = {lista1}")
# lista2 = gerador_lista_ordenada()
# print(f"lista 2 = {lista2}")



# lista_final = []
# for numero_1 in lista1:
#     if len(lista2)!=0:
#         for numero_2 in lista2:
#             if numero_1<numero_2:
#                 lista_final.append(numero_1)
#                 break
#             elif numero_2<numero_1:
#                 lista_final.append(numero_2)
#         lista2.remove(numero_2)
#     else:
#         lista_final.append(numero_1)
# print(lista_final)

lista1 = [5,10,15,20,25]
lista2 = [3,6,9,10]



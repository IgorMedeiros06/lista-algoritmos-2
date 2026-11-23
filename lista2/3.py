import random

def gera_carrinho():
    x = int(input("Numeros de produtos: "))
    carrinho = []
    for _ in range(x):
        produtos = []
        produtos.append(random.randint(1000,9999))
        produtos.append(random.randint(1,12))
        produtos.append(round(random.uniform(1,50),2))
        tupla = tuple(produtos)
        carrinho.append(tupla)
        produtos = []
    return carrinho

def recibo(carrinho):
    valor_total = 0
    Maior_preco = 0
    produtoCaro = []
    for produto in carrinho:
        preco_totalProduto = produto[1] * produto[2]
        valor_total += preco_totalProduto
        if preco_totalProduto > Maior_preco:
            Maior_preco = preco_totalProduto
            produtoCaro = [produto[0], (f"R$ {preco_totalProduto:.2f}")]
    return (f"R$ {valor_total:.2f}\nItem de maior custo: {produtoCaro}")

print(recibo(gera_carrinho()))
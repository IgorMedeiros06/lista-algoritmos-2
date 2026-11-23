import random

def gera_catalogo_filmes():
    nome_filmes = ["Gigante", "Força","Jubilo", "Justiça", "Jacaré" ,"O bêdado", "Línguas", "Piratas", "A lagoa", "Lixo","Luxúria" ,"Omg","O gemido","O grito","Machuca", "Marco Pollo", "pelados, mas não largados","O vacilo", "Carros", "Se é louco","Cães","Preto no branco", "O mar", "Ele caiu", "Novamente", "Perdidos", "Os irmões", "A cura", "Compaixão", "Vsfd", "Timão", "A torcida", "Gênios", "A lagarta", "Lucas", "Mentira", "Humínculo", "Legumes", "Pizzaria", "Sneakers", "Números", "Nostalgia", "Adultos", "Crianças", "O velho", "Letícia", "O pendulo"]
    generos = ["Comédia", "Ação", "Drama", "Documentário", "Terror"]
    catalgo=[]
    for _ in range (len(nome_filmes)):
        filme_dados = []
        nome = random.choice(nome_filmes)
        filme_dados.append(nome)
        nome_filmes.remove(nome)
        filme_dados.append(random.randint(1965,2026))
        filme_dados.append(random.choice(generos))
        filme_dados.append(round(random.uniform(1,10), 2))
        tupla = tuple(filme_dados)
        catalgo.append(tupla)
        filme_dados = []
    return(catalgo)

catalogo = (gera_catalogo_filmes())

def busca_catalago(catalogo):
    filmes = []
    menor_ano = 2027
    tupla = []
    print(["Comédia", "Ação", "Drama", "Documentário", "Terror"])
    genero = str(input("Escolha um dos generos acimas: "))
    nota_corte = float(input("Escolha a nota de corte: "))
    if type(genero) == str and type(nota_corte) == float:
        for filme in catalogo:
            if filme[2] == genero and filme[3] >= nota_corte:
                filmes.append(filme[0])
                if filme[1] < menor_ano:
                    tupla = [filme[0], filme[1]]
        tupla = tuple(tupla)
        return (f"Filmes: {filmes} \nFilme mais antigo: {tupla}")
    else:
        return("Parametros errados")

print(busca_catalago(catalogo))
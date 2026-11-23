#  Desenvolva um programa completo em Python nativo para controle de estoque de
# uma empresa. Utilize duas listas paralelas: `produtos` (strings) e `quantidades`
# (inteiros). Implemente um menu interativo dentro de um laço `while` com as opções: 1.
# Cadastrar Produto; 2. Listar Estoque; 3. Atualizar Quantidade; 4. Excluir Produto; 5.
# Sair. Garantir a integridade dos índices sincronizados entre as duas listas.

def controle_estoque():
    produtos = []
    quantidades = []
    while True:
        print("Digite os seguintes valores para cada ação: \n1 - cadastrar produtos\n2 - Lista estoque\n3 - Atualizar quantidade\n4 - Exlcluir produto\n5 - sair")
        opcao = int(input(": "))
        if  opcao == 1:
            produto = str(input("Nome do produto: "))
            if produto == "":
                print("ERRO!\nNome do produto vazio")
            else:
                quantidade = int(input(f"Quantidade do {produto}: "))
                if quantidade <= 0:
                    print("ERRO!\n Quantidade inválida")
                else:
                    produtos.append(produto)
                    quantidades.append(quantidade)
                    print("Operação executada com sucesso!")
        elif opcao == 2:
            for i in range(len(produtos)):
                    print(f"{produtos[i]}: {quantidades[i]}")
        elif opcao == 3:
            print(f"Qual produto deseja atualizar a quantidade:\n{produtos}")
            escolha = str(input(": "))
            existe = False
            for produto in produtos:
                if escolha == produto:
                    existe = True
            if existe:
                x = int(input(f"Digite a quantidade atualizade de {produto}: "))
                if x <= 0:
                    print("ERRO!\nQuantidade inválida")
                else:
                    quantidades[produtos.index(escolha)] = x
                    print("Operação executada com sucesso!")
            else:
                print("ERRO! produto não encontrado")
        elif opcao == 4:
            print(f"Qual produto deseja excluir a quantidade:\n{escolha}")
            escolha = str(input(": "))
            existe = False
            for produto in produtos:
                if escolha == produto:
                    existe = True
            if existe:
                x = produtos.index(escolha)
                quantidades.pop(x)
                produtos.remove(escolha)
                print("Operação executada com sucesso!")
            else:
                print("ERRO!\nProduto não encontrado")
        elif opcao == 5:
            break
        else:
            print("Opção inválida")

controle_estoque()
def main():
    alunos = []
    while True:
        print("Digite um dos numeros abaixos para executar as seguintes opções:\n" \
        "1-Cadastrar aluno\n2-Remover aluno\n3-Calcular as médias\n4-indentificar o aluno com a maior média\n5-Exibir todos o alunos\n6-sair")
        try:
            opcao = int(input(": "))
        except ValueError:
            print("Erro!\nSó é valido numeros")
            continue
        if opcao == 1:
            nome = str(input("Nome do aluno: "))
            notas = []
            while len(notas) < 4:
                try:
                    nota = float(input(f"Digite as notas do aluno {nome}: "))
                    if nota<0 or nota>10:
                        print("Erro!\nNota inválida\nCadrasto inválido")
                        continue
                    notas.append(nota)
                except ValueError:
                    print("Erro!\nValor atribuído a nota inválido\nCadastro inválidado")
                    continue
            aluno = {
                'nome': nome,
                'notas': notas
            }
            alunos.append(aluno)
        elif opcao == 2:
            nome_remover = str(input("Digite o nome do aluno: "))
            for aluno in alunos:
                if aluno['nome'] == nome_remover:
                    alunos.remove(aluno)
                    break
        elif opcao == 3:
            for aluno in alunos:
                aluno['media'] = sum(aluno["notas"])/4
                print(f"{aluno["nome"]} possui a média de {aluno["media"]}")
        elif opcao == 4:
            if not alunos:
                print("Nenhum aluno encontrado!")
                continue
            aluno_sem_media = False
            for aluno in alunos:
                if "media" not in aluno:
                    aluno_sem_media = True
                    continue
            if aluno_sem_media:
                print("Calcule a média de todos os alunos primeiro")
            else:
                média_maior = alunos[0]["media"]
                aluno_maior_média = alunos[0]["nome"]
                for aluno in alunos:
                    try:
                        if aluno["media"] > média_maior:
                            média_maior = aluno['media']
                            aluno_maior_média = aluno["nome"]
                    except KeyError:
                        print ("Calcule a média dos alunos antes")
                        continue
                print("O aluno com a maior maior média foi: ",aluno_maior_média," com a média de: ",média_maior)
        elif opcao == 5:
            for aluno in alunos:
                print(aluno)
        elif opcao == 6:
            break
        else:
            print("Opção inválida")

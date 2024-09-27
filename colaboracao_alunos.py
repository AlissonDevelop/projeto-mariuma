while True:    
    pesquisa = input("\nPara Pesquisar o nome e RA do aluno:\nEscolha [sim] para realizar a pesquisa \nou\nEscolha [não] para encerrar o programa: \nDigite aqui sua decisão: ").strip().lower()
    
    if pesquisa == 'sim':
        try:
            n = int(input("\nDigite seu número da lista de chamada: "))

            match n:
                case 1:
                    print("\n\n\n\nNão Participou da Atividade")
                case 3:
                    print("\n\n\n\nNão Participou da Atividade")
                case 4:
                    print("\n\n\n\nNão Participou da Atividade")
                case 5:
                    print("\n\n\n\nNão Participou da Atividade")
                case 6:
                    print("\n\n\n\nNão Participou da Atividade")
                case 7:
                    print("\n\n\n\nNão Participou da Atividade")
                case 8:
                    print("\n\n\n\nNão Participou da Atividade")
                case 9:
                    print("\n\n\n\nNão Participou da Atividade")
                case 10:
                    print("\n\n\n\nNão Participou da Atividade")
                case 11:
                    print("\n\n\n\nNão Participou da Atividade")
                case 12:
                    print("\n\n\n\nNão Participou da Atividade")
                case 13:
                    print("\n\n\n\nNão Participou da Atividade")
                case 14:
                    print("\n\n\n\nNão Participou da Atividade")
                case 15:
                    print("\n\n\n\nNome:isabela analy pereira dos santos emidio, RA: 00001117118563sp")
                case 17:
                    print("\n\n\n\nNão Participou da Atividade")
                case 18:
                    print("\n\n\n\nNão Participou da Atividade")
                case 19:
                    print("\n\n\n\nNão Participou da Atividade")
                case 20:
                    print("\n\n\n\nNão Participou da Atividade")
                case 21:
                    print("\n\n\n\nNão Participou da Atividade")
                case 22:
                    print("\n\n\n\nNão Participou da Atividade")
                case 24:
                    print("\n\n\n\nNão Participou da Atividade")
                case 25:
                    print("\n\n\n\nNão Participou da Atividade")
                case 26:
                    print("\n\n\n\nNão Participou da Atividade")
                case 27:
                    print("\n\n\n\nNão Participou da Atividade")
                case 28:
                    print("\n\n\n\nNão Participou da Atividade")
                case 29:
                    print("\n\n\n\nNão Participou da Atividade")
                case 30:
                    print("\n\n\n\nNão Participou da Atividade")
                case 31:
                    print("\n\n\n\nNão Participou da Atividade")
                case 33:
                    print("\n\n\n\nNão Participou da Atividade")
                case 34:
                    print("\n\n\n\nNão Participou da Atividade")
                case 35:
                    print("\n\n\n\nNão Participou da Atividade")
                case 36:
                    print("\n\n\n\nNão Participou da Atividade")
                case 37:
                    print("\n\n\n\nNão Participou da Atividade")
                case 38:
                    print("\n\n\n\nNão Participou da Atividade")

                case _:
                    print("\n\nNúmero de chamada não encontrado.\n\n")

        except ValueError:
            print("\n\nErro: Por favor, insira um número inteiro válido.\n\n")

    elif pesquisa == 'não' or pesquisa == 'nao':
            print("\n\nObrigado pela preferência e volte sempre ;)\n\n")
            break
    else:
        print("\n\nOpção inválida, por favor, digite 'sim' ou 'não'.\n\n")

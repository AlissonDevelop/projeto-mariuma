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
                case 5:
                    print("\n\n\n\nNome: Esther Martins - RA:00002083395871sp" )
                case 6:
                    print("\n\n\n\nNão Participou da Atividade")
                case 8:
                    print("\n\n\n\nNome: Grazielly vitoria - RA: 00001132729774sp")
                case 9:
                    print("\n\n\n\nNome: João Roberty - RA: 00001093230691sp")
                case 10:
                    print("\n\n\n\nNome: Julia Reis -RA: 00001082676627sp")
                case 11:
                    print("\n\n\n\nNão Participou da Atividade")
                case 14:
                    print("\n\n\n\nNão Participou da Atividade")
                case 17:
                    print("\n\n\n\nNão Participou da Atividade")
                case 18:
                    print("\n\n\n\nNão Participou da Atividade")
                case 19:
                    print("\n\n\n\nNome: Paulo Rogerio - RA: 00001093547790sp")
                case 21:
                    print("\n\n\n\nNão Participou da Atividade")
                case 24:
                    print("\n\n\n\nNome: Mariana ferreira - RA: 00001093729971sp")
                case 26:
                    print("\n\n\n\nNão Participou da Atividade")
                case 27:
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
                    print("\n\n\n\nNome: Yasmin Gobbi - RA 00001121667843sp")
                case 38:
                    print("\n\n\n\nNão Participou da Atividade")                

                case _:
                    print("\n\n\n\nNão Participou da Atividade")

        except ValueError:
            print("\n\nErro: Por favor, insira um número inteiro válido.\n\n")

    elif pesquisa == 'não' or pesquisa == 'nao':
            print("\n\nObrigado pela preferência e volte sempre ;)\n\n")
            break
    else:
        print("\n\nOpção inválida, por favor, digite 'sim' ou 'não'.\n\n")

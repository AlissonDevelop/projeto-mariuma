while True:    
    pesquisa = input("\nPara Pesquisar o nome e RA do aluno:\nEscolha [sim] para realizar a pesquisa \nou\nEscolha [não] para encerrar o programa: \nDigite aqui sua decisão: ").strip().lower()
    
    if pesquisa == 'sim':
        try:
            n = int(input("\nDigite seu número da lista de chamada: "))

            match n:
                case 1:
                    print("\n\n\n\nNome: Abner Farias - RA: 00008378854748sp")
                case 3:
                    print("\n\n\n\nNome:Bruno Gama - RA:00005463647567998sp")
                case 5:
                    print("\n\n\n\nNome: Esther Martins - RA:00002083395871sp" )
                case 6:
                    print("\n\n\n\nNome: Grazielly Santos - RA 0001212557311sp")
                case 8:                    
                    print("\n\n\n\nNome: Grazielly vitoria - RA: 00001132729774sp")
                case 9:
                    print("\n\n\n\nNome: João Roberty - RA: 00001093230691sp")
                case 10:
                    print("\n\n\n\nNome:Guilherme Cecatto - RA:000042435475467sp")
                case 11:
                    print("\n\n\n\nNome: Guilherme Santos - RA: 000083483487284sp")
                case 14:
                    print("\n\n\n\nNome: Herik Rodrigues - RA: 000094837498434sp")
                case 17:
                    print("\n\n\n\nNão Participou da Atividade")
                case 18:
                    print("\n\n\n\nNão Participou da Atividade")
                case 19:
                    print("\n\n\n\nNome: Paulo Rogerio - RA: 00001093547790sp")
                case 21:
                    print("\n\n\n\nNome: Julia Reis -RA: 00001082676627sp")
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
                    print("\n\n\n\nNome: Stella - RA: 00038748747sp")
                case 35:
                    print("\n\n\n\nNão Participou da Atividade")
                case 36:
                    print("\n\n\n\nNome:Vitor Araujo - RA:00007578475987sp")
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

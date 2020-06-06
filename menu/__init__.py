while True:
    print('='*30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('='*30)
    print('''[1] - JOGAR
[2] - CADASTRAR PALAVRA E DICA
[3] - EXIBIR PALAVRAS E DICAS
[0] - SAIR''')

    while True:
        from palavras import cadastrar, exibircadastros
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao == 0:
                from load import finalizando
                finalizando()
            elif opcao == 1 or opcao == 2 or opcao == 3:
                break
            else:
                print('\033[31mERRO! OPÇÃO INVALIDA\033[m')
        except(ValueError):
            print('\033[31mERRO! Opção não selecionada ou incorreta!\033[m')
    if opcao == 1:
        try:
            import Jogodaforca
        except(FileNotFoundError):
            print('\033[31mERROR! Ainda não foi cadastrado nenhuma palavra!\033[m')
    elif opcao == 2:
        cadastrar()
    elif opcao == 3:
        exibircadastros()

    while True:
        try:
            while True:
                print('='*30)
                resp = str(input('Quer Voltar ao MENU? (S/N) ')).strip().upper()
                if resp in 'SN':
                    break
                else:
                    print('\033[31mERRO! Responda corretamente S ou N!\033[m')
            if resp == 'S':
                break
            if resp == 'N':
                from load import finalizando
                finalizando()
        except(IndexError):
            print('\033[31mERRO! Responda corretamente!\033[m')

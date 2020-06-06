import verifica, palavras, desenho
partida = 0
derrota = vitoria = 0

while True:
    if partida == 0:
        jogador = verifica.palavras('Nome do Jogador: ')
        partida += 1
    else:
        print(f'Partida {partida}')
        letras = []
        erros = 0
        letraRepetida = []

        palavra = palavras.sortear()  # SORTEIA A PALAVRA===============================================================

        for x in range(0, len(palavra[0])):  # ADICIONA A QUANTIDADE DE LETRAS EM FORMA DE TRAÇOS A UMA LISTA ==========
            letras.append('_')

        while True:
            resposta = verifica.vitoria(letras, erros, jogador)  # VERIFICA SE GANHOU/PERDEU ===========================
            if resposta == 'perdeu':
                derrota += 1
                break
            if resposta == 'venceu':
                vitoria += 1
                desenho.sete(jogador)
                palavras.exibir(palavra[0], letras)  # EXIBI A PALAVRA COMPLETADA ANTES DE DAR OS PARABÉNS
                break

            verifica.erro(erros, jogador, partida)
            print(f'\n{6 - erros} tentativas restantes!')
            print(f'DICA : {palavra[1]}')

            palavras.exibir(palavra[0], letras)  # EXIBI TRAÇOS E AS LETRAS CONFORME VÃO SENDO REVELADAS ===============
            print(f'Letras Digitadas {letraRepetida}')
            letradigitada = verifica.letraRepetida(letraRepetida) # VERIFICA SE HÁ REPETIÇÃO NAS LETRAS DIGITADAS ======

            erros = verifica.acerto(palavra[0], erros, letras, letradigitada)  # É retornado o numero de erros  # VERIFICA
            # SE ACERTOU ALGUMA LETRA ==================================================================================
        while True:
            try:
                while True:
                    print('='*30)
                    resp = str(input('Jogar novamente? (S/N) ')).strip().upper()
                    if resp in 'SN':
                        break
                    else:
                        print('\033[31mERRO! Responda corretamente S ou N!\033[m')
                if resp == 'S':
                    partida += 1
                    break
                if resp == 'N':
                    from load import finalizando
                    print(f'Partidas Disputadas {partida}')
                    print(f'Vitórias : {vitoria}')
                    print(f'Derrotas : {derrota}')

                    finalizando()
            except(IndexError):
                print('\033[31mERRO! Responda corretamente!\033[m')

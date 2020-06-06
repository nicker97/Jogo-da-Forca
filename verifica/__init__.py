def acerto(palavra, errou, letras, letradigitada):
    """
    Compara se o jogador acertou alguma letra ou não, da palavra
    :param palavra: palavra em si
    :param errou: número de erros
    :param letras: lista com todas as letras da palavra, desvendadas ou não
    :return: número de erros
    """
    from time import sleep
    errouletra = True
    cont = 0

    for i, letra in enumerate(palavra):
        if palavra[i] == letradigitada:
            letras[i] = letradigitada
            errouletra = False
            cont += 1
            print(f'ACERTOU {cont} LETRAS!!')
            sleep(0.3)
    if errouletra:
        print('NÃO POSSUI ESTA LETRA!')
        errou += 1
    return errou


def vitoria(letras, errou, jogador):
    """
    Verifica se o jogador acertou todas as letras ou errou mais que o permitido
    :param letras: Lista com todas as letras reveladas ou não
    :param errou: número de erros
    :return: resultado obtido
    """
    import desenho
    ganhouJogo = True
    for let in letras:
        if let == '_':
            ganhouJogo = False
    if ganhouJogo:
        return 'venceu'
    if errou == 6:
        desenho.seis(jogador)
        return 'perdeu'

def erro(errou, jogador, partida):
    '''
    Recebe o numero de erros do usuario, mostra o desenho do respectivo erro
    :param errou: número de erros cometidos
    :return: sem retorno
    '''
    import desenho
    if errou == 0:
        desenho.zero(jogador, partida)
    if errou == 1:
        desenho.um(jogador, partida)
    if errou == 2:
        desenho.dois(jogador, partida)
    if errou == 3:
        desenho.tres(jogador, partida)
    if errou == 4:
        desenho.quatro(jogador, partida)
    if errou == 5:
        desenho.cinco(jogador, partida)
    if errou == 6:
        desenho.seis(jogador, partida)

def palavras(texto):
    while True:
        palavra = str(input(texto).strip().upper())
        valida = palavra.isnumeric()
        if len(palavra) <= 2:
            print('\033[31mERRO! Não possui caracteres suficientes!\033[m')
        elif valida == True:
            print('\033[31mERRO! Formato inválido!\033[m')
        else:
            return palavra

def validaletra(texto):
    while True:
        palavra = str(input(texto)).strip().upper()
        valida = palavra.isnumeric()
        if len(palavra) > 1 or palavra == '':
            print('\033[31mERRO! Favor digitar uma letra!\033[m')
        elif palavra not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('\033[31mERRO! Caracteres não são letra!\033[m')
        elif valida == True:
            print('\033[31mERRO! Formato inválido!\033[m')
        else:
            return palavra

def letraRepetida(letras):
    while True:
        numero = 0
        letradigitada = validaletra('Escolha uma Letra: ')
        for x in range(0, len(letras)):
            if letradigitada == letras[x]:
                numero +=1
        if numero == 0:
            letras.append(letradigitada)
            break
        else:
            print('ERRO! Essa letra ja foi digitada!')
    return letradigitada

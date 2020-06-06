def sortear():
    """
    Sorteia uma palavra para ser adivinhada
    :return: palavra sorteada com sua dica como lista
    """
    from random import randint
    print('=' * 30)
    palavra = open('palavras.txt', 'r')
    dicas = open('dicas.txt', 'r')

    palavracomdica = [palavra.readlines(), dicas.readlines()] # ADICIONA TODAS AS LINHAS DOS ARQUIVOS .txt A UMA LISTA
    quantidade = len(palavracomdica[0])

    indice = randint(0, quantidade - 1)

    palavraescolhida = [palavracomdica[0][indice].rstrip().upper(), palavracomdica[1][indice].rstrip().upper()]# ADICIONA
    #UMA PALAVRA ALEATÓRIA COM SUA DICA A UMA LISTA
    palavra.close()
    dicas.close()
    return palavraescolhida


def exibir(palavra, letras):
    """
    Exibe a quantidade de letras que a palavra possui, letras adivinhadas ou traços
    :param palavra: palavra em si
    :param letras: lista com numero total de letras
    :return: sem retorno
    """
    print(f'{len(palavra)} Letras: ', end='')
    for letra in letras:
        print(letra, end=' ')
    print()

def cadastrar():
    """
    Cadastra palavras e dicas a um arquivo de texto
    :return: Sem retorno
    """
    from verifica import palavras
    print('=' * 30)
    arquivopalavra = open('palavras.txt', 'a')
    arquivodica = open('dicas.txt', 'a')
    palavra = palavras('Palavra: ')
    dica = palavras('Dica: ')
    arquivodica.write(dica + '\n')
    arquivopalavra.write(palavra + '\n')
    print('CADASTRO SUCEDIDO!')
    arquivopalavra.close()
    arquivodica.close()

def exibircadastros():
    """
    Exibi todas palavras e suas respectivas dicas
    :return: Sem retorno
    """
    try:
        print('=' * 30)
        palavra = open('palavras.txt', 'r')
        dicas = open('dicas.txt', 'r')
        palavracomdica = [palavra.readlines(), dicas.readlines()]
        quantidade = len(palavracomdica[0])
        print('PALAVRA  /  DICA')
        print()
        for x in range(0, quantidade):
            print(palavracomdica[0][x].rstrip().upper(), end=' - ')
            print(palavracomdica[1][x].rstrip().upper())
        palavra.close()
        dicas.close()
    except(FileNotFoundError):
        print('\033[31mERROR! Ainda não foi cadastrado nenhuma palavra!\033[m')

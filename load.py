from time import sleep

def carregando(carregando):
    print(carregando, end='')
    sleep(0.3)
    print('.',end='')
    sleep(0.3)
    print('.',end='')
    sleep(0.3)
    print('.',end='')
    sleep(0.3)
    print('.',end='')
    sleep(0.3)
    print('.')
    sleep(0.3)

def finalizando():
    print('FINALIZANDO', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    exit()
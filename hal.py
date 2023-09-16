import random

# Camada de abstracao do Hardware (Simulação), onde os valores sao gerados para simularmos um ambiente onde haveria a variação de temperatura.


def temperatura():
    return random.randrange(20,40)


def temperatura2():
    return random.randrange(20,40)

def aquecedor(status: str):
    if status == 'on':
        return print('AQUECEDOR LIGADO')
    else:
        return print('AQUECEDOR DESLIGADO')
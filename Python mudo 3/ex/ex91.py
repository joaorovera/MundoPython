from random import randint
from time import sleep

pontos = {}
pontos['jogador1'] = randint(1,6)
pontos['jogador2'] = randint(1,6)
pontos['jogador3'] = randint(1,6)
pontos['jogador4'] = randint(1,6)
for i in pontos:
    print(f'O {i} tirou {pontos[i]}')
    sleep(1)


from random import randint

jogo = []
palpites = []
jogos = int(input('Quantos jogos você quer que eu sorteie: '))
for i in range(jogos):
    for i in range(6):
        n = randint(1, 60)
        while n in jogo:
            n = randint(1, 60)
        jogo.append(n)
    jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()
print('-='*3, f'Sorteando {jogos} jogos', '-='*3)
for i in range(jogos):
    print(palpites[i])
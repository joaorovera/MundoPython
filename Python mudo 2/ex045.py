from random import randint
itens = ('Pedra','Papel','Tesoura')
comp = randint(0,2)


print('<==>'*10)
print('''[1] - Pedra
[2] - Papel
[3] - Tesoura''')
print('<==>'*10)
joga = int(input('Qual a sua jogada: '))
jogad = joga-1
print('<==>'*10)
print(f'O computador escolheu {itens[comp]} e você escolheu {itens[joga-1]}')
print('<==>'*10)


if comp == jogad:
    print('EMPATE!')
elif comp == 0 and jogad == 2:
    print("O computador GANHOU!")
elif jogad == 0 and comp == 2:
    print("O JOGADOR GANHOU!")
elif jogad> comp:
    print(("O JOGADOR GANHOU!"))
elif comp>jogad:
    print("O computador ganhou")
else:
    print('Algo deu errado...')

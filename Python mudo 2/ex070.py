s = 0
caros = 0
barato = ''
valbar = 0

while True:
    nome = input('Qual o nome do produto: ')
    valor = float(input('Qual o valor do produto: R$'))
    s += valor
    if valor > 1000: 
        caros += 1
    if barato == '':
        barato = nome
        valbar = valor
    elif valor < valbar:
        barato = nome
        valbar = valor
    cont = int(input('Quer continuar [1] sim - [2] nao - '))
    if cont == 2:
        break
print('='*20,'FIM','='*20)
print(f'O total gasto na compra foi R${s:.2f}')
print(f'Com um total de {caros} produtos custando mais de 1000 reais')
print(f'O produto mais barato foi - {barato} custando R${valbar}')
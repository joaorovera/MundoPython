vel = float(input('Qual a velocidade marcada no radar? '))
multa = (vel-80)*7

if vel <=80:
    print('Tenha um bom dia!')
else:
    print(f'Moiou, pague uma multa de R${multa:.2f}')

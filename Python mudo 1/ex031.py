dis = float(input('Qual a distancia da vaigem? '))
preco1 = dis*0.5
preco2 = dis*0.45

if dis<=200:
    print(f'O total a pagar será R${preco1}')
else:
    print(f'O total a pagar será R${preco2}')

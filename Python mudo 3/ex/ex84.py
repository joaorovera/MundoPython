pessoas = []
aux = []
for i in range(5):
    aux.append(input('Nome: '))
    aux.append(float(input('Peso: ')))
    pessoas.append(aux[:])
    aux.clear()

maior = pessoas[0][1]
menor = pessoas[0][1]
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
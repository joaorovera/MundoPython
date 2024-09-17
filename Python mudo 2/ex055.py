maior = 0
menor = 0
for i in range(0,5):
    p = float(input('Qual o peso: '))
    if i == 0:
        maior = p
        menor = p
    else:   
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O menor peso foi {menor}Kg e o maior foi {maior}Kg')
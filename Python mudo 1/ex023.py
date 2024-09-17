n1 = str(input('Digite um numero de 0 a 9999: '))
print(f'unidade = {n1[-1]}')
if len(n1)>1:
    print(f'dezena = {n1[-2]}')
if len(n1)>2:
    print(f'centena = {n1[-3]}')
if len(n1)>3:
    print(f'milhar = {n1[0]}')
sal = float(input('Qual o salário do funcionário: '))
aum1 = sal*1.15
aum2 = sal*1.1

if sal<=1250:
    print(f'O novo salário do funcionário é R${aum1}')
else:
    print(f'O novo salário do funcionário é R${aum2}')

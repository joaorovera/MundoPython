n = float(input('Digite o valor do item: R$'))
forma = int(input('1-a vista no din ou cheque\n2-a vista no cartão\n3-2x no cartão\n4-3x ou mais no cartão\nOpção: '))

if forma ==1:
    print(f'O novo valor será R${n*0.9}')
elif forma ==2:
    print(f'O novo valor será R${n*0.95}')
elif forma ==3:
    print(f'O valor será R${n}')
elif forma ==4:
    print(f'O novo valor será R${n*1.2}')
else:
    print('Essa opção não existe')
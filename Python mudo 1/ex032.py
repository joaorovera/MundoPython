ano = int(input('Digite um ano para saber se foi bissexto: '))

if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Bissexto')
else:
    print('Não')

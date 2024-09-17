ano = int(input('Digite seu ano de nascimento: '))
idade = 2024-ano

if idade<=9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print(f'MAsTER')
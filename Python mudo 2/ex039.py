ano = int(input('Digite seu ano de nascimento: '))
idade = 2024-ano

if idade == 18:
    print('Está na hora de se alistar')
elif idade < 18:
    print(f'Não está na hora ainda, faltam {18 - idade} anos')
else:
    print(f'Já passou da hora, passaram {idade-18} anos')

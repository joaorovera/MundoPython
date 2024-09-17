n1 = float(input('Digite a nota do aluno: '))
n2 = float(input('Digite a nota 2 do aluno: '))
media = (n1+n2)/2

if media < 5:
    print('Está na hora de estudar, REPROVADO')
elif media >= 5 and media <7:
    print(f'Não está na hora de se desesperar, apenas recuperação')
else:
    print(f'parabéns irmão')
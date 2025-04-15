aluno = {}

aluno['nome'] = input('Nome: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1+nota2)/2
aluno['media'] = media
if (nota1+nota2)/2<7:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'

print(aluno)
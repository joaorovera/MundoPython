alunos = []
aux = []
medias = []
for i in range(3):
    aux.append(input('Nome: '))
    aux.append(float(input('Nota 1: ')))
    aux.append(float(input('Nota 2: ')))
    alunos.append(aux[:])
    aux.clear()
for i in alunos:
    media = (i[1] + i[2]) / 2
    aux.append(i[0])
    aux.append(media)
    medias.append(aux[:])
    aux.clear()
print('-='*30)
for i in medias:
    print(f'{i[0]} teve média {i[1]}')

for i in alunos:
    print(f'O aluno {i[0]} tirou {i[1]} e {i[2]}')
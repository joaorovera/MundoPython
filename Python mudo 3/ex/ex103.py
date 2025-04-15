def estatisticas(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols no camp'

nome = str(input("Nome do jogador: "))
gols = str(input("Numero de gols:"))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    nome = '<desconhecido>'

print(estatisticas(nome,gols))
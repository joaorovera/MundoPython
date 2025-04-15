jogador = {}
gols = []

jogador['nome'] = input("Nome: ")
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
for i in range(jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)  # Adiciona o total de gols ao dicionário

print(jogador)
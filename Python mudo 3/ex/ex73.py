times_brasileirao_2024 = (
    "Flamengo", "Palmeiras", "Atlético-MG", "São Paulo", "Fluminense",
    "Corinthians", "Internacional", "Grêmio", "Athletico-PR", "Santos",
    "Ceará", "Fortaleza", "Bahia", "Vasco da Gama", "Botafogo",
    "Cruzeiro", "Sport", "Goiás", "Coritiba", "América-MG"
)


print(f'Os 5 primeiros sao{times_brasileirao_2024[0:5]}')
print('__________________________________________________')
print(f'Os 4 ultimos sao {times_brasileirao_2024[-4:]} ')
print('__________________________________________________')
print(f"Em orde alfabética:\n {sorted(times_brasileirao_2024)}"),
print('__________________________________________________')
print(f'O Botafogo ficou em {times_brasileirao_2024.index("Botafogo")}')
pessoa = {}

pessoa['nome'] = input("Nome: ")
pessoa['idade'] = 2025 - int(input("Ano de nascimento: "))
pessoa['ctps'] = int(input("Carteira de trabalho (0 se nao tem): "))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input("Ano de contratacao: "))
    pessoa['salario'] = float(input("salario: "))
    pessoa['aposentadoria'] = (pessoa['idade'] - (2025 - pessoa['contratacao'])) + 35
    print(pessoa)
else:
    print(f"O {pessoa['nome']} nao tem carteira")
for k, v in pessoa.items():
    print(f'O {k} tem o valor de {v}')
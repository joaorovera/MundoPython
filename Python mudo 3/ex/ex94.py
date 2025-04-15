pessoas = []
idades = 0
mulheres = []
for i in range(4):
    pessoa = {}
    pessoa['nome'] = input("Nome: ")
    pessoa['idade'] = 2025 - int(input("Ano de nascimento: "))
    pessoa['sexo'] = input("M ou F: ")
    pessoas.append(pessoa)

print(pessoas)
for i in pessoas:
    idades += i['idade']
    if i['sexo'] == 'f':
        mulheres.append(i)
print (f"A média de idade do grupo é {idades/4}")
print (f"A lista das mulheres é {mulheres}")

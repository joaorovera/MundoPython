n = []
for i in range(5):
    n.append(int(input('Digite um valor: ')))

print(f'Foram digitados {len(n)} valores')
if n.index(5):
    print('O 5 foi digitado')
else:
    print('O 5 não foi digitado')
print(f'A lista em ordem decrescente: {sorted(n, reverse=True)}')
n = []
for i in range(5):
    n.append(int(input('Digite um valor: ')))
nc = n[:]
nc.sort()
print(f'O menor valor foi {nc[0]} na posição {n.index(nc[0])}')
print(f'O maior valor foi {nc[-1]} na posição {n.index(nc[-1])}')
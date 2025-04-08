n = []
pares = []
impares = []
numeros = []
for i in range(7):
    n.append(int(input('Digite um número: ')))

for i in n:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')
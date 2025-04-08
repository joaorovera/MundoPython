matriz = []
aux = []
for i in range(3):
    for j in range(3):
        aux.append(int(input(f'Digite um número para a posição [{i}, {j}]: ')))
    matriz.append(aux[:])
    aux.clear()
print('-='*30)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print('')
print('-='*30)
somapares = 0
impares = 0
soma3coluna = 0
for i in range(3):
    for j in range(3):
        if j == 2:
            soma3coluna += matriz[i][j]
        if matriz[i][j] % 2 == 0:
            somapares += matriz[i][j]
        else:
            impares += matriz[i][j]
print(f'A soma dos números pares é: {somapares}')
print(f'A soma dos números ímpares é: {impares}')
print(f'A soma dos números da terceira coluna é: {soma3coluna}')
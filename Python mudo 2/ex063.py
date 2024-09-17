n = int(input('Numero inteiro: '))
cont = 2
inicio = 1
inicio1 = 0

print(f"{inicio1}->{inicio}", end='->')
while cont != n:
    result = inicio + inicio1
    inicio1 = inicio
    inicio = result
    print(result, end='->')
    cont += 1

print('FIM')

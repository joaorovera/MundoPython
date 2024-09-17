

while True:
    n = int(input('Digite um numero inteiro: '))
    if 0>n:
        break
    for i in range(1,11):
        print(f'{n} X {i} = {n*i}')
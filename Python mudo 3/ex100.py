from random import randint

def somapar(numeros):
    soma = 0
    for i in numeros:
        if i%2 == 0:
            soma += i
    print(f'A soma dos números pares é {soma}')

def sorteio():
    num = []
    for i in range(5):
        n = randint(1,10)
        num.append(n)
    print(f"Os numeros sorteados foram: {num}")
    somapar(num)

sorteio()
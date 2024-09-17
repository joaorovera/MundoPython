n = int(input('Digite um numero inteiro: '))
nc = n
result = 1
while n != 0:
    result *= n
    n -= 1

print(f"o fatorial do numero {nc} é {result}")
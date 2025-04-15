from uteis import numeros as n

preco = float(input("Digite o preço: R$ "))
print(f'A metade do preço é {n.metade(preco)}')
print(f'O dobro do preço é {n.dobro(preco)}')
print(f'Aumentando 10%, temos {n.aumentar(preco, 10)}')
print(f'Reduzindo 13%, temos {n.reduzir(preco, 13)}')
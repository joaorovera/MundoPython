from uteis import numeros as n

preco = float(input("Digite o preço: R$ "))
print(f'A metade do {n.moeda(preco)} é {n.metade(preco, True)}')
print(f'O dobro do {n.moeda(preco)} é {n.dobro(preco, True)}')
print(f'Aumentando 10%, temos {n.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {n.reduzir(preco, 13, True)}')
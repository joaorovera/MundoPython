from uteis import numeros as n

preco = float(input("Digite o preço: R$ "))
print(f'A metade do {n.moeda(preco)} é {n.moeda(n.metade(preco))}')
print(f'O dobro do {n.moeda(preco)} é {n.moeda(n.dobro(preco))}')
print(f'Aumentando 10%, temos {n.moeda(n.aumentar(preco, 10))}')
print(f'Reduzindo 13%, temos {n.moeda(n.reduzir(preco, 13))}')
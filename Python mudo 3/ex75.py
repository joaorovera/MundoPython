n = (int(input("Digite um valor 0 a 9: ")),int(input("Digite um valor 0 a 9: ")),int(input("Digite um valor 0 a 9: ")),int(input("Digite um valor 0 a 9: ")))
print(f"Voce digitou os valores {n}")
if 3 in n:
    print(f"O 3 ficou na posicao {n.index(3)+1}")
else:
    print(f"O 3 foi pro além")
print(f"O 9 apareceu {n.count(9)} vezex")
pares = 0
for i in range(len(n)):
    if n[i]%2==0:
        pares+=1
print(pares, "pares")
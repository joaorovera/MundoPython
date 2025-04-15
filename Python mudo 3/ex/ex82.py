n = []
par=[]
impar=[]
for i in range(6):
    n.append(int(input('Digite um valor: ')))
    if n[i] % 2 == 0:
        par.append(n[i])
    else:
        impar.append(n[i])
print(f'Os valores pares são: {par}')
print(f'Os valores ímpares são: {impar}')
print(f'Foram digitados {n}')
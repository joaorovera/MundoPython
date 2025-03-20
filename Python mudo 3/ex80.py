n = []
for i in range(5):
    if i == 0:
        n.append(int(input('Digite um valor: ')))
    else:
        val = int(input('Digite um valor: '))
        for j in range(len(n)):
            if val < n[j] or val == n[j]:
                aux = n[j]
                n[j] = val
                n.append(aux)
print(n)

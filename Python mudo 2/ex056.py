soma= 0
mh = 0
nv = ''
mn = 0
for i in range(0,4):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma+=idade
    if i == 0 and sexo == "M":
        mh = idade
        nv = nome
    if sexo =="M" and idade > mh:
        nv = nome
        mh = idade
    if sexo == "F" and idade < 20:
        mn += 1

media = soma/4
print(f'A média de idade é de {media} anos')
print(f'O nome do homem mais velho é {nv} e tem {mh} anos')
print(f'existem {mn} mulheres novas')


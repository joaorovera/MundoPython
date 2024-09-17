a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))


if a + b > c and a + c > b and b + c > a:
    print('Pode formar um triangulo')
    if a == b and a == c:
        print('E é equilátero')
    elif a==b or a==c or c==b:
        print('E é isóceles')
    else:
        print('E é escaleno')
else: 
    print('Não pode!!!!!!!!!!')

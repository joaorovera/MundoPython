n = 0
n1 = int(input('Digite o primeiro valor: '))
n2= int(input('Digite o segundo valor: '))

while n != 5:
    print('''[1] - Soma
[2] - Multiplica
[3] - Maior
[4] - Novos numeros
[5] - Sair''')
    n = int(input('Selecione uma opção: '))
    if n == 1:
        print(n1+n2)
    elif n == 2:
        print(n1*n2)
    elif n == 3:
        if n1>n2:
            print(f'{n1} é o maior')
        else:
            print(f'{n2} é o maior')
    elif n == 4:
            n1 = int(input('Digite o primeiro valor: '))
            n2= int(input('Digite o segundo valor: '))
    elif n == 5:
        print("Você está saindo do programa!")
    else:
        print('Essa opção não existe!')


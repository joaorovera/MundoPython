n = int(input('Digite um numero para saber se é primo: '))

if n%2==0:
    print('Não é primo')
else:
    for i in range(3,(n+1)//2):
        if n%i==0:
            print('não é primo')
            break
        elif i == (n//2):
            print('é primo')

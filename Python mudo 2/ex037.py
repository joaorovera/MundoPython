n = int(input('Digite um numero para converter: '))
forma = int(input('1-Binário\n2-octal\n3-hexadecimal\nOpção: '))

if forma ==1:
    print(f'Esse número convertido em binário é {bin(n)}')
elif forma ==2:
    print(f'Esse número convertido em octal é {oct(n)}')
elif forma ==3:
    print(f'Esse número convertido em hexadecimal é {hex(n)}')
else:
    print('Essa opção não existe')
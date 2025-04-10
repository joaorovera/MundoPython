def maior(*args):
    """
    Função que retorna o maior número entre os argumentos passados.
    """
    if len(args) == 0:
        return None
    maior = args[0]
    for num in args:
        if num > maior:
            maior = num
    print(f'O maior valor é {maior}')
    print(f'Foram informados {len(args)} valores ao todo.')


lista = []
continuar = 998
while continuar != 0:
    try:
        continuar = int(input("Digite um número (ou 0 para parar): "))
        if continuar != 0:
            lista.append(continuar)
    except ValueError:
        print("Por favor, insira apenas números inteiros válidos.")
maior(*lista)
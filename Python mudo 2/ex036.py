casa = float(input("Digite o valor da casa: R$"))
sal = float(input("Digite seu salario atual: R$"))
parc = int(input("Quantas anos você vai pagar: "))

prest = casa/(parc*12)

if sal*0.3>= prest:
    print(f'as parcelas serão de R${prest}, portanto poderá financiar')
else:
    print(f'as parcelas serão de R${prest}, portanto não poderá financiar')
d = int(input('Quantos dias o carro ficou alugado: '))
km = float(input('Quantos Km foram rodados: '))
t = (60*d)+(km*0.15)

print(f'O total a ser pago é R${t:.2f}')
numerosPorExtenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
    'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 
    'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    numeroSelecionado = int(input("Digite um numero de 0 a 20: "))
    if 0 <= numeroSelecionado <= 20:
        print(numerosPorExtenso[numeroSelecionado])
        break
    else:
        print("numero inválido")
a = float(input('Altura em m: '))
p = float(input('Peso: '))
imc = p/a**2

if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else: 
    print('Obesidade Morbida')
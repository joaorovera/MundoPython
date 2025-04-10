def voto(nascimento):
    idade = 2025 - nascimento
    if idade > 18 and idade < 65:
        return 'Voto obrigatório'
    elif idade < 18:
        return 'Voto não obrigatório'
    elif idade >= 65:
        return "Voto opcional"
    else:
        return 'Algo está errado'
    
nascimento = int(input("Que ano nasceste: "))
print(voto(nascimento))
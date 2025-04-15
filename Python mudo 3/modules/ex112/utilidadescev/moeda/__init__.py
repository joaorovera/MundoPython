def fatorial(n):
    f = 1
    for i in range(f,n+1):
        f *= i
    return f

def dobro(n, fmt=False):
    if fmt:
        return moeda( n *2)
    else:
        return n *2 

def triplo(n, fmt=False):
    if fmt:
        return moeda( n *3 )
    else:
        return n *3 

def metade(n, fmt=False):
    if fmt:
        return moeda(n / 2)
    else:
        return n / 2

def reduzir(n, porcentagem, fmt=False):
    if fmt:
        return moeda(n - (n *(porcentagem / 100)))
    else:
        return n - (n *(porcentagem / 100))

def aumentar(n, porcentagem, fmt=False):
    if fmt:
        return moeda((n + (n * (porcentagem / 100))))
    else:
        return (n + (n * (porcentagem / 100)))

def moeda(n):
    return f"R${n:.2f}".replace('.',',')

def resumo(n, a=10, r=5):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço analisado: {moeda(n)}")
    print(f"Dobro do preço: {dobro(n, True)}")
    print(f"Triplo do preço: {triplo(n, True)}")
    print(f"Metade do preço: {metade(n, True)}")
    print(f"{a}% de aumento: {aumentar(n, a, True)}")
    print(f"{r}% de redução: {reduzir(n, r, True)}")
    print("-"*30)
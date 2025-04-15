def area(c,l):
    a = c * l
    return a

c = int(input("Digite o comprimento (m): "))
l = int(input("Digite a largura (m): "))

area = area(c,l)
print(f"A área do terreno é: {area}m²")

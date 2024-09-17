from math import hypot

ca = float(input('Qual o valor do cateto adjascente: '))
co = float(input('Qual o valor do cateto oposto: '))
h = hypot(ca, co)

print(h)
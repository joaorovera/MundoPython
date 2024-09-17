import math

a = float(input('Qual angulo deseja calcular: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print(f'{s:.2f}')
print(f'{c:.2f}')
print(f'{t:.2f}')
from random import randint

n = randint(0,10)
r = 11
pa = 0

while r != n:
    r = int(input('Em que numero eu pensei? '))
    pa += 1
    if r == n:
        break
    print('\033[4;31mNão foi dessa vez\033[m')


print(f'\033[32mParabéns\033[m! Você venceu com {pa} palpites')
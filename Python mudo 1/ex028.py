from random import randint

n = randint(0,5)
r = int(input('Em que numero eu pensei? '))

if r == n:
    print('\033[32mParabéns\033[m! Você venceu')
else:
    print('\033[4;31mNão foi dessa vez\033[m')

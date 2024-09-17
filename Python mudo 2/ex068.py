from random import randint

pc = randint(0,10)
win = 0

while True:
    parimpar= int(input('Você escolhe par ou impar \n[1] - par\n[2] - impar\n-> '))
    n = int(input('Jogue um numero inteiro de 0 a 10- '))
    if parimpar == 1:
        s = pc + n
        if s % 2 == 0:
            win +=1
            print(f'Parabéns, você conseguiu ganhar')

        else:
            break
    else:
        s = pc + n
        if s % 2 != 0:
            win +=1
            print(f'Parabéns, você conseguiu ganhar')
        else:
            break

print(f'Parabéns, você conseguiu ganhar {win} vezes seguidas!!')

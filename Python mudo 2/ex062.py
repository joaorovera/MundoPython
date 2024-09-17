t = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a razao: '))
cont = 0


while True:
    while cont < 10:
        cont+=1
        if cont == 10:
            print(t)
        else:
            print(t, end="->")
        t +=r
    add = int(input('\nVocê deseja adiconar mais quantos numeros [0 - fim do programa]: '))
    if add == 0:
        break
    else:
        cont -= add
print('FIM')
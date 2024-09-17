t = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a razao: '))
cont = 0

while cont < 10:
    cont+=1
    print(t, end="->")
    t +=r
print('FIM')
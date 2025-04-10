def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo = -passo
    for i in range(inicio,fim+1,passo):
        print(i,end=' ')
    print("FIM")

contador(1,10,1)
contador(10,0,-2)
print("Agora é sua vez!")
try:
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
except ValueError:
    print("Por favor, insira apenas números inteiros válidos.")
    inicio, fim, passo = 0, 0, 1
contador(inicio,fim,passo)